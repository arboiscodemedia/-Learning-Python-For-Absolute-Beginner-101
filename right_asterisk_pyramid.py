
def right_pyramid(n):

    for i in range(0, n):
        for j in range(0, i + 1):
            print("* ", end = "")

        print("\r")

n = input("Enter values: \n")
n = int(n)
right_pyramid(n)