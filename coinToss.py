from random import *

heads = 0
tails = 0

chosen = 0
choose = input("Heads or Tails? ")

rounds = int(input("How many times would you like to flip the coin? "))

expected = rounds // 2

for i in range(rounds):
    result = randint(1,2)
    if result == 1:
        heads += 1
    if result == 2:
        tails += 1

    if choose.lower() == "tails":
        chosen = tails  # chosen now points to tails

    elif choose.lower() == "heads":
        chosen = heads  # chosen now points to heads

    else:
        print("Invalid input. Try again")
        exit(0)

    if rounds > 10000000 and i % 100 == 0:
        intermediateCheck = "Intermediate check at " + str(i) + "th round"
        print(intermediateCheck)
        print("Expected:", expected, "/", rounds)
        print("Actual: ", chosen, "/", rounds)
        print()

print("Our expected result for landing on", choose, "is", expected, "out of", rounds)
print("In this round, our actual result of", choose, "was", chosen, "out of", rounds)
print("The difference between the expected and the actual results were", abs(chosen - expected))