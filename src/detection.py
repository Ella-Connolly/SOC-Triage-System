import pandas as pd

def detect_threats(file_path):
    df = pd.read_csv(file_path)

    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    df['Threat_Type'] = "NONE"

    location_counts = df['Location'].value_counts()
    suspicious_locations = location_counts[location_counts > 5].index

    df['Repeated_Location'] = df['Location'].isin(suspicious_locations) #checks for repeated alerts from the same location 3 times within a single log file (we generate 400 logs)

    df['Suspicious_Signature'] = df['Signature'].str.contains("SQL|Injection|Brute|Trojan|Ransomware|Exploit|Hack", case=False, na=False) #checks signature for common attack vectors

    df = df.sort_values(by='Timestamp')

    df['Time_Diff'] = df.groupby('Location')['Timestamp'].diff().dt.total_seconds()

    df['Rapid_Activity'] = df['Time_Diff'] < 300

    df.loc[(df['Repeated_Location']) & (df['Suspicious_Signature']) & (df['Rapid_Activity']), 'Threat_Type'] = "HIGH_CONFIDENCE_OF_ATTACK" #repeated locations + suspicious signature + rapid activity

    df.loc[(df['Repeated_Location']) & (df['Suspicious_Signature']) & (df['Threat_Type'] == "NONE"), 'Threat_Type' ] = "MEDIUM_CONFIDENCE_OF_ATTACK" #repeated locations + suspicious signature but no rapid activity

    df.loc[(df['Suspicious_Signature']) & (df['Threat_Type'] == "NONE"), 'Threat_Type'] = "LOW_CONFIDENCE_OF_ATTACK" #suspicious signature but no repeated locations or rapid activity

    return df


if __name__ == "__main__":
    df = detect_threats('data/preprocessed_alerts.csv')

    print("Detection Complete:")
    print(df.head())

    df.to_csv('data/detected_alerts.csv', index=False)
