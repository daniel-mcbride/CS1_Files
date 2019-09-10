#1
def problem1():
    for i in range(5):
        print("Daniel", end=" ")

#2
def problem2():
    for i in range(5):
        print("Daniel")

#3
def problem3():
    count = 10
              
    while count > 0:
        print(count)
        count -= 1
    print("Blast Off!!")

#4
def problem4():
    for denominator in range(2, 11):
        print( 1 / denominator)

# More Practice 3
def problem5():
    for outer in range(1, 11):
        print("Multiples of", outer)
        for inner in range(1, 11):
            print(outer, "*", inner, "=", inner * outer)
        print()

problem5()
