#!/usr/bin/env python
import xlrd

def create_csvdir():
    csv_filepath = "csv/"
    if not os.path.isdir(_filepath):
        if DEBUG == 1:
            print ("\nDEBUG_MSG: DIR 'csv/' doesn't exist.")
        os.makedirs(csv_filepath, exist_ok=True)
    else:
        if DEBUG == 1:
            print ("\nDEBUG_MSG: DIR 'csv/' exists.")
            print ("\nDEBUG_MSG: Deleting 'csv/' DIR.")
        shutil.rmtree(csv_filepath, ignore_errors=True)
        os.makedirs(csv_filepath, exist_ok=True)

def xls_to_csv():

