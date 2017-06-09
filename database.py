from pymongo import MongoClient

POS = {
    'NNPS': 1,
    'NNP': 1,
    'NNS': 1,
    'NN' : 1,

    'VBD': 1,
    'VBG': 1,
    'VBP': 1,
    'VBZ': 1,
    'VBN': 1,
    'VBT': 1,
    'VB' : 1,

    'SYM': 0,

    'IN' : .1,
    'CC' : .1,
    'PRP': .1,
    'TO' : .1,
    'UH' : .1,

    'DT' : .2,
    'JJ' : .2,
    'JJR': .2,
    'JJS': .2,

    'CD' : .3,

    'RB' : .4,
    'RBR': .4,
    'RBS': .4,
    'RP' : .4,
    'WP' : .4,
    'WRB': .4
}

other = .1

class database(object):
    def __init__(self):
        client = MongoClient()
        self.db_conn = client['summary']
        self.working_keys = set()

    def load_existing_set(self):
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
        self.load_existing_set()
        for val in word_dict.keys():
            if '.' not in val and '$' not in val:
                if val not in self.working_keys:
                    self.db_conn.summary.insert_one({val : word_dict[val],
                                                    'word' : val})
                    self.working_keys.add(val)
                else:
                    cursor = self.db_conn.summary.find({'word':val})
                    try:
                        new_freq = cursor[0][val]['freq'] + word_dict[val]['freq']
                        result = self.db_conn.summary.update_one(
                                {'word' : val},
                                {'$set': {val + '.freq' : new_freq}}
                            )
                    except IndexError:
                        print "No item for cursor"

    def add_scores(self):
        cursor = self.db_conn.summary.find({})
        # print self.db_conn.summary.count()
        for value in cursor:
            word = value['word']
            try:
                score = self.calc_word_score(value[word]['pos'], value[word]['freq'])
                self.db_conn.summary.update(
                    {'word': word}, {'$unset' : {'score': score}}
                )
                self.db_conn.summary.update(
                    {'word': word}, {'$set' : {word+'.score': score}}
                )
                # print word, score
            except KeyError:
                pass
            except TypeError:
                pass
                # print 'not a word'


    def calc_word_score(self, pos, freq):
        value = freq * POS[pos]
        # print word, value
        return value


if __name__ == '__main__':
    db = database()
    # db.print_db()
    db.add_scores()
    # print db.load_existing_set()
