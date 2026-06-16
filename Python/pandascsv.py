import pandas as pd

data = {
    "name": ["Ashwin", "Rahul", "Priya", "Karan", "Sneha", "Amit", "Diya"],
    "age": [19, 20, None, 21, 19, None, 22],
    "score": [85, 72, 91, None, 78, 65, None],
    "city": ["Chennai", "Mumbai", "Delhi", "Chennai", "Mumbai", None, "Delhi"]
}

df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)
print("CSV created")

import pandas as pd

df = pd.read_csv("students.csv")
print(df)
print(df.info())
print(df.isnull().sum())

print("problem 1")

print(df.isnull().sum())
df["age"] = df["age"].fillna(df["age"].mean())
df["score"] = df["score"].fillna(df["score"].median())
df["city"] = df["city"].fillna("unknown")
print(df)

print("problem 2")
df["grade"] = df["score"].apply(lambda x: "A" if x >= 90 else ("B" if x >= 75 else ("C")))
print(df)
print(df["grade"].value_counts())

print("problem 3")
print(df.groupby("city")["score"].mean())
print(df.groupby("city")["name"].count())
print(df[(df["city"] == "Chennai") | (df["city"] == "Delhi")])

data2 = {
    "name": ["Ashwin", "Rahul", "Priya", "Karan", "Sneha"],
    "club": ["Basketball", "Chess", "Dance", "Football", "Basketball"]
}

df2 = pd.DataFrame(data2)

print("problem 4")
merged_df = pd.merge(df, df2, on="name", how="left")
print(merged_df)
print(merged_df[merged_df["club"] == "Basketball"])