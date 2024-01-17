matris = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "6", "9"],
]


def map():
    return f"""
    | {matris[0][0]} | {matris[0][1]} | {matris[0][2]} |
    -------------
    | {matris[1][0]} | {matris[1][1]} | {matris[1][2]} |
    -------------
    | {matris[2][0]} | {matris[2][1]} | {matris[2][2]} |
    """


print(map())
