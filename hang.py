
import random
from images import IMAGES


def getWord():

    list_words=[]
    with open('words.txt','r') as file:
    # reading each line    
        for line in file:
    
            # reading each word        
            for word in line.split():
    
                # displaying the words           
                list_words.append(word)

       # getting a list of random words

    word = random.choice(list_words)
    # chossing the random word

  

    # checking if it is alphnumeric aand removing this

    return word

# To check if platform is complted or not


def check(platform, length):

    checked = 0
    for i in range(0, length):
        if platform[i] == '_':
            checked = 1

    return checked

# main fuction where we will play game


def play(word, length):
    platform = ''
    for i in range(0, 2*length):
        platform = platform+'_ '

    no_of_guesses = 8
    # no of guess is given equal to the game
    wrong=0
    while True:

        if no_of_guesses > 0:

            print(platform)
            # printing the platform for entering alphbets

            guess = input("Enter the alphabet you want to guess: ")

            j = 0
            done = 0
            # checking and editing our platform
            while j < length:
                if word[j] == guess:
                    index = j*2
                    done = 1
                    platform = platform[:index] + guess + platform[index+1:]

                j = j+1

            
            if done == 0:
                # To print images from images array 
                print(IMAGES[wrong])
                wrong=wrong+1
                no_of_guesses = no_of_guesses-1
                # reducing no of guesses for unsuccesful attempts

            result = check(platform, length)
            # checking result if completed or not

            if result == 0:
                print(f'The Word is {platform}')
                print("You Win!")
                break
            if no_of_guesses == 0:
                print("You Lose!")
                break

            print("\n")
            print(f'The number of guesses left is: {no_of_guesses}\n')
            print("\n")

        else:
            print("You lose")
            break


def game():
    word = getWord()
    print("Guess The Bollywond movie name:\n")
    word_length = len(word)

    play(word, word_length)


if __name__ == "__main__":
    game()
