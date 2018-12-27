#-*- coding:utf-8 -*-
from framework.basepage import BasePage

class HomePage(BasePage):

    input_box = "id=>kw"
    search_button = "xpath=>//*[@id='su']"
    news_link = "xpath=>//*[@id='u1']/a[@name='tj_trnews']"

    def type_search(self,text):
        self.type(self.input_box,text)

    def submit_button(self):
        self.click(self.search_button)

    def click_news_link(self):
        self.click(self.news_link)
        self.sleep(3)