from emails import emails
import summarize
import database


if __name__ == '__main__':
    db_obj = database.database()
    email_list = emails()

    counter = 0

    for email in email_list.get_emails():
    # email = str(email_list.get_emails()[1])
        email = str(email).replace('\\n', ' ')
        word_dict = summarize.generate_dict(email)
        db_obj.add_values(word_dict)

        print 'email', counter, 'done'
        counter += 1
