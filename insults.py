import pandas as pd

insults = pd.read_csv("insults.csv")


def get_insult(insults):
    return insults.sample().iloc[0]["insult"]
