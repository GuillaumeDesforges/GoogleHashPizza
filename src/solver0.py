def solve(data):
    # extract data
    meta = data[0]
    map_pizza = data[1]
    n_lines = meta[0]
    n_columns = meta[1]
    min_component = meta[2]
    # max_slice_size equals zero if unlimited slice size
    max_slice_size = meta[3]
    # represent which cases have been used
    map_distributed = [[0 for i_column in range(n_columns)] for i_line in range(n_lines)]
    # vars to store line management
    # each time we iterate through a line to create slices, we record the max height of those
    line_max_height = 0
    current_valid_slice_id = 1
    # look for max

    for i_line in range(n_lines):
        for i_column in range(n_columns):
            # if cell is not attributed to a slice
            if map_distributed[i_line][i_column] == 0:
                # look for a valid slice
                validSliceFound = False
                y0 = i_line
                x0 = i_column
                slice_max_width = min(max_slice_size,
                                      n_columns - i_column + 1) if max_slice_size > 0 else n_columns - i_column + 1
                for slice_width in range(0, slice_max_width):
                    if validSliceFound:
                        break
                    reached_right_end = slice_width == n_columns - i_column
                    max_slice_y_cursor = slice_width if not reached_right_end else line_max_height
                    for slice_y_cursor in range(max_slice_y_cursor):
                        if validSliceFound:
                            break
                        if not reached_right_end:
                            slice_x_cursor = slice_width - slice_y_cursor - 1
                        else:
                            slice_x_cursor = slice_width - 1
                        y1 = i_line + slice_y_cursor
                        x1 = i_column + slice_x_cursor
                        # check slice size is less than max
                        if max_slice_size == 0 or (y1 - y0 + 1) * (x1 - x0 + 1) <= max_slice_size:
                            # check if y is in bound (then all slice is in bound)
                            if y1 < n_lines:
                                # no need to check if slices are available
                                # check if enough of each component
                                counter_component0 = 0
                                counter_component1 = 0
                                all_cells_free = True
                                for y in range(y0, y1 + 1):
                                    for x in range(x0, x1 + 1):
                                        if map_distributed[y][x] != 0:
                                            all_cells_free = False
                                        if map_pizza[y][x] == 0:
                                            counter_component0 += 1
                                        else:
                                            counter_component1 += 1
                                if all_cells_free and counter_component0 >= min_component and counter_component1 >= min_component:
                                    # slice is valid, add it
                                    validSliceFound = True
                                    # print("Valid slice found", x0, y0, x1, y1)
                                    for y in range(y0, y1 + 1):
                                        for x in range(x0, x1 + 1):
                                            map_distributed[y][x] = current_valid_slice_id
                                    current_valid_slice_id += 1
                                    # set new max height for line
                                    line_max_height = max(line_max_height, y1 - y0 + 1)
                                else:
                                    # slice is not valid, go to next
                                    pass
    # expand slices as much as possible
    distribution_modified = True
    while distribution_modified:
        distribution_modified = False
        for i_line in range(n_lines):
            for i_column in range(n_columns):
                # if cell is part of a slice
                slice_id = map_distributed[i_line][i_column]
                if slice_id != 0:
                    # find slice's points
                    x0, y0, x1, y1 = i_column, i_line, i_column, i_line
                    while x0 - 1 >= 0 and map_distributed[y0][x0 - 1] == slice_id:
                        x0 -= 1
                    while x1 + 1 < n_columns and map_distributed[y1][x1 + 1] == slice_id:
                        x1 += 1
                    while y0 - 1 >= 0 and map_distributed[y0 - 1][x0] == slice_id:
                        y0 -= 1
                    while y1 + 1 < n_lines and map_distributed[y1 + 1][x1] == slice_id:
                        y1 += 1
                    # try to expand in all directions by 1
                    # left
                    if x0 - 1 >= 0:
                        all_cells_free = True
                        # check if all cells on the left are free
                        for y in range(y0, y1 + 1):
                            if map_distributed[y][x0 - 1] != 0:
                                all_cells_free = False
                                break
                        if all_cells_free:
                            # if expanded slice size is conform
                            x0 = x0 - 1
                            if max_slice_size == 0 or (y1 - y0 + 1) * (x1 - x0 + 2) <= max_slice_size:
                                distribution_modified = True
                                for y in range(y0, y1 + 1):
                                    map_distributed[y][x0] = slice_id
                    # up
                    if y0 - 1 >= 0:
                        all_cells_free = True
                        # check if all upper cells are free
                        for x in range(x0, x1 + 1):
                            if map_distributed[y0 - 1][x] != 0:
                                all_cells_free = False
                                break
                        if all_cells_free:
                            # if expanded slice size is conform
                            y0 = y0 - 1
                            if max_slice_size == 0 or (y1 - y0 + 2) * (x1 - x0 + 1) <= max_slice_size:
                                distribution_modified = True
                                for x in range(x0, x1 + 1):
                                    map_distributed[y0][x] = slice_id
                    # right
                    if x1 + 1 < n_columns:
                        all_cells_free = True
                        # check if all cells on the right are free
                        for y in range(y0, y1 + 1):
                            if map_distributed[y][x1 + 1] != 0:
                                all_cells_free = False
                                break
                        if all_cells_free:
                            # if expanded slice size is conform
                            if max_slice_size == 0 or (y1 - y0 + 1) * (x1 - x0 + 2) <= max_slice_size:
                                x1 = x1 + 1
                                distribution_modified = True
                                for y in range(y0, y1 + 1):
                                    map_distributed[y][x1] = slice_id
                    # down
                    if y1 + 1 < n_lines:
                        all_cells_free = True
                        # check if all lower cells are free
                        for x in range(x0, x1 + 1):
                            if map_distributed[y1 + 1][x] != 0:
                                all_cells_free = False
                                break
                        if all_cells_free:
                            # if expanded slice size is conform
                            if max_slice_size == 0 or (y1 - y0 + 2) * (x1 - x0 + 1) <= max_slice_size:
                                y1 = y1 + 1
                                distribution_modified = True
                                for x in range(x0, x1 + 1):
                                    map_distributed[y1][x] = slice_id
    return map_distributed


def getSlicesData(map_distributed):
    m = [row[:] for row in map_distributed]
    n_lines = len(m)
    n_columns = len(m[0])
    output = ""
    slices_counter = 0
    for i_line in range(n_lines):
        for i_column in range(n_columns):
            # if cell is part of a slice
            slice_id = m[i_line][i_column]
            if slice_id != 0:
                # find slice's points
                x0, y0, x1, y1 = i_column, i_line, i_column, i_line
                while x0 - 1 >= 0 and m[y0][x0 - 1] == slice_id:
                    x0 -= 1
                while x1 + 1 < n_columns and m[y1][x1 + 1] == slice_id:
                    x1 += 1
                while y0 - 1 >= 0 and m[y0 - 1][x0] == slice_id:
                    y0 -= 1
                while y1 + 1 < n_lines and m[y1 + 1][x1] == slice_id:
                    y1 += 1
                # print(y0, x0, y1, x1)
                for x in range(x0, x1 + 1):
                    for y in range(y0, y1 + 1):
                        m[y][x] = 0
                output += str(y0) + " " + str(x0) + " " + str(y1) + " " + str(x1) + "\n"
                slices_counter += 1
    output = str(slices_counter) + "\n" + output
    return output
