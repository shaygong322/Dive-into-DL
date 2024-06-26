This is my notes studying [Matplotlib-NumPy-Pandas](https://www.bilibili.com/video/BV1wN4y1T7K9/?share_source=copy_web) on Bilibili.  

# Matplotlib
mainly use the pyplot submodule
## 1 PyPlot
use .plot() function
### 1.1 Draw a line
### 1.2 Draw without line
### 1.3 Multiple turning points
### 1.4 Default x points
## 2 Markers
### 2.1 Keyword argument marker
.plot(marker='*')
### 2.2 Marker Size Color Reference
### 2.3 Formatted string fmt
marker|line|color: plt.plot(..., 'o:r')
### 2.4 Marker size
plt.plot(..., marker='o', ms=20)
### 2.5 Marker color
mec # markeredgecolor
mfc # markerfacecolor
## 3 Lines
### 3.1 Line Style
plt.plot(..., linestyle='dotted')
### 3.2 Shorter Syntax
linestyle --> ls
dotted --> :
dashed --> --
### 3.3 Line Reference
### 3.4 Line color
keyword argument color/c: plt.plot(..., color='r')  
use hexadecimal color values: plt.plot(..., c='#4CAF50')  
named colors: plt.plot(..., c='hotpink')
### 3.5 Line Width
keyword argument linewidth: plt.plot(..., linewidth='20.5')
### 3.6 Multiple Lines
simply calling the plt.plot() function multiple times  
or plt.plot(x1, y1, x2, y2)
## 4 Labels and Titles
### 4.1 Create Labels for the Plots
plt.xlabel("Average Pulse")  
plt.ylabel("Calorie Burnage")
### 4.2 Create Titles for the Plots
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
### 4.3 Set Font Properties for Titles and Labels
fontdict in the xlabel(), ylabel(), and title()
font = {'family': 'serif', 'color': 'blue', 'size': 20}
plt.title(..., fontdict=font) plt.xlabel/ylabel(..., fontdict=font)
### 4.4 Title Positions
loc in the title() function  
Valid values are: 'left', 'right', and 'center'. The default is 'center'.
## 5 Grid
### 5.1 Add Grid Lines to the Plot
plt.grid()
### 5.2 Specify Grid Lines to Display
plt.grid(axis='x')  
Valid values are: 'x', 'y', and 'both'. The default is 'both'.
### 5.3 Set Grid Line Properties
plt.grid(color='green', linestyle='--', linewidth=1.5)
## 6 Multiple Plots
Using the subplots() function: subplots(rows, columns, and the index)  
Using the title() function to add titles to each plot, use the suptitle() function to add a title to the entire figure.
## 7 Scatter Plot
### 7.1 Creating a Scatter Plot
plt.scatter(x, y)
### 7.2 Color
plt.scatter(x, y, color='#88c999')
### 7.3 Coloring Each Point
colors = np.array(['orange', 'purple', 'beige', 'brown', 'gray'])  
plt.scatter(x, y, c=colors) # can only use c
### 7.4 Color Maps
```python
x = np.array([5, 7, 8, 7])
y = np.array([99, 86, 87, 88])
colors = np.array([0, 10, 20, 30])

plt.scatter(x, y, c=colors, cmap='viridis')
plt.colorbar()
```
### 7.4 Sizes
s
### 7.5 Transparency
alpha
## 8 Bar Charts
### 8.1 Creating Bar Charts
.bar(ndarray, ndarray)
### 8.2 Horizontal Bar Chart
.barh(ndarray, ndarray)
### 8.3 Bar Chart Colors
### 8.4 Bar Width (.bar())
### 8.5 Bar Height (.barh())
## 9. Histogram
```python
x = np.random.normal(170, 10, 250) # 250 values, with the mean centered around 170 and a standard deviation of 10
plt.hist(x)
```
## 10. Pie Chart
### 10.1 Creating a Pie Chart
.pie(ndarray)
### 10.2 Labels
.plt.pie(ndarray, labels=list)
### 10.3 Starting Angle
.pie(startangle=90)
### 10.4 Explode
plt.pie(explode=List)
### 10.5 Shadow
plt.pie(shadow=True)
### 10.6 Colors
plt.pie(colors=List)
### 10.7 Legend
plt.legend()
#### Legend with title
plt.legend(title="Four Fruits")
## 11 Width & Height & savefig

# NumPy
## 1 ndarray
### 1.1 create an ndarray object
### 1.2 array dimension
attribute: .ndim
### 1.3 array index
### 1.4 array slice
## 2 Data Types
### 2.1 Check
attribute: .dtype
### 2.2 Converting
arr = np.array(['1', '2', '3'], dtype='i')  
or  
arr = np.array([1.1, 2.1, 3.1])  
newarr = arr.astype('i')
## 3 Copy vs View
according to attribute: .base
## 4 Shape
attribute: .shape  
function: .reshape() --> return a view
## 5 Operation
### 5.1 Iteration
for loop  
nditer()  
ndenumerate()
### 5.2 Concatenation
### 5.3 Splitting
array_split()  
split() # have to be equal division  
hsplit()
### 5.4 Array Search
.where()  
.searchsorted() and multiple values
### 5.5 Array Sorting
### 5.6 Array Filtering
filter  
create filter array  
directly create filters from arrays

# Pandas
## 1 Object Creation
pd.Series([])  
pd.DataFrame({})  
pd.data_range('20130101', periods)  
pd.DataFrame(data, index=, columns=list('ABCD'))
## 2 Viewing Data
df.dtypes  
df.head()  
df.tail()  
df.index  
df.columns  
df.describe()
## 3 Sorting
df.sort_index(axis=1, ascending=False) # column name  
df.sort_values(by='B')
## 4 Selecting Data
df['A']  
df[1:3]  
df['2013-01-02':'2013-01-04']
### 4.1 Selecting by Label
.loc[]  
.at[] # getting a scalar value
### 4.2 Selecting by Position
.iloc[]  
.iat[]
### 4.3 Boolean Indexing
df[df['B'] > 0]  
df[df > 0]  
.isin()
## 5 Setting Values
df['F'] = s1  
df.at['2013-01-01', 'A'] = 0  
df.iat[0, 2] = 0  
df.loc[:, 'D'] = np.array([5] * len(df))  
df3[df3 < 0] = 0
## 6 Handling Missing Data
reindexing and .dropna(): how='any'/'all'  
.fillna(value=5)  
.isna(df)
## 7 Operations
### 7.1 Arithmetic
### 7.2 Comparison
### 7.3 Statistical
.mean()  
.cumsum()  
### 7.4 .concat([df1, df2])
### 7.5 .merge(left, right, on='key')
### 7.6 Append (has been deprecated)
### 7.7 Group
df.groupby('A').sum()  
df.groupby(['A', 'B']).sum()
## 8 Pivot Table
pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
## 9 Time Series
ts.resample('5Min').sum()  
ts.tz_localize('UTC')  
ts.to_period()  
## 10 Visualization
df.plot()  
plt.figure() + df.plot() + plt.legend(loc='best')
## 11 Data Input/Output
### 11.1 CSV
df.to_csv('foo.csv') + pd.read_csv('foo.csv')
### 11.2 HDFS
### 11.3 Excel