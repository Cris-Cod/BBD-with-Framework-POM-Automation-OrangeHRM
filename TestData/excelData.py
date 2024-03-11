import openpyxl
import os


def getTestData():
    path = os.getcwd()
    book = openpyxl.load_workbook(f"{path}\\data.xlsx")
    sheet = book.active
    data_comb = []
    cell = sheet.cell(row=2, column=1)
    print(cell.value)
    print(sheet.max_row)
    print(sheet.max_column)

    for row in sheet.iter_rows(min_row=2, max_row=sheet.max_row, min_col=1, max_col=2, values_only=True):
        username, password = row
        print(f"Username: {username}, Password: {password}")
        data_comb.append((username, password))
        print(data_comb)

    return  data_comb

print(getTestData())

