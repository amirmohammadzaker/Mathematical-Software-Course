import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set style for professional-looking plots
sns.set_theme(style="whitegrid")

# =============================================================================
# PART 2 (a): Reading the Excel file dynamically
# =============================================================================
# Replace 'پروژه 3.xlsx' with the exact name/path of your Excel file if needed
excel_file = 'پروژه 3.xlsx'

try:
    # Read excel file dynamically
    df = pd.read_excel(excel_file)
except FileNotFoundError:
    # Fallback/Demo data in case the file is not in the same directory during execution
    print(f"Warning: '{excel_file}' not found. Creating the dataset from the provided structure.")
    data = {
        'Run time for different data size': ['100KB', '200KB', '300KB', '400KB', '500KB', '600KB'],
        'Alg.1': [50, 55, 60, 65, 70, 75],
        'Alg.2': [200, 220, 240, 260, 280, 300],
        'Alg.3': [100, 200, 300, 400, 500, 600]
    }
    df = pd.DataFrame(data)

# Clean column names just in case there are leading/trailing spaces
df.columns = df.columns.str.strip()

# =============================================================================
# PART 2 (c): Calculating the mean for Alg.2 (Before adding the new data row)
# =============================================================================
# Calculate mean execution time for Alg.2 for sizes 100KB to 600KB
mean_alg2 = df['Alg.2'].mean()
print("--- Part 2 (c): Statistical Analysis ---")
print(f"Mean execution time for Alg.2 (100KB to 600KB): {mean_alg2:.2f}\n")

# =============================================================================
# PART 2 (b): Dynamically appending new data row (700KB row)
# =============================================================================
new_row = {
    'Run time for different data size': '700KB',
    'Alg.1': 80,
    'Alg.2': 320,
    'Alg.3': 700
}
# Append the new row dynamically using pandas.DataFrame.loc or pd.concat
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print("--- Part 2 (b): Updated Dataframe with 700KB Row ---")
print(df)
print("\n")

# Extract sizes for X-axis labels and algorithms data for plotting
size_col = df.columns[0] # Dynamically get the first column name
algorithms = [col for col in df.columns if col != size_col]

# =============================================================================
# PART 2 (a): Plotting Bar, Line, and Box Plots
# =============================================================================

# 1. LINE PLOT: Excellent for showing execution time trends as data size grows
plt.figure(figsize=(10, 6))
for alg in algorithms:
    plt.plot(df[size_col], df[alg], marker='o', linewidth=2, label=alg)

plt.title('Execution Time Trend across Different Data Sizes', fontsize=14, fontweight='bold')
plt.xlabel('Data Size', fontsize=12)
plt.ylabel('Execution Time (ms)', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('execution_time_line_plot.png', dpi=300)
plt.show()

# 2. BAR PLOT: Ideal for comparing specific values at each data size level
# Reshape dataframe to long-format for easier plotting with seaborn
df_long = pd.melt(df, id_vars=[size_col], value_vars=algorithms, 
                  var_name='Algorithm', value_name='Execution Time')

plt.figure(figsize=(10, 6))
sns.barplot(data=df_long, x=size_col, y='Execution Time', hue='Algorithm', palette='muted')
plt.title('Comparison of Algorithm Execution Times per Data Size', fontsize=14, fontweight='bold')
plt.xlabel('Data Size', fontsize=12)
plt.ylabel('Execution Time (ms)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('execution_time_bar_plot.png', dpi=300)
plt.show()

# 3. BOX PLOT: Perfect for analyzing the overall distribution and spread of each algorithm
plt.figure(figsize=(8, 6))
sns.boxplot(data=df[algorithms], palette='pastel')
plt.title('Distribution of Execution Times per Algorithm (Spread Analysis)', fontsize=14, fontweight='bold')
plt.xlabel('Algorithm', fontsize=12)
plt.ylabel('Execution Time Range', fontsize=12)
plt.tight_layout()
plt.savefig('execution_time_box_plot.png', dpi=300)
plt.show()

print("All plots generated and saved successfully!")