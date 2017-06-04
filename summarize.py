import nltk
import word_info
import string

def summarize(text, n_lines):
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
                curr_score += word_dict[word]['freq']
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


test = """ Soon after word of two terror attacks in London broke late Saturday, Donald Trump began to offer his thoughts.

Did he release a statement offering condolences to the victims? Did he grant an interview with a TV network to insist that the US remains resolute in our fight against terror even in the wake of these latest attacks? Nope! He tweeted! Five times, to be exact.
On Saturday night, Trump kicked off his tweetstorm with this: "We need to be smart, vigilant and tough. We need the courts to give us back our rights. We need the Travel Ban as an extra level of safety!"
Then he offered this tweet: "Whatever the United States can do to help out in London and the U. K., we will be there - WE ARE WITH YOU. GOD BLESS!"
After a night's sleep, Trump woke up Sunday morning and, around 8 a.m., fired off three more tweets.
"We must stop being politically correct and get down to the business of security for our people. If we don't get smart it will only get worse," Trump started.
"At least 7 dead and 48 wounded in terror attack and Mayor of London says there is "no reason to be alarmed!," he continued.
"Do you notice we are not having a gun debate right now? That's because they used knives and a truck!," he ended.
Of those five, one is the sort of thing you can imagine a president not named Donald Trump saying in the wake of a major terrorism event like the one in London; that's the second one Saurday night in which he pledges to help London in whatever way they need it and insists America stands with them.
The other four tweets are pure Trump -- and the exact opposite of what we have long considered "presidential."
In one -- the first he sends out -- he uses the just-breaking terror attacks as a way to make the case for his travel ban, which continues to be hung up in the courts.
In another, he suggests political correctness is responsible for the attack, a common Trump refrain during the campaign.
In a third, he takes on those pushing gun control -- noting that they are silent because these attacks didn't involve guns.
And, finally and most Trumpian, he attacks the mayor of London, Sadiq Khan, for allegedly insisting that the people of London have "no reason to be alarmed."
As is often the case with Trump, he has taken that comment from Khan heavily out of context. In a statement, Khan said: "Londoners will see an increased police presence today and over the course of the next few days. There's no reason to be alarmed. One of the things the police and all of us need to do is ensure that we're as safe as we possibly can be."
Khan is clearly referring not to the threat from terrorists but to the increased police presence when he uses the words "no reason to be alarmed." Trump chooses to misunderstand him for political purposes.
Trump tweeting things to forward his own agenda in the wake of terrorist attacks is nothing new. Following shootings in an Orlando nightclub that left 53 people dead, Trump offered this: "Appreciate the congrats for being right on radical Islamic terrorism, I don't want congrats, I want toughness & vigilance. We must be smart!" After an incident of a knife-wielding man at the Louvre Museum in Paris, Trump tweeted: "A new radical Islamic terrorist has just attacked in Louvre Museum in Paris. Tourists were locked down. France on edge again. GET SMART U.S."
In short, the tweetstorm following the London attacks isn't the exception, it's the rule for Trump. Using these attacks to prove his political point is his default position not a one-time popping off.
Trump's responses are the latest example of how he is radically altering the idea of what it means to be "presidential." During the 2016 campaign, Trump's attacks on John McCain's war hero status, his savaging of a Gold Star family, his wild exaggerations about his wealth and his seeming disinterest in the truth were all taken, at one point or another, as signs that he simply wasn't "presidential" enough to actually win anything. That, while voters liked his unorthodox style, they would eventually tire of him as they looked for the sort of statesman who had traditionally held the nation's top political job.
It didn't happen. And Trump has never stopped. His quintet of tweets on London are not only something that no previous American president would ever have said, they're also statements that it's hard to imagine any other leader in any other democracy around the world saying.
They are more the statements of a conservative talk radio show host than they are of what we have come to think of as a president -- bombastic, over the top and out of context. They are, by traditional standards, anti-presidential.
Which, come to think of it, is a good way to describe Trump. He is sort of an anti-president -- at least in terms of how we have always defined those terms. Trump's attitude and approach in office is closer to Jerry Springer than to Gerald Ford. He's more Limbaugh than Lincoln.
What we know: Trump isn't going to stop Trumping. The only question now is whether voters want an anti-president as their president.
 """

summarize(test, 5)
