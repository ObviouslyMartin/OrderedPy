class WordData:
  def __init__(self, word=None, length=None, vowels=None, consonants=None, digits=None, specialChars=None):
      self.word = word
      self.length = length
      self.vowels = vowels
      self.consonants = consonants
      self.digits = digits
      self.specialChars = specialChars

  def isVowel(self, letter):
      upcase = upper(letter)
      return upcase == 'A' or upcase == 'E' or upcase == 'I' or upcase == 'O' or upcase == 'U'

  def SetWord(self, word):
     self.word = word
     self.precessWord()

  def processWord(self, word):
     for letter in word:
         if isalpha(letter):
             if self.isVowel(letter):
                 self.vowels += 1
             else:
                 self.consonants += 1
         elif isnumeric(letter):
             self.digit += 1
         else:
             self.specialChars += 1

  def PrintData(self):
      print(self.word,  ":", self.length)
      print("vowels:", self.vowels)
      print("consonants:", self.consonants)
      print("digits:", self.digits)
      print("Special Characters:", self.specialChars)


  def __gt__(self, other):
      if self.length < other.length:
          return True
      if self.length > other.length:
          return False



  def __lt__(self, other):
      if self.length < other.length:
         return True
      if self.length > other.length:
         return False

  def CopyWord(self, other):
      if self is other:
          return self
      return wordData(word=other.word,
                        length=other.length,
                        vowels=other.vowels,
                        consonants= other.consonants,
                        digits=other.digits,
                        specialChars=other.specialChars)


  def __add__(self, other):
      sum = self.length + other.length
      sum += self.vowels + other.vowels
      sum += self.consonants + other.consonants
      sum += self.digits + other.digits
      sum += self.specialChars + other.specialChars
      return sum
