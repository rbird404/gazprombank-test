import pandas as pd

file_path = 'f.csv'

data = pd.read_csv(file_path, sep='|', dtype=str)

unique_rows = data.drop_duplicates()

print("Уникальные записи:")
print(unique_rows)

duplicate_ids = data[data.duplicated('id', keep=False)].sort_values(by='id')

print("Записи с одинаковым ID, но разными данными:")
print(duplicate_ids)
