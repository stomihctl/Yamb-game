import random
top_menu = ['YAMB', 'downward', 'upward', 'manual']
left_menu = ['1    ', '2    ', '3    ', '4    ', '5    ', '6    ', 'Str8t', 'Full ', 'Poker', 'Yamb ', 'Σ    ']
rows = [10, 10, 10]
columns = [0, 1, 2]
values = [0, 0, 0]

def dice_roll_in_yamb():
    def parity_bit(number):
        binary_number = bin(number)
        binary_list = list(binary_number)
        del binary_list[0]
        del binary_list[0]
        x = 0
        for i in range(len(binary_list)):
            if int(binary_list[i]) == 1:
                x += 1
        if x % 2 == 0:
            return 0
        else:
            return 1

    def single_dice():
        while True:
            binary_digit_list = []
            for i in range(3):
                x = random.randint(1, 1000)
                p = 23
                q = 31
                M = p * q
                y = ((x ** 2) % M)
                binary_digit = parity_bit(y)
                binary_digit_list.append(binary_digit)
            binary_number = (binary_digit_list[0] * 2 ** 0 + binary_digit_list[1] * 2 ** 1 + binary_digit_list[2] * 2 ** 2) + 1
            if binary_number < 7:
                return binary_number

    def roll_five_dice():
        zero = input('0 - roll dice\n')
        if int(zero) == 0:
            all_five = []
            for i in range(5):
                if i == 4:
                    all_five.append(single_dice())
                else:
                    all_five.append(single_dice())
            return all_five
        else:
            exit()

    all_five = roll_five_dice()
    for i in range(len(all_five)):
        if i != 4:
            print(all_five[i], end='         ')
        else:
            print(all_five[i])

    keep_indices = input('enter indices for numbers to keep (space-separated, 0-4)\n').split()
    first_reroll = []
    for i in range(len(keep_indices)):
        first_reroll.append(all_five[int(keep_indices[i])])

    if len(first_reroll) < 5:
        second_round = []
        for i in range(5 - len(first_reroll)):
            second_round.append(single_dice())
        print('kept - ', end='')
        for i in range(len(first_reroll)):
            print(first_reroll[i], end=' ')
        print('\nnew - ', end='')
        for i in range(len(second_round)):
            print(second_round[i], end=' ')

        second_reroll = first_reroll
        keep_indices2 = input('\nenter indices for new numbers to keep (space-separated)\n').split()
        for i in range(len(keep_indices2)):
            second_reroll.append(second_round[int(keep_indices2[i])])

        if len(second_reroll) < 5:
            third_round = []
            for i in range(5 - len(second_reroll)):
                third_round.append(single_dice())
            print('kept - ', end='')
            for i in range(len(second_reroll)):
                print(second_reroll[i], end=' ')
            print('\nnew - ', end='')
            for i in range(len(third_round)):
                print(third_round[i], end=' ')

            final_list = second_reroll
            final_list.extend(third_round)
            print('\nfinal list - ', end='')
            for i in range(len(final_list)):
                print(final_list[i], end=' ')
            roll_count = 3
            return final_list, roll_count
        else:
            print('final list - ', end='')
            for i in range(len(second_reroll)):
                print(second_reroll[i], end=' ')
            roll_count = 2
            return second_reroll, roll_count
    else:
        print('final list - ', end='')
        for i in range(len(first_reroll)):
            print(first_reroll[i], end=' ')
        roll_count = 1
        return first_reroll, roll_count

standard_list = []
array = []
is_transformed = False

def display_score_table(rows, columns, values):
    sum_col1 = 0
    sum_col2 = 0
    sum_col3 = 0
    for y in range(len(top_menu)):
        if y != len(top_menu) - 1:
            print(top_menu[y], end='         ')
        else:
            print(top_menu[y])
    k = -1
    counter = 1
    left_index = 0
    for i in range(11):
        print(left_menu[left_index], end='         ')
        left_index += 1
        for j in range(3):
            for v in range(len(values)):
                if columns[v] == j and rows[v] == i:
                    k = v
                    break
                else:
                    k = -1
            if k >= 0:
                if counter == 33:
                    print(sum_col3)
                    counter += 1
                    values[2] = sum_col3
                elif counter == 32:
                    print(sum_col2, end='                ')
                    counter += 1
                    values[1] = sum_col2
                elif counter == 31:
                    print(sum_col1, end='                ')
                    counter += 1
                    values[0] = sum_col1
                elif counter % 3 == 0:
                    print(values[k])
                    sum_col3 += values[k]
                    if counter == 18:
                        print('Σ', end='             ')
                        print(sum_col1, end='                ')
                        print(sum_col2, end='                ')
                        print(sum_col3)
                    counter += 1
                elif counter % 3 == 2:
                    print(values[k], end='                ')
                    counter += 1
                    sum_col2 += values[k]
                else:
                    print(values[k], end='                ')
                    counter += 1
                    sum_col1 += values[k]
            else:
                if counter % 3 == 0:
                    print("\x1b[31m" + str(0) + "\x1b[0m")
                    if counter == 18:
                        print('Σ', end='             ')
                        print(sum_col1, end='                ')
                        print(sum_col2, end='                ')
                        print(sum_col3)
                    counter += 1
                else:
                    print("\x1b[31m" + str(0) + "\x1b[0m", end='                ')
                    counter += 1
    return '\t'

def transform_table(rows, columns, values):
    if len(values) >= 6:
        k = -1
        for i in range(11):
            for j in range(3):
                for v in range(len(values)):
                    if columns[v] == j and rows[v] == i:
                        k = v
                        break
                    else:
                        k = -1
                if k >= 0:
                    standard_list.append(values[k])
                else:
                    standard_list.append(0)
        global is_transformed
        is_transformed = True
        return array
    else:
        return ''

def standard_array_with_sum(array):
    sum1_to_6 = 0
    sum2_to_6 = 0
    sum3_to_6 = 0
    sum_col1 = 0
    sum_col2 = 0
    sum_col3 = 0
    for i in range(len(array) - 3):
        if i % 3 == 0:
            sum_col1 += array[i]
            if i < 18:
                sum1_to_6 += array[i]
        elif i % 3 == 1:
            sum_col2 += array[i]
            if i < 18:
                sum2_to_6 += array[i]
        else:
            sum_col3 += array[i]
            if i < 18:
                sum3_to_6 += array[i]
    array[30] = sum_col1
    array[31] = sum_col2
    array[32] = sum_col3
    return array, sum1_to_6, sum2_to_6, sum3_to_6

def print_standard_array(array, sum1_to_6, sum2_to_6, sum3_to_6, white_zeros):
    for y in range(len(top_menu)):
        if y != len(top_menu) - 1:
            print(top_menu[y], end='            ')
        else:
            print(top_menu[y])
    counter2 = 0
    for i in range(11):
        print(left_menu[i], end='                ')
        for j in range(3):
            if (counter2) % 3 == 2:
                if array[counter2] != 0:
                    print(array[counter2])
                else:
                    if counter2 in white_zeros:
                        print(0)
                    else:
                        print("\x1b[31m" + str(0) + "\x1b[0m")
                if counter2 == 17:
                    print('Σ', end='                    ')
                    print(sum1_to_6, end='               ')
                    print(sum2_to_6, end='                ')
                    print(sum3_to_6)
                counter2 += 1
            else:
                if array[counter2] != 0:
                    print(array[counter2], end='                ')
                else:
                    if counter2 in white_zeros:
                        print(0, end='                ')
                    else:
                        print("\x1b[31m" + str(0) + "\x1b[0m", end='                ')
                counter2 += 1

def assign_points(row, dice, roll_count):
    points = 0
    if row >= 0 and row <= 5:
        for i in range(5):
            if row + 1 == dice[i]:
                points += dice[i]
    elif row == 6:
        if (1 in dice or 6 in dice) and 2 in dice and 3 in dice and 4 in dice and 5 in dice:
            for i in dice:
                points += i
            if roll_count == 1:
                points += 66
            elif roll_count == 2:
                points += 56
            else:
                points += 46
    elif row == 7:
        counter1 = 1
        counter2 = 1
        index2 = 0
        for i in range(4):
            if dice[0] == dice[i + 1]:
                counter1 += 1
            else:
                index2 = i + 1
        for i in range(5):
            if index2 != i and dice[index2] == dice[i]:
                counter2 += 1
        if counter1 == 2 and counter2 == 3 or counter1 == 3 and counter2 == 2:
            for i in dice:
                points += i
            points += 30
        else:
            points = 0
    elif row == 8:
        counter3 = 1
        index1 = 0
        points = 0
        for i in range(4):
            if dice[0] == dice[i + 1]:
                counter3 += 1
                index1 = i + 1
        if counter3 == 4:
            points += 40
            points += 4 * dice[index1]
        else:
            counter3 = 1
            for i in range(3):
                if dice[1] == dice[i + 2]:
                    counter3 += 1
                    index1 = i + 2
            if counter3 == 4:
                points += 40
                points += 4 * dice[index1]
            else:
                points = 0
    elif row == 9:
        for i in range(4):
            if dice[i] == dice[i + 1]:
                points += dice[i]
                t = True
            else:
                points = 0
                t = False
                break
        if t == True:
            points += dice[0]
            points += 50
    return points

row1 = 0
row2 = 9
row3_list = []
row3 = 0
white_zeros = [30, 31, 32]

while True:
    if len(values) >= 6:
        array = transform_table(rows, columns, values)
        rows = []
        columns = []
        values = []
    menu = input('1 - Empty Table | 2 - Display Table | 3 - Move\n')
    if menu == '1':
        rows = [10, 10, 10]
        columns = [0, 1, 2]
        values = [0, 0, 0]
        print(display_score_table(rows, columns, values))
        row1 = 0
        row2 = 9
        row3_list = []
        row3 = 0
        white_zeros = [30, 31, 32]
        continue
    elif menu == '2':
        if len(values) < 6 and is_transformed == False:
            print(display_score_table(rows, columns, values))
        if len(values) == 0 and is_transformed == True:
            array, sum1_to_6, sum2_to_6, sum3_to_6 = standard_array_with_sum(array)
            print_standard_array(array, sum1_to_6, sum2_to_6, sum3_to_6, white_zeros)
        if len(values) >= 6:
            array = transform_table(rows, columns, values)
            rows = []
            columns = []
            values = []
            if len(values) == 0 and is_transformed == True:
                array, sum1_to_6, sum2_to_6, sum3_to_6 = standard_array_with_sum(array)
                print_standard_array(array, sum1_to_6, sum2_to_6, sum3_to_6, white_zeros)
    elif menu == '3':
        dice, roll_count = dice_roll_in_yamb()
        direction = input('\n1 - down | 2 - up | 3 - manual\n')
        if direction == '1' and row1 < 10:
            c = 0
            points = assign_points(row1, dice, roll_count)
            if is_transformed == False:
                rows.append(row1)
                columns.append(c)
                values.append(points)
                if points == 0:
                    white_zeros.append(3 * row1 + c)
            else:
                array[3 * row1 + c] = points
                if points == 0:
                    white_zeros.append(3 * row1 + c)
            print('Points scored in this round: ', points)
            row1 += 1
        elif direction == '2' and row2 >= 0:
            c = 1
            points = assign_points(row2, dice, roll_count)
            if is_transformed == False:
                rows.append(row2)
                columns.append(c)
                values.append(points)
                if points == 0:
                    white_zeros.append(3 * row2 + c)
            else:
                array[3 * row2 + c] = points
                if points == 0:
                    white_zeros.append(3 * row2 + c)
            print('Points scored in this round: ', points)
            row2 += -1
        elif len(row3_list) < 9:
            c = 2
            row3 = input('Enter desired row index (1-6 for numbers, 7 - straight, 8 - full, 9 - poker, 10 - yamb)\n')
            row3 = int(row3) - 1
            if row3 not in row3_list:
                if is_transformed == False:
                    points = assign_points(row3, dice, roll_count)
                    rows.append(row3)
                    columns.append(c)
                    values.append(points)
                    if points == 0:
                        white_zeros.append(3 * row3 + c)
                else:
                    array[row3 * 3 + c] = points
                    if points == 0:
                        white_zeros.append(3 * row3 + c)
                print('Points scored in this round: ', points)
                row3_list.append(row3)
            else:
                print('error, move will restart')
        else:
            print('error, move restarts')
            continue
    else:
        print('Error, move restarts')
