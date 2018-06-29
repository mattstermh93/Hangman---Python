from random import choice as c 
from IPython.display import clear_output
class Categories():
    def __init__(self):
        self.teams = ['Hawks', '76ers', 'Cavaliers', 'Celtics', 'Mavericks', 'Raptors', 'Wizards', 'Bucks', 'Knicks', 
                      'Lakers', 'Spurs', 'Wizards', 'Clippers', 'Jazz', 'Rockets', 'Pacers', 'Warriors', 'Pistons', 'Nets', 'Hornets', 'Pelicans']
            
        self.countries = ['Belize', 'El Salvador', 'Honduras', 'Costa Rica', 'Guatemala', 'Nicaragua', 'Panama']
        self.cars = ['Toyota', 'Subaru', 'Honda', 'Mitsubishi', 'Lexus', 'Ford', 'Cadillac', 'Volvo', 'Acura', 'Lincoln']
        

        self.pickedTeam = []
        self.pickedCountry = []
        self.pickedCar = []
        
    
                            ##########################################################
                            ##########################################################
                            ##########################################################

                
class Hangman(Categories):    
    
    def __init__(self):
        super().__init__()

    def displayInstructions(self):
        print("Welcome to hangman! Below are the categories to choose from." )
        print("Sports - Type 'sports' to pick an NBA sports team")
        print("Car Manufacturers - Type 'cars' to pick a car manufacturer to choose from")
        print("Countries in Central America - Type 'countries' top pick a country from Central America")
        print("\n")

        
    def sportTeams(self):
        lives_remaining = 6
        rand_team = c(self.teams)
        print('Your team has been chosen! Start the guessing! ') #start of the game!
        
        print(('You have {} lives remaining'.format(lives_remaining)))
        
        print('_ ' * (len(rand_team)))
        while lives_remaining > 0:
 
            letter_picked = input("Please enter a letter: ")
            
            if len(letter_picked) > 1:
                print('You can only enter one letter!')
            elif len(letter_picked) < 1:
                print('You did not enter anything, please try again. ')
                continue
            elif letter_picked not in rand_team.lower(): #incorrect guess
                lives_remaining -=1
                print('Incorrect')
                print('You have {} lives remaining'.format(lives_remaining)) 
            elif letter_picked in rand_team.lower(): #correct guess
                print(letter_picked)
                print('{} is correct! \n'.format(letter_picked))
                self.pickedTeam.append(letter_picked)
            if len(rand_team) == len(self.pickedTeam): #winning condition
                print('Congrats! You guessed it - {} '.format(rand_team))
                print('Play again!')
                break
            while lives_remaining <= 0: #when the player loses
                print('Your word was {}  - better luck next time!'.format(rand_team))
                print('Try again!')
                break
                
  
            
    def countriesToPick(self):
        lives_remaining = 6
        rand_country = c(self.countries)
        print('Your country has been chosen! Start the guessing! ') #start of the game!
        
        print(('You have {} lives remaining'.format(lives_remaining)))
        
        print('_ ' * (len(rand_country)))
        while lives_remaining > 0:
            
            letter_picked = input("Please enter a letter: ")
            if len(letter_picked) > 1:
                print('You can only enter one letter!')
            elif len(letter_picked) < 1:
                print('You did not enter anything, please try again. ')
                continue
            elif letter_picked not in rand_country.lower(): #incorrect guess
                lives_remaining -=1
                print('Incorrect')
                print('You have {} lives remaining'.format(lives_remaining)) 
            elif letter_picked in rand_country.lower(): #correct guess
                print(letter_picked)
                print('{} is correct! \n'.format(letter_picked))
                self.pickedCountry.append(letter_picked)
            if len(rand_country) == len(self.pickedCountry): #winning condition
                print('Congrats! You guessed it - {} '.format(rand_country))
                print('Play again!')
                break
            while lives_remaining <= 0: #when the player loses
                print('Your word was {}  - better luck next time!'.format(rand_country))
                print('Try again!')
                break
            
    def carsToPick(self):
        lives_remaining = 6
        rand_car = c(self.cars)
        print('Your car manufacturer has been decided! Start the guessing! ') #start of the game!
        
        print(('You have {} lives remaining'.format(lives_remaining)))
        
        print('_ ' * (len(rand_car)))
        while lives_remaining > 0:
           
            letter_picked = input("Please enter a letter: ")
            if len(letter_picked) > 1:
                print('You can only enter one letter!')
            elif len(letter_picked) < 1:
                print('You did not enter anything, please try again. ')
                continue
            elif letter_picked not in rand_car.lower(): #incorrect guess
                lives_remaining -=1
                print('Incorrect')
                print('You have {} lives remaining'.format(lives_remaining)) 
            elif letter_picked in rand_car.lower(): #correct guess
                print(letter_picked)
                print('{} is correct! \n'.format(letter_picked))
                self.pickedCar.append(letter_picked)
            if len(rand_car) == len(self.pickedCar): #winning condition
                print('Congrats! You guessed it - {} '.format(rand_car))
                print('Play again!')
                break
            while lives_remaining <= 0: #when the player loses
                print('Your word was {}  - better luck next time!'.format(rand_car))
                print('Try again!')
                break
   
    def quitProgram(self):
        quit = input("\n Do you want to quit? Type yes or no \n")
        print('Have a great day! See you next time!')
        if quit == 'yes':
            return True
        elif quit == 'no':
            return False
        elif quit == 'quit':
            return False
        

    def main(self):
        
        self.displayInstructions()
        while True:
            what_to_do = input ("\n What category would you like to choose from? \n ")
            if what_to_do == 'sports':
                self.sportTeams()
                continue
            elif what_to_do == 'cars':
                self.carsToPick()
                continue
            elif what_to_do == 'countries':
                self.countriesToPick()
                continue
            elif what_to_do == 'quit':
                if self.quitProgram() == True:
                    break
                

timeToPlay = Hangman()
timeToPlay.main()