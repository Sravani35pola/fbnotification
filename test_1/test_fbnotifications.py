import pytest
from DATA.reading_objects import ReadExcel
from POM.fb_notifications import Notification
from LIBRARY.config import Config

class TestNotification:
    read_xl=ReadExcel()
    data=read_xl.read_test_data(Config.fb_testdata_sheet)

    @pytest.mark.parametrize("email,password",data)
    def test_fbnotifications(self,email,password,_driver):
         fn = Notification(_driver)
         fn.enter_email(email)
         fn.enter_pwd(password)
         fn.click_login()
         # fn.icon_display()
         fn.icon_click()
         fn.click_seeall_option()
         fn.all_option_click()
         fn.unread()
         # fn.like_img()
         # fn.comment_img()
         # fn.display_time()
