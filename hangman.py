import random

# Function that converts string to list in order to index
def indexConversion (answer):
    wlist = list(answer)
    wlist[index] = guess
    answer = ''.join(wlist)
    return answer

# Function that disguises letters in word
def setWord (word):
    answer = ''
    for i in range(0,len(word)):
        if word[i] is ' ':
            answer += ' '
        else:
            answer += '*'
    return answer


responses = ["You suck.","Try again you idiot.","Your mom could do better than that.","Say wallah..","InshaAllah","My mensef is better than yours"]
print "Welcome to Hangman"
word = "hello world"
# word = raw_input("Please give a word that you would like to have someone else guess: ")

answer = setWord(word)

print "\nYour word/sentence is %s" % (answer)

guesses = []
guesses_max = 7
count  = 0

while count != guesses_max and '*' in answer:
    index = 0
    guess = raw_input("\nGuess: ")
    if guess.isalpha():
        if guess in guesses:
            print "Sorry you've already guessed the letter %c" % guess
        elif guess in word:
            while index < len(word):
                index = word.find(guess, index)
                if index == -1:
                    break
                answer = indexConversion(answer)
                index += 1
        else:
            count += 1
            print responses[random.randrange(0,7)]
            print "Number of guesses left: %d" % (7 - count)
        print answer
        guesses.append(guess)
    else:
        print "That is not a letter."

if '*' in answer:
    print "GAME OVER. The word was '%s'." % word
else:
    print "You won!"