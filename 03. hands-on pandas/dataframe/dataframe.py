import pandas as pd
from palmerpenguins import load_penguins

#df = pd.read_csv('https://www.kaggle.com/parulpandey/penguin-dataset-the-new-iris/input/palmer-archipelago-antarctica-penguin-data/penguins_size.csv')

#pip install palmerpenguins
penguins = load_penguins()
#print(penguins.head())
df = pd.DataFrame(penguins)

#print(df['species'])
#print(df[['species', 'island', 'sex']])
#print(df[5:50])
#print(df[6:])
#print(df.loc[5:50,'sex'])
#print(df.loc[5:50,['species', 'island', 'sex']])
#print(df.iloc[5:50,[1,2,4]])
#print(df.iloc[5:50,1:4])
#print(df[df["year"] > 2007])
#print(df["year"]>2007)


#print(df.head())
#print(df.head(len(df)))
#print(df[5:50].head())
#print(df[['species', 'island', 'sex']].head())
#print(df.tail(3))
#print(df.shape)
#print(df.size)
#print(df.values)
#print(df.info())
#print(df.describe())
#print(df.describe(include='all'))
#print(df.dtypes)
#print(df.dtypes.value_counts())
#print(df.dtypes == 'object')
#print(df.ndim)
#print(df.empty)
#print(df.axes)
#print(df.index)
#print(df.columns)
#print(df.to_numpy())
#print(df.T)
#print(df.sort_index(axis=1, ascending=False))
#print(df.cov())
#print(df.corr())



num_var = df.columns[df.dtypes != 'object']
cat_var = df.columns[df.dtypes == 'object']
#print(num_var)
#print(cat_var)
#print(df[num_var])
#print(df[num_var].isnull())
#print(df[num_var].isnull().sum())
#print(df[num_var].isnull().sum().sort_values(ascending=False))
#print(df[num_var].isnull().sum().sort_values(ascending=False)/len(df))



null_data = df[df.isnull().any(axis=1)]
#print(null_data)
#print(sum(df.isnull().values.any(axis=1)))



def missing_values_table(df):
        # Total missing values
        mis_val = df.isnull().sum()
        
        # Percentage of missing values
        mis_val_percent = 100 * df.isnull().sum() / len(df)
        
        # Make a table with the results
        mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
        
        # Rename the columns
        mis_val_table_ren_columns = mis_val_table.rename(
        columns = {0 : 'Missing Values', 1 : '% of Total Values'})
        
        # Sort the table by percentage of missing descending
        mis_val_table_ren_columns = mis_val_table_ren_columns[
            mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
        '% of Total Values', ascending=False).round(1)
        
        # Print some summary information
        print ("Your selected dataframe has " + str(df.shape[1]) + " columns.\n"      
            "There are " + str(mis_val_table_ren_columns.shape[0]) +
              " columns that have missing values.")
        
        # Return the dataframe with missing information
        return mis_val_table_ren_columns
#print(missing_values_table(df))


''''
data = df.dropna()
print(data.head())

data = df.fillna(0)

df['culmen_length_mm'].fillna((df['culmen_length_mm'].mean()), inplace=True)
df['culmen_depth_mm'].fillna((df['culmen_depth_mm'].mean()), inplace=True)
df['flipper_length_mm'].fillna((df['flipper_length_mm'].mean()), inplace=True)
df['body_mass_g'].fillna((df['body_mass_g'].mean()), inplace=True)

df['sex'].fillna((df['sex'].value_counts().index[0]), inplace=True)

df.reset_index()
df.head()


df.loc[(data['sex'] != 'FEMALE') & (data['sex'] != 'MALE')]
data = df.drop([336])
data.reset_index()
'''