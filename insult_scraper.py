"""Using beautiful soup to scrape insults from the web"""

import re

import requests
from bs4 import BeautifulSoup


def get_insults():
    """Get insults from the web"""
    url = "https://prowritingaid.com/art/2287/negative-adjectives.aspx"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    ths = soup.find_all("th")
    master_list = []
    for th in ths:
        master_list.extend([a for a in re.split(r"([A-Z][a-z]*)", th.prettify())])
    return [
        string.lower() for string in master_list if not re.search(r"[^a-zA-Z]", string)
    ]


def main():
    """Main function"""
    with open("insults.csv", "w") as file:
        # Write the header
        file.write("number,insult\n")
        for i, insult in enumerate(get_insults()):
            print(f"Insult #{i}: {insult}")
            file.write(f"{i},{insult} \n")


if __name__ == "__main__":
    main()
