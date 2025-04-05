
#Data Exploration

def structure(df):
    print("First 5 rows")
    print(df.head())

    print("Checking for null values")
    print(df.isnull().sum())

    print("checking for duplicates")
    print(df.duplicated().sum())

    print("Shape of data")
    print(df.shape)

    print("Total rows: ", df.shape[0])
    print("Total columns: ", df.shape[1])

