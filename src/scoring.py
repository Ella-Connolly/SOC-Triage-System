import pandas as pd

df = pd.read_csv('alert.csv')

summary = df.groupby('Location').size().reset_index(name='Alert_Count')

priorities = []

for count in summary['Alert_Count']:
    if count > 3:
        priorities.append('HIGH')
    else:
        priorities.append('Low/Medium')

summary['Priority'] = priorities

summary = summary.sort_values(by='Priority')

print("--- SOC TRIAGE REPORT ---")
print(summary)

summary.to_csv('final_triage_report.csv', index=False)

print("\nSuccess: Triage report saved as final_triage_report.csv")
