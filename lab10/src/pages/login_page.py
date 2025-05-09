from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class LoginPage:
    URL = "https://the-internet.herokuapp.com/login"

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def load(self):
        """Navigate to the login page."""
        self.driver.get(self.URL)

    @property
    def username_input(self):
        return self.driver.find_element(By.ID, "username")

    @property
    def password_input(self):
        return self.driver.find_element(By.ID, "password")

    @property
    def login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, "button.radius")

    @property
    def flash_message(self):
        return self.driver.find_element(By.ID, "flash")

    def login(self, username: str, password: str):
        """Fill in credentials (without submitting)."""
        self.username_input.clear()
        self.username_input.send_keys(username)
        self.password_input.clear()
        self.password_input.send_keys(password)

    def submit(self):
        """Click the login button."""
        self.login_button.click()

