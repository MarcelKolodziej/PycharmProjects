# def build_profile(first, last, **options):
#     """Build a dictionary containing everything we know about a user."""
#     options['first_name'] = first
#     options['last_name'] = last
#     return options
#
#
# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)

# def build_sandwich(*items):
#     """Make sandwich with customers choice of items"""
#     print("Making a great sandwich")
#     for item in items:
#         print(f"....adding {item} to your sandwich.")
#     print("your sandwich is ready!\n")
#
# build_sandwich('cheese', 'tomatoes sauce', 'ham')
# build_sandwich('ham', 'cheese')
# build_sandwich('mushrooms')

def build_car(manufacturer, model_name, **options):
    """Print info about a car to make, take optional arguments from users info"""
    options['manufacturer'] = manufacturer
    options['model name'] = model_name
    return options

print(build_car('subaru', 'outback',
                color = 'blue',
                tow_package=True))
