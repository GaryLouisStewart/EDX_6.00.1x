'''some more epsilon examples below for you to run. comment out the blocks of code that you do not want to run and try each one out.'''


#1
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))



#2

y = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while guess <= y:
    if abs(guess**2 -y) >= epsilon:
        guess += step

if abs(guess**2 - y) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))



#3

z = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2 -z) >= epsilon:
    if guess <= z:
        guess += step
    else:
        break

if abs(guess**2 - z) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))