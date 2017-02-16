import sys

def count(T, i):
    return sum(row.count(i) for row in T)


def density_local_score(T, pizza_weight=1, void_weight=1):
    """
    Calcul de la densitée locale autour d'un point donné
    0 = hors losange, 1=vide, 2=tomate et 3=champignon
    :param T:
    :return:
    """
    void = count(T, 1)
    n_tomato = count(T, 2)
    n_mushroom = count(T, 3)
    return void * void_weight + pizza_weight * abs(n_mushroom - n_tomato)


def get_density_array(data):
    """
    Trace un losange (norme 1 <= max_slice_size) autour de chaque point et calcule la densitée corrigée selon la formule :
    abs(nb_tomates-nb_mushrooms)+nb_cases_vides
    :param data: Le tableau des données d'entrées
    :return: Le tableau des densitées
    """

    # extract data
    meta = data[0]
    map_pizza = data[1]
    n_lines = meta[0]
    n_columns = meta[1]
    min_component = meta[2]
    max_slice_size = meta[3]

    # On privilegie priorité uniformité vs priorité des bords si trouver une part est dur
    pizza_weight = min_component
    # pizza_weight = 1

    # Initialisation du tableau de densité
    density = [[0 for i in range(n_columns)] for j in range(n_lines)]

    # show progress
    coordinates_counter = 0
    max_coordinates_counter = n_lines * n_columns
    next_percentage = 0

    for i_line in range(n_lines):
        for i_column in range(n_columns):
            coordinates_counter += 1
            if int((coordinates_counter / max_coordinates_counter) * 100) == next_percentage:
                sys.stdout.write("\r" + str(int(coordinates_counter / max_coordinates_counter * 100)) + "%")
                next_percentage += 1
            # Selectionne le carré de taille max_slice_size autour du point i_line, i_column
            # On met 0 = hors losange, 1=vide, 2=tomate et 3=champignon
            T = [[0 for i in range(2 * max_slice_size - 1)] for j in range(2 * max_slice_size - 1)]
            for x in range(-max_slice_size + 1, max_slice_size):
                for y in range(-max_slice_size + 1, max_slice_size):
                    # Test losange
                    if ((abs(x) + abs(y)) <= max_slice_size - 1):
                        # Test non vide
                        if (
                                            i_line + x >= 0 and i_line + x < n_lines and i_column + y >= 0 and i_column + y < n_columns):
                            if (map_pizza[i_line + x][i_column + y] == 0):
                                T[max_slice_size - 1 + x][max_slice_size - 1 + y] = 2
                            else:
                                T[max_slice_size - 1 + x][max_slice_size - 1 + y] = 3
                        else:
                            T[max_slice_size - 1 + x][max_slice_size - 1 + y] = 1

            density[i_line][i_column] = density_local_score(T)

    return density

def organize_coordinates_by_level(map_density):
    max_level = max([max(line) for line in map_density])
    result = [[] for k in range(max_level + 1)]
    for y, line in enumerate(map_density):
        for x, level in enumerate(line):
            # max priority is at index 0
            result[max_level - level].append([y, x])
    return result
