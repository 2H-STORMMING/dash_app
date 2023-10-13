import pandas as pd
from IPython.display import display

df_0 = pd.read_csv(r'C:\Users\pc\Desktop\projects\python\candy_app\candy\quantium-starter-repo\data\daily_sales_data_0.csv', delimiter=',')
df_1 = pd.read_csv(r'C:\Users\pc\Desktop\projects\python\candy_app\candy\quantium-starter-repo\data\daily_sales_data_1.csv', delimiter=',')
df_2 = pd.read_csv(r'C:\Users\pc\Desktop\projects\python\candy_app\candy\quantium-starter-repo\data\daily_sales_data_2.csv', delimiter=',')

df = pd.concat([df_0, df_1, df_2],ignore_index=True)

# Remove dollar sign and convert 'price' column to float
df['price'] = df['price'].str.replace('$', '').astype(float)


df_filtered = df[df['product'] == 'pink morsel']


df_filtered['sales'] = df_filtered['price'] * df_filtered['quantity']
df_filtered.drop(['price'], axis = 1, inplace = True) 


display(df_filtered)


df_filtered.to_csv('pink_morsel.csv')

# Displaying the DataFrame
display(df_filtered)
