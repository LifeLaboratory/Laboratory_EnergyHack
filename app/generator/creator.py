"""Модуль для генерации кода по входным правилам"""
from string import ascii_letters
from random import choice


class GenerateCode:
    def __init__(self):
        self.operations = {
            'open_file': self.open_file,
            'condition': self.condition,
            'click': self.click,
            'save_value': self.save_value,
            'cycle': self.cycle,
        }
        self.code = [
            'from pywinauto.application import Application'
            '''
import openpyxl
class Excel:
    def __init__(self, file_path):
        wb = openpyxl.load_workbook('file_path')
        self.sheet = wb.get_sheet_by_name('Лист1')

    def get_value(self, position):
        return self.sheet[position].value
'''
        ]

    def create_code(self, struct, indent=0, iterator=None):
        """
        Формирование кода по входной структуре
        :param struct:
        :param indent:
        :param iterator:
        :return:
        """
        for operation in struct:
            self.operations[operation.get('action')](operation, indent, iterator)
        return '\n'.join(self.code)

    def open_file(self, operation, indent, iterator=None):
        """
        Формирование открытия файла
        :param operation:
        :param indent:
        :param iterator:
        :return:
        """
        if 'xls' in operation.get('file_path'):
            self.code.append(f'''{' '*indent}excel = Excel({operation.get('file_path')})''')
        else:
            self.code.append(f'''{' '*indent}app = Application().Start(cmd_line=u'"{operation.get('file_path')}" ')''')
            self.code.append(f'''{' '*indent}acmw = app[u\'AC-MW\']''')

    def condition(self, operation, indent, iterator=None):
        """
        Формирование условий
        :param operation:
        :param indent:
        :param iterator:
        :return:
        """
        self.code.append(f'''{' '*indent}if {operation.get('value')}:''')
        self.code.append(f'''{' '*(indent+4)}raise Exception('Не правильно заполнено поле')''')

    def click(self, operation, indent, iterator=None):
        """
        Формирование клика
        :param operation:
        :param indent:
        :param iterator:
        :return:
        """
        self.code.append(f'''{' ' * indent}acmw.Wait('ready')''')
        self.code.append(f'''{' ' * indent}acdp = acmw[u'{operation.get('object')}']''')
        self.code.append(f'''{' ' * indent}acdp.Click()''')

    def save_value(self, operation, indent, iterator=None):
        """
        Формирование установки значения
        :param operation:
        :param indent:
        :param iterator:
        :return:
        """
        if operation.get('source'):
            self.code.append(f'''{' ' * indent}param = excel.get_value('{operation.get('source')}{str(iterator) if iterator else ''}')''')
            self.code.append(f'''{' ' * indent}acmw[u'{operation.get('object')}'].set_text(param)''')
        elif operation.get('value'):
            self.code.append(f'''{' ' * indent}acmw[u'{operation.get('object')}'].set_text('{operation.get('value')}')''')

    def cycle(self, operation, indent, iterator=None):
        """
        Формирование циклов
        :param operation:
        :param indent:
        :param iterator:
        :return:
        """
        iterator = ''.join([choice(ascii_letters) for _ in range(5)])
        self.code.append(f'''{' ' * indent}for {iterator} in range({operation.get('index')}):''')
        self.create_code(operation.get('for'), indent+4, iterator)
