import json
from typing import Any, Union, Dict, List

class FileContext:

    def __init__(self, file_name: str, mode: str = 'r', encoding: str = 'utf-8'):
        self.file_name = file_name
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        """Вхід в контекст"""
        try:
            self.file = open(self.file_name, self.mode, encoding=self.encoding)
            return self.file
        except IOError as e:
            print(f"Помилка відкриття файлу: {e}")
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Вихід з контексту"""
        if self.file:
            self.file.close()
        return False

    @classmethod
    def write_json(cls, file_name: str, data: Union[Dict, List], indent: int = 2):
        """Запис даних у JSON файл"""
        with cls(file_name, 'w') as file:
            json.dump(data, file, ensure_ascii=False, indent=indent)

    @classmethod
    def read_json(cls, file_name: str) -> Union[Dict, List]:
        """Читання даних з JSON файлу"""
        with cls(file_name, 'r') as file:
            return json.load(file)
