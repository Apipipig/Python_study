import  openpyxl, pprint
print('Opening book...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}
# TODO: Fill in countyData with each county's population and tracts.
print('Reading rows...')
for row in range(2, sheet.get_highest_row() + 1):
    # Each row in the spreadsheet has data for one census tract.
    State = sheet['B' + str(row)].value
