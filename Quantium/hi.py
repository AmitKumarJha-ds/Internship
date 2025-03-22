import pandas as pd

# Load the uploaded CSV files to understand their structure and contents
purchase_behaviour_file = "/mnt/data/QVI_purchase_behaviour.csv"
transaction_data_file = "/mnt/data/QVI_transaction_data.xlsx"
qvi_data_file = "/mnt/data/QVI_data.csv"

# Read the CSV files
purchase_behaviour_df = pd.read_csv(purchase_behaviour_file)
qvi_data_df = pd.read_csv(qvi_data_file)

# Read the Excel file (assuming the first sheet contains relevant data)
transaction_data_df = pd.read_excel(transaction_data_file, sheet_name=0)

# Display the first few rows of each dataset
purchase_behaviour_df.head(), qvi_data_df.head(), transaction_data_df.head()
