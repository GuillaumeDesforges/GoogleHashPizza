def expand_slices_to_fullest(meta, ordered_coordinates_per_level, map_distribution):
    n_lines = meta[0]
    n_columns = meta[1]
    max_slice_size = meta[3]
    # expand slices as much as possible
    distribution_modified = True
    while distribution_modified:
        distribution_modified = False
        for list_coordinates in ordered_coordinates_per_level:
            for coordinates in list_coordinates:
                y, x = tuple(coordinates)
                # if cell is part of a slice
                slice_id = map_distribution[y][x]
                if slice_id != 0:
                    # find slice's points
                    x0, y0, x1, y1 = x, y, x, y
                    while x0 - 1 >= 0 and map_distribution[y0][x0 - 1] == slice_id:
                        x0 -= 1
                    while x1 + 1 < n_columns and map_distribution[y1][x1 + 1] == slice_id:
                        x1 += 1
                    while y0 - 1 >= 0 and map_distribution[y0 - 1][x0] == slice_id:
                        y0 -= 1
                    while y1 + 1 < n_lines and map_distribution[y1 + 1][x1] == slice_id:
                        y1 += 1
                    # try to expand in all directions by 1
                    # left
                    if x0 - 1 >= 0:
                        all_cells_free = True
                        # check if all cells on the left are free
                        for y in range(y0, y1 + 1):
                            if map_distribution[y][x0 - 1] != 0:
                                all_cells_free = False
                                break
                        if all_cells_free:
                            # if expanded slice size is conform
                            x0 = x0 - 1
                            if max_slice_size == 0 or (y1 - y0 + 1) * (x1 - x0 + 2) <= max_slice_size:
                                distribution_modified = True
                                for y in range(y0, y1 + 1):
                                    map_distribution[y][x0] = slice_id
                    # up
                    if y0 - 1 >= 0:
                        all_cells_free = True
                        # check if all upper cells are free
                        for x in range(x0, x1 + 1):
                            if map_distribution[y0 - 1][x] != 0:
                                all_cells_free = False
                                break
                        if all_cells_free:
                            # if expanded slice size is conform
                            y0 = y0 - 1
                            if max_slice_size == 0 or (y1 - y0 + 2) * (x1 - x0 + 1) <= max_slice_size:
                                distribution_modified = True
                                for x in range(x0, x1 + 1):
                                    map_distribution[y0][x] = slice_id
                    # right
                    if x1 + 1 < n_columns:
                        all_cells_free = True
                        # check if all cells on the right are free
                        for y in range(y0, y1 + 1):
                            if map_distribution[y][x1 + 1] != 0:
                                all_cells_free = False
                                break
                        if all_cells_free:
                            # if expanded slice size is conform
                            if max_slice_size == 0 or (y1 - y0 + 1) * (x1 - x0 + 2) <= max_slice_size:
                                x1 = x1 + 1
                                distribution_modified = True
                                for y in range(y0, y1 + 1):
                                    map_distribution[y][x1] = slice_id
                    # down
                    if y1 + 1 < n_lines:
                        all_cells_free = True
                        # check if all lower cells are free
                        for x in range(x0, x1 + 1):
                            if map_distribution[y1 + 1][x] != 0:
                                all_cells_free = False
                                break
                        if all_cells_free:
                            # if expanded slice size is conform
                            if max_slice_size == 0 or (y1 - y0 + 2) * (x1 - x0 + 1) <= max_slice_size:
                                y1 = y1 + 1
                                distribution_modified = True
                                for x in range(x0, x1 + 1):
                                    map_distribution[y1][x] = slice_id
