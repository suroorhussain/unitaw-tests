from typing import Iterable

import titanic


def test_number_of_passengers():
    # According to the CSV, there were 891 passengers aboard.
    assert titanic.number_of_passengers() == 891


def test_total_fare_paid():
    # The sum of the fares paid by all passengers. The input data has at most
    # four decimal places. If you had to round your answer, where did the extra
    # places come from?
    assert titanic.total_fare_paid() == 28693.9493


def test_median_fare():
    # The median of the fares paid by all passengers
    assert titanic.median_fare() == 14.4542


def test_cherbourg_survival_rate():
    # Passengers boarded at three different ports before the Atlantic crossing
    # began. Those who boarded at Cherbourg had the best chance of survival at
    # ~55%.
    assert titanic.cherbourg_survival_rate() == (93 / 168)


def test_passenger_class_by_survival():
    # The three passenger classes had very different survival rates; the more
    # you paid, the better your chances.
    actual = titanic.passenger_class_by_survival()
    expected = [1, 2, 3]
    assert isinstance(actual, Iterable)
    assert list(actual) == expected
