def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musican = build_person('Jimy' ,'Hendrix', 25)
print(musican)

def get_formatted_name(f_name, l_name):
    """Return a full name, neatly formatted."""
    full_name = f"{f_name} {l_name}"
    return full_name.title()
# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time for quit)")

    f_name = input('First name:')
    if f_name == 'q':
        break

    l_name = input('Last name:')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f'\nHello, {formatted_name}!')