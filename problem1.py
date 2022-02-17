"""1. Գրել ծրագիր, որը օգտագործողից հարցնում է աշխատանքային ժամերի քանակը,
 մեկ ժամի դրույքաչափը և հաշվում աշխատավարձը:"""

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

print(f"Pay: {hours * rate}")
