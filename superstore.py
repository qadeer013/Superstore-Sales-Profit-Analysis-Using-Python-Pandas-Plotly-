import pandas as pd
import plotly.express as px
import plotly.graph_objects as go 
import plotly.io as pio
import plotly.colors as color
pio.templates.default="plotly_white"
data = pd.read_csv(r"C:\Project  1\sample_-_superstore.csv")


print(data.head())
print(data.describe())
print (data.info())

#CONVERTING ORDER DATE and SHIP DATE "DATA TYPE"

data['Order Date'] = pd.to_datetime(data['Order Date'], dayfirst=True)
data['Ship Date'] = pd.to_datetime(data['Ship Date'], dayfirst=True)

print(data.info())

print(data.head())

#ADD NEW COLUMNS

data['Order Month'] = data['Order Date'].dt.month
data['Order Year'] = data['Order Date'].dt.year
data['Order of the Week']= data['Order Date'].dt.weekday
print(data.head())

#MONTHLY SALES ANALYSIS

sales_by_month= data.groupby('Order Month')['Sales'].sum().reset_index()
print(sales_by_month.head())

fig= px.line(sales_by_month,
             x= 'Order Month'
             ,y='Sales',
             title='Monthly Analysis')

print(fig.show())


#SALES BY CATEGORY

sales_by_category= data.groupby('Category')['Sales'].sum().reset_index()
print(sales_by_category)

fig=px.pie(sales_by_category,
           values='Sales',
           names='Category',
           hole= 0.2,
           color_discrete_sequence=px.colors.qualitative.Pastel)
fig.update_traces(textposition='inside',textinfo='percent+label')
fig.update_layout(title_text='Sales Analysis by Category',title_font=dict(size=24))
print(fig.show())


#SALES BY SUB-CATEGORY

sales_by_sub_category= data.groupby('Sub-Category')['Sales'].sum().reset_index()
print(sales_by_sub_category)

fig= px.bar(sales_by_sub_category,
            x= 'Sub-Category',
            y= 'Sales',
            title= "Sales Analysis by Sub-Category"
            )
print(fig.show())

#Monthly Profit

profit_by_month= data.groupby('Order Month')['Profit'].sum().reset_index()
print(profit_by_month)

fig=px.bar(profit_by_month,
           x='Order Month',
           y='Profit',
           title= 'Profit Analysis ')
print(fig.show())

#Profit by Category 
profit_by_category = data.groupby('Category')['Profit'].sum().reset_index()
print(profit_by_category)

fig= px.pie(profit_by_category,
            values= 'Profit',
            names= 'Category',
            hole=0.3,
            color_discrete_sequence=px.colors.qualitative.Pastel)
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(title_text='Profit Analysis By Category',title_font=dict(size=24))
print(fig.show())

#profit by subcategory
profit_by_subcategory = data.groupby('Sub-Category') ['Profit'].sum().reset_index()
fig= px.bar(profit_by_subcategory,
           x='Sub-Category',
           y='Profit',
           title='Profit Analysis by Sub-Category')
print(fig.show())


#sales and profit customer segment
sales_profit_by_segment= data.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
color_palette = color.qualitative. Pastel
fig= go. Figure()
fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'],
y=sales_profit_by_segment ['Sales'],
name='Sales',
marker_color=color_palette[0]))
fig.add_trace(go.Bar(x=sales_profit_by_segment['Segment'],
y=sales_profit_by_segment['Profit'], name='Profit',
marker_color=color_palette[1]))
fig.update_layout(title='Sales and Profit Analysis by Customer Segment',
xaxis_title='Customer Segment', yaxis_title='Amount')
print(fig.show())


#sales to profit ratio

sales_profit_by_segment =data.groupby('Segment').agg({'Sales': 'sum', 'Profit': 'sum'}).reset_index()
sales_profit_by_segment['Sales_to_Profit_Ratio'] = sales_profit_by_segment['Sales'] / sales_profit_by_segment['Profit']
print(sales_profit_by_segment [['Segment', 'Sales_to_Profit_Ratio']])
