# Converting a Nested Dictionary to a Pandas DataFrame

import pandas as pd

nested_dict = {
    '1': {'name': 'Alice', 'salary': 1500},
    '2': {'name': 'Bobby', 'salary': 1200},
}

df = pd.DataFrame.from_dict(nested_dict, orient='index')

#     name  salary
# 1  Alice    1500
# 2  Bobby    1200
print(df)