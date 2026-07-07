# coding: utf8
import pickle

dict_qns1 = {'count': 5,
             1: {'qn': 'Which one is the antonym of the word \'compulsory?\'',
                 'ans': 'Voluntary', 'var1': 'Obligatory', 'var2': 'Mandatory', 'var3': 'Forced'},
             2: {'qn': 'Who painted the Water Lilies?',
                 'ans': 'Claude Monet', 'var1': 'Pablo Picasso', 'var2': 'Vincent Van Gogh', 'var3': 'Rembrandt'},
             3: {'qn': 'What year did World War II end?',
                 'ans': '1945', 'var1': '1944', 'var2': '1939', 'var3': '1941'},
             4: {'qn': 'What\'s the name of the river that runs through Egypt?',
                 'ans': 'The Nile', 'var1': 'White Nile', 'var2': 'Blue Nile', 'var3': 'Orange River'},
             5: {'qn': 'What\'s the capital of Italy?',
                 'ans': 'Rome', 'var1': 'Bologna', 'var2': 'Venice', 'var3': 'Milan'}}

dict_qns2 = {'count': 5,
             1: {'qn': 'What is the world’s smallest country?',
                 'ans': 'Vatican City', 'var1': 'Monaco', 'var2': 'Tuvalu', 'var3': 'Brussels'},
             2: {'qn': 'What nationality was Charlie Chaplin?',
                 'ans': 'British', 'var1': 'German', 'var2': 'French', 'var3': 'American'},
             3: {'qn': 'How many sides does a dodecahedron have?',
                 'ans': '12', 'var1': '13', 'var2': '9', 'var3': '11'},
             4: {'qn': 'Banksy is most associated with which city?',
                 'ans': 'Bristol', 'var1': 'Liverpool', 'var2': 'Cardiff', 'var3': 'Cambridge'},
             5: {'qn': 'Which chess piece can’t move in a straight line?',
                 'ans': 'Knight', 'var1': 'Bishop', 'var2': 'Pawn', 'var3': 'Rock'}}

dict_qns3 = {'count': 5,
             1: {'qn': 'Which of these phrases refers to a brief success?',
                 'ans': 'Flash in the pan', 'var1': 'Blaze in the pot', 'var2': 'Spark in the tub',
                 'var3': 'Flare in the jug'},
             2: {'qn': 'Which of these is a type of hat?',
                 'ans': 'Pork pie', 'var1': 'Sausage roll', 'var2': 'Scotch egg', 'var3': 'Potato crisp'},
             3: {'qn': 'In Welsh, what does ‘afon’ mean?',
                 'ans': 'River', 'var1': 'Fort', 'var2': 'Meadow', 'var3': 'Pool'},
             4: {'qn': 'Where does a cowboy wear chaps?',
                 'ans': 'On his legs', 'var1': 'On his head', 'var2': 'On his arms', 'var3': 'On his hands'},
             5: {'qn': 'Which king wrote a famous denunciation of smoking?',
                 'ans': 'James I', 'var1': 'Richard I', 'var2': 'William I', 'var3': 'George I'}}

# CREATING ALL DICTIONARY QUESTIONS

pickled_lvl1 = open('dict1.txt', 'wb')
pickle.dump(dict_qns1, pickled_lvl1)
pickled_lvl1.close()

pickled_lvl2 = open('dict2.txt', 'wb')
pickle.dump(dict_qns2, pickled_lvl2)
pickled_lvl2.close()

pickled_lvl3 = open('dict3.txt', 'wb')
pickle.dump(dict_qns3, pickled_lvl3)
pickled_lvl3.close()


# CREATING USERS FILE
# User1: user12003, User2: user22003, User3: user32003, User4: user42003

user = {'Admin': {'passw': 'mrd2003', 'score': 0},
        'User1': {'passw': 'user12003', 'score': 0},
        'User2': {'passw': 'user22003', 'score': 0},
        'User3': {'passw': 'user32003', 'score': 0},
        'User4': {'passw': 'user42003', 'score': 0}}

file = open('users.txt', 'wb')
pickle.dump(user, file)
file.close()
