"""
Hello from LivePreso :) This is the file you should be editing. Good luck!
"""
import pandas as pd

path = "./titanic.csv"

df = pd.read_csv(path)

def number_of_passengers():
    return len(df)


def total_fare_paid():
    return df["Fare"].sum()


def median_fare():
    return df["Fare"].median()


def cherbourg_survival_rate():
    cherbourg_passangers = df[df["Embarked"] == "C"]
    cherbourg_survivors = cherbourg_passangers[cherbourg_passangers["Survived"] == 1]
    return len(cherbourg_survivors) / len(cherbourg_passangers)


def passenger_class_by_survival():
    class_survival = df.groupby("Pclass")["Survived"].mean().sort_values(ascending=False)
    return class_survival.index.to_list()
