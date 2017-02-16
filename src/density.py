def get_density_array(data):
    meta = data[0]
    n_lines = meta[0]
    n_columns = meta[1]
    return [[0 for c in range(n_columns)] for l in range(n_lines)]


def organize_coordinates_by_level(map_density):
    max_level = max([max(line) for line in map_density])
    result = [[] for k in range(max_level + 1)]
    for y, line in enumerate(map_density):
        for x, level in enumerate(line):
            # max priority is at index 0
            result[max_level - level].append([y, x])
    return result
