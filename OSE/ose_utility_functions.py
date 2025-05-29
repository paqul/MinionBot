# ose_file_names = ["cleric", "fighter", "magic_user", "thief"]
ose_file_names = ["class", "char_card"]


def check_if_file_exist(file_name: str):
    for classes_names in ose_file_names:
        if file_name.startswith(classes_names):
            return file_name

