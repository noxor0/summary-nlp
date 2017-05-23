import nltk
import sqlite3

class emails(object):

    def __init__(self):
        self.conn = sqlite3.connect('database.sqlite')
        self.cursor = self.conn.cursor()

    def get_emails(self):
        to_return = []
        temp = self.cursor.execute('SELECT RawText FROM Emails')
        for entry in temp:
            to_return.append(entry[0].encode('ascii', 'ignore'))
        return to_return


email_list = emails()
with open('emailinfo.txt', 'w') as outfile:
# email = email_list.get_emails()[1]
    for email in email_list.get_emails():
        text = nltk.word_tokenize(email)
        text = nltk.pos_tag(text)

        fdist = nltk.FreqDist(text)
        word_dict = {}

        for word in fdist.keys():
            word_dict[word[0]] = {'freq' : fdist[word], 'pos' : word[1]}
            outfile.write(str(word_dict))

    outfile.close()
