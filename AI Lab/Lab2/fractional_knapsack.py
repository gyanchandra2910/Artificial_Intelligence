from functools import cmp_to_key
def cpma(a, b):
    if a[0] > b[0]:
        return -1  
    elif a[0] < b[0]:
        return 1
    else:
        return 0
    
# Name, Price, Weight
items = [
    ("A", 60, 10), 
    ("B", 100, 20),
    ("C", 120, 30),
    ("D", 75, 15)
]
capacity = 50

items_with_ratio = []

for name, price, weight in items:
    ratio = price/ weight
    items_with_ratio.append((ratio, name, price, weight))
    
items_with_ratio.sort(key=cmp_to_key(cpma))

total_price = 0
bag = []
current_wt = 0

for ratio , name , price, weight in items_with_ratio:
    if current_wt + weight <= capacity:
        current_wt = current_wt + weight
        bag.append(name)
        total_price = total_price + price
        

print("The total price is ", total_price)
print("The bag is ", bag)
print("The current wt is ", current_wt)