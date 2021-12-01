with open("input.txt", "r") as measurements:
    prev_sum_window = None
    curr_sum_window = None
    window_1 = None
    window_2 = None
    window_3 = None
    increased = 0

    for curr_value in measurements:
        curr_value = int(curr_value)

        if window_1 is None:
            window_1 = curr_value
            continue
        if window_2 is None:
            window_2 = curr_value
            continue
        if window_3 is None:
            window_3 = curr_value
            continue
        if prev_sum_window is None:
            prev_sum_window = window_3 + window_2 + window_1

        window_1, window_2, window_3 = window_2, window_3, curr_value
        curr_sum_window = window_3 + window_2 + window_1

        if prev_sum_window < curr_sum_window:
            increased += 1

        prev_sum_window = curr_sum_window

    print(increased)
