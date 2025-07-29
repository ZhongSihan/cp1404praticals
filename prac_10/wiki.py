"""
CP1404/CP5632 Practical 10
Wikipedia API usage example
"""

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    while True:
        user_input = input("Enter page title: ").strip()
        if not user_input:
            print("Thank you.")
            break

        try:
            # Try to get the page
            page = wikipedia.page(user_input, auto_suggest=False)
            print(f"\n{page.title}")
            print(f"{page.summary}\n")
            print(page.url)
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except PageError:
            print(f'Page id "{user_input}" does not match any pages. Try another id!')
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

