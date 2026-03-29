import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Mohan"],
    "Age": [20, 21, 22],
    "City": ["Jabalpur", "Bhopal", "Indore"]
}

df = pd.DataFrame(data)

print(df)