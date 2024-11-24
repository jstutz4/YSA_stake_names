import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# use creds to create a client to interact with the Google Drive API

scopes =['https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name('./update-stake-name.json', scopes)
client = gspread.authorize(creds)
all_sheets = client.open("get-home-stake-name-from-address-bulk-run-sample")

master_dir = all_sheets.worksheet("Master Directory")
master_df = pd.DataFrame(master_dir.get_all_records())

id_col_name = "MRN"
row_id_to_update = 24
col_name_to_update = "first name"
stake_name = "Jon"
col_index_fallback = 2

# Adding 2 to account for header row and 0-based index
row_index = master_df.index[master_df[id_col_name] == row_id_to_update].tolist()[0] + 2

# Adding 1 to account for 0-based index
col_index = master_df.columns.get_loc(col_name_to_update) + 1

print(master_df.columns[col_index_fallback])

# update the stake name for the given row
master_dir.update_cell(row_index, col_index, stake_name)



