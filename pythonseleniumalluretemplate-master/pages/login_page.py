from selenium.webdriver.common.by import By
from bases.page_base import PageBase


class LoginPage(PageBase):

    USUARIO_FIELD = (By.NAME, "username")
    SENHA_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//*[@class = 'button' and @value='Login']")
    ERRO_TEXTAREA = (By.XPATH, "//*[contains(text(),'may be disabled or blocked')]")

    def type_user(self, user):
        self.send_Keys(self.USUARIO_FIELD, user)

    def type_password(self, password):
        self.send_Keys(self.SENHA_FIELD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERRO_TEXTAREA)


