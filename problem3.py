""" 3. Գրել ծրագիր, որը օգտագործողից որպես մուտքային տվյալ կստանա տառ և կտպի հաղորդագրություն,
տառը ձայնավոր է, բաղաձայն, թե և՜ ձայնավոր, և՜ բաղաձայն:
Ձայնավոր են a, e, i, o, u տառերը, y-ը և՜ ձայնավոր է, և՜ բաղաձայն, մնացածը՝ բաղաձայն:"""

vowels = ['a', 'e', 'i', 'o', 'u']

letter = input("տառը: ")

print("ձայնավոր է" if letter in vowels else "բաղաձայն է" if letter != 'y' else "և՜ ձայնավոր, և՜ բաղաձայն")
