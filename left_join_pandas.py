import pandas as pd 

pc = pd.read_csv(r"<path to main file>")
hm = pd.read_csv(r"<path to file we want to join>")

join = pd.merge(left=pc,right=hm,how='left', indicator=True, left_on='person_identifier', right_on='person_identifier')

join.head()

join.to_csv(r"<path to destination>")
