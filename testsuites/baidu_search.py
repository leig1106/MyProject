from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
from pageobjects.baidu_news_home import NewsHomePage
from pageobjects.baidu_sports_home import SportsHomePage
from config.get_config_value import Get_Config_Value
import unittest

class BaiduSearch(unittest.TestCase):


    url = Get_Config_Value().get_value('testServer','URL')

    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserEngine().get_browser()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_check_search(self):
        homepage = HomePage(self.driver)
        homepage.open_url(self.url)
        homepage.sleep(2)
        homepage.type_search('selenium')
        homepage.submit_button()
        homepage.sleep(2)
        homepage.back()
        homepage.sleep(2)
        homepage.forward()
        homepage.sleep(2)
        assert 'selenium' in homepage.get_page_title()

    def test_check_nbalist(self):
        homepage = HomePage(self.driver)
        homepage.open_url(self.url)
        homepage.sleep(2)
        homepage.click_news_link()
        homepage.sleep(2)
        newspage = NewsHomePage(self.driver)
        newspage.click_sports_link()
        newspage.sleep(2)
        sportspage = SportsHomePage(self.driver)
        sportspage.click_nba_list()
        sportspage.sleep(2)
        assert 'NBA' in sportspage.get_page_title()