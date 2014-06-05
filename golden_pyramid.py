def traverse(pyramid, i, j):
    """
    traverse from every possible position
    """
    l = len(pyramid)
    if i == l-1:
        return pyramid[i][j]
    else:
        ld = traverse(pyramid, i+1, j)
        rd = traverse(pyramid, i+1, j+1)
        return (ld if ld > rd else rd) + pyramid[i][j]

def count_gold(pyramid):
    """
    Return max possible sum in a path from top to bottom
    """
    return traverse(pyramid,0,0)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
