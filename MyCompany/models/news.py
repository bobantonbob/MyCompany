class News(object):

    def __init__(self, news_id: int, news_name: str, news_description: str):
        self._id = news_id
        self._name = news_name
        self._description = news_description


    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @id.setter
    def id(self, new_id: int) -> None:
        self._id = new_id

    @name.setter
    def name(self, new_name) -> None:
        self._name = new_name

    @description.setter
    def description(self, new_description) -> None:
        self._description = new_description
