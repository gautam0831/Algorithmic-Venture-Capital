import pandas as pd
import numpy as np

funding_rounds = pd.read_csv("bulk_export_sample/funding_rounds.csv")
print(funding_rounds.shape)
#print(funding_rounds.head())

filter_onlyUSA = funding_rounds[funding_rounds['country_code'] == "USA"]
print(filter_onlyUSA.shape)
print(filter_onlyUSA.info())
print(filter_onlyUSA.head())
