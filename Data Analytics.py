import numpy as np
from numpy import pi
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
#style.use('ggplot')


data = pd.read_csv("countrystats.csv")
df = pd.DataFrame(data)



#print(df.to_string())
#print(pd.options.display.max_rows)
#print(df.head())
#print(df.shape)
#print(df.columns)
#print(df.dtypes)
#print(df.info())
#country_df = df['country']
#print(country_df.head())
#print(country_df.tail())
subset = df[['country','goals_scored']]
print(subset.head())
#print(subset.tail())
#print(subset.head())
#Pandas-Data Cleaning Cells
"""Data cleaning means to remove unwanted, incorrect, duplicates, empty cells in a  data set"""
#Empty cells can potentially give you a wrong result when you're analyzing a data
#Ways to fix this is for you to filter the dataset to remove the empty rows by:
#new_df = df.dropna(),,,,then print(new_df.to_string())
"""Default this dropna() method only return a new
# dataframe and wont affect the initial or original dataframe but if you want to change the original
dataframe use df.dropna(inplace = True)..
 df.dropna(inplace = True) == will not rewrite a new dataframe,but will remove all rows containing NULL values from
 the original Dataframe
"""
#Replacing NULL values: Just in case you dont really want to excommunicate the row from the rest data you
#can repalce the particular NULL value with your desired "string" or "int", or "FLOAt"
#df.fillna(15, inplace= True)
#You can specify the columns you want to replace the NULL values
#df["name of column"].fillna(132, inplace = True)
"""You can as well replace the NULL values by 
calculating the mean of columns if it contains floats or integers"""
#x = df["Total"].sum()
#x = df["Price"].mean()
#x = df["Total"].sum()
#x = df["Size"].mode()
#print(x)
"""One way to fix a wrong data is by replacing them with a value: this might be caused from typo error """
"""#So you can fix it by writing the code like this ###df.loc[row_num, "colomn variable"] = 'string','int','float'### objects
If you have a small data set you can fix them one by one but 
if you have a large dataset its adviseable you loop through all the values in the specified column"""
#for x in df.index:
#    if df.loc[x,'particular column'] > sososo:
#        df.loc[x,"particular column"] = desired_value
#or you can just remove the row
#for x in df.index:
#    if df.loc[x,'particular column'] > sososo:
#        df.drop[x, inplace = True]
#Removing Duplicate Values
#There may be some rows that are appearing twice in the dataset they are called duplicate values
"""To expose any duplicate value in your data set you can use the duplicate method"""
#print(df.duplicated())
#Remove duplicate values by using
#df.drop_duplicates(inplace = True)+++The inplace = True  will make sure that the method does not return a new DataFrame


#plotting Pandas as a graph
#pandas uses .plot() method to create figures
#style.use('ggplot')
#style.use('fivethirtyeight')
style.use('dark_background')
#style.use('classic')
#style.use('Solarize_Light2')
#style.use('bmh')
#style.use('tableau-colorblind10')
#gender_counts = df["Gender"].value_counts()
bg_img = "tinazze_ig.png"
pic = plt.imread(bg_img)


#ax.bar(name_of_players,goals_scored,color=bar_color)
#plt.imshow(pic, extent=[0.8,5,3,8],aspect='auto')
#plt.set_yticklabels([])
#description_counts= df["Description"].value_counts()
#plt.barh(description_counts.index,description_counts.values, color='g')
#plt.xlabel("Description")
#plt.xticks(rotation=90)
#plt.figure(figsize=(15,10))
#plt.ylabel("Count")
#plt.grid(False)
#plt.subplots_adjust(bottom=0.2)

#df["Gender"].plot(kind = 'bar',color='teal',rwidth=0.9)
#plt.pie(gender_counts.values,labels=gender_counts.index,autopct='%1.1f%%',colors="gender_counts.index")
#plt.title("Gender distribution".title())
#plt.show()

#print(new_df.to_string)
#Subset Rows by index Label:loc command
#print(df.loc[0])
#print(df.loc[15])
#gettin the last row
#print(df.tail(n=1))
#print(df.loc[[0, 15, 20]])
#Using the iloc Command
#print(df.iloc[1])
#print(df.iloc[99])
#print(df.iloc[-1])
#Subsetting Columns
#subset = df.loc[:, ['Size','Quantity']]
#print(subset.head())
#Using the iloc command for columns
#Define the iloc subset of the data first
#subset = df.iloc[:, [2,4,-1]]
# Asscesing the columns
#print(subset.head())
#You can subset column using "range" command
#Create a range of integers from 0-4
"""small_range = list(range(5))
print(small_range)
subset = df.iloc[:,small_range]
print(subset.head())"""

#SUBSETTING ROWS AND COLUMNS SIMULTENEOUSLY
#Using location--loc command
#print(df.loc[42, 'country'])
#Using the iloc command
#print(df.iloc[42, 0])


#NUMPY LECTURE
#A = np.array([['1', '2', '3'],
#              ['5', '6', '7'],
#              ['7', '8', '9' ]])

#print(A[:,:2])
#print(A[:2,:2])
#A[1] = np.array(['10','12','14'])
#A[2] = '99'
#print(A)
#Numpy Statistics
#a = np.array([1, 2, 3, 4])
#print(a.sum())
#print(a.mean())
#print(a.std())
#print(a.var())
         #axis[0  0  0]
#A = np.array([[1, 2, 3],#axis1
#              [4, 5, 6],#axis1
#              [7, 8, 9]])#axis1
#print(A.sum())
#print(A.mean())
#print(A.std())
#print(A.var())
#print(A.sum(axis=0))
#print(A.sum(axis=1))
#print(A.sum(axis=2))
#print(A.mean(axis=0))
#print(A.mean(axis=1))
#print(A.std(axis=0))

#BROADCASTING AND VECTORIZED OPERATIONS
#x = np.arange(5)
#print(x + 20) #Broadcasting to each individual element in the x array
#print(x - 100)
#print(x - 10)
#y = [0,1,2,3]
#y = np.arange(4)
#print([i + 10 for i in y])
#z = np.array([10,10,10,10])
#print(y)
#print(z)
#print(y + z)

#BOOLEAN ARRAYS (ALSO CALLED MASKS)
"""m = np.arange(4)
print(m)
#print(m[[0, -1]])
print(m >= 2)
print(m[m>=2])
print(m.mean())
print(m[m > m.mean()])
print(m[~(m > m.mean())])
print(m[(m == 0) | (m == 1) ])
print(m[(m <= 2) & (m % 2 == 0)])

X = np.random.randint(100, size=(3, 3))
print(X)"""

#a = np.ones(3, dtype=np.int32)
#b = np.linspace(0, pi, 3)
#print(b)
