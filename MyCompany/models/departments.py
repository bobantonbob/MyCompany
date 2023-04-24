class Department(object):

    def __init__(self, dep_id: int, dep_name: str):
        self._id = dep_id
        self._name = dep_name

    @property
    def id(self) -> int:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @id.setter
    def id(self, new_id: int) -> None:
        self._id = new_id

    @name.setter
    def name(self, new_name) -> None:
        self._name = new_name