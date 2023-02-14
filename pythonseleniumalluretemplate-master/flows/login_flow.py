from pages.login_page import LoginPage


class LoginFlow:

    def do_login(self, user, password):
        login_page = LoginPage()

        login_page.type_user(user)
        login_page.type_password(password)
        login_page.click_login()
        received_message = login_page.get_error_message()
        return received_message
