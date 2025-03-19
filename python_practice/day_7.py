# while loop

n = 0
while n < 5:
    print(f"It is less than 5 and the number is {n}")
    n = n + 1


num = [1,2,3]
num_square = []
n = 0
while n < len(num):
    num_square.append(num[n]**2)
    n = n + 1

num_square

# for loop

num_square_loop = []
for n in num:
    num_square_loop.append(n**2)
num_square_loop

