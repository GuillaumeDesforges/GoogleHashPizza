# renvoie une liste de toutes les parts possibles (et pas forcément valides!) contenant la cellule en y,x
# une part = [y0,x0,y1,x1] en haut a gauche puis en bas a droite
# 0 pour tomate, 1 pour mushroom ; map_pizza est deja en 0 et 1
#on explore un carre de cote 2*max_size-1
#a chaque fois, on regarde si l'aire du rectangle formé par le point choisi et y,x est correcte
#si oui, on l'ajoute


# créer les prototypes de parts en coordonnées relatives en fonction de la taille min/max
def get_slices_prototype(meta):
    min_component = meta[2]
    max_slice_size = meta[3]
    slices_prototype = []
    for y in range(-max_slice_size, max_slice_size + 1):
        for x in range(-max_slice_size, max_slice_size + 1):
            y0, x0, y1, x1 = min(y, 0), min(x, 0), max(y, 0), max(x, 0)
            area = (y1 - y0 + 1) * (x1 - x0 + 1)
            if area >= 2 * min_component and area <= max_slice_size:
                slice_new = [y0, x0, y1, x1]
                slices_prototype.append(slice_new)
    return slices_prototype


def get_all_local_slices(y, x, data, slices_prototype):
    meta = data[0]
    n_lines = meta[0]
    n_columns = meta[1]
    slices = slices_prototype[:]
    slices_to_remove = []
    for i, slice in enumerate(slices):
        y0, x0, y1, x1 = y + slice[0], x + slice[1], y + slice[2], x + slice[3]
        if not (0 <= y0 and y1 < n_lines and 0 <= x0 and x1 < n_columns):
            slices_to_remove.append(slice)
        else:
            slices[i] = [y0, x0, y1, x1]
    for slice in slices_to_remove:
        slices.remove(slice)
    return slices

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


def get_all_local_correct_slices(slices_list, meta, map_pizza):
    min_component = meta[2]
    # j suit l'indice actuel, en tenant compte des suppressions
    j = 0
    for i in range(len(slices_list)):
        A = count_number_of_each_in_slice(slices_list[j], map_pizza)
        if A[0] < min_component or A[1] < min_component:
            del slices_list[j]
        else:
            j += 1
    return slices_list