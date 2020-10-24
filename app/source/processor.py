from app.serializer.controller import serialize
from app.generator import get_code


class Processor:
    def create_file(self, data):
        """
        Метод создания файла <----
        :return:
        """
        struct = serialize(data)
        file = get_code(struct)
        return {'file': file}