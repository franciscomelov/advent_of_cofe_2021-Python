with open("input.txt", "r") as commands:
    horizontal_pos = 0
    depth = 0

    for command in commands:
        command = command.split(" ")
        units = int(command[1])
        direction = command[0]

        if direction == "forward":
            horizontal_pos += units
        elif direction == "up":
            depth -= units
        elif direction == "down":
            depth += units

    print("horizontal_pos:", horizontal_pos)
    print("depth:", depth)
    print(depth * horizontal_pos)
