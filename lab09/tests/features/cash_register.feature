Feature: Cash Register Operations
  As a cashier
  I want to use a cash register
  So that I can process customer purchases

  Background:
    Given a new cash register

  Scenario: Add single item to cash register
    When I add item "Coffee" with price 5.99
    Then the total should be 5.99
    And the receipt should contain "Coffee: $5.99"

  Scenario: Add multiple items to cash register
    When I add item "Coffee" with price 5.99
    And I add item "Sandwich" with price 7.50
    Then the total should be 13.49
    And the receipt should contain "Coffee: $5.99"
    And the receipt should contain "Sandwich: $7.50"

  Scenario: Apply discount to purchase
    Given I add item "Book" with price 30.00
    When I apply a 10 percent discount
    Then the total should be 27.00
    And the discount amount should be 3.00

  Scenario: Calculate total with tax
    Given I add item "Book" with price 100.00
    When I calculate the total with tax
    Then the final amount should be 123.00

  Scenario: Handle invalid price
    When I try to add item "Invalid" with price -5.00
    Then I should get a price error message

  Scenario: Handle invalid discount
    Given I add item "Book" with price 100.00
    When I try to apply a 150 percent discount
    Then I should get a discount error message

  Scenario Outline: Apply various discounts and calculate total with tax
    Given I add item "<item_name>" with price <price>
    When I apply a <discount> percent discount
    And I calculate the discounted total with tax
    Then the final amount after discount and tax should be <expected_total>

    Examples:
      | item_name    | price  | discount | expected_total |
      | Laptop       | 1000.00 | 20      | 984.00        |
      | TV           | 500.00  | 10      | 553.50        |
      | Phone        | 300.00  | 15      | 313.05        |
      | Headphones   | 80.00   | 5       | 93.48         |
      | Tablet       | 250.00  | 0       | 307.50        |