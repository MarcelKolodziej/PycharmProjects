# Returning a simple Value

# def get_formatted_name(first_name, last_name):
#     """Return a full name, neatly formatted."""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# musican = get_formatted_name('jimi', 'hendrix')
# print(musican)

# Making a argument optional


# def get_formatted_name(first_name, middle_name, last_name):
#     """Return a full name, neatly formatted"""
#     full_name = f"{first_name} {middle_name} {last_name}"
#     return full_name.title()
#
# musican = get_formatted_name('Jimy', 'Anderson', 'Hendrix')
# print(musican)

# def get_formatted_name(first_name, last_name, middle_name=''):
#     """Return a full name,with middle_name as optional argument"""
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
# musican = get_formatted_name('Jimmy', 'Albion', 'Hendrix')
# print(musican)