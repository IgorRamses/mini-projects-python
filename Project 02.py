# Write a program that asks for the user's first name. If the name has 4 letters or
# at least write "Your name is short", if it has between 5 and 6 letters, write
# "Your name is medium", greater than 6 write "Your name is large".

name = input('Write your first name: ')
qtt_characters_name = len(name)

if qtt_characters_name <= 4:
    print('Your name is short. ')

elif qtt_characters_name >=5 and qtt_characters_name <=6:
    print('Your name is medium. ')

elif qtt_characters_name >6:
    print('Your name is big. ')