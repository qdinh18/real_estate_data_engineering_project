import pandas as pd  # Import pandas for data manipulation
import numpy as np  # Import numpy for handling NaN values
from datetime import date  # Import datetime for date-related operations
def clean_data():
    # Load raw data from JSONL file
    raw_df = pd.read_json('data_stage/raw_data/bds.jsonl', dtype=str, lines=True)

    # Replace string 'None' with NaN
    raw_df.replace('None', np.nan, inplace=True)

    # Iterate through rows to clean and transform data
    for index, row in raw_df.iterrows():
        if 'triệu/m²' in str(row['price']):  
            if pd.notna(row['price']):
                raw_df.at[index, 'price_per_m²'], raw_df.at[index, 'price'] = row['price'], row['price_per_m²']
        
        if 'phòng' not in str(row['bedroom']):  # Check if 'bedroom' contains 'phòng'
            raw_df.at[index, 'bedroom'] = np.nan
        
        if 'phòng' not in str(row['bathroom']):  # Check if 'bathroom' contains 'phòng'
            raw_df.at[index, 'bathroom'] = np.nan
        
        if 'Thỏa thuận' in str(row['price']):  # Remove negotiated prices
            raw_df.at[index, 'price'] = np.nan
        
        if '.' in str(row['number_of_apartments']):  # Convert thousands format to integer
            raw_df.at[index, 'number_of_apartments'] = float(row['number_of_apartments']) * 1000
        
        if str(row['broker_name']) is not np.nan:  # Format broker names with title case
            raw_df.at[index, 'broker_name'] = str(row['broker_name']).title()
        
        if 'triệu' in str(row['price']):  # Remove 'triệu' in price values
            raw_df.at[index, 'price'] = np.nan
        
        if 'nghìn/m²' in str(row['price_per_m²']):  # Remove invalid price per m²
            raw_df.at[index, 'price_per_m²'] = np.nan
            
        if 'tỷ/m²' in str(row['price_per_m²']):  # Remove invalid price per m²
            raw_df.at[index, 'price_per_m²'] = np.nan

    # Define a dictionary for regex-based text replacements
    replace_dict = {
        'price': {r'~': '', r' tỷ': '', r',': '.'},
        'area': {r' m²': '', r',': '.'},
        'bedroom': {r' phòng': ''},
        'bathroom': {r' phòng': ''},
        'price_per_m²': {r' triệu/m²': '', r'~': '', r',': '.'}
    }

    # Apply text replacements using regex
    raw_df.replace(replace_dict, regex=True, inplace=True)
    # Convert date columns to datetime format
    raw_df['posted_date'] = pd.to_datetime(raw_df['posted_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
    raw_df['expired_date'] = pd.to_datetime(raw_df['expired_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')
    # Convert data types to float where applicable
    raw_df['price'] = raw_df['price'].astype(float)
    raw_df['area'] = raw_df['area'].astype(float)
    raw_df['bedroom'] = raw_df['bedroom'].astype(float)
    raw_df['bathroom'] = raw_df['bathroom'].astype(float)
    raw_df['price_per_m²'] = raw_df['price_per_m²'].astype(float)
    raw_df['number_of_apartments'] = raw_df['number_of_apartments'].astype(float)
    raw_df['number_of_buildings'] = raw_df['number_of_buildings'].astype(float)

    # Handle missing values and remove duplicates
    raw_df.fillna(np.nan, inplace=True)
    raw_df.drop_duplicates(inplace=True, keep='first')
    raw_df['update_date'] = date.today().strftime('%Y-%m-%d')
    # Save the cleaned data to a CSV file
    file_path = 'data_stage/cleaned_data/bds.csv'
    raw_df.to_csv(file_path, mode='w', header=True, index=False)
    
    print(f"Created {file_path} with header.")
