import pandas as pd

data = [
    {"name":"manish", "age":29,"city":"sikar"},
    {"name":"krish", "age":35,"city":"bangaluru"},
    {"name":"sunny", "age":27,"city":"bhopal"},
    {"name":"sudh", "age":37,"city":"delhi"}
]

df=pd.DataFrame(data)
df.to_csv("data/data.csv", index=False)