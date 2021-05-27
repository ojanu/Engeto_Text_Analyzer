TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

separator01 = '=' * 40
separator02 = '-' * 40

users = (
    ('bob', '123'),
    ('ann', 'pass123'),
    ('mike', 'password123'),
    ('liz', 'pass123')
)

# Request a login name and password from the user
print(separator01)
print('LOGIN')
print(separator02)
username = input('Username: ')
password = input('Password: ')
print(separator01)

# Verify that the information entered matches one of the users
i = 0
while i < len(users):
    if username == users[i][0] and password == users[i][1]:
        break
    i += 1
else:
    print('Sorry, wrong login, exiting the program!')
    exit()

print(f'Welcome to the app, {username}')
print(f'We have {len(TEXTS)} texts to be analyzed.')
print(separator01)

# Text selection
choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")
print(separator01)
if choice.isdigit():
    choice = int(choice) - 1
    if choice < 0 or choice > 2:
        print('Sorry, wrong select, exiting the program!')
        exit()
else:
    print('Sorry, wrong select, exiting the program!')
    exit()

selected_text = TEXTS[choice]
print('Selected text:')
print(selected_text)
print(separator01)

# Text analysis
