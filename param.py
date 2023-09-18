import os 
directory = os.path.dirname(os.path.abspath(__file__))

splitted = directory.split('\\')
base=''
for x in range(len(splitted)):
    base += splitted[x]
    base += '/'
base  



#1
sink_json = base + 'sink.json'

#2
input_xlsx = base + 'input.xlsx'

#3
convert_xlsx = base + 'Files/json_bot/code_files/convert.xlsx'

#4
flat_json = base + 'Files/json_bot/code_files/flat_json.json'

#5
nested_json = base + 'Files/json_bot/code_files/nested_json.json'


