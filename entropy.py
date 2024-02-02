import random

def entropy():
    lettersprob = {}
    alphabet_liste = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    i = int(max(2, random.random() ** 2 * 15))

    aufgabenalphabet = alphabet_liste[0:i]

    def generate_numbers(n):
        numbers = [random.randint(0, 1000) for _ in range(n - 1)]
        numbers.sort()
        numbers = [0] + numbers + [1000]
        numbers = [numbers[i + 1] - numbers[i] for i in range(n)]
        #numbers = [("0." +("0"*(3-len(str(i)))) + str(i)) for i in numbers]
        return numbers

    
    finallist = list(zip(aufgabenalphabet, generate_numbers(len(aufgabenalphabet))))
    number = 0.0
    for x in finallist:
        number += float(x[1])

    print(finallist, number)



entropy()




