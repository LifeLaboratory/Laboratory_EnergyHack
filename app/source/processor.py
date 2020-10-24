from app.serializer.controller import serialize
from app.generator import get_code, get_file
from json import dumps


class Processor:
    def create_file(self, data):
        """
        Метод создания файла <----
        :return:
        """
        struct = serialize(data)
        print(dumps(struct))
        file = get_file(struct)
        return {'file': f'dist/{file}'}