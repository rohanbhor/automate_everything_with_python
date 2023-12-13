import gspread
import re
from time import sleep

gc = gspread.service_account('secrets.json')

spreadsheet = gc.open("Test_Sheet")

ws1 = spreadsheet.get_worksheet(0)
ws2 = spreadsheet.get_worksheet(1) # sheet name : Watch


while True:
    value1 = ws1.acell('E21').value
    sleep(2)
    value2 = ws1.acell('E21').value
    if value1 != value2:
        ws2.update('A1', "CHANGED")

