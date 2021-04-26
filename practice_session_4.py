n = int(input())

if n % 2 == 0:
    print('The number is even')
else:
    print('The number is odd')

if n < 10 and n % 4 == 0:
    print('The number is divisible with 4')
elif n > 10:
    n = n % 100
    if n % 4 == 0:
        print('The number is divisible with 4')
    else:
        print('The number is not divisible with 4')
else:
    print('The number is not divisible with 4')

num = int(input())
check = int(input())

if num % check == 0:
    print('num is a multiple of check')
else:
    print('num is not a multiple of check')

##################
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print(i, end = ' ')
print()

new_list = []
for i in a:
    if i < 5:
        new_list.append(i)
print(new_list)

print([i for i in a if i < 5])

user_number = int(input())

print([i for i in a if i < user_number])

###############

while True:
    p1 = input('p1  ')
    p2 = input('p2  ')

    if p1 == 'Rock':
        if p2 == 'Paper':
            print('p2 you are the winner!!')
        else:
            print('p1 you are the winner!!!')

    if p1 == 'Paper':
        if p2 == 'Scissors':
            print('p2 you are the winner!!!')
        else:
            print('p1 you are the winner')

    if p1 == 'Scissors':
        if p2 == 'Paper':
            print('p1 you are the winner!!!')
        else:
            print('p2 you are the winner!!!')

    answer = input('Do you want to play again?')
    if answer in ['yes', 'Yes', 'YES']:
        pass
    else:
        break
