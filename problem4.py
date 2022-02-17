""" 4. Գրել ծրագիր, որը կստանա շախմատի վանդակի
կոորդինատները և կտպի վանդակի գույնը։"""

coords = list(input("Enter the coordinates of the square: ").upper())

print('white ' if ((ord(coords[0]) - 64) + int(coords[1])) % 2 else 'black ')  # ord('A') equals 65
