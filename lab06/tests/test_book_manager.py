import unittest
from src.book_manager import BookManager


class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()

    def test_add_book(self):
        # Test adding a new book
        result = self.manager.add_book("B001", "Python Programming", "John Smith")
        self.assertTrue(result)
        self.assertEqual(len(self.manager.books), 1)

        # Test adding a duplicate book
        result = self.manager.add_book("B001", "Python Again", "Jane Doe")
        self.assertFalse(result)
        self.assertEqual(len(self.manager.books), 1)

    def test_remove_book(self):
        # Add a book first
        self.manager.add_book("B001", "Python Programming", "John Smith")

        # Test removing the book
        result = self.manager.remove_book("B001")
        self.assertTrue(result)
        self.assertEqual(len(self.manager.books), 0)

        # Test removing a non-existent book
        result = self.manager.remove_book("B002")
        self.assertFalse(result)

    def test_register_user(self):
        # Test registering a new user
        result = self.manager.register_user("U001", "Alice Brown")
        self.assertTrue(result)
        self.assertEqual(len(self.manager.users), 1)

        # Test registering a duplicate user
        result = self.manager.register_user("U001", "Alice Again")
        self.assertFalse(result)
        self.assertEqual(len(self.manager.users), 1)

    def test_borrow_book(self):
        # Add a book and register a user
        self.manager.add_book("B001", "Python Programming", "John Smith")
        self.manager.register_user("U001", "Alice Brown")

        # Test borrowing the book
        result = self.manager.borrow_book("B001", "U001")
        self.assertTrue(result)
        self.assertFalse(self.manager.books["B001"]["available"])
        self.assertEqual(len(self.manager.users["U001"]["books"]), 1)

        # Test borrowing a non-existent book
        result = self.manager.borrow_book("B002", "U001")
        self.assertFalse(result)

        # Test borrowing with a non-existent user
        result = self.manager.borrow_book("B001", "U002")
        self.assertFalse(result)

        # Test borrowing an unavailable book
        result = self.manager.borrow_book("B001", "U001")
        self.assertFalse(result)

    def test_return_book(self):
        # Add a book, register a user, and borrow the book
        self.manager.add_book("B001", "Python Programming", "John Smith")
        self.manager.register_user("U001", "Alice Brown")
        self.manager.borrow_book("B001", "U001")

        # Test returning the book
        result = self.manager.return_book("B001", "U001")
        self.assertTrue(result)
        self.assertTrue(self.manager.books["B001"]["available"])
        self.assertEqual(len(self.manager.users["U001"]["books"]), 0)

        # Test returning a non-existent book
        result = self.manager.return_book("B002", "U001")
        self.assertFalse(result)

        # Test returning with a non-existent user
        result = self.manager.return_book("B001", "U002")
        self.assertFalse(result)

    def test_get_available_books(self):
        # Add some books
        self.manager.add_book("B001", "Python Programming", "John Smith")
        self.manager.add_book("B002", "Java Programming", "Jane Doe")

        # Test getting available books
        available_books = self.manager.get_available_books()
        self.assertEqual(len(available_books), 2)

        # Borrow a book
        self.manager.register_user("U001", "Alice Brown")
        self.manager.borrow_book("B001", "U001")

        # Test getting available books after borrowing
        available_books = self.manager.get_available_books()
        self.assertEqual(len(available_books), 1)
        self.assertEqual(available_books[0]["id"], "B002")

    def test_get_user_books(self):
        # Register a user
        self.manager.register_user("U001", "Alice Brown")

        # Test getting books for a user with no books
        user_books = self.manager.get_user_books("U001")
        self.assertEqual(len(user_books), 0)

        # Add a book and borrow it
        self.manager.add_book("B001", "Python Programming", "John Smith")
        self.manager.borrow_book("B001", "U001")

        # Test getting books for a user with books
        user_books = self.manager.get_user_books("U001")
        self.assertEqual(len(user_books), 1)
        self.assertEqual(user_books[0]["id"], "B001")

        # Test getting books for a non-existent user
        user_books = self.manager.get_user_books("U002")
        self.assertIsNone(user_books)

    def test_search_books(self):
        # Add some books
        self.manager.add_book("B001", "Python Programming", "John Smith")
        self.manager.add_book("B002", "Java Programming", "Jane Doe")
        self.manager.add_book("B003", "Python Advanced", "John Smith")

        # Test searching by title
        results = self.manager.search_books("Python")
        self.assertEqual(len(results), 2)

        # Test searching by author
        results = self.manager.search_books("Jane")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "B002")

        # Test searching with no results
        results = self.manager.search_books("C++")
        self.assertEqual(len(results), 0)