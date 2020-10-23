from subprocess import Popen
from pywinauto import Desktop

Popen('calc.exe', shell=True)
dlg = Desktop(backend="uia").Калькулятор
dlg.window(auto_id='num8Button', control_type='Button')
dlg.wait('visible')