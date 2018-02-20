def load_data(hams, spams, filename):
    f = open(filename, 'r', encoding="utf8")
    for line in f:
        if line[0] == 's':
            spams.append(line[4:])
        else:
            hams.append(line[3:])


def get_data(filename):
    f = open(filename, 'r', encoding="utf8")
    list = []
    for line in f:
        list.append(line)
    return list


def divide_data(list, hams, spams):
    for item in list:
        if item[0] == 's':
            spams.append(item[4:])
        else:
            hams.append(item[3:])
