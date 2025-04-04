class StringUtils:
    def reverse_string(self, text):
        return text[::-1]

    def count_vowels(self, text):
        vowels = "aeiouAEIOU"
        count = 0
        for char in text:
            if char in vowels:
                count += 1
        return count

    def is_palindrome(self, text):
        cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
        return cleaned_text == cleaned_text[::-1]

    def to_uppercase(self, text):
        return text.upper()

    def to_lowercase(self, text):
        return text.lower()


class ListUtils:
    def find_max(self, numbers):
        if not numbers:
            return None
        return max(numbers)

    def find_min(self, numbers):
        if not numbers:
            return None
        return min(numbers)

    def calculate_average(self, numbers):
        if not numbers:
            return None
        return sum(numbers) / len(numbers)

    def remove_duplicates(self, items):
        return list(set(items))

    def sort_ascending(self, items):
        return sorted(items)

    def sort_descending(self, items):
        return sorted(items, reverse=True)