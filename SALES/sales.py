import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = '/Users/dv/Downloads/DATA.xlsx'
ecom_data = pd.read_excel(file_path)


ecom_data['Order Date'] = pd.to_datetime(ecom_data['Order Date'])


total_sales = ecom_data['Sales'].sum()


ecom_data['Year'] = ecom_data['Order Date'].dt.year
ecom_data['Month'] = ecom_data['Order Date'].dt.to_period('M').astype(str)


sales_trend = ecom_data.groupby(['Year', 'Month']).agg({'Sales': 'sum'}).reset_index()


top_products_sales = ecom_data.groupby('Product Name').agg({'Sales': 'sum', 'Quantity': 'sum'}).sort_values(by='Sales', ascending=False).reset_index()


top_products_quantity = top_products_sales.sort_values(by='Quantity', ascending=False).reset_index(drop=True)


sns.set(style='whitegrid')


plt.figure(figsize=(14, 7))
sns.lineplot(data=sales_trend, x='Month', y='Sales', hue='Year', palette='tab10')
plt.title('Sales Trends Over Time')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.legend(title='Year')
plt.tight_layout()
plt.show()


plt.figure(figsize=(14, 7))
sns.barplot(data=top_products_sales.head(10), x='Sales', y='Product Name', hue='Product Name', dodge=False, palette='viridis', legend=False)
plt.title('Top 10 Best-Selling Products by Total Sales')
plt.xlabel('Total Sales')
plt.ylabel('Product Name')
plt.tight_layout()
plt.show()


plt.figure(figsize=(14, 7))
sns.barplot(data=top_products_quantity.head(10), x='Quantity', y='Product Name', hue='Product Name', dodge=False, palette='magma', legend=False)
plt.title('Top 10 Best-Selling Products by Quantity Sold')
plt.xlabel('Quantity Sold')
plt.ylabel('Product Name')
plt.tight_layout()
plt.show()

print(f"Total Sales Revenue: ${total_sales:,.2f}")
print("\nTop 5 Best-Selling Products by Sales:")
print(top_products_sales.head())
print("\nTop 5 Best-Selling Products by Quantity:")
print(top_products_quantity.head())
