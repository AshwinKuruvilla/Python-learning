import pandas as pd
print(pd.__version__)

students = {"name": ["ashwin", "rahul", "priya", "karan", "sneha"],
            "age": [19, 20, 18, 21, 19],
            "score": [85,72,91,68,78]}
df = pd.DataFrame(students)
print(df)
print(df["score"])
print(df[0:3])
print(df.shape)

print("problem 2")

print(df[df["score"] > 75])
print(df[["name", "score"]])
print(df.iloc[2])

print("problem 3")
df["passed"] = df["score"] > 75
print(df)
print(df[df["passed"] == True])


print("problem 4")

print(df["score"].mean())
print(df["score"].idxmax())
print(df.groupby("age")["score"].mean())

print("problem 5")

data = {"product": ["laptop", "phone", "shirt", "pants", "headphones"],
        "category": ["electronics", "electronics", "clothing", "clothing", "electronics"],
        "price": [800, 500, 40, 60, 150],
        "quantity": [5, 10, 50, 30, 20]}
df_products = pd.DataFrame(data)
print(df_products[df_products["category"] == "electronics"])
df_products["total_value"] = df_products["price"] * df_products["quantity"]
print(df_products)
print(df_products.groupby("category")["price"].mean())
print(df_products.loc[df_products["total_value"].idxmax(), "product"])