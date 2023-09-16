from panther.db import Model


class User(Model):
    connection_id: str
