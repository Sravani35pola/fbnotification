# from selenium import webdriver
# import time
# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument("--disable-notification")
#
# chrome_option.add_argument("--disable-infobars")
#
# chrome_option.add_argument("start-maximized")
#
# chrome_option.add_argument("--disable-extensions")
#
# chrome_option.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications": 2})
#
# chrome_option.add_argument("use-fake-ui-for-media-stream")
# path =r"C:\Users\Sravani\Downloads\chromedriver_win32\chromedriver.exe"
# driver_obj=webdriver.Chrome(executable_path=path, options=chrome_option)
# driver_obj.get("https://www.facebook.com/")
# driver_obj.maximize_window()
# driver_obj.implicitly_wait(30)

#from DATA import reading_objects
#notifications=reading_objects.read_locators()
#print(notifications)

from selenium import webdriver
from LIBRARY.config import Config
from DATA.reading_objects import ReadExcel
import re
import time
import pytest

# chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument("--disable-notification")
#
# chrome_option.add_argument("--disable-infobars")
#
# chrome_option.add_argument("start-maximized")
#
# chrome_option.add_argument("--disable-extensions")
#
# chrome_option.add_experimental_option("prefs",{"profile.default_content_setting_values.notifications": 2})
#
# chrome_option.add_argument("use-fake-ui-for-media-stream")
# time.sleep(3)

class  Notification:
    obj_1=ReadExcel()
    locator_n=obj_1.read_locator(Config.notification_sheet)



    def __init__(self,driver):
        self.driver=driver
    def enter_email(self,email):
         locator=self.locator_n["fb_email"]
         self.driver.find_element(*locator).send_keys(email)

    def enter_pwd(self,password):
        locator=self.locator_n["fb_password"]
        self.driver.find_element(*locator).send_keys(password)
    def click_login(self):
        locator=self.locator_n["fb_login"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    # def icon_display(self):
    #     locator = self.locator_n["fb_notification icon"]
    #     self.driver.find_element(*locator)

    def icon_click(self):
         locator = self.locator_n["fb_notification icon_click"]
         self.driver.find_element(*locator).click()
         time.sleep(2)

    def click_seeall_option(self):
        locator = self.locator_n["notification_see all"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def all_option_click(self):
        locator = self.locator_n["all_option"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    def unread(self):
        locator = self.locator_n["unread"]
        self.driver.find_element(*locator).click()
        time.sleep(2)

    # def like_img(self):
    #     locator = self.locator_n["like_img"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(2)
    #
    # def comment_img(self):
    #     locator = self.locator_n["comment"]
    #     self.driver.find_element(*locator).click()
    #     time.sleep(2)
    #
    # def display_time(self):
    #         locator = self.locator_n["display_time"]
    #         self.driver.find_element(*locator).display()
    #         time.sleep(2)

# fn=Notification()
# fn.enter_email()
# fn.enter_pwd()
# fn.click_login()
# fn.icon_display()
# fn.icon_click()
# fn.click_seeall_option()
# fn.all_option_click()
#fn.unread()
# fn.like_img()
# fn.comment_img()
# fn.display_time()










    # driver_obj.find_element_by_name("email").send_keys("Sravanii P")
    #     self.driver_obj.find_element(["fb_email"]).send_keys("Sravanii P")
    # def enter_pwd(self):
    #      # driver_obj.find_element_by_id("pass").send_keys("Sravani@7")
    #       driver_obj.find_element(*notifications["fb_password"]).send_keys("Sravani@7")
    # def click_login(self):
    #      driver_obj.find_element_by_name("login").click()
    # def icon_display(self):
    #     driver_obj.find_element("xpath",'//span[@class="x6s0dn4 x3nfvp2 x5yr21d xl56j7k xexx8yu x1mpkggp x18d9i69 x1t2a60a xh8yej3 xtk6v10"]')
    # def icon_click(self):
    #     driver_obj.find_element("xpath",'//a[@href="/notifications/"]').click()
    # def click_seeall_option(self):
    #     driver_obj.find_element("xpath","//span[text()='See all']").click()
    # def like_img(self):
    #     driver_obj.find_element("xpath",'//img[@class="x1b0d499 xl1xv1r"]')
    # def comment_img(self):
    #     driver_obj.find_element("xpath",'//i[@class="x1b0d499 xl1xv1r"]')
    # def display_time(self):
    #     driver_obj.find_element("xpath",'//span[@class="x3nfvp2 xwnonoy x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x1kpxq89 xsmyaan x972fbf xcfux6l x1qhh985 xm0m39n x14yjl9h xudhj91 x18nykt9 xww2gxu"]')
    # def all_option_click(self):
    #     driver_obj.find_element("xpath",'//span[text()="All"]').click()
    # def unread_option_click(self):
    #     driver_obj.find_element("xpath",'//span[text()="Unread"]').click()


#
# fn=Notification()
# fn.enter_email()
# fn.enter_pwd()
# fn.click_login()
# # fn.icon_display()
# fn.icon_click()
# fn.click_seeall_option()
# fn.like_img()
# fn.comment_img()
# fn.display_time()
# fn.all_option_click()
# fn.unread_option_click()
