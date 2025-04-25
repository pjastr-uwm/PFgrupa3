class CashRegister:
    def __init__(self):
        self.total = 0.0
        self.items = []
        self.tax_rate = 0.23

    def add_item(self, name, price):
        if price <= 0:
            raise ValueError("Price must be greater than zero")
        self.items.append({"name": name, "price": price})
        self.total += price

    def apply_discount(self, percentage):
        if percentage < 0 or percentage > 100:
            raise ValueError("Discount must be between 0 and 100")
        discount_amount = self.total * (percentage / 100)
        self.total -= discount_amount
        return discount_amount

    def calculate_total_with_tax(self):
        tax_amount = self.total * self.tax_rate
        return self.total + tax_amount

    def get_receipt(self):
        receipt_lines = ["=== RECEIPT ==="]
        for item in self.items:
            receipt_lines.append(f"{item['name']}: ${item['price']:.2f}")
        receipt_lines.append(f"Subtotal: ${self.total:.2f}")
        receipt_lines.append(f"Tax ({self.tax_rate * 100}%): ${self.total * self.tax_rate:.2f}")
        receipt_lines.append(f"Total: ${self.calculate_total_with_tax():.2f}")
        receipt_lines.append("===============")
        return "\n".join(receipt_lines)

    def clear(self):
        self.total = 0.0
        self.items = []