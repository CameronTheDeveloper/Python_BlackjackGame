#!/usr/bin/env python3
FILENAME = "balSaved.txt"

def write_bal(bal):
    try:
        with open("balSaved.txt", "w") as file:
            file.write((str(bal)))
    except FileNotFoundError:
        print("Data file missing! resetting starting amount to 1000")
        bal = 1000.0

def read_bal():
    try:
        with open(FILENAME, "r") as file:
            line=file.readline()

        bal = float(line)
        return bal
    except FileNotFoundError:
        print("Data file missing! resetting starting amount to 1000")
        bal = 1000.0
        return bal