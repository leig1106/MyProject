#-*- coding:utf-8 -*-

import importlib
from config.get_config_value import Get_Config_Value

class DataBaseLibrary(object):
    """
    执行数据库操作的方法
    """
    def __init__(self):
        self._dbconnection = None

    def connect_to_database(self,dbproject,dbModuleName=None,dbName=None,dbUsername=None,dbPwd=None,dbHost=None,dbPort=None):
        projects = Get_Config_Value().get_options('projects')
        if dbproject in projects:
            if dbproject == 'ticket':
                conf = Get_Config_Value()
                dbModuleName = dbModuleName or conf.get_value('database_ticket','dbModuleName')
                dbName = dbName or conf.get_value('database_ticket','dbName')
                dbUsername = dbUsername or conf.get_value('database_ticket','dbUsername')
                dbPwd = dbPwd or conf.get_value('database_ticket','dbPwd')
                dbHost = dbHost or conf.get_value('database_ticket','dbHost')
                dbPort = int(dbPort or conf.get_value('database_ticket','dbPort'))
            elif dbproject == 'dbman':
                conf = Get_Config_Value()
                dbModuleName = dbModuleName or conf.get_value('database_dbman', 'dbModuleName')
                dbName = dbName or conf.get_value('database_dbman', 'dbName')
                dbUsername = dbUsername or conf.get_value('database_dbman', 'dbUsername')
                dbPwd = dbPwd or conf.get_value('database_dbman', 'dbPwd')
                dbHost = dbHost or conf.get_value('database_dbman', 'dbHost')
                dbPort = int(dbPwd or conf.get_value('database_dbman', 'dbPort'))
        else:
            raise ValueError("there is nothing about %s project info" % dbproject)

        db_module = importlib.import_module(dbModuleName)
        #print(dbModuleName,dbName,dbUsername,dbPwd,dbHost,dbPort)
        if dbModuleName in ['pymysql']:
            self._dbconnection = db_module.connect(host=dbHost,user=dbUsername,password=dbPwd,database=dbName,port=dbPort)
        elif dbModuleName in ['cx_Oracle']:
            pass
        else:
            self._dbconnection = db_module.connect(database=dbName,user=dbUsername,password=dbPwd,host=dbHost,port=dbPort)

    def disconnect_from_database(self):
        self._dbconnection.close()

    def __execute_sql(self,cur,sqlstatement):
        return cur.execute(sqlstatement)

    def execute_dql_sql(self,selectStatement):
        cur = self._dbconnection.cursor()
        self.__execute_sql(cur,selectStatement)
        allrows = cur.fetchall()
        return allrows

    def execute_dml_sql(self,sqlstring):
        try:
            cur = self._dbconnection.cursor()
            self.__execute_sql(cur,sqlstring)
            self._dbconnection.commit()
        except Exception as e:
            self._dbconnection.rollback()
            print(e)

