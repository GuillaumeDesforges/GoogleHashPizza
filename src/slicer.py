# renvoie une liste de toutes les parts possibles (et pas forcément valides!) contenant la cellule en y,x
# une part = [y0,x0,y1,x1] en haut a gauche puis en bas a droite
# 0 pour tomate, 1 pour mushroom ; map_pizza est deja en 0 et 1
#on explore un carre de cote 2*max_size-1
#a chaque fois, on regarde si l'aire du rectangle formé par le point choisi et y,x est correcte
#si oui, on l'ajoute


def get_all_local_slices(y, x, data):
    meta = data[0]
    n_lines = meta[0]
    n_columns = meta[1]
    min_component = meta[2]
    max_slice_size = meta[3]
    slices_list = []
    for i_line in range(2 * max_slice_size - 1):
        for j_column in range(2 * max_slice_size - 1):
            i_current = y - (max_slice_size - 1) + i_line
            j_current = x - (max_slice_size - 1) + j_column
            if 0 <= i_current and i_current < n_lines and 0 <= j_current and j_current < n_columns:
                # l'aire, c'est le nombre de cellules dedans lol
                area = abs(-(max_slice_size - 1) + i_line + 1) * abs(-(max_slice_size - 1) + j_column + 1)
                if area >= 2 * min_component and area <= max_slice_size:
                    slice_new = [min(y, i_current), min(x, j_current), max(y, i_current), max(x, j_current)]
                    slices_list.append(slice_new)
    return slices_list

#compte le nombre de tomates et de shrooms pour chaque part


def count_number_of_each_in_slice(slice_new, map_pizza):
    m = 0
    t = 0
    for i_line in range(slice_new[0], slice_new[2] + 1):
        for j_column in range(slice_new[1], slice_new[3] + 1):
            if map_pizza[i_line][j_column] == 0:
                m += 1
            else:
                t += 1
    return [m, t]

#s'il n'y a pas assez d'un des deux ingredients, on supprime la part


def get_all_local_correct_slices(slices_list, min_component, map_pizza):
    # j suit l'indice actuel, en tenant compte des suppressions
    j = 0
    for i in range(len(slices_list)):
        A = count_number_of_each_in_slice(slices_list[j], map_pizza)
        if A[0] < min_component or A[1] < min_component:
            del slices_list[j]
        else:
            j += 1
    return slices_list