import re
import param
sink_json = param.sink_json


def replace_text_in_file(pattern, replacement):
    # define the pattern to search for
    pattern = re.compile(pattern)

    # open the file for reading and writing
    with open(sink_json, 'r+') as file:
        # read the file contents
        contents = file.read()

        # perform the find and replace operation
        new_contents = pattern.sub(replacement, contents)

        # move the file pointer to the beginning of the file
        file.seek(0)

        # write the updated contents back to the file
        file.write(new_contents)

        # truncate any remaining content
        file.truncate()
