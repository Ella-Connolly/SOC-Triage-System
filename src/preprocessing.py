import pandas as pd

def clean_and_sort_logs(file_path):
    df = pd.read_csv(file_path)

    df['Timestamp'] = pd.to_datetime(df['Timestamp'])

    filtered_df = df[df['Status'] != 'closed']

    sorted_df = filtered_df.sort_values(by='Timestamp')

    return sorted_df

if __name__ == "__main__":
    cleaned_data = clean_and_sort_logs('data/alert.csv')

    print("Preprocessing Complete:")
    print(cleaned_data.head())
        
    cleaned_data.to_csv('data/preprocessed_alerts.csv', index=False)
