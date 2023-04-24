from sqlite3 import connect
from os import getcwd, path

class SQLieProvider(object):
    def __init__(self):
        self._db_name = 'my_data.db'
        self._db_path = path.join(getcwd(), 'data', self._db_name)
        if not path.exists(self._db_path):
            print('\n> Бази не знайдено!!!!')
            self._connection = None
            self._db_cursor = None
        else:
            self._connection = connect(self._db_path)
            self._db_cursor = self._connection.cursor()

    def display_db_info(self) -> None:
        print(self._db_path)
        print(self._connection)
        print(self._db_cursor)

