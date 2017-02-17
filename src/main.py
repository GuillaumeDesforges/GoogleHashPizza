from src import solver1

def getData(name):
    with open("../assets/" + name + ".in", 'r') as file:
        meta = [int(k) for k in file.readline().split(" ")]
        map_pizza = [[0 if case == 'T' else 1 for case in line[:-1]] for line in file.readlines()[0:]]
    return [meta, map_pizza]


for name in [
    "example",
    "small",
    "medium",
    "big"
]:
    print("Starting", name)
    data = getData(name)
    result = solver1.solve(data)
    output = solver1.getSlicesData(result)
    with open("../outputs/" + name + ".txt", 'w') as file:
        file.write(output)
    print("Done", name)