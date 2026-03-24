import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data/final_triage_report.csv')

priority_counts = df['Priority'].value_counts()

plt.figure(figsize=(8, 6))
    
plt.bar(priority_counts.index, priority_counts.values, color=['skyblue', 'red'])

plt.title('SOC Triage: Incident Priority Levels')
plt.xlabel('Priority Level')
plt.ylabel('Number of Incidents')
plt.savefig('data/priority_chart.png')
print("Success: Chart saved to data/priority_chart.png")
plt.show()

# per location severity
plt.figure()
sns.barplot(x='Location', y='Severity', data=df)
plt.xticks(rotation=45)
plt.title("Severity by Location")
plt.show()

top_5 = df.sort_values(by='Alert_Count', ascending=False).head(5)

plt.figure(figsize=(10, 6))

plt.bar(top_5['Location'], top_5['Alert_Count'], color='orange')

plt.title('Top 5 Most Attacked Locations')
plt.xlabel('Location Name')
plt.ylabel('Number of Alerts')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('data/top_5_attacks.png')
print("Success: Top 5 chart saved to data/top_5_attacks.png")
plt.show()

    
