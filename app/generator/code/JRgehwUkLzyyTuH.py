from pywinauto.application import Application
import openpyxl
class Excel:
    def __init__(self, file_path):
        wb = openpyxl.load_workbook('file_path')
        self.sheet = wb.get_sheet_by_name('Sheet3')

    def get_value(self, position):
        return self.sheet[position].value

app = Application().Start(cmd_line=u'"B:/Program Files (x86)/AbilityCash/AbilityCash.exe" ')
acmw = app[u'AC-MW']
excel = Excel("B:/Program Files (x86)/AbilityCash/AbilityCash.xls")
acmw.Wait('ready')
acdp = acmw[u'AC-E']
acdp.Click()
for VsPrq in range(10):
    acmw.Wait('ready')
    acdp = acmw[u'AC-E']
    acdp.Click()
    acmw[u'AC-E'].set_text('123')
    param = excel.get_value('AVsPrq')
    acmw[u'AC-E'].set_text(param)
    for SxpGy in range(10):
        acmw.Wait('ready')
        acdp = acmw[u'AC-E']
        acdp.Click()
        acmw[u'AC-E'].set_text('123')
        param = excel.get_value('BSxpGy')
        acmw[u'AC-E'].set_text(param)
acmw[u'AC-E'].set_text('123')
param = excel.get_value('A1')
acmw[u'AC-E'].set_text(param)