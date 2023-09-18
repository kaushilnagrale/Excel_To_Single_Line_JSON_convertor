import openpyxl
import pandas as pd
import Unflatten_to_single_line
import findNreplace
import param

sink_json = param.sink_json
input_xlsx= param.input_xlsx
convert_xlsx= param.convert_xlsx
flat_json= param.flat_json
nested_json= param.nested_json

# Open the file in write mode
with open(sink_json, 'w') as f:
    # Write an empty string to the file
    f.write('')

# Load the Excel workbook
workbook = openpyxl.load_workbook(input_xlsx)

# Select the active worksheet
worksheet = workbook.active

# Get the maximum number of columns in the worksheet
max_col = worksheet.max_column

# Get the number of iterations from the user
num_iterations = max_col-1

# Load the Excel file with increasing usecols index
for i in range(num_iterations):
    usecols = [0, i+1]  # Set the columns to read
    df = pd.read_excel(input_xlsx, usecols=usecols)
    df_t = df.transpose()
    df_t.to_excel(convert_xlsx, index=False, header=False)
    Unflatten_to_single_line.convert_json(sink_json,convert_xlsx,flat_json,nested_json)

paramold=['com_urbanairship_aaid','com_urbanairship_gimbal_aii','com_urbanairship_idfa','com_urbanairship_limited_ad_tracking_enabled','com_urbanairship_vendor']
paramnew=['com.urbanairship.aaid','com.urbanairship.gimbal.aii','com.urbanairship.idfa','com.urbanairship.limited_ad_tracking_enabled','com.urbanairship.vendor']

for p1,p2 in zip(paramold,paramnew):
    findNreplace.replace_text_in_file(p1,p2)



print("OK The Excel payload was converted to Single line Json")