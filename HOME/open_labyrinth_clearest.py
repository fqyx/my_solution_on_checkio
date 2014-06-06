def checkio(data):
    result = []
    dirs = [[-1, 0, "W"], [+1, 0, "E"], [0, -1, "N"], [0, +1, "S"]]
    def move(path, x, y, field):
        field[y][x] = 1
        if x == 10 and y == 10:
            result.append(path)
        for d in dirs:
            if field[y + d[1]][x + d[0]] == 0:
                move(path + d[2], x + d[0], y + d[1], field)
    move("", 1, 1, data)
    return result[0]
