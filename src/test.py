import random
import csv
import numpy as np
from data import get_data_dtc


def get_error_names(n_erros):
    codes = []
    error = []
    with open("data/obd-trouble-codes.csv", "r") as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            codes.append(row[0])
    for i in range(n_erros):
        error.append(np.random.choice(codes))
    return error


def car_values():
    rmp = random.randrange(0, 4000)
    railPresure = random.randrange(0, 200)
    boostPresure = random.randrange(0, 100)
    dtc = True
    error = []
    n_erros = random.randrange(0, 3)
    if dtc is True:
        json = get_data_dtc(get_error_names(n_erros))
        print(json)
        for i in range(len(json)):
            error.append(json[i]["desc"])
    print(error)


if __name__ == "__main__":
    car_values()
