import nltk
import word_info
import string
import sys
import database

def summarize(text, n_lines):
    db = database.database()
    word_dict = generate_dict(text)
    #add db values here
    sents = str(text).replace('\n', ' ').split('.')

    sent_scores = []
    sent_itter = 0
    for sent in sents:
        sent = sent.translate(None, string.punctuation)
        curr_score = 0
        for word in sent.split(' '):
            if word in word_dict:
                #do value modifications here
                try:
                    cursor = db.db_conn.summary.find({'word' : word})
                    # print cursor[0]['word'], cursor[0][word]
                    curr_score += word_dict[word]['freq'] + cursor[0][word]['score']
                except IndexError:
                    curr_score += word_dict[word]['freq'] + 10
                except KeyError:
                    curr_score += word_dict[word]['freq'] + 10

        sent_scores.append((sent_itter, curr_score))
        sent_itter += 1


    sent_scores = sorted(sent_scores, key = lambda x : (x[1]), reverse = True)
    trimmed_summary = sent_scores[:n_lines]

    summary = ''
    for sent_tuple in trimmed_summary:
        summary += sents[sent_tuple[0]] + '.'
    print summary

def generate_dict(text):
    parse_text = nltk.word_tokenize(text)
    parse_text = nltk.pos_tag(parse_text)

    word_info_obj = word_info.word_info()

    fdist = nltk.FreqDist(parse_text)
    for word in fdist.keys():
        word_info_obj.add_word(word, fdist[word], word[1])

    return word_info_obj.entire_word_dict


if __name__ == '__main__':

    valu = {'http://www.cnn.com/2017/06/04/politics/donald-trump-london-terror-tweets/index.html' : 'text1',
            'http://www.cnn.com/2017/06/05/politics/trump-comey-executive-privilege/index.html' : 'text2',
            'http://money.cnn.com/2017/06/05/technology/gadgets/apple-wwdc-2017/index.html' : 'text3'}

    if len(sys.argv) > 1:
        doc = sys.argv[1]
    else:
        doc = valu.keys()[0]

    doc = valu[doc]

    with open(doc, 'r') as document:
        summarize(document.read(), 5)
