# INTERACTIVE PYTHON DEMOS


import time
import random

#for better console display 
def animate_loading(text):
    print("\n" * 100)
    frames = ["|", "/", "-", "\\", "|", ""]
    for frame in frames:    
        print(f"\r{text[0]} {frame}", end = " ", flush=True)
        time.sleep(0.1)
    print("\n" * 100)
    print(f"\r{text[1]} ", end=" ", flush=True)
    time.sleep(1)
    print("\n" * 100)
# project_start_code
# Ask input from the user what action they want to perform
# 1. Calculator  
# 2. Number Guesser game
# 3. Random password generator
# 4. Rock scissors paper
# 5. Temperature converter (celsius, fahrenheit, kelvin)
# 6. Multiplication table
# 7. Random math problem solving
     
# Code for calculator
def calculator():
  # sum function
    def sum(a,b):
        return a+b
        

  # difference function
    def difference(a,b):
        return a-b
        

  # multiplication function
    def multiplication(a,b):
        return a*b
        
    # division function
    def division(a,b):
        return a/b
        
    # power function    
    def power(a,b):
        return a**b
    # modulus function
    def remainder(a,b):
        return a%b
        
    try:
        num1=float(input("Enter the first number: "))
        operator = str(input("Enter the operator for action(+,-,*,/,^,%):"))
        num2=float(input("Enter the second number: "))
        result = 0
        match operator:
            case "+" :
                result= sum(num1,num2)
                print(f"Output: {result}")
            case "-":
                result= difference(num1,num2)
                print(f"Output: {result}")
            case "*":
                result= multiplication(num1,num2)
                print(f"Output: {result}")
            case "/":
                result= division(num1,num2)
                print(f"Output: {result}")
            case "^":
                result= power(num1,num2)
                print(f"Output: {result}")
            case "%":
                result= remainder(num1,num2)
                print(f"Output: {result}")
            case _:
                print("Invalid Operator please use +,-,*,/,^,%")
        time.sleep(5)
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        time.sleep(2)
    except ValueError:
        print("Invalid Input. Please enter valid number")
        time.sleep(2)
    except:
        print("Unexpected error has occured")
        time.sleep(2)
        
# Code for number guesser game
def number_guessor():
    while True:
        try:
            print("Welcome to Number Guessing Game")
            low = int(input("Enter the lowest range of number you want to set: "))
            high = int(input("Enter the highest range of number you want to set: "))
            chance = int(input("Enter the number of chances you want:"))
            tempchance = chance
            guessnum = random.randint(low, high)
            print("\n"*400)
            print(f"Guess the number between {low} and {high} within {chance} attempts")
            while tempchance != 0:
                try:
                    guess = int(input("Enter your guess: "))
                    
                    if guess < guessnum:
                        if guessnum - guess <=5:
                            print("You are abit low but very close. Guess abit higher")
                        elif guessnum - guess <=10:
                            print("Too low! But you are close. Guess higher")
                        else:
                            print("Too low! Try again")
                        tempchance -= 1
                        print(f"You got {tempchance} chances")
                        
                    elif guess > guessnum:
                        if guess - guessnum <= 5:
                            print("You are abit high but very close. Guess abit lower")
                        elif guess - guessnum <=10:
                            print("Too high! But you are close. Guess lower")
                        else:
                            print("Too high! Try again")
                        tempchance -= 1
                        print(f"You got {tempchance} chances")
                            
                    else:
                        tempchance -= 1
                        print(f"Congratulation! You have guessed the correct number in {chance - tempchance} attempts")
                        time.sleep(3)
                        break
                except ValueError:
                    print("Invalid Input! Please enter a number.")
            if(tempchance==0 and guess!=guessnum):
                print(f"You have run out of chances!\nThe answer is {guessnum}\nBetter luck next time")
            time.sleep(3)
            break
        except ValueError:
            print("Invalid Input. Please enter valid number")
            time.sleep(2)
        
# Code for random password generator
def random_password_generator():
  # create collection of small letters in a single string
  smallAlphabet = "abcdefghijklmnopqrstuvwxyz"
  capitalAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  numColl = "1234567890"
  specialChar="!@#$%&*-."
  characters = smallAlphabet + capitalAlphabet + numColl + specialChar
#   password = [random.choice(smallAlphabet), random.choice(capitalAlphabet), random.choice(numColl), random.choice(specialChar)]
  password = [smallAlphabet[random.randint(0, len(smallAlphabet)-1)],capitalAlphabet[random.randint(0, len(capitalAlphabet)-1)], numColl[random.randint(0, len(numColl)-1)], specialChar[random.randint(0, len(specialChar)-1)]]
  passLen = int(input("Please enter the length for your password(must be more than or equal to 8): "))
  if (passLen<8):
        print("The length of password must be equal or greater than 8")
        time.sleep(2)
      
  else:
    for i in range(passLen - 4):
        pass
        rand_index = random.randint(0, len(characters)-1)
        password += characters[rand_index]   
    random.shuffle(password)
    generatedPass = ''.join(password)
    print(f"Your password is {generatedPass}")
    userIn = ""
    while userIn.lower() != "e":
        userIn = input("Copy your password and enter e to exit: ")
        if userIn.lower() == "e":
            break
        else:
            print("Wrong Key! Try again")
    
# Code for rock scissor paper
def rock_scissor_paper():
    options = ["rock", "paper", "scissors"]  
    def getComputerChoice(options):
        return random.choice(options)
    
    def getUserChoice():
        while True:
            userChoice = input("Enter your choice (rock, paper, scissors): ").lower()
            if userChoice in options:
                return userChoice
            else: 
                print("Invalid Choice! Please enter rock, paper or scissors.")
    def determineWinner(userChoice, computerChoice):
        if userChoice == computerChoice:
            return "Its a draw"
        elif (userChoice == "rock" and computerChoice == "scissors" or
              userChoice == "paper" and computerChoice == "rock" or
              userChoice == "scissors" and computerChoice == "paper"):
            return "Congrats you won!"
        else:
            return "UF! You lost :(("
        
    print("Welcome to Rock, Paper, Scissors game!")
    compChoice = getComputerChoice(options)
    userChoice = getUserChoice()
    result = determineWinner(userChoice, compChoice)
    print(f"You chose {userChoice}")
    print(f"Computer chose {compChoice}")
    print(result)
    time.sleep(3)


  # make a option list of rock, scissors, paper
  # make a computer choice using random.choice() function
  # ask choice from the user
  # check whether the choice is valid or not
  # make multiple comparisions to decide whether the match is tie, computer won or user
  # print the result

# Code for temperature converter
def temperature_converter():
  # Celsius to Fahrenheit conversion
  # create function celsius_to_fahrenheit
  # use this formula (celsius * 9/5) + 32

  # Fahrenheit to celsius conversion
  # create function fahrenheit_to_celsius
  # use this formula (fahrenheit - 32) * 5/9

  # Celsius to kelvin conversion
  # create function celsius_to_kelvin
  # use this formula celsius + 273

  # Kelvin to celsius conversion
  # create function kelvin_to_celsius
  # use this formula kelvin - 273
  def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

  def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

  def celsius_to_kelvin(celsius):
    return celsius + 273.15

  def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
  
  while True:
        print("--------------------------------------------------------------------")
        print(f"{"1":<3} | {"Celsius to Fahrenheit Conversion":<60} |")
        print(f"{"2":<3} | {"Fahrenheit to Celsius Conversion":<60} |")
        print(f"{"3":<3} | {"Celsius to Kelvin Conversion":<60} |")
        print(f"{"4":<3} | {"Kelvin to Celsius Conversion":<60} |")
        print(f"{"5":<3} | {"To Exit":<60} |")
        print("--------------------------------------------------------------------")
        userChoice = str(input(f"{" ":<3} | Enter your choice: "))
        isInput = False

        try:
            match userChoice:
                case "1":
                    animate_loading(["Loading Your Choice", "Loading Completed"])
                    userInput = float(input("Input the temperature value in Celsius: "))
                    print(f"{userInput} Celsius to Fahrenheit: {celsius_to_fahrenheit(userInput)}")
                    isInput = True
                    
                case "2":
                    animate_loading(["Loading Your Choice", "Loading Completed"])
                    userInput = float(input("Input the temperature value in Fahrenheit: "))
                    print(f"{userInput} Fahrenheit to Celsius: {fahrenheit_to_celsius(userInput)}")
                    isInput = True
                    
                case "3":
                    animate_loading(["Loading Your Choice", "Loading Completed"])
                    userInput = float(input("Input the temperature value in Celsius: "))
                    print(f"{userInput} Celsius to Kelvin: {celsius_to_kelvin(userInput)}")
                    isInput = True
                    
                case "4":
                    animate_loading(["Loading Your Choice", "Loading Completed"])
                    userInput = float(input("Input the temperature value in Celsius: "))
                    print(f"{userInput} Kelvin to Celsius: {kelvin_to_celsius(userInput)}") 
                    isInput = True
                    
                case "5":
                    animate_loading(["Exiting program", "Program Exited"])
                    break
                    
                case _ :
                    print("\n"*100)
                    print("Invalid Input! Please try again.")
                    time.sleep(2)
                    print("\n"*100)
            while True:
                exit = input("Enter e to exit if you're done reading: ")
                if exit.lower() == "e":
                    break
                else:
                    print("Wrong Key!")
        except ValueError:
            print("Invalid Input! Please try again")
               
# Code for multiplication table
def multiplication_table():
  # take input for which table the user wants
  # run a for loop to
  # 2 X 1 = 2
  # 2 X 2 = 4
    while True:
        try:
            userWant = int(input("Enter the number for which you want the multiplication table: "))
            tableLimit = int(input("Enter the highest number for the table: "))
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

    print(f"Multiplication table for {userWant}:")
    for i in range(1, tableLimit + 1):
        print(f"{userWant} x {i} = {userWant * i}")
    
    while True:
        exit = input("Enter e to exit if you're done reading: ")
        if exit == "e":
            break
        else:
            print("Wrong Key!")
    
# Code for random math problem solving
def math_test():
  # generate 2 random numbers and store them in variables
  # store a randomly picked operation (either +  or - or  *) in a variable
  # display the 2 numbers with the operation to be performed and ask user for the answer
  # use loop to run this multiple times and count their chances (maximum 5)
  # Decrement chance by 1 after each mistake guess
  # check and display if the answer is correct or not
  while True:
        print("Welcome to Math Test Game")
        print("--------------------------------------------------------------------")
        print("You can choose a level for the test.")
        print("--------------------------------------------------------------------")
        print(f"{"1":<3} | {"Easy":<60} |")
        print(f"{"2":<3} | {"Normal":<60} |")
        print(f"{"3":<3} | {"Hard":<60} |")
        print(f"{"4":<3} | {"Exit to Menu":<60} |")
        print("--------------------------------------------------------------------")
        level=str(input(f"{" ":<3} | Enter your choice: "))
        animate_loading(["Loading Your Choice", "Loading Completed"])
        attempt = 0
        isInput = False
        match level:
            case "1":
                print("You have 5 attempts to answer")   
                operators = ["+", "-", "*"]
                operator = random.choice(operators)
                num1= random.randint(1,100)
                num2= random.randint(1,100)
                result = 0
                isInput = True
                match operator:
                    case "+":
                        result = num1 + num2
                    case "-":
                        result = num1 - num2
                    case "*":
                        result = num1 * num2
                while(attempt!=5):
                    try: 
                        answer = int(input(f"{num1} {operator} {num2} = "))
                        if answer == result:
                            print("Congrats! Thats the right answer.")
                            time.sleep(3)
                            break
                        else:
                            if answer > result:
                                if answer - result <= 5:
                                    print("You are really close! But the answer is a bit lower.")
                                elif answer - result <= 10:
                                    print("You are getting close! Enter lower")
                                elif answer - result <= 20:
                                    print("You're mid way there! Enter lower")
                                else: 
                                    outputChoice = ["Not even close ! Try again","Wrong Answer! Please try again.", "Really far! Think properly and answer"]
                                    print(random.choice(outputChoice))
                            elif answer < result:
                                if result - answer <= 5:
                                    print("You are really close! But the answer is a bit higher.")
                                elif result - answer <= 10:
                                    print("You are getting close! Enter higher")
                                elif result - answer <= 20:
                                    print("You're mid way there! Enter higher")
                                else: 
                                    outputChoice = ["Not even close ! Try again","Wrong Answer! Please try again.", "Really far! Think properly and answer"]
                                    print(random.choice(outputChoice))
                            attempt +=1
                            print(f"You've got {5-attempt} attemps left")
                            if(attempt==5):
                                print("You've ran out of attemps. You failed to answer")
                                break
                    except ValueError:
                        print("Invalid Input. Please Try again.")
            case "2":
                print("You have 5 attempts to answer")   
                operators = ["+", "-", "*", "/"]
                operator = random.choice(operators)
                num1= random.randint(100, 1000)
                num2= random.randint(100,1000)
                result = 0
                isInput = True
                match operator:
                    case "+":
                        result = num1 + num2
                    case "-":
                        result = num1 - num2
                    case "*":
                        result = num1 * num2
                    case "/":
                        result = round(num1 / num2, 2)
                while(attempt!=5):
                    try: 
                        answer = int(input(f"{num1} {operator} {num2} = "))
                        if answer == result:
                            print("Congrats! Thats the right answer.")
                            time.sleep(3)
                            break
                        else:
                            print("Wrong Answer! Please try again.")
                            attempt +=1
                            print(f"You've got {5-attempt} attemps left")
                            if(attempt==5):
                                print("You've ran out of attemps. You failed to answer")
                                break
                    except ValueError:
                        print("Invalid Input. Please Try again.")
            case "3":
                print("You have 5 attempts to answer")   
                operators = ["+", "-", "*", "/"]
                operator = random.choice(operators)
                num1= random.randint(1000, 10000)
                num2= random.randint(1000,10000)
                result = 0
                isInput = True
                match operator:
                    case "+":
                        result = num1 + num2
                    case "-":
                        result = num1 - num2
                    case "*":
                        result = num1 * num2
                    case "/":
                        result = round(num1 / num2, 2)
                while(attempt!=5):
                    try: 
                        answer = int(input(f"{num1} {operator} {num2} = "))
                        if answer == result:
                            print("Congrats! Thats the right answer.")
                            time.sleep(3)
                            break
                        else:
                            print("Wrong Answer! Please try again.")
                            attempt +=1
                            print(f"You've got {5-attempt} attemps left")
                            if(attempt==5):
                                print("You've ran out of attemps. You failed to answer")
                                break
                    except ValueError:
                        print("Invalid Input. Please Try again.")
            case "4":
                break
            case _ :
                print("Wrong Input!")
        if attempt == 5:
            print(f"The correct answer is {result}")
        while isInput:
            exit = input("Enter e to exit: ")
            if exit.lower() == "e":
                break
            else:
                print("Wrong Key!")
                               
# code for Credit Card Validator
def ccvalidator():
    def verify_card_number(card_number):
        sum_of_odd_digits = 0
        card_number_reversed = card_number[::-1]
        odd_digits = card_number_reversed[::2]

        for digit in odd_digits:
            sum_of_odd_digits += int(digit)

        sum_of_even_digits = 0
        even_digits = card_number_reversed[1::2]
        for digit in even_digits:
            number = int(digit) * 2
            if number >= 10:
                number = (number // 10) + (number % 10)
            sum_of_even_digits += number
        total = sum_of_odd_digits + sum_of_even_digits
        return total % 10 == 0     
    print("Welcome To Credit Card Validator.")
    while True:
        card_number = input("Enter Your Card Number: ")
        card_translation = str.maketrans({'-': '', ' ': ''})
        translated_card_number = card_number.translate(card_translation)
        if translated_card_number.isdigit():
            break
        else:
            print("Invalid card number. Please enter only digits, spaces, and hypens")

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')        
    
    while True:
        exit = input("Enter e to exit: ")
        if exit.lower() == "e":
            break
        else:
            print("Wrong Key!")  

# code for Cipher Text encoding and decoding
def ciphar():
    def vigenere(message, key, direction=1):
        key_index = 0
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        final_message = ''

        for char in message.lower():
            # Append any non-letter character to the message
            if not char.isalpha():
                final_message += char
            else:        
                # Find the right key character to encode/decode
                key_char = key[key_index % len(key)]
                key_index += 1

                # Define the offset and the encrypted/decrypted letter
                offset = alphabet.index(key_char)
                index = alphabet.find(char)
                new_index = (index + offset*direction) % len(alphabet)
                final_message += alphabet[new_index]
        
        return final_message

    def encrypt(message, key):
        return vigenere(message, key)
        
    def decrypt(message, key):
        return vigenere(message, key, -1)


    print("Welcome to Ciphar Text\n")
    
    while(True):
        choice=int(input("Press 1 for encryption\nPress 2 for decryption\nPress 3 for exit\nenter ur choice:"))
        if (choice == 1):
            custom_key = input("Enter custom key for encoding:")
            text = input("Enter any text to encrypt: ")
            print(f"Encrypted text: {encrypt(text, custom_key)}")
        elif(choice==2):
            custom_key = input("Enter custom key for decoding:")
            text = input("Enter any text to decrypt: ")
            print(f"Decrypted text: {decrypt(text, custom_key)}")
        elif(choice==3):
            animate_loading(["Exiting the Program", "Program Exited"])    
            break
        else:
            print("Please enter right choice")      
            
 


while(True):
    print("\n"*200)
    print("--------------------------------------------------------------------")
    print(f"{"1":<3} | {"Calculator":<60} |")
    print(f"{"2":<3} | {"Number Guesser Game":<60} |")
    print(f"{"3":<3} | {"Random Password Generator":<60} |")
    print(f"{"4":<3} | {"Rock Scissors Paper":<60} |")
    print(f"{"5":<3} | {"Temperature converter (celsius, fahrenheit, kelvin)":<60} |")
    print(f"{"6":<3} | {"Multiplication Table":<60} |")
    print(f"{"7":<3} | {"Random math Problem Solving":<60} |")
    print(f"{"8":<3} | {"Credit Card Validator":<60} |")
    print(f"{"9":<3} | {"Cipher Text":<60} |")
    print(f"{"10":<3} | {"Exit the program":<60} |")
    print("--------------------------------------------------------------------")
    choice=str(input(f"{" ":<3} | Enter your choice: "))
    match choice:
        case "1":
            animate_loading(["Loading Your Choice", "Loading Completed"])    
            calculator()
        case "2":
            animate_loading(["Loading Your Choice", "Loading Completed"])    
            number_guessor()
        case "3":
            animate_loading(["Loading Your Choice", "Loading Completed"])    
            random_password_generator()
        case "4":
            animate_loading(["Loading Your Choice", "Loading Completed"])    
            rock_scissor_paper()
        case "5":
            animate_loading(["Loading Your Choice", "Loading Completed"])    
            temperature_converter()
        case "6":
            animate_loading(["Loading Your Choice", "Loading Completed"])    
            multiplication_table()
        case "7":
            animate_loading(["Loading Your Choice", "Loading Completed"])    
            math_test()
        case "8":
            animate_loading(["Loading Your Choice", "Loading Completed"])    
            ccvalidator()
        case "9":
            animate_loading(["Loading Your Choice", "Loading Completed"])    
            ciphar()
        case "10":
            animate_loading(["Exiting the Program", "Program Exited"])    
            break
        case _:
            print("\n"*100)
            print("Invalid Input! Please try again.")
            time.sleep(2)
            print("\n"*100)