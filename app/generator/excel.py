import openpyxl
class Excel:
    def __init__(self, file_path):
        wb = openpyxl.load_workbook('file_path')
        self.sheet = wb.get_sheet_by_name('Лист1')

    def get_value(self, position):
        return self.sheet[position].value