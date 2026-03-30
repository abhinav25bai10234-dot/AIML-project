import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_clean_report_chart():
    try:
        df = pd.read_csv('data.csv')
        df.columns = [c.strip().lower() for c in df.columns]
        
        # 1. Clean the RAM column to make it sortable (remove 'GB' if it's there)
        # This ensures 4GB comes before 16GB
        df['ram_numeric'] = df['ram'].astype(str).str.extract('(\d+)').astype(float)
        df = df.sort_values('ram_numeric')

        plt.figure(figsize=(12, 7))
        sns.set_style("whitegrid")

        # 2. Use 'showfliers=False' to hide those messy AI-looking dots
        # 3. Use a consistent color palette
        sns.boxplot(x='ram', y='price', data=df, palette="Blues", showfliers=False)

        plt.title('Average Laptop Price Trend by RAM Capacity', fontsize=16, pad=20)
        plt.xlabel('RAM Size', fontsize=12)
        plt.ylabel('Price (Market Value)', fontsize=12)
        
        plt.tight_layout()
        plt.savefig('price_analysis_clean.png')
        print("Done! Check 'price_analysis_clean.png' for a much cleaner version.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_clean_report_chart()