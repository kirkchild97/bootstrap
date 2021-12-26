import os
import glob
from posixpath import dirname

print(os.path.dirname(__file__))

def find_classes():
    parent_dir_path = os.path.dirname(os.path.dirname(__file__))
    class_dir_path = r'\scss'
    total_path = parent_dir_path + class_dir_path
    css_extension = r'\*.scss'

    base_class_files = glob.glob(total_path + css_extension, recursive= True)

    # testFile = open(base_class_files[5], "r")

    # print(testFile.readlines())
    class_snippets = []
    for class_file in base_class_files:
        # print(class_file)
        read_file = open(class_file, "r")
        for file_line in read_file.readlines():
            if file_line[0] == ".":
                if " " in file_line:
                    file_line = file_line.split(" ")[0]
                if "," in file_line:
                    file_line = file_line.split(",")[0]
                if ":" in file_line:
                    file_line = file_line.split(":")[0]
                class_snippets.append(file_line)
                print(file_line, " Added")
    return class_snippets


def make_class_snippets(classes, fileType="html"):
    # snippet_file = open(os.path.dirname(__file__),"/html.json", "w")
    snippet_file = """"""
    for snip in range(0, len(classes)):
        if snip == len(classes) - 1:
            snippet_file += f'''
            "{classes[snip]}": {{
                "prefix": "{classes[snip]}",
                "body":[ 
                    "{classes[snip]}"
                ],
                "description": "Bootstrap Simple Snippet"
            }}'''
        else:
            snippet_file += f'''
            "{classes[snip]}": {{
                "prefix": "{classes[snip]}",
                "body":[ 
                    "{classes[snip]}"
                ],
                "description": "Bootstrap Simple Snippet"
            }},
            '''
    with open("snippets.json", "w") as f:
        f.write(snippet_file)
get_snips = find_classes()
make_class_snippets(get_snips)
