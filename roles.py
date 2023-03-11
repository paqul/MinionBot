roles_list = ["Specjalista", "Dyrektor Techniczny", "Dyrektor Badań i Rozwoju", "Dyrektor Marketingu i Reklamy", "Dyrektor Testów i Jakości"]
role_list_test = ["Test pierwszy", "test drugi", "Trzeci Test", "cos"]


def handle_roles(member) -> str:
    # print(type(member), member, type(member.name), member.name, type(member.id), member.id)
    name = member.name.lower()

    if member.id == 608017745346560000:
        return roles_list[1]
    else:
        return roles_list[0]
