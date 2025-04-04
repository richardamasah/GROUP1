import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#define a class 
class DataCleaning_and_EDA_pipeline:
    def __init__(self,file_path):
        self.df= pd.read_parquet(file_path) 
        
    def view_data(self):
        self.df.head()
        self.df.info()
    
    def clean_data(self):
        self.df.drop_duplicates(inplace=True)
        self.df.dropna(inplace=True)
        return self.df
    
    def check_missing_values(self):
        print("Missing values:", self.df.isnull().sum())
        
        
    def handle_missing_values(self):   
        self.df.fillna(self.df.median(numeric_only=True), inplace=True)
        
        
    def data_description(self):
        print("Description of Dataset:", self.df.describe())
        
    def standardize_columns(self):
        self.df.columns = [col.lower().replace(' ', '_') for col in df.columns]
        return self.df
    
    def date_timeconv(self):
           self.df['date'] = pd.to_datetime(self.df['date'])
           return self.df

    def data_visualization(self):
            num_cols = self.df.select_dtypes(include=['number']).columns  # Select numerical columns
            for col in num_cols:
                plt.figure(figsize=(10, 4))
                
                # Box Plot
                plt.subplot(1, 2, 2)
                sns.boxplot(x=self.df[col])
                plt.title(f'Boxplot of {col}')
                plt.show()
                
    def hist_visulaization(self):
        
        num_cols = self.df.select_dtypes(include=['number']).columns  # Select numerical columns
        for col in num_cols:
                plt.figure(figsize=(10, 4))

                # Histogram
                plt.subplot(1, 2, 1)
                sns.histplot(self.df[col], bins=30, kde=True)
                plt.title(f'Distribution of {col}')
        plt.show()
        


file_path = "../data/cleaned-stocks.parquet"  
Pline = DataCleaning_and_EDA_pipeline(file_path)
# Pline.view_data()
# Pline.check_missing_values()
# Pline.handle_missing_values()
# Pline.data_description()
# Pline.date_timeconv()
# Pline.data_visualization()


df_cleaned = Pline.df 


def moving_average(df, column='close', window=200):
     return df[column].rolling(window=window).mean()
 

df_cleaned_MA = moving_average(df_cleaned, column='close', window=200)
print("The Moving Averages are below\n", df_cleaned_MA)
