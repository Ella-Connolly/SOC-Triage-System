import pandas as pd

def detect_threats(file_path):
    df = pd.read_csv(file_path)

    df['Threat_Type'] = "NONE"

    location_counts = df['Location'].value_counts()

    suspicious_locations = location_counts[location_counts > 3].index #checks for repeated alerts from the same location 3 times within a single log file (we generate 50 logs)

    df.loc[df['Location'].isin(suspicious_locations), 'Threat_Type'] = "SAME_LOCATION_REPEATED_ALERTS"

    df.loc[df['Signature'].str.contains("SQL|Injection|Brute"), 'Threat_Type'] = "COMMON_ATTACK_VECTORS" #checks signature for common attack vectors

    return df

if __name__ == "__main__":
    df = detect_threats('data/preprocessed_alerts.csv')

    print("Detection Complete:")
    print(df.head())

    df.to_csv('data/detected_alerts.csv', index=False)
