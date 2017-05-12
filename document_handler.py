import nltk

test  = """A short story is a piece of prose fiction that can be read in one sitting. Emerging from earlier oral storytelling traditions in the 17th century, the short story has grown to encompass a body of work so diverse as to defy easy characterization. At its most prototypical the short story features a small cast of named characters, and focuses on a self-contained incident with the intent of evoking a "single effect" or mood.In doing so, short stories make use of plot, resonance, and other dynamic components to a far greater degree than is typical of an anecdote, yet to a far lesser degree than a novel. While the short story is largely distinct from the novel, authors of both generally draw from a common pool of literary techniques.
Short stories have no set length. In terms of word count there is no official demarcation between an anecdote, a short story, and a novel. Rather, the form's parameters are given by the rhetorical and practical context in which a given story is produced and considered, so that what constitutes a short story may differ between genres, countries, eras, and commentators. Like the novel, the short story's predominant shape reflects the demands of the available markets for publication, and the evolution of the form seems closely tied to the evolution of the publishing industry and the submission guidelines of its constituent houses.
The short story has been considered both an apprenticeship form preceding more lengthy works, and a crafted form in its own right, collected together in books of similar length, price, and distribution as novels. Short story writers may define their works as part of the artistic and personal expression of the form. They may also attempt to resist categorization by genre and fixed formation."""

test = test.split(' ')
word_dict = {}
viewed_words = []

for word in test:
    if word not in viewed_words:
        word_dict[word] = test.count(word)
        viewed_words.append(word)

print word_dict
