Feature: User Authentication
  In order to access secure parts of the app
  As a registered user
  I want to log in successfully

  Scenario: Successful login with valid credentials
    Given I open the login page
    When I enter username "tomsmith" and password "SuperSecretPassword!"
    And I click the login button
    Then I should see a success message

  Scenario: Unsuccessful login with invalid password
    Given I open the login page
    When I enter username "tomsmith" and password "wrongpassword"
    And I click the login button
    Then I should see an error message
