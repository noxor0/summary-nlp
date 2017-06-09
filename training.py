from emails import emails
import summarize
import database

email_list = emails()

# for email in email_list.get_emails():
email = str(email_list.get_emails()[1])
email = email.replace('\\n', ' ')

word_dict = summarize.generate_dict(email)

db_obj = database.database()
db_obj.add_values(word_dict)
