#-*- coding:utf-8 -*-

from framework.basepage import BasePage

class SportsHomePage(BasePage):

    nba_sports_list = "xpath=>//*[text()='NBA赛程表']"

    def click_nba_list(self):
        self.click(self.nba_sports_list)
        self.switch_to_window()
        self.sleep(2)

