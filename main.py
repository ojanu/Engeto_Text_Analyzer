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

separator01 = '=' * 50
separator02 = '-' * 50

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
print(f'We have {len(TEXTS)} text(s) to be analyzed.')
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

print('Selected text:')
print(TEXTS[choice])
print(separator01)

# Text analysis
word_count = 0
word_count_title = 0
word_count_upper = 0
word_count_lower = 0
num_count = 0
num_sum = 0
selected_splited_text = TEXTS[choice].split()

while selected_splited_text:
    striped_string = selected_splited_text.pop().strip('.,?!')
    word_count += 1
    if striped_string.isalnum() and striped_string.istitle():
        word_count_title += 1
    elif striped_string.isalpha():
        if striped_string.isupper():
            word_count_upper += 1
        if striped_string.islower():
            word_count_lower += 1
    elif striped_string.isdigit():
        num_count += 1
        num_sum += int(striped_string)

print(f'There is/are {word_count} word(s) in the selected text.')
print(f'There is/are {word_count_title} titlecase word(s).')
print(f'There is/are {word_count_upper} uppercase word(s).')
print(f'There is/are {word_count_lower} lowercase word(s).')
print(f'There is/are {num_count} numeric string(s).')
print(f'The sum of all the numbers: {num_sum}')
print(separator01)

# Graph generation
selected_splited_text = TEXTS[choice].split()
occur = {}
num_rows = 0

for string in selected_splited_text:
    if len(string) > num_rows:
        num_rows = len(string)

for i in range(num_rows):
    occur.setdefault(i+1)

print(occur)




# TODO Vypsat postupne počet slov podle delky a vykreslit graf
# print('LEN', 'OCCURRENCES', 'NR.', sep='|')
# for i in range(num_rows):
#    print(i + 1, sep='|')
