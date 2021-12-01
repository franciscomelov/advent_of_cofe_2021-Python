with open("input.txt", "r") as measurements:
    prev_value = None
    increased = 0

    for curr_value in measurements:
        curr_value = int(curr_value)

        if prev_value is None:
            prev_value = curr_value
            continue

        if prev_value < curr_value:
            increased += 1
        prev_value = curr_value

    print(increased)
