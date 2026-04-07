import pandas as pd

def score_alerts(file_path):
    df = pd.read_csv(file_path)

    severity_counter = {
    "NONE": 1,
    "LOW_CONFIDENCE_ATTACK": 2,
    "MEDIUM_CONFIDENCE_ATTACK": 4,
    "HIGH_CONFIDENCE_ATTACK": 6
    }

    df['Severity'] = df['Threat_Type'].map(severity_counter)

    summary = df.groupby('Location').agg({'Severity': 'sum','Threat_Type': 'count'}).rename(columns={'Threat_Type': 'Alert_Count'}).reset_index()

    def assign_priority(score):
        if score >= 15:
            return "HIGH"
        elif score >= 5:
            return "MEDIUM"
        else:
            return "LOW"

    summary['Priority'] = summary['Severity'].apply(assign_priority)

    summary = summary.sort_values(by='Severity', ascending=False)

    return summary


if __name__ == "__main__":
    summary = score_alerts('data/detected_alerts.csv')

    print("--- SOC TRIAGE REPORT ---")
    print(summary)

    summary.to_csv('data/final_triage_report.csv', index=False)

    print("\nSuccess: Triage report saved.")
