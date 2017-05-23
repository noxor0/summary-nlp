import sqlite3

class emails(object):

    def __init__(self):
        self.conn = sqlite3.connect('database.sqlite')
        self.cursor = self.conn.cursor()

    def get_emails(self):
        to_return = []
        temp = self.cursor.execute('SELECT RawText FROM Emails')
        for entry in temp:
            to_return.append(entry)
        return to_return

test = emails()
print test.get_emails()