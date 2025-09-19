#You have two lists: names = ["Alice", "Bob", "Charlie"] and scores = [85, 92, 78]. Print these lists as a simple table with columns “Name” and “Score”.


names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

print(f"{'Name':<10} {'Score':<5}")
print("-"*20)

for name, score in zip(names, scores):
    print(f"{name:<10} {score:<5}")

