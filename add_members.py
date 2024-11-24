import pandas as pd

# url must be in a CSV format append export?format=csv to the end of the url

master_member_list_url = "https://docs.google.com/spreadsheets/d/1Jhk7kqEsjQMBTFQfVPHwrW8KySbLkxrN0Qyjk04xZw4/export?format=csv"

members_with_stakes_assigned_url = "https://docs.google.com/spreadsheets/d/1UBSJTMes68zuL0PsF8P-w_-gftCwsJmEZTodjwDS0OA/export?format=csv"

sheet2_url = "https://docs.google.com/spreadsheets/d/1Jhk7kqEsjQMBTFQfVPHwrW8KySbLkxrN0Qyjk04xZw4/export?gid=1720524604#gid=1720524604&format=csv"

id_column_name = "MRN"
address_col_name = "Search"
# Read the google sheets into the DataFrame

master_member_sheet = pd.read_csv(master_member_list_url)
member_with_stakes_sheet = pd.read_csv(members_with_stakes_assigned_url)

# Clean the Data
master_ids = master_member_sheet[id_column_name].dropna()
complied_ids = member_with_stakes_sheet[id_column_name].dropna()

# Get new members
new_member_rows = set(master_ids).symmetric_difference(set(complied_ids))

new_member_addresses = []
for id in new_member_rows:
    new_member_addresses.append(master_member_sheet.loc[master_member_sheet[id_column_name] == id, address_col_name])

address_values = []
for address in new_member_addresses:
    # convert address data to a list of string addresses
    address_values.append(list(address)[0])

print(address_values)
