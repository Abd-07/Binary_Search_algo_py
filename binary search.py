numbers = []

numbers_size = 100_000
#So we don't count zero as one of the elements
numbers_size += 1

for i in range(numbers_size):
    numbers.append(i)

#print(numbers)

wanted_number = 89000

def divider():
    print("----------------------------------------")

def binary_search():
    divider()
    min_ = 0
    max_ = len(numbers)-1
    tries = 0

    print("Binary Search : ")

    while min_ <= max_ :
        tries += 1

        median = min_ + (max_ - min_)//2
        guess = numbers[median]

        if guess > wanted_number:
            max_ = median - 1
        if guess < wanted_number:
            min_ = median + 1

        if guess == wanted_number :
            print(f"The wanted number {wanted_number}, was found")
            print(f'Tries required {tries}')
            break

        '''if guess == wanted_number:
            print(f"The wanted number {wanted_number}, was found")
            print(f'Tries required {tries}')
            break
        elif guess < wanted_number : 
            min_ = median + 1
        else:
            max_ = median - 1'''

    print()
    divider()

binary_search()