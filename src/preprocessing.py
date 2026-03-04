import pandas as pd

def clean_and_sort_logs(file_path):
    df = pd.read_csv(file_path)
    
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    filtered_df = 
