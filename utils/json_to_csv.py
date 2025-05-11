import csv
import pandas as pd
import os

DIRECTORY = os.path.dirname(__file__)
TARGET_FILE = 'todo_db.json'
CSV_TARGET_FILE = 'todo_db1.csv'

TARGET_FILE_ABS = os.path.join(DIRECTORY, TARGET_FILE)
CSV_TARGET_FILE_ABS = os.path.join(DIRECTORY, CSV_TARGET_FILE)
 

with open(TARGET_FILE_ABS, 'r', encoding='utf-8') as input_file:
    df = pd.read_json(input_file)


df.to_csv(CSV_TARGET_FILE_ABS, encoding='utf-8', index=False, quoting=csv.QUOTE_ALL)
