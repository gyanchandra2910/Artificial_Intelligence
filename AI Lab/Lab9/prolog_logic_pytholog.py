import pytholog as pl

my_kv = pl.KnowledgeBase("Facts")

my_kv([
    "likes(shyam, mango)",
    "girl(seema)",
    "red(rose)",
    "likes(bill, cindy)",
    "owns(john,gold)"
])
    
goal = pl.Expr("likes(shyam, What)")

res = my_kv.query(goal)

print(res)
