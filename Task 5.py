import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("cleaned.csv")
sns.set(style="whitegrid")

def plot_factor_vs_severity(column_name, title):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=column_name, hue='Accident_severity', palette='viridis')
    plt.title(f'Accident Severity vs {title}')
    plt.xticks(rotation=45)
    plt.xlabel(title)
    plt.ylabel('Number of Accidents')
    plt.legend(title='Severity (1=Low, 2=Medium, 3=High)')
    plt.tight_layout()
    plt.show()

plot_factor_vs_severity('Weather_conditions', 'Weather Conditions')
plot_factor_vs_severity('Road_surface_type', 'Road Surface Type')
plot_factor_vs_severity('Light_conditions', 'Light Conditions')
plot_factor_vs_severity('Cause_of_accident', 'Cause of Accident')
