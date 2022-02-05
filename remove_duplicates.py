#remove duplicates in a list

numbers = [2,4,7,7,9,4,6,6]

numbers.sort()

print(set(numbers))

# alternative

numbers = [2,4,7,7,9,4,6,6]

uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)