from pytest_bdd import scenarios, given, when, then, parsers
from src.pages.login_page import LoginPage

# Load all scenarios from the feature file
scenarios('../features/login.feature')

@given('I open the login page', target_fixture='login_page')
def open_login_page(driver):
    page = LoginPage(driver)
    page.load()
    return page

@when(parsers.parse('I enter username "{username}" and password "{password}"'))
def enter_credentials(login_page, username, password):
    login_page.login(username, password)

@when('I click the login button')
def click_login(login_page):
    login_page.submit()

@then('I should see a success message')
def should_see_success(login_page):
    message = login_page.flash_message.text
    assert "You logged into a secure area!" in message

@then('I should see an error message')
def should_see_error(login_page):
    message = login_page.flash_message.text
    assert "Your password is invalid!" in message
