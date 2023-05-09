import pandas as pd
df = pd.DataFrame(data={'a':[2,3], 'b':[10,15]})
print(df)
with open('data.txt') as reader:
    print(reader.read())