from pymongo import MongoClient


class MongoDb:
    def __init__(self, host, port, username, password, database):
        self._client = MongoClient(host=host,
                                   port=port,
                                   username=username,
                                   password=password)
        self.db = self._client.get_database(database)

    def __del__(self):
        return self._client.close()
