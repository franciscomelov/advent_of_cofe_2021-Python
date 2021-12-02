with open("input.txt", "r") as commands:
    horizontal_pos = 0
    depth = 0
    aim = 0

    for command in commands:
        command = command.split(" ")
        units = int(command[1])
        direction = command[0]

        if direction == "forward":
            horizontal_pos += units
            depth += aim * units
        elif direction == "up":
            aim -= units
        elif direction == "down":
            aim += units

        # print(units, direction)
        # print("horizontal_pos:", horizontal_pos)
        # print("depth:", depth)
        # print("aim:", aim)
        # print("_________________")

    print("horizontal_pos:", horizontal_pos)
    print("depth:", depth)
    print(depth * horizontal_pos)
