class BookManager:
    def __init__(self):
        self.books = {}
        self.users = {}
        self.borrowed_books = {}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            return False

        self.books[book_id] = {
            'title': title,
            'author': author,
            'available': True
        }
        return True

    def remove_book(self, book_id):
        if book_id not in self.books:
            return False

        if not self.books[book_id]['available']:
            return False

        del self.books[book_id]
        return True

    def register_user(self, user_id, name):
        if user_id in self.users:
            return False

        self.users[user_id] = {
            'name': name,
            'books': []
        }
        return True

    def borrow_book(self, book_id, user_id):
        if book_id not in self.books:
            return False

        if user_id not in self.users:
            return False

        if not self.books[book_id]['available']:
            return False

        self.books[book_id]['available'] = False
        self.users[user_id]['books'].append(book_id)

        if user_id not in self.borrowed_books:
            self.borrowed_books[user_id] = []

        self.borrowed_books[user_id].append(book_id)
        return True

    def return_book(self, book_id, user_id):
        if book_id not in self.books:
            return False

        if user_id not in self.users:
            return False

        if book_id not in self.users[user_id]['books']:
            return False

        self.books[book_id]['available'] = True
        self.users[user_id]['books'].remove(book_id)

        if user_id in self.borrowed_books and book_id in self.borrowed_books[user_id]:
            self.borrowed_books[user_id].remove(book_id)

            # This branch is never tested
            if not self.borrowed_books[user_id]:
                del self.borrowed_books[user_id]

        return True

    def get_available_books(self):
        available = []
        for book_id, book in self.books.items():
            if book['available']:
                available.append({
                    'id': book_id,
                    'title': book['title'],
                    'author': book['author']
                })
        return available

    def get_user_books(self, user_id):
        if user_id not in self.users:
            return None

        user_books = []
        for book_id in self.users[user_id]['books']:
            if book_id in self.books:
                user_books.append({
                    'id': book_id,
                    'title': self.books[book_id]['title'],
                    'author': self.books[book_id]['author']
                })
        return user_books

    def search_books(self, query):
        results = []
        if not query:
            return results

        query = query.lower()
        for book_id, book in self.books.items():
            if (query in book['title'].lower() or
                    query in book['author'].lower()):
                results.append({
                    'id': book_id,
                    'title': book['title'],
                    'author': book['author'],
                    'available': book['available']
                })
        return results