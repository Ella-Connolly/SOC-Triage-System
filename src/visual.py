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

#show only top 10 locations by severity (when we switched to 400 logs it lagged systems)
top_locations = df.sort_values(by='Severity', ascending=False).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(x='Location', y='Severity', data=top_locations)

plt.xticks(rotation=45)
plt.title("Top 10 Locations by Severity")
plt.tight_layout()
plt.savefig('data/top_severity_locations.png')
print("Success: Top severity chart saved.")
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

df_detected = pd.read_csv('data/detected_alerts.csv')

threat_counts = df_detected['Threat_Type'].value_counts()

plt.figure(figsize=(8,6))
plt.bar(threat_counts.index, threat_counts.values)

plt.title("Threat Classification Distribution")
plt.xlabel("Threat Type")
plt.ylabel("Number of Events")
plt.xticks(rotation=30)

plt.savefig('data/threat_distribution.png')
print("Saved threat distribution chart")
plt.show()
