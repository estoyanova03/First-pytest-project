from Pages.base_page import BasePage
from Utilities.locators import ChangePasswordLocatorFields
from Pages.my_account_page import MyAccountPage

class ChangePasswordPage(BasePage):

    def __init__(self, driver):
        self.locate = ChangePasswordLocatorFields
        super().__init__(driver)

    def change_password(self, password, confirm_password):
        self.set(self.locate.password_field, password)
        self.set(self.locate.confirm_password_field, confirm_password)
        self.click(self.locate.continue_button)
        return MyAccountPage(self.driver)
    
    def get_confirmation_error_message(self):
        return self.get_text(self.locate.confirmation_error_message)