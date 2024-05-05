import pandas as pd

# Read the CSV files for controlled and traditional environments
df_controlled = pd.read_csv('data2.csv')
df_traditional = pd.read_csv('data4.csv')

# Calculate summary statistics for controlled environment
controlled_summary = df_controlled.describe()

# Calculate summary statistics for traditional environment
traditional_summary = df_traditional.describe()

# Save the summary statistics to an Excel file with two decimal places
with pd.ExcelWriter('comparison_summary.xlsx') as writer:
    controlled_summary.to_excel(writer, sheet_name='Controlled Environment', float_format="%.2f")
    traditional_summary.to_excel(writer, sheet_name='Traditional Environment', float_format="%.2f")

print("Summary saved as 'comparison_summary.xlsx'")
