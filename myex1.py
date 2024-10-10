print('Welcome to Wilson Hospital')
print('We will need some information from you before proceeding.')

# Collecting basic information
name = input('What is your name? ')
age = int(input('How old are you? '))
contagious_disease = input('Do you have any contagious disease? (yes/no) ').strip().lower()

# Checking the level of disease
if contagious_disease == 'yes':
    print('Let\'s go to the red room.')
elif contagious_disease == 'no':
    print('Let\'s go to the yellow room.')
else:
    print('We will go to the black room to study your case.')

# Checking queue position based on age
if age >= 65:
    print('Due to your age, we will put you first in line.')
elif age > 50:
    print('You will have priority, but not the highest.')
else:
    print('Please wait in line normally.')
