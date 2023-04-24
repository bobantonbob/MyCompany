from providers.sqlite_provider import SQLieProvider
from models.news import News


class NewsService(SQLieProvider):

    def __init__(self):
        super().__init__()
        self._news = []

    def get_all_news(self) -> list:
        # 1 Зчитуемо данні із таблиці News:
        query = 'select * from News'
        self._db_cursor.execute(query)
        result = self._db_cursor.fetchall()
        # 2 - Перетворюємо дані у колекцію обєктів (ORM):
        for row in result:
            new = News(row[0], row[1], row[2])
            self._news.append(new)
        # 3 Повертаємо поточну колекцію у зовнішній код:
        return self._news