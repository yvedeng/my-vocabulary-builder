import json


class Vocabulary:
    def __init__(self, db, language='english'):
        self.collection = db[language]

    def insert_word(self, word_obj={}):
        return self.collection.insert_one(word_obj)

    def find_word(self, word):
        data = self.collection.find({"word": word})
        result = []
        for x in data:
            result.append(str(x))
        return result
