#!/usr/bin/env python
import xlrd
import csv
import os

csv_filepath = "csv/"
xls_filepath = "xls/"

DEBUG = 1

def create_csvdir():
    if not os.path.isdir(csv_filepath):
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
    for xls in os.listdir(xls_filepath):
        if os.path.isfile(os.path.join(xls_filepath, xls)):
            xlsfile = xlrd.open_workbook(os.path.join(xls_filepath, xls))
            xlssheet = xlsfile.sheet_by_index(0)
            xlsname = xls.split('.')[0]
            csvfile = open(os.path.join(csv_filepath, (xlsname + '.csv')), 'w', encoding='utf8')
            csvwrite = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            for rownum in range(xlssheet.nrows):
                csvwrite.writerow(xlssheet.row_values(rownum))
            csvfile.close()
            #break
            #print(xls)

