# -*- coding: utf-8 -*-
"""Модуль для генерации кода по входным правилам"""
from string import ascii_letters
from random import choice
from subprocess import call
import os


class GenerateCode:
    def __init__(self):
        self.operations = {
            'open_file': self._open_file,
            'condition': self._condition,
            'click': self._click,
            'fill_field': self._fill_field,
            'cycle': self._cycle,
        }
        self.excel = False
        self.prefix = ''
        self.code = [
            'from pywinauto.application import Application'
            '''
import openpyxl
class Excel:
    def __init__(self, file_path):
        wb = openpyxl.load_workbook('file_path')
        self.sheet = wb.get_sheet_by_name('Sheet3')

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
            self.operations[operation.get('category')](operation, indent, iterator)
        return '\n'.join(self.code)

    def create_file(self, struct):
        """
        Метод для формирования exe файла по сформированному коду
        :param struct:
        :return:
        """
        code = self.create_code(struct)
        file_name = ''.join([choice(ascii_letters) for _ in range(15)])
        abspath = os.path.abspath(os.path.dirname(__file__))
        with open(os.path.join(abspath, f'code\\{file_name}.py'), 'wb') as f:
            f.write(code.encode())
        file_py = os.path.join(abspath, f'code\\{file_name}.py')
        call(f'pyinstaller --onefile {file_py} -n task_{file_name}.exe', shell=True)
        os.remove(f'task_{file_name}.exe.spec')
        return f'task_{file_name}.exe'

    def _open_file(self, operation, indent, iterator=None):
        """
        Формирование открытия файла
        :param operation:
        :param indent:
        :param iterator:
        :return:
        """
        if 'xls' in operation.get('file_path') or 'xlsx' in operation.get('file_path'):
            self.code.append(f'''{' '*indent}excel = Excel("{operation.get('file_path')}")''')
            self.excel = True
        else:
            self.code.append(f'''{' '*indent}app = Application().Start(cmd_line=u'"{operation.get('file_path')}" ')''')
            self.code.append(f'''{' '*indent}acmw = app[u\'AC-MW\']''')

    def _condition(self, operation, indent, iterator=None):
        """
        Формирование условий
        :param operation:
        :param indent:
        :param iterator:
        :return:
        """
        self.code.append(f'''{' '*indent}if {operation.get('value')}:''')
        self.code.append(f'''{' '*(indent+4)}raise Exception('Не правильно заполнено поле')''')
        # self.create_code(operation.get('if'), indent+4, iterator)

    def _click(self, operation, indent, iterator=None):
        """
        Формирование клика
        :param operation:
        :param indent:
        :param iterator:
        :return:
        """
        self.code.append(f'''{' ' * indent}acmw.Wait('ready')''')
        if '->' in operation.get('object'):
            self.code.append(f'''{' ' * indent}acdp = app[u'AC-MW'].MenuItem(u'{operation.get('object')}')''')
            if 'Insert' in operation.get('object'):
                self.prefix = '.Dialog'
        else:
            self.code.append(f'''{' ' * indent}acdp = app[u'{operation.get('object')}']''')
        self.code.append(f'''{' ' * indent}acdp.Click()''')

    def _fill_field(self, operation, indent, iterator=None):
        """
        Формирование установки значения
        :param operation:
        :param indent:
        :param iterator:
        :return:
        """
        if operation.get('source'):
            if not self.excel:
                raise Exception('Не задан EXCEL файл')
            self.code.append(f'''{' ' * indent}param = excel.get_value('{operation.get('source')}{str(iterator) if iterator else ''}')''')
            self.code.append(f'''{' ' * indent}app{self.prefix}[u'{operation.get('object')}'].type_keys(param)''')
        elif operation.get('value'):
            self.code.append(f'''{' ' * indent}app[u'{operation.get('object')}'].type_keys('{operation.get('value')}')''')

    def _cycle(self, operation, indent, iterator=None):
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
