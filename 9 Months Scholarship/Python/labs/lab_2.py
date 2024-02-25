from re import compile, fullmatch
from random import choice
from time import sleep
import json
#problems = {
#    1:
#    {"desc": "Write a function that accepts two arguments (length, start) to generate an array of a specific length filled with integer numbers increased by one from start.","call":problem_1,"inp":"input a string containing vowels"},
#    2:
#    {"desc": "write a function that takes a number as an argument and if the number divisible by 3 return 'Fizz' and if it is divisible by 5 return 'buzz' and if is is divisible by both return 'FizzBuzz' ","call":problem_2,"inp":"input 5 strings"},
#    3:
#    {"desc":"Write a function which has an input of a string from user then it will return the same string reversed.","call":problem_3,"inp":"input a string containing 'iti'"},
#    4:
#    {"desc": "Ask the user for his name then confirm that he has entered his name(not an empty string/integers). then proceed to ask him for his email and print all this data (Bonus) check if it is a valid email or not","call":problem_4,"inp":"input a string"},
#    5:
#    {"desc": "Write a function that takes a string and prints the longest alphabetical ordered substring occurred For example, if the string is 'abdulrahman' then the output is: Longest substring in alphabetical order is: abdu","call":problem_5,"inp":"input a string"},
#    6:
#    {"desc": "Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake, print an error message and skip to the next number.","call":problem_6,"inp":"input a number"},
#    7:
#    {"desc": """Word guessing game (hangman)
#○ A list of words will be hardcoded in your program, out of
#which the interpreter will
#○ choose 1 random word.
#○ The user first must input their names
#○ Ask the user to guess any alphabet. If the random word
#contains that alphabet, it
#○ will be shown as the output(with correct placement)
#○ Else the program will ask you to guess another alphabet.
#○ Give 7 turns maximum to guess the complete word""","call":problem_7,"inp":"input the height of the pyramid"},
#        }
def problem_1(length, start):
        array=[x for x in range(start, start + length)]
        return array
def problem_2(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
def problem_3(string):
    string = string[::-1]
    return string
def problem_4():
    regex = compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    while(True):
        name = input("What's your name?\n>> ")
        if name != "":
            break
        print("you didn't enter anything...")
    while(True):
        email = input("What's your email?\n>> ")
        if fullmatch(regex, email):
            break
        print("you didn't give a valid email.")
    print(f"you are {name} and your email is {email}")
def problem_5(string):
    current= string[0]
    longest= string[0]

    for i in range(1, len(string)):
        if ord(string[i]) >= ord(string[i - 1]):
            current+= string[i]
        else:
            current= string[i]

        if len(current) > len(longest):
            longest = current

    print("Longest substring: ", longest)

# Example usage:
problem_5(input('string >> '))

def problem_6():
    num_array= []
    while(True):
        inp = input("number>> ")
        if inp.lower() == "done":
            break
        try:
            inp = int(inp)
            num_array.append(inp)
        except:
            print("you gave invalid input")
    total = sum(num_array)
    count = len(num_array)
    average = total / count
    print(f"total:{total}\ncount:{count}\naverage:{average}")
class Problem_7:
#    self.word = choice(wordlist)
#    self.obfuscate = ["_" for x in range(len(word))]
    def __init__(self,wordlist,prompt="guess>> "):
        self.prompt = prompt
        self.man = ['i','/','|','\\','|','/','\\']
        self.count = 1
        self.guesses = []
        self.word = choice(wordlist)
        self.obfuscate = ["_" for x in range(len(self.word))]
        self.default_filename = "savegame0.json"
        self.state = {'players':[]}
        self.player = {"playername": "", "wins": 0, "loses": 0}
#        self.state = self.load("savegame0.txt")
    def save(self):
        for idx,player in enumerate(self.state['players']):
            if self.player['playername'] == player['playername']:
                player = self.player
                break
        else:
            self.state['players'].append(self.player)
        with open(self.default_filename,"w") as savefile:
            json.dump(self.state, savefile)
    def load(self):
        with open(self.default_filename,"r") as savefile:
            self.state = json.load(savefile)
    def selector(self):
        playernum = None
        #print(len(self.state['players']))
        name = input("Whats your player name? (leave empty to see existing players)\nname >> ")
        if name == "":
            print("player:Win/Losses ratio")
            for idx,player in enumerate(self.state['players']):
                print(f"{idx}){player['playername']}:{player['wins']}/{player['loses']}")
            while type(playernum) != int or playernum > len(self.state['players'])-1:
                
                print("Enter a number of an available player")
                playernum = input("number>> ")
                try:
                    playernum = int(playernum)
                except:
                    print("Please Enter a number of an available player")
            self.player = self.state['players'][playernum]
        else:
            for idx,player in enumerate(self.state['players']):
                if name == player['playername']:
                    self.player = player
                    break
            else:
                self.player['playername'] = name
        print(self.player)
    def hang(self):
        man = [*self.man[0:self.count], *[" " for x in range(self.count, 8)]]
        hanged=f"""
    :{"".join(self.obfuscate)}
__________________
        |
        |
        O
        {man[0]}
       {man[1]}{man[2]}{man[3]}
        {man[4]}
       {man[5]} {man[6]}
__________________
        """
        print(hanged)
    def gameover(self):
        if self.word == "".join(self.obfuscate):
            print("You won")
            self.player['wins']+=1
            sleep(2)
            print("exitting...")
            return False
        if self.count == 7:
            print("You loose")
            self.player['loses']+=1
            sleep(2)
            print("Game exitting...")
            return False
        return True
    def check(self,guess):
        if guess == '-':
            print("wrong guess...")
            sleep(1)
            return
        if guess in self.guesses:
            print("character already guessed, try another...")
            return
        self.guesses.append(guess)
        loc_array=[]
        for idx,ch in enumerate(self.word):
#        print(ch)
            if ch == guess:
                loc_array.append(idx)
        if loc_array == []:
            self.count+=1
            return
        for loc in loc_array:
            self.obfuscate[loc] = guess
    def guess(self):
        guess = input(self.prompt).lower()
        regex = compile("[a-z]")
        if fullmatch(regex,guess):
            return guess
        return '-'
    def play(self):
        print("loading save file...")
        self.load()
        self.selector()
        while(self.gameover()):
            self.hang()
#            self.guess()
            self.check(self.guess())
        self.save()
        print("Saving game",end="")
        for x in range(3):
            sleep(0.5)
            print(".",end="")
        print("Thank you for playing!\n\n")
#    check('a')
#    print(obfuscate)
game = Problem_7(["art","pain","suffering","torture","great"])
#game.load()
#game.selector()
#print(game.state)
game.play()
#problem_6()
#print(problem_1(5,5))
#for n in [3,4,5,9,12,15]:
#print(f"number: {n}, {problem_2(n)}")
#print(problem_3("Heroyuken"))
#problem_4()
