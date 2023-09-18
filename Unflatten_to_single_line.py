import pandas as pd
import json

def convert_json(path,convert,flat,nested):
    def convert_node(text, pos):
        split_node = text.split(".", pos)  # split at the given position
        new_node = split_node[0] + "." + split_node[pos-1] + "." + split_node[pos].replace(".", "_")
        return new_node

    # read the Excel file
    df = pd.read_excel(convert)

    # convert the dataframe to a flat JSON object
    records = df.to_dict(orient='records')
    flat_json = {}
    #store=''
    for record in records:
        for key, value in record.items():
            # check if key starts with "device.identifiers."
            if key.startswith("device.identifiers."):
                key = convert_node(key, 2)
            flat_json[key] = value
            #Additional coed
            #if key.startswith("type"):
                #store = value

    # save the flat JSON object to a text file
    with open(flat, 'w') as f:
        f.write(json.dumps(flat_json))


    # Open flattened JSON file
    with open(flat, 'r') as flattened_file:

        # Load flattened JSON data
        flattened_data = json.load(flattened_file)

        # Create an empty nested dictionary
        nested_data = {}

        # Loop through flattened data
        for key, value in flattened_data.items():


            # Split key into parts
            parts = key.split('.')

            # Initialize nested dictionary pointer
            pointer = nested_data

            # Loop through key parts, creating nested dictionaries as needed
            for i, part in enumerate(parts):
                if i == len(parts) - 1:
                    pointer[part] = value
                else:
                    if part not in pointer:
                        pointer[part] = {}
                    pointer = pointer[part]

        # Open output file
        with open(nested, 'w') as nested_file:

            # Write nested data to output file
            json.dump(nested_data, nested_file, indent=4)

    # Read the contents of the source file
    with open(nested, "r") as source_file:
        json_data = json.load(source_file)

    # Write the contents to the sink file as a single line
    with open(path, "a") as sink_file:
        sink_file.write(json.dumps(json_data, separators=(',', ':')))
        # Add a newline character to the end of the file
        sink_file.write('\n')

    #return(store)
