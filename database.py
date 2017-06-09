from pymongo import MongoClient

class database(object):
    def __init__(self):
        client = MongoClient()
        self.db_conn = client['summary']
        self.working_keys = set()

    def load_existing_db(self):
        cursor = self.db_conn.summary.find()
        for val in cursor:
            for i in range(2):
                if val.keys()[i] != '_id':
                    self.working_keys.add(val.keys()[i])
        return self.working_keys

    def clear_db(self):
        result = self.db_conn.summary.delete_many({})
        return result

    def get_db_cursor(self):
        return self.db_conn.summary.find()

    def print_db(self):
        cursor = self.db_conn.summary.find()
        for val in cursor:
            print val

    def val_exist(self, value):
        cursor = self.db_conn.summary.find()
        for val in cursor:
            if value in val:
                return val[value]
        return 'not in db'

    def add_values(self, word_dict):
        self.load_existing_db()
        for val in word_dict.keys():
            if '.' not in val:
                if val not in self.working_keys:
                    self.db_conn.summary.insert_one({val : word_dict[val],
                                                    'word' : val})
                    self.working_keys.add(val)
                else:
                    cursor = self.db_conn.summary.find({'word':val})
                    new_freq = cursor[0][val]['freq'] + word_dict[val]['freq']
                    result = self.db_conn.summary.update_one(
                            {'word' : val},
                            {'$set': {val + '.freq' : new_freq}}
                        )


if __name__ == '__main__':
    db = database()
    # db.clear_db()
    db.print_db()

    # print db.load_existing_db()
