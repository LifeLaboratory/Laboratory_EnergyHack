from json import loads
from app.generator.creator import GenerateCode


def get_code(struct):
    """
    Публичный метод для построения кода по правилам
    :param struct:
    :return:
    """
    return GenerateCode().create_code(struct)


def get_file(struct):
    """
    Публичный метод для построения кода по правилам и формирования exe
    :param struct:
    :return:
    """
    return GenerateCode().create_file(struct)


data = loads('''
[
  {"name": "open", "action": "open_file", "file_path": "C:\\tmp"},
  {"name": "cycle", "action": 
    [
        {"name": "write", "action": "write", "filter": "flt", "code": "code"}  
    ]
  },
  {"name": "close", "action": "close_file"}
]
''')

data = loads('''
[
  {"name": "open", "action": "open_file", "file_path": "B:/Program Files (x86)/AbilityCash/AbilityCash.exe"},
  {"name": "open", "action": "open_file", "file_path": "B:/Program Files (x86)/AbilityCash/AbilityCash.xls"},
  {"name": "Condition", "action": "click",  "object":  "AC-E"},
  {"name": "cycle", "action": "cycle", "index": 10, "for": 
    [
        {"name": "Condition", "action": "click",  "object":  "AC-E"},
        {"name": "Condition", "action": "save_value",  "object":  "AC-E", "value": "123"},
        {"name": "Condition", "action": "save_value",  "object":  "AC-E", "source": "A"},
        {"name": "cycle", "action": "cycle", "index": 10, "for": 
          [
              {"name": "Condition", "action": "click",  "object":  "AC-E"},
              {"name": "Condition", "action": "save_value",  "object":  "AC-E", "value": "123"},
              {"name": "Condition", "action": "save_value",  "object":  "AC-E", "source": "B"}
          ]
        }
    ]
  },
  {"name": "Condition", "action": "save_value",  "object":  "AC-E", "value": "123"},
  {"name": "Condition", "action": "save_value",  "object":  "AC-E", "source": "A1"}
]
''')
# print(GenerateCode().create_file(data))

