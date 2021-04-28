import random
from hangman import Hangman


def getWord():
    with open('words.txt', 'r') as words:
        lines = words.readlines()
        return random.choice(lines)

def main():
     hangman = Hangman(getWord().strip())
     print(">>>>>>>>>>Hangman<<<<<<<<<<")
     print(hangman.getBoard())

     while (not hangman.hasFinished()):
          letter = input("\nDigite uma letra: ")
          hangman.guess(letter)
          print(hangman.getBoard())

     if (hangman.hasWon()):
          print("\n\nVocê venceu! =)")
     else:
          print("\n\nVocê perdeu! =( \nA palavra era %s" % hangman.word)

     print("\n\nFoi bom jogar com você! Agora vá estudar!")

if (__name__ == "__main__"):
     main()
