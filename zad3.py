file_path = r"./Dane_PR2/pary.txt"
with open(file_path, "r") as f:
    raw_data = f.readlines()

pairs = [(int(x.split(" ")[0]), x.split(" ")[1][:-1]) for x in raw_data]
pairs = [x for x in pairs if x[0] == len(x[1])]

pairs.sort(key=lambda x: x[0])
smallest_length = pairs[0][0]

pairs = [x for x in pairs if x[0] == smallest_length]

pairs.sort(key=lambda x: x[1])

print(pairs[0][0], pairs[0][1])