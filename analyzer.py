import pandas as pd

def analyze_data():
    # pandas okuma yaparken her türlü DataFrame döndürür ekstradan dataframe ataması yapmana gerek yok
    data=pd.read_csv('kayit.csv', names=['zaman', 'yüz sayisi'])
    return data


