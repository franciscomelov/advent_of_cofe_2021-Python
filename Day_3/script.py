with open("input.txt", "r") as diagnostic:
    gamma = ""
    epsilon = ""

    counter_1 = 0
    size_number = 5
    diagnostic = list(diagnostic)

    for i in range(size_number):
        counter_1 = 0
        for number in diagnostic:
            digit = number[i]
            if digit == "1":
                counter_1 += 1
            else:
                counter_1 -= 1

        if counter_1 >= 1:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"


    print("gama:", gamma, int(gamma, 2))
    print("epsilon:", epsilon, int(epsilon, 2))
    print("power:", int(gamma, 2) * int(epsilon, 2))







