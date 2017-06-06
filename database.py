from pymongo import MongoClient


client = MongoClient()
db = client['summary']

if 1 == 2:
    result = db.summary.insert_one(
        {
            'word': {
                'freq': 1,
                'pos' : 'NN'
            }
        }
    )

cursor = db.summary.find()
for val in cursor:
    print val['word']

# result = db.summary.delete_many({})

# send in word_dict of curr email
# go through each word in word_dict
# check if its in db
    # it is - add freq
    # if not - add to table
