from json import loads
from app.generator import GenerateCode


def get_code(struct):
    """
    Публичный метод для построения кода по правилам
    :param struct:
    :return:
    """
    return GenerateCode().create_code(struct)


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
  {"name": "Condition", "action": "click",  "object":  "AC-E"},
  {"name": "Condition", "action": "condition",  "value":  "1 < 2"},
  {"name": "cycle", "action": "cycle", "index": 10, "for": 
    [
        {"name": "Condition", "action": "click",  "object":  "AC-E"},
        {"name": "Condition", "action": "save_value",  "object":  "AC-E", "value": "123"},
        {"name": "cycle", "action": "cycle", "index": 10, "for": 
          [
              {"name": "Condition", "action": "click",  "object":  "AC-E"},
              {"name": "Condition", "action": "save_value",  "object":  "AC-E", "value": "123"}
          ]
        }
    ]
  },
  {"name": "Condition", "action": "save_value",  "object":  "AC-E", "value": "123"}
]
''')
# print(GenerateCode().create_code(data))

