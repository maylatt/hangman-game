# -*- coding: utf-8 -*-
# Hangman Game

class Hangman():

     board = '''
      +---+
      |   |
      {}   |
     {}{}{}  |
     {} {}  |
          |
     ========='''

     doll = ['0','/','|','\\','/','\\']

     def __init__(self, word):
          self.word = word
          self.letters = []
     
     def hasWon(self):
          return self.displayedWord() == self.word
     
     def hasFinished(self):
          return ((len(self.wrongLetters()) >= len(self.doll)) or self.hasWon())
     
     def displayedWord(self):
          displayed = [x if x in self.rigthLetters() else '_' for x in self.word]
          return ''.join(displayed)
     
     def rigthLetters(self):
          return [x for x in self.letters if x in self.word]
     
     def wrongLetters(self):
          return [x for x in self.letters if not x in self.word]
     
     def getBoard(self):
          function = lambda t : t[1] if t[0] < len(self.wrongLetters()) else ' '
          dollParts = list(map(function, enumerate(self.doll)))
          return self.board.format(*dollParts) + \
               "\n\nPalavra: " + ''.join(self.displayedWord()) + \
               "\n\nLetras erradas: " + ' '.join(self.wrongLetters()) + \
               "\n\nLetras corretas: " + ' '.join(self.rigthLetters()) 

     def guess(self, letter):
          if (not letter in self.letters):
               self.letters.append(letter)