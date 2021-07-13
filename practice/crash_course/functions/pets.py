# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# describe_pet('ant-eater', 'czupakabra')
# describe_pet('Dog', 'Gody')


# def keywords_arguments(animal_type, pet_name):
#     """Display information about pet using keywords arguments"""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# keywords_arguments(animal_type='ant-eater', pet_name='dziobas')

# def describe_pet(pet_name, animal_type='dog'):
#     """Display information about a pet."""
#     print(f"\nI have a {animal_type}")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
#
# describe_pet(pet_name='willie')
# describe_pet('willie')
#
# # A hamster named Harry
# describe_pet('harry', 'hamster')
# describe_pet(pet_name='harry', animal_type='hamster')
# describe_pet(animal_type='hamster', pet_name='harry')

def make_shirt(size='[L]arge', massage='I love python'):
    """Summarize the size and massage on shirt"""
    print(f'\nThe size of the shirt is {size} and have massage "{massage}" on it ')


make_shirt(12, 'Hello World!')
make_shirt()
make_shirt(size='[M]edium', massage='Default massage')
make_shirt(massage='Default massage', size='[M]edium')
