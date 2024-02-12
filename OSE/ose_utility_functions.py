ose_file_names = ["cleric", "fighter", "user-magic", "thief"]


def check_if_file_exist(file_name: str):
    for classes_names in ose_file_names:
        if file_name.startswith(classes_names):
            return file_name

