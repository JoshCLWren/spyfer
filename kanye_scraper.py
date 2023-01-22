"""Script to Scrape Quotes from the kanye west API. And save them to a file."""

import requests


def get_quote():
    """Get a quote from the kanye west API."""
    return requests.get("https://api.kanye.rest").json()["quote"]


def main():
    """Main function."""
    with open("kanye_quotes.csv", "w") as file:
        # Write the header
        file.write("number,quote\n")
        for i in range(1, 1001):
            quote = get_quote()
            # strip the quotes of punctuation
            quote = quote.replace('"', "").replace(",", "")
            print(f"Quote #{i}: {quote}")
            file.write(f"{i},{quote} \n")


if __name__ == "__main__":
    main()
