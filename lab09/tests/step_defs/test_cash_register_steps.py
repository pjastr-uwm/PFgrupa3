from pytest_bdd import scenarios, given, when, then, parsers
import pytest
from src.cash_register import CashRegister

# Load scenarios from the feature file
scenarios('../features/cash_register.feature')

# Fixtures
@pytest.fixture
def cash_register():
    return CashRegister()

@pytest.fixture
def test_context():
    """Context to store test-specific values"""
    return {}

# Given steps
@given("a new cash register")
def new_cash_register(cash_register):
    """Create a new cash register instance."""
    return cash_register

@given(parsers.parse('I add item "{name}" with price {price:f}'))
def given_add_item(cash_register, name, price):
    """Add an item to the cash register."""
    cash_register.add_item(name, price)

# When steps
@when(parsers.parse('I add item "{name}" with price {price:f}'))
def when_add_item(cash_register, name, price):
    """Add an item to the cash register."""
    cash_register.add_item(name, price)

@when(parsers.parse('I apply a {percentage:d} percent discount'))
def apply_discount(cash_register, test_context, percentage):
    """Apply a discount percentage."""
    test_context['discount_amount'] = cash_register.apply_discount(percentage)

@when('I calculate the total with tax')
def calculate_with_tax(cash_register, test_context):
    """Calculate the total with tax."""
    test_context['final_amount'] = cash_register.calculate_total_with_tax()

@when(parsers.parse('I try to add item "{name}" with price {price:f}'))
def try_add_invalid_item(cash_register, test_context, name, price):
    """Try to add an item with an invalid price."""
    with pytest.raises(ValueError) as excinfo:
        cash_register.add_item(name, price)
    test_context['error_message'] = str(excinfo.value)

@when(parsers.parse('I try to apply a {percentage:d} percent discount'))
def try_apply_invalid_discount(cash_register, test_context, percentage):
    """Try to apply an invalid discount."""
    with pytest.raises(ValueError) as excinfo:
        cash_register.apply_discount(percentage)
    test_context['error_message'] = str(excinfo.value)

# Then steps
@then(parsers.parse('the total should be {expected:f}'))
def check_total(cash_register, expected):
    """Verify the total amount."""
    assert cash_register.total == pytest.approx(expected, 0.01)

@then(parsers.parse('the receipt should contain "{expected_text}"'))
def check_receipt_content(cash_register, expected_text):
    """Verify receipt contains expected text."""
    receipt = cash_register.get_receipt()
    assert expected_text in receipt

@then(parsers.parse('the discount amount should be {expected:f}'))
def check_discount_amount(test_context, expected):
    """Verify the discount amount."""
    assert 'discount_amount' in test_context, "Discount was not applied in the test"
    assert test_context['discount_amount'] == pytest.approx(expected, 0.01)

@then(parsers.parse('the final amount should be {expected:f}'))
def check_final_amount(test_context, expected):
    """Verify the final amount with tax."""
    assert 'final_amount' in test_context, "Total with tax was not calculated in the test"
    assert test_context['final_amount'] == pytest.approx(expected, 0.01)

@then('I should get a price error message')
def check_price_error(test_context):
    """Verify the price error message is received."""
    assert 'error_message' in test_context, "No error was caught in the test"
    assert "Price must be greater than zero" in test_context['error_message']

@then('I should get a discount error message')
def check_discount_error(test_context):
    """Verify the discount error message is received."""
    assert 'error_message' in test_context, "No error was caught in the test"
    assert "Discount must be between 0 and 100" in test_context['error_message']

@when('I calculate the discounted total with tax')
def calculate_discounted_total_with_tax(cash_register, test_context):
    """Calculate the total with tax after discount has been applied."""
    test_context['final_discounted_amount'] = cash_register.calculate_total_with_tax()


@then(parsers.parse('the final amount after discount and tax should be {expected:f}'))
def check_final_discounted_amount(test_context, expected):
    """Verify the final amount after discount and tax."""
    assert 'final_discounted_amount' in test_context, "Discounted total with tax was not calculated in the test"
    assert test_context['final_discounted_amount'] == pytest.approx(expected, 0.01)