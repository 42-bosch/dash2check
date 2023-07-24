import csv
import pandas as pd
from typing import List


def get_data_dtc(codes: List[str] | str = None):
    if codes is None:
        return []
    with open("data/obd-trouble-codes.csv", "r") as file:
        csvreader = csv.reader(file)
        json = []
        for row in csvreader:
            if (type(codes) is str and codes == row[0]) or (
                type(codes) is list and (row[0] in codes)
            ):
                json.append({"code": row[0], "desc": row[1]})
        return json
