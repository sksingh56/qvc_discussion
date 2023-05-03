import pytest
import pandas as pd
import numpy as np


"""
The conftest.py file is to share fixtures, configurations, and plugins among multiple test files.

Fixtures feature of pytest allows to share setup and teardown code across multiple tests.
"""


@pytest.fixture(scope="module")
def nest_dict_data_q1():
    """
    The dictionary to be used for testing the logic
    """
    data = {
        "key11": {
            "key21": "a",
            "key22": "b",
        },
        "key12": "c",
        "key13": {
            "key31": "d",
            "key32": {
                "key21": "e",
                "key22": "f",
            },
        },
    }
    return data


@pytest.fixture(scope="module")
def nest_dict_data_q2():
    """
    The dictionary to be used for testing the logic
    """

    data = {
        "key11": {
            "key21": "a",
            "key22": "b",
        },
        "key12": "c",
        "key13": {
            "key31": "d",
            "key32": {
                "key21": "e",
                "key22": "f",
            },
        },
        "key14": [1, 2, 3],
        1: (2, 3),
    }
    return data


@pytest.fixture(scope="module")
def expected_result_dict_q1():
    """
    The dictionary to be used for testing output of the expected result
    """
    return {
        "key11": {"key21": "aa", "key22": "bb"},
        "key12": "cc",
        "key13": {"key31": "dd", "key32": {"key21": "ee", "key22": "ff"}},
    }


@pytest.fixture(scope="module")
def expected_result_dict_q2():
    """
    The dictionary to be used for testing output of the expected result
    """

    return {
        "key11": {"key21": "aa", "key22": "bb"},
        "key12": "cc",
        "key13": {"key31": "dd", "key32": {"key21": "ee", "key22": "ff"}},
        "key14": [1, 2, 3, 1, 2, 3],
        1: (2, 3, 2, 3),
    }


@pytest.fixture(scope="module")
def retail_data():
    data = [
        {  # 0
            "skn": "302129",
            "dropship": False,
            "date": pd.Timestamp("2023-04-23"),
            "sales_per_day": 10,
            "price": 13,
            "current_stock": 200,
            "date_new_stock_arrival": pd.Timestamp("2023-06-03"),
            "new_stock": 300,
            "reorder": True,
            "days_stock_age": 90,
        },
        {  # 1
            "skn": "332121",
            "dropship": True,
            "date": pd.Timestamp("2023-04-23"),
            "sales_per_day": 5,
            "price": 150,
            "current_stock": 20,
            "date_new_stock_arrival": pd.Timestamp("2023-05-10"),
            "new_stock": 10,
            "reorder": True,
            "days_stock_age": 100,
        },
        {  # 2
            "skn": "112124",
            "dropship": False,
            "date": pd.Timestamp("2023-04-23"),
            "sales_per_day": 2,
            "price": 1000,
            "current_stock": 100,
            "date_new_stock_arrival": pd.Timestamp("2023-05-15"),
            "new_stock": 10,
            "reorder": True,
            "days_stock_age": 20,
        },
        {  # 3
            "skn": "192123",
            "dropship": False,
            "date": pd.Timestamp("2023-04-23"),
            "sales_per_day": 2,
            "price": 29,
            "current_stock": 50,
            "date_new_stock_arrival": pd.Timestamp("2023-05-15"),
            "new_stock": 100,
            "reorder": True,
            "days_stock_age": 120,
        },
        {  # 4
            "skn": "762129",
            "dropship": False,
            "date": pd.Timestamp("2023-04-23"),
            "sales_per_day": 2,
            "price": 77,
            "current_stock": 15,
            "date_new_stock_arrival": pd.Timestamp("2023-05-05"),
            "new_stock": 10,
            "reorder": True,
            "days_stock_age": 10,
        },
        {  # 5
            "skn": "762134",
            "dropship": False,
            "date": pd.Timestamp("2023-04-23"),
            "sales_per_day": 2,
            "price": 99,
            "current_stock": 20,
            "date_new_stock_arrival": pd.Timestamp("2023-06-03"),
            "new_stock": 10,
            "reorder": True,
            "days_stock_age": 30,
        },
        {  # 6
            "skn": "762134",
            "dropship": False,
            "date": pd.Timestamp("2023-04-23"),
            "sales_per_day": 2,
            "price": 299,
            "current_stock": 200,
            "date_new_stock_arrival": np.nan,
            "new_stock": 0,
            "reorder": False,
            "days_stock_age": 200,
        },
    ]
    return data
