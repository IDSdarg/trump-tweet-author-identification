from bs4 import BeautifulSoup


def clean_up_text(df, column):
    '''
    takes a DataFrame and a column name containing text and cleans up unicode
    characters, then outputs each text cell as an element in a list
    INPUT: DataFrame, string
    OUTPUT: list of strings
    '''

    tweets = []
    for tweet in testing['text']:
        soup = BeautifulSoup(str(tweet.encode("utf8")))
        tweets.append(soup.text)
    return tweets