class word_info(object):
    def __init__(self):
        #[{word: {freq : #, pos : str}}, {word: {freq : #, pos : str}}]
        self.entire_word_dict = {}

    def add_word(self, word, freq, pos):
        #{word: {freq : #, pos : str}}
        self.entire_word_dict[word[0]] = {'freq' : freq, 'pos' : pos}
