from emails import emails
import summarize

email_list = emails()

# for email in email_list.get_emails():
email = str(email_list.get_emails()[1])
email = email.replace('\\n', ' ')

word_dict = summarize.generate_dict(email)
print word_dict
