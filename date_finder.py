import csv
from datetime import datetime
with open('yourfile.csv') as fin:
    seen_columns = set()
    invalid_columns = set()
    for row in csv.reader(fin):
        for colno, col in enumerate(row, 1):
            if colno in invalid_columns:
                continue
            seen_columns.add(colno)
            try:
                datetime.strptime(col, '%m/%d/%y')
            except ValueError:
                invalid_columns.add(colno)
    valid_columns = seen_columns - invalid_columns