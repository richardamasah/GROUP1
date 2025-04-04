
#Importing Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_parquet("/Users/hakeemwikireh/Desktop/DataEngineering/GroupAssignment/stockmarket/cleaned-stocks.parquet")

#Data Exploration
data.head()

data.isnull().sum()

data.duplicated().sum()

data.shape
print("Total rows: ", data.shape[0])
print("Total columns: ", data.shape[1])
