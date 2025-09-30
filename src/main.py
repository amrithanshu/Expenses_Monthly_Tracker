import pandas as pd
import matplotlib.pyplot as plt
import os
from glob import glob

os.makedirs('../results', exist_ok=True)

csv_files = glob('data/month_expenses.csv')
if not csv_files:
    print("No CSV files found in data/ folder!")
    exit()
latest_csv = max(csv_files, key=os.path.getctime)
df = pd.read_csv(latest_csv)

summary_by_category = df.groupby('Category')['Amount'].sum()
summary_by_day = df.groupby('Date')['Amount'].sum()
total_spent = df['Amount'].sum()
top_category = summary_by_category.idxmax()
highest_day = summary_by_day.idxmax()

print(f"Total Spent: ${total_spent:.2f}")
print(f"Top Spending Category: {top_category} (${summary_by_category[top_category]:.2f})")
print(f"Highest Spending Day: {highest_day} (${summary_by_day[highest_day]:.2f})\n")

for date, amt in summary_by_day.items():
    if amt > 50:
        print(f"⚠ Warning: High spending on {date} (${amt:.2f})")

summary_by_category.to_csv('/results/summary_by_category.csv')
summary_by_day.to_csv('/results/summary_by_day.csv')

plt.figure(figsize=(6,4))
summary_by_category.plot(kind='bar', title='Expenses by Category')
plt.ylabel('Amount ($)')
plt.tight_layout()
plt.savefig('/results/expense_summary.png')
plt.show()

plt.figure(figsize=(5,5))
summary_by_category.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Spending Distribution by Category')
plt.ylabel('')
plt.tight_layout()
plt.savefig('/results/expense_pie.png')
plt.show()
