def listaz(colors):
    for color in colors:
        if isinstance(color, int) and color > 5:
            print(color)

listaz([1,11,2.0,8.0, 9.2, 'A', "QQ",6])