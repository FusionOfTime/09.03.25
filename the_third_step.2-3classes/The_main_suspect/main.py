"""
This module analyzes social network user data to identify users with
a high frequency of forbidden words in their posts.
"""
import re
from collections import namedtuple

User = namedtuple("User", ["name", "speech", "forbidden_words_count"])

class SocialNetworkAnalyzer:
    """
    Analyzes users' speeches in a social network to identify users who
    frequently mention forbidden words.
    """

    def __init__(self):
        """Initializes a SocialNetworkAnalyzer object."""
        self.users = []
        self.max_forbidden_words_count = 0
        self.users_with_max_count = []

    def process_input(self, n):
        """
        Processes input from the user to create User objects and add them
        to the list of users.

        Args:
            n (int): The number of users to process.
        """
        forbidden_words = [
            "Fire", "Bomb", "Hate", "Revolution", "Weapon",
            "Shoot", "Bullet", "Government"
        ]
        for _ in range(n):
            try:
                line = input()
                name, speech = line.split(": ", 1)
                forbidden_words_count = 0  # Calculate forbidden words count.
                words = speech.lower().split()
                for word in words:
                    if word in [w.lower() for w in forbidden_words]:
                        forbidden_words_count += 1
                self.users.append(User(name=name, speech=speech, forbidden_words_count=forbidden_words_count))  # Create the tuple.

            except ValueError:
                print("Ошибка ввода. Проверьте формат ввода.")
                return

    def analyze_users(self):
        """
        Analyzes the users to find the ones with the maximum number of
        forbidden words in their speeches.
        """
        for user in self.users:
            if user.forbidden_words_count > self.max_forbidden_words_count:
                self.max_forbidden_words_count = user.forbidden_words_count
                self.users_with_max_count = [user.name]
            elif (user.forbidden_words_count == self.max_forbidden_words_count and
                  self.max_forbidden_words_count > 0):
                self.users_with_max_count.append(user.name)

    def print_results(self):
        """
        Prints the names of the users with the maximum forbidden word count
        and the count itself.
        """
        if not self.users_with_max_count:
            print("")
            print(0)
            return

        print(" ".join(self.users_with_max_count))
        print(self.max_forbidden_words_count)


def main():
    """
    The main function of the program. Reads input, analyzes users' speeches,
    and prints the results.
    """
    n = int(input())
    analyzer = SocialNetworkAnalyzer()
    analyzer.process_input(n)
    analyzer.analyze_users()
    analyzer.print_results()


if __name__ == "__main__":
    main()