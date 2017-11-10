"""
Database fake interface
"""
from datetime import datetime
from random import randint


def get_report_data():
    """
    Responsible to produce some data in this style
    [
        ["placa", "data", "data", "codigo_infracao", "desdobramento", "valor"]
    ]
    """
    data = []

    for index in range(10):
        data.append(["OGF{}".format(randint(1000, 9999)),
                     datetime.now(), datetime.now(), randint(100, 999),
                     randint(0, 9), float(randint(10, 500))
                    ])

    return data
