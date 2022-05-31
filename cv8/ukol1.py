colours = [ ['red', 255, 0, 0 ],
            ['blue', 0, 0, 255],
            ['green', 0, 255, 0],
            ['red', 178, 34, 34],
            ['red', 139, 0, 0],
            ['green', 34, 139, 34],
            ['blue', 70, 130, 180],
            ['green', 50, 205, 50],
]

def alter_duplicates(colorlist : list) -> list:
    unique_colors = []
    rgbs = []
    
    for color in colorlist:
        unique_colors.append(color[0])
        rgbs.append(color[1:])

    red = 1
    green = 1
    blue = 1
    for index, color in enumerate(unique_colors):
        if color == "red":
            unique_colors[index] = "red_{0}".format(red)
            red += 1
        if color == "green":
            unique_colors[index] = "green_{0}".format(green)
            green += 1
        if color == "blue":
            unique_colors[index] = "blue_{0}".format(blue)
            blue += 1
        
        rgbs[index].insert(0, unique_colors[index])

    return rgbs

print(alter_duplicates(colours))