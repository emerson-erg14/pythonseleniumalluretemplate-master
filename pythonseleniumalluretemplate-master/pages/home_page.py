from selenium.webdriver.common.by import By
from bases.page_base import PageBase


class HomePage(PageBase):

    USUARIO_TEXTAREA = (By.XPATH, "//td[@class='login-info-left']//following::span[text()='templateautomacao']")

    def get_logged_user(self):
        return self.get_text(self.USUARIO_TEXTAREA)
