import pandas
df = pandas.read_csv('screenings', delimiter='/', lineterminator=',', skipinitialspace=True)
df = df.replace('\n', '', regex=True)
df = df.replace('\r', '', regex=True)
print(df)
