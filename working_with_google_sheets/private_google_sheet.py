import gspread
import re
gc = gspread.service_account('secrets.json')

spreadsheet = gc.open("Test_Sheet")

ws1 = spreadsheet.get_worksheet(0)

all_data = ws1.get_all_records()  # get all records

data_range = ws1.get_values("A5:F7") # Get data range

cols = ws1.col_values(2) # Get column values

rows = ws1.row_values(2) # Get row values

# Get a cell value
cell2 = ws1.acell('D5').value

# Search for a cell
cell3 = ws1.find('14')

#print(cell3.row, cell3.col)

# Search for many cells
cells = ws1.findall('12')

# Search cells using regex
regex = re.compile(r'99')
cells_2 = ws1.findall(regex)

print(cells_2)