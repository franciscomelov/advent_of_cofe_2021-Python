with open("input.txt", "r") as diagnostic:
    size_number = 5
    gamma = "10110"
    epsilon = "01001"
    power = 198
    diagnostic = list(diagnostic)

    ox_gen = list(diagnostic)
    print(ox_gen)

    for i in range(size_number):
        ox_gen = [number for number in ox_gen if number[i] == gamma[i]]
        print(ox_gen)


