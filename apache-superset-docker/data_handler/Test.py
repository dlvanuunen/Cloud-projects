import pandas as pd

print("hello world")


a = {"Column1": [1, 2, 3], "Column2": ["a", "b", "c"]}

df = pd.DataFrame(a)
print(df.head())

df.to_excel("Test.xlsx")
