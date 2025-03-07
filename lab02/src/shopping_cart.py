class ShoppingCart:

    def __init__(self, items):
        if not isinstance(items, list):
            raise TypeError

        for elem in items:
            if not isinstance(elem, str):
                raise ValueError

        self.items = items

    def __str__(self):
        return f"Shopping cart: {self.items}."

    def add_item(self, value):
        if not isinstance(value, str):
            raise ValueError

        self.items.append(value)

    def remove_item(self, index):
        if not isinstance(index, int):
            raise TypeError

        if index < 0 or index >= len(self.items):
            raise IndexError

        self.items.remove(self.items[index])

    def __eq__(self, other):
        return self.items == other.items


if __name__ == "__main__":
    s1 = ShoppingCart([])
    print(s1)
    s1.add_item("Milk")
    s1.add_item("Bread")
    print(s1)
    s1.remove_item(0)
    print(s1)
