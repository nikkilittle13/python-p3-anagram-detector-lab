class Anagram:
  def __init__(self, word):
    self.word = word
  
  def match(self, word_list):
    matches = []

    for word in word_list:
      if sorted(list(word.lower())) == sorted(list(self.word.lower())):
        matches.append(word)

    return matches
    



    