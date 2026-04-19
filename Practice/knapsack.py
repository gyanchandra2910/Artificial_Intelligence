def cmp(item):
  return (-item[0], item[3])

# name price wt
items = [
  ("A", 60, 70),
  ("B", 100, 20),
  ("C", 120, 30),
  ("D", 75, 15)
]
capacity = 50

items_with_ratio = []

for name, price, wt in items:
  ratio = price/wt
  items_with_ratio.append((ratio, name, price, wt))

items_with_ratio.sort(key=cmp)

bag = []
total_price = 0
cur_wt = 0

for ratio, name, price, wt in items_with_ratio:
  if cur_wt + wt <= capacity:
    # 1. ERROR FIXED: Bori ka wazan badao!
    cur_wt = cur_wt + wt 
    total_price = total_price + price
    bag.append(name)
  else:
    # 2. FRACTION LOGIC: Agar poora nahi aata, toh kaat lo!
    remaining_capacity = capacity - cur_wt
    
    # Bachi hui jagah ko uske "Price per kg (ratio)" se multiply kar do
    total_price = total_price + (ratio * remaining_capacity)
    
    bag.append(name + " (Half/Fraction)")
    
    # Bori ab theek 50kg full ho chuki hai, isliye loop tod do
    break 

print("Items in Bag:", bag)
print("Total Profit:", total_price)