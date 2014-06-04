eckio(game_result):
    x = []
    #column
    x.append(game_result[0][0]+game_result[1][0]+game_result[2][0])
    x.append(game_result[0][1]+game_result[1][1]+game_result[2][1])
    x.append(game_result[0][2]+game_result[1][2]+game_result[2][2])
    #row
    for e in game_result:
        x.append(e)
    #diagonal
    x.append(game_result[0][0]+game_result[1][1]+game_result[2][2])
    x.append(game_result[2][0]+game_result[1][1]+game_result[0][2])

    #check same
    f=[e for e in x if e[0]==e[1] and e[2]==e[1] and e[0]!='.']
    if f:
        return f[0][0]
    else:
        return "D"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        u"X.O",
        u"XX.",
        u"XOO"]) == "X", "Xs wins"
    assert checkio([
        u"OO.",
        u"XOX",
        u"XOX"]) == "O", "Os wins"
    assert checkio([
        u"OOX",
        u"XXO",
        u"OXX"]) == "D", "Draw"
    assert checkio([
        u"O.X",
        u"XX.",
        u"XOO"]) == "X", "Xs wins again"
