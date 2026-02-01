"""
chart_builder.py
----------------
Interactive chart builder for user-uploaded CSV files.

Features:
- Lets user choose X and Y columns
- Automatically generates charts (bar, line, scatter)
- Saves charts to 'reports/' folder
- Calculates basic summary statistics
"""

import os
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------
# Folder setup
# -----------------------
DATA_DIR = "data"
REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)

# -----------------------
# Load CSV
# -----------------------
csv_path = input("Enter the path to your CSV file (e.g., data/user_data.csv): ").strip()
if not os.path.exists(csv_path):
    print("❌ File not found. Make sure the path is correct.")
    exit()

try:
    df = pd.read_csv(csv_path)
except Exception as e:
    print(f"❌ Error reading CSV: {e}")
    exit()

print("\n✅ CSV loaded successfully!")
print("Available columns:")
for i, col in enumerate(df.columns):
    print(f"{i + 1}. {col}")

# -----------------------
# User chooses X and Y columns
# -----------------------
x_col = input("\nEnter the column name for X-axis: ").strip()
if x_col not in df.columns:
    print("❌ Column not found.")
    exit()

y_col = input("Enter the column name for Y-axis: ").strip()
if y_col not in df.columns:
    print("❌ Column not found.")
    exit()

# -----------------------
# User chooses chart type
# -----------------------
print("\nChart types:")
print("1. Line")
print("2. Bar")
print("3. Scatter")
chart_choice = input("Choose chart type (1/2/3): ").strip()

chart_type = "line"
if chart_choice == "1":
    chart_type = "line"
elif chart_choice == "2":
    chart_type = "bar"
elif chart_choice == "3":
    chart_type = "scatter"
else:
    print("❌ Invalid choice. Defaulting to line chart.")

# -----------------------
# Generate chart
# -----------------------
plt.figure(figsize=(8, 5))
if chart_type == "line":
    plt.plot(df[x_col], df[y_col], marker='o')
elif chart_type == "bar":
    plt.bar(df[x_col], df[y_col])
elif chart_type == "scatter":
    plt.scatter(df[x_col], df[y_col])

plt.xlabel(x_col)
plt.ylabel(y_col)
plt.title(f"{chart_type.capitalize()} Chart: {y_col} vs {x_col}")
plt.xticks(rotation=45)
plt.tight_layout()

# Save chart
chart_file = os.path.join(REPORT_DIR, f"{y_col}_vs_{x_col}_{chart_type}.png")
plt.savefig(chart_file)
plt.close()
print(f"\n✅ Chart saved to {chart_file}")

# -----------------------
# Summary statistics
# -----------------------
summary = df[[y_col]].describe()
summary_file = os.path.join(REPORT_DIR, f"{y_col}_summary.csv")
summary.to_csv(summary_file)
print(f"✅ Summary statistics saved to {summary_file}")

print("\n🎉 All done! Check the 'reports/' folder for charts and summaries.")
