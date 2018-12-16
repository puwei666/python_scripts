
# 传入name，返回首字母大写，其余字母小写的name
def formate_name (name):
    return name[0:1].upper() + name[1:].lower()

# 传入name list，返回首字母大写，其余字母小写的name list
def formate_names (names):
    return map(formate_name, names)


name_list = ['cHerry', 'CLH', 'SeVen']

print formate_names(name_list)


