"""
CP1404/CP5632 Practical 10 - Enhanced Wikipedia API Program
This version includes search, suggest, and summary before attempting to load full pages.
"""

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    print("Wikipedia Searcher. Press Enter with no input to quit.\n")

    while True:
        query = input("Enter page title or search phrase: ").strip()
        if not query:
            print("Thank you.")
            break

        # Suggest a better match
        suggestion = wikipedia.suggest(query)
        if suggestion and suggestion.lower() != query.lower():
            print(f"Did you mean: {suggestion}? Using suggested term.\n")
            query = suggestion

        try:
            # Try to get the page object directly
            page = wikipedia.page(query, auto_suggest=False)
            print(f"\n{page.title}")
            print(f"{page.summary}\n")
            print(page.url)

        except DisambiguationError as e:
            print("\nWe need a more specific title. Try one of the following:")
            for option in e.options[:10]:  # limit to first 10 suggestions
                print(f"- {option}")
        except PageError:
            print(f'Page "{query}" does not match any pages. Try another keyword!')
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
