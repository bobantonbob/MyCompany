from providers.sqlite_provider import SQLieProvider
from models.departments import Department


class DepsService(SQLieProvider):

    def __init__(self):
        super().__init__()
        self._departments = []

    def get_all_departments(self) -> list:
        # 1 Зчитуемо данні із таблиці Departments:
        query = 'select * from Departments'
        self._db_cursor.execute(query)
        result = self._db_cursor.fetchall()

            #2 - Перетворюємо дані у колекцію обєктів (ORM):
        for row in result:
            dep = Department(row[0], row[1])
            self._departments.append(dep)
         # 3 Повертаємо поточну колекцію у зовнішній код:
        return self._departments

