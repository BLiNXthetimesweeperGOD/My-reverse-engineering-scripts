import os
def subfolder_scan(input_folder):
    files = []
    for item in os.listdir(input_folder):
        item_path = os.path.join(input_folder, item)
        if os.path.isdir(item_path):
            files.extend(subfolder_scan(item_path))
        else:
            files.append(item_path)
    return files

def name_split(file_path):
    head, tail = os.path.split(file_path)
    name, ext = os.path.splitext(tail)
    return head, name, ext
