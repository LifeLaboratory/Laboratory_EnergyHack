"""Модуль для генерации кода по входным правилам"""


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
        ]

    def create_code(self, struct, indent=0):
        """
        Формирование кода по входной структуре
        :param struct:
        :param indent:
        :return:
        """
        for operation in struct:
            self.operations[operation.get('action')](operation, indent)
        return '\n'.join(self.code)

    def open_file(self, operation, indent):
        """
        Формирование открытия файла
        :param operation:
        :param indent:
        :return:
        """
        self.code.append(f'''{' '*indent}app = Application().Start(cmd_line=u'"{operation.get('file_path')}" ')''')
        self.code.append(f'''{' '*indent}acmw = app[u\'AC-MW\']''')

    def condition(self, operation, indent):
        """
        Формирование условий
        :param operation:
        :param indent:
        :return:
        """
        self.code.append(f'''{' '*indent}if {operation.get('value')}:''')
        self.code.append(f'''{' '*(indent+4)}raise Exception('Не правильно заполнено поле')''')

    def click(self, operation, indent):
        """
        Формирование клика
        :param operation:
        :param indent:
        :return:
        """
        self.code.append(f'''{' ' * indent}acmw.Wait('ready')''')
        self.code.append(f'''{' ' * indent}acdp = acmw[u'{operation.get('object')}']''')
        self.code.append(f'''{' ' * indent}acdp.Click()''')

    def save_value(self, operation, indent):
        """
        Формирование установки значения
        :param operation:
        :param indent:
        :return:
        """
        self.code.append(f'''{' ' * indent}acmw[u'{operation.get('object')}'].set_text('{operation.get('value')}')''')

    def cycle(self, operation, indent):
        """
        Формирование циклов
        :param operation:
        :param indent:
        :return:
        """

        self.code.append(f'''{' ' * indent}for _ in range({operation.get('index')}):''')
        self.create_code(operation.get('for'), indent+4)
