from src import solver0


def getData(name):
    with open("../assets/" + name + ".in", 'r') as file:
        meta = [int(k) for k in file.readline().split(" ")]
        map_pizza = [[0 if case == 'T' else 1 for case in line[:-1]] for line in file.readlines()[0:]]
    return [meta, map_pizza]


for name in [
    "example",
    # "small",
    # "medium",
    # "big"
]:
    data = getData(name)
    result = solver0.solve(data)
    output = solver0.getSlicesData(result)
    with open("../outputs/" + name + ".txt", 'w') as file:
        file.write(output)
    print("Done", name)
