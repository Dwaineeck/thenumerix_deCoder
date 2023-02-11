import random

#Function generates list of random numbers
def secret_list(max_range):
    secret_list = []
    for i in range(4):
        secret_list.append(random.randint(1,max_range))
    return secret_list

deCoder_list = secret_list(5)
print(deCoder_list)

#deCoder Game
print("Welcome deCoder!")
print("Wanna play a game? \n")

correct = 0
tries = 0
while correct <  4:
    guess1 = int (input("Please guess the First number: "))
    guess2 = int (input("Please guess the Second number: "))
    guess3 = int (input("Please guess the Third number: "))
    guess4 = int (input("Please guess the Fourth number: "))
    tries += 1

    if guess1 == deCoder_list[0]:
        correct += 1
    if guess2 == deCoder_list[1]:
        correct += 1
    if guess3 == deCoder_list[2]:
        correct += 1
    if guess4 == deCoder_list[3]:
        correct += 1
    if correct < 4:
        print("You guessed " + str(correct) + " number(s) correctly. \n")
        correct = 0
        continue
    else:
        if tries == 1:
            print("Congratulations, you guessed all four numbers!! It took you " + str(tries) + " try. \n")
        else:
            print("Congratulations, you guessed all four numbers!! It took you " + str(tries) + " tries. \n")