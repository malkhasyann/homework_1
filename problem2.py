""" Գրել ծրագիր, որն անընդհատ ընդունում է թվեր մինչև օգտագործողը մուտքագրում է «done»:
«done» մուտքագրելուց հետո տպել մուտքագրված թվերի գումարը, քանակը,և միջին թվաբանականը:
Եթե օգտագործողը մուտքագրում է այլ բան թվի փոխարեն,
տպել հաղորդագրություն սխալ մուտքի մասին և սպասել հաջորդ թվին:"""

s = 0  # sum
i = 0  # number of inputs
current_input = input("Enter a number: ")

while current_input != "done":
    try:
        s += int(current_input)
        i += 1
    except ValueError:
        print("Invalid input")
    current_input = input("Enter a number: ")

print(s, i, (float(s) / i) if i != 0 else 0)  # sum, count, average
