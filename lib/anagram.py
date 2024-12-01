# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, anagrams):
        sort_words =sorted(self.word)
        return[anagram for anagram in anagrams if sort_words == sorted(anagram)]    
    
listen = Anagram("cat")
grams = listen.match(['act', 'atc', 'cat', 'tca', 'cta', 'tac'])

print(grams)     