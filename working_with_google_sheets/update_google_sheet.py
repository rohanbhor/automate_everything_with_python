import gspread
import re
gc = gspread.service_account('secrets.json')

spreadsheet = gc.open("Test_Sheet")

ws1 = spreadsheet.get_worksheet(0)

ws1.update("E2:E20")