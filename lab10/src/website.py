from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def main():
    driver = webdriver.Firefox()
    try:
        driver.get("https://the-internet.herokuapp.com/login")
        # Wyszukiwanie po ID
        username = driver.find_element(By.ID, "username")
        password = driver.find_element(By.ID, "password")
        username.send_keys("tomsmith")
        password.send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button.radius").click()

        # Czekaj na komunikat
        time.sleep(1)
        flash = driver.find_element(By.ID, "flash")
        print("Komunikat po zalogowaniu:", flash.text.strip())
    finally:
        driver.quit()


if __name__ == "__main__":
    main()