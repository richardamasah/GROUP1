#import dependencies and packages
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
def load_stock_data(path):
    return pd.read_csv(path)