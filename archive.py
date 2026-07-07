from tkinter import *
import random
import pickle
from tkinter import messagebox

'''
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
             1: {'qn': 'What is the world's smallest country?',
                 'ans': 'Vatican City', 'var1': 'Monaco', 'var2': 'Tuvalu', 'var3': 'Brussels'},
             2: {'qn': 'What nationality was Charlie Chaplin?',
                 'ans': 'British', 'var1': 'German', 'var2': 'French', 'var3': 'American'},
             3: {'qn': 'How many sides does a dodecahedron have?',
                 'ans': '12', 'var1': '13', 'var2': '9', 'var3': '11'},
             4: {'qn': 'Banksy is most associated with which city?',
                 'ans': 'Bristol', 'var1': 'Liverpool', 'var2': 'Cardiff', 'var3': 'Cambridge'},
             5: {'qn': 'Which chess piece can�t move in a straight line?',
                 'ans': 'Knight', 'var1': 'Bishop', 'var2': 'Pawn', 'var3': 'Rock'}}

dict_qns3 = {'count': 5,
             1: {'qn': 'Which of these phrases refers to a brief success?',
                 'ans': 'Flash in the pan', 'var1': 'Blaze in the pot', 'var2': 'Spark in the tub',
                 'var3': 'Flare in the jug'},
             2: {'qn': 'Which of these is a type of hat?',
                 'ans': 'Pork pie', 'var1': 'Sausage roll', 'var2': 'Scotch egg', 'var3': 'Potato crisp'},
             3: {'qn': 'In Welsh, what does �afon� mean?',
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
'''

# READING ALL DICTIONARY QUESTIONS

pickled_lvl1 = open('dict1.txt', 'rb')
dict_qns1 = pickle.load(pickled_lvl1)
pickled_lvl1.close()

pickled_lvl2 = open('dict2.txt', 'rb')
dict_qns2 = pickle.load(pickled_lvl2)
pickled_lvl2.close()

pickled_lvl3 = open('dict3.txt', 'rb')
dict_qns3 = pickle.load(pickled_lvl3)
pickled_lvl3.close()


global name, passw, qn_str, varA, varB, varC, varD, lvl, ans, qn, dct, x


def sign():

    def sign_up():

        label_error = NONE

        frame = Frame(window, bd=10)
        frame.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.6)

        # labels, entries, and 'continue' button
        label = Label(frame, text='SIGN UP', font='Arial 16 bold')
        label.place(relwidth=1, relheight=0.1)

        label_name = Label(frame, text='Enter your name:', font='16')
        label_name.place(relx=0.1, rely=0.2, relwidth=0.4, relheight=0.1)

        label_password1 = Label(frame, text='Enter password:', font='16')
        label_password1.place(relx=0.1, rely=0.4, relwidth=0.4, relheight=0.1)

        label_password2 = Label(frame, text='Confirm password:', font='16')
        label_password2.place(relx=0.1, rely=0.6, relwidth=0.4, relheight=0.1)

        entry_name = Entry(frame, font='Arial', bd=3)
        entry_name.place(relx=0.5, rely=0.2, relwidth=0.4, relheight=0.1)

        entry_password1 = Entry(frame, font='Arial', bd=3, show='*')
        entry_password1.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.1)

        entry_password2 = Entry(frame, font='Arial', bd=3, show='*')
        entry_password2.place(relx=0.5, rely=0.6, relwidth=0.4, relheight=0.1)

        button_continue = Button(frame, font='Arial', text='Continue',
                                 bg='#c6daf5', activebackground='#8797ad', command=lambda: button_continue_check())
        button_continue.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.2)

        # save login and pass
        def save():
            global name
            global passw

            file = open('users.txt', 'rb')
            user = pickle.load(file)
            file.close()

            # user = dict()
            name = entry_name.get()
            passw = entry_password1.get()
            user[name] = {'passw': passw, 'score': 0}
            # print(user) --> {'Admin': {'passw': 'mrd2003', 'score': 0}}

            file = open('users.txt', 'wb')
            pickle.dump(user, file)
            file.close()

        # Testing password
        def button_continue_check():
            nonlocal label_error
            error = ''

            if len(entry_name.get()) == 0:
                error = '*login error'
            elif len(entry_password1.get()) == 0 or len(entry_password2.get()) == 0:
                error = '*password error'
            elif not 6 <= len(entry_password1.get()) <= 14:
                error = '*your password needs to be between 6 and 14 characters'
            elif entry_password1.get() != entry_password2.get():
                error = '*password error'
            else:
                save()
                image_between()

            label_error = Label(frame, fg='#eb0c0c')
            label_error.config(text=error)
            label_error.place(rely=0.7)

    def sign_in():
        global name
        global passw

        label_error = NONE

        frame = Frame(window, bd=10)
        frame.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.6)

        # labels, entries, and 'continue' button
        label = Label(frame, text='SIGN IN', font='Arial 16 bold')
        label.place(relwidth=1, relheight=0.1)

        label_name = Label(frame, text='Enter your name:', font='16')
        label_name.place(relx=0.1, rely=0.2, relwidth=0.4, relheight=0.1)

        label_password1 = Label(frame, text='Enter password:', font='16')
        label_password1.place(relx=0.1, rely=0.4, relwidth=0.4, relheight=0.1)

        entry_name = Entry(frame, font='Arial', bd=3)
        entry_name.place(relx=0.5, rely=0.2, relwidth=0.4, relheight=0.1)

        entry_password = Entry(frame, font='Arial', bd=3, show='*')
        entry_password.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.1)

        name = entry_name.get()
        passw = entry_password.get()

        button_continue = Button(frame, font='Arial', text='Continue', command=lambda: button_continue_check2(),
                                 bg='#c6daf5', activebackground='#8797ad')
        button_continue.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.2)

        # Testing password
        def button_continue_check2():
            global name, passw
            nonlocal label_error
            error = ''

            file = open('users.txt', 'rb')
            u = pickle.load(file)
            file.close()

            if len(entry_name.get()) == 0:
                error = '*login error'
            elif len(entry_password.get()) == 0:
                error = '*password error'
            elif entry_name.get() in u and entry_password.get() == u[entry_name.get()]['passw']:
                name = entry_name.get()
                passw = entry_password.get()
                image_between()
            else:
                messagebox.showerror('Error', 'Invalid login or password')

            label_error = Label(frame, text=error, fg='#eb0c0c')
            label_error.place(rely=0.7)

    frame_sign = Frame()

    button_signup = Button(window, font='Arial', text='Sign Up', command=sign_up,
                           bg='#5179b5', fg='white', activebackground='#1d437a')
    button_signup.place(relx=0.2, rely=0.1, relwidth=0.3, relheight=0.1)

    button_signin = Button(window, font='Arial', text='Sign In', command=sign_in,
                           bg='#5179b5', fg='white', activebackground='#1d437a')
    button_signin.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.1)
    frame_sign.mainloop()


def image_between():
    def countdown(count):
        if count > 0:
            frame.after(1000, countdown, count-1)
            frame.mainloop()
        else:
            label.pack_forget()
            image_menu()

    frame = Frame()

    label = Label()
    label.config(image=image1)
    label.pack()

    countdown(1)

    frame.mainloop()


def image_menu():
    menu_frame = Frame()
    label = Label()
    label.config(image=image2)
    label.pack()

    def show_top():
        file = open('users.txt', 'rb')
        dct = pickle.load(file)
        file.close()
        lst_n = list(dct.keys())
        lst_s = list()
        for i in lst_n:
            lst_s.append(dct[i]['score'])
        print(lst_n)
        print(lst_s)

        def sort_scores(a, b):
            for i in range(len(lst_n)):
                max_score = max(b[i:])
                index = b[i:].index(max_score) + i
                if index != i:
                    a[i], a[index] = a[index], a[i]
                    b[i], b[index] = b[index], b[i]

        sort_scores(lst_n, lst_s)

        txt = []
        for i in range(len(lst_s)):
            txt.append(f'{i+1}. {lst_n[i]} - {lst_s[i]}')
            print(f'{i+1}. {lst_n[i]} - {lst_s[i]}')

        label_top5.config(text=f'TOP 5:\n{txt[0]}$\n{txt[1]}$\n{txt[2]}$\n{txt[3]}$\n{txt[4]}$')

    label_top5 = Label(text='', bg='#1c1154', fg='gold', font='Arial 14 bold')
    label_top5.place(relx=0.75, rely=0.03, relwidth=0.24, relheight=0.5)

    show_top()

    button_play = Button(font='Boilder 14', text='PLAY', fg='white', command=lambda: image_qns(),
                         bg='#eb9710', activebackground='#eb9710', activeforeground='#031145')
    button_play.place(relx=0.25, rely=0.69, relwidth=0.52, relheight=0.08)

    button_add = Button(font='Boilder 12', text='ADD QUESTION', fg='white', command=lambda: add_qn(),
                        bg='#031145', activebackground='#031145', activeforeground='#eb9710', state=ACTIVE)
    button_add.place(relx=0.25, rely=0.8, relwidth=0.52, relheight=0.07)

    def image_qns():
        label.pack_forget()
        frame = Frame()

        label2 = Label()
        label2.config(image=image3)
        label2.pack()

        qns_asked_num = 0
        asked_qns = []

        def ask():
            global qn_str, varA, varB, varC, varD, lvl, ans, qn, dct
            nonlocal qns_asked_num
            qns_asked_num += 1

            if qns_asked_num <= 5:
                file = open('dict1.txt', 'rb')
                dct = pickle.load(file)
                file.close()

            elif 6 <= qns_asked_num <= 10:
                file = open('dict2.txt', 'rb')
                dct = pickle.load(file)
                file.close()

            elif 11 <= qns_asked_num <= 15:
                file = open('dict3.txt', 'rb')
                dct = pickle.load(file)
                file.close()

            print("dct\n", dct)

            count_add = dct['count']
            qn = random.randint(1, count_add)  # question number
            qn_str = dct[qn]['qn']

            if qn_str in asked_qns:
                qns_asked_num -= 1
                ask()
            else:
                asked_qns.append(qn_str)
                list_sq = [dct[qn]['ans'],
                           dct[qn]['var1'],
                           dct[qn]['var2'],
                           dct[qn]['var3']]

                random.shuffle(list_sq)
                varA = list_sq[0]
                varB = list_sq[1]
                varC = list_sq[2]
                varD = list_sq[3]
                print(dct[qn]['qn'], list_sq[0], list_sq[1],
                      list_sq[2], list_sq[3])

            # SCORES
            image_sb = image_dict[qns_asked_num]
            label_sb = Label(text=scores[qns_asked_num], font='Arial 14', bg='black', fg='white', image=image_sb)
            label_sb.place(relx=0.02, rely=0.02, relwidth=0.2, relheight=0.5)

            label_score = Label(text=f'{scores[qns_asked_num]} $', font='Arial 14', bg='black', fg='white')
            label_score.place(relx=0.72, rely=0.1, relwidth=0.16, relheight=0.055)

            # QUESTION + VARIANTS
            label_qn = Label(font='Boulder 14', text=qn_str, bg='black', fg='white')
            label_qn.place(relx=0.2, rely=0.55, relwidth=0.6, relheight=0.1)

            button_var_a = Button(font='Boulder 14', text=varA, bg='black', fg='white',
                                  activebackground='#1c6ab8', command=lambda: check_a())
            button_var_a.place(relx=0.17, rely=0.72, relwidth=0.29, relheight=0.07)
            button_var_c = Button(font='Boulder 14', text=varC, bg='black', fg='white',
                                  activebackground='#1c6ab8', command=lambda: check_c())
            button_var_c.place(relx=0.17, rely=0.83, relwidth=0.29, relheight=0.07)
            button_var_b = Button(font='Boulder 14', text=varB, bg='black', fg='white',
                                  activebackground='#1c6ab8', command=lambda: check_b())
            button_var_b.place(relx=0.585, rely=0.72, relwidth=0.29, relheight=0.07)
            button_var_d = Button(font='Boulder 14', text=varD, bg='black', fg='white',
                                  activebackground='#1c6ab8', command=lambda: check_d())
            button_var_d.place(relx=0.585, rely=0.83, relwidth=0.29, relheight=0.07)

            button_pass = Button(font='Boulder 14', text='Continue', bg='black', fg='white',
                                 activebackground='#1c6ab8', state=DISABLED, command=lambda: ask())
            button_pass.place(relx=0.7, rely=0.4, relwidth=0.25, relheight=0.07)

            if qns_asked_num == 15:
                button_pass.config(text='Finish', command=lambda: result())

            # TIMER FOR QUESTIONS
            label_time = Label(text='Timer', bg='black', fg='white')
            label_time.place(relx=0.45, rely=0.48, relwidth=0.1, relheight=0.05)

            def count_time(count):
                if count >= 0:
                    label_time.config(text=count)
                    label_time.after(1000, count_time, count - 1)
                if button_pass.cget('text'):
                    count += 20 - count
                else:
                    label.pack_forget()
                    result()

            count_time(10)

            # COUNTDOWN
            def countdown(count):
                if count > 0:
                    frame.after(1000, countdown, count - 1)
                    frame.mainloop()
                else:
                    label.pack_forget()
                    result()

            # CHECKING ANSWER
            def check_a():
                if button_var_a.cget('text') == dct[qn]['ans']:
                    button_var_a.config(bg='green', fg='black', state=DISABLED)
                    button_var_b.config(state=DISABLED)
                    button_var_c.config(state=DISABLED)
                    button_var_d.config(state=DISABLED)
                    button_pass.config(state=ACTIVE)
                else:
                    button_var_a.config(bg='red', state=DISABLED)
                    button_var_b.config(state=DISABLED)
                    button_var_c.config(state=DISABLED)
                    button_var_d.config(state=DISABLED)
                    button_pass.config(state=DISABLED)
                    countdown(2)

            def check_b():
                if button_var_b.cget('text') == dct[qn]['ans']:
                    button_var_a.config(state=DISABLED)
                    button_var_b.config(bg='green', fg='black', state=DISABLED)
                    button_var_c.config(state=DISABLED)
                    button_var_d.config(state=DISABLED)
                    button_pass.config(state=ACTIVE)
                else:
                    button_var_a.config(state=DISABLED)
                    button_var_b.config(bg='red', state=DISABLED)
                    button_var_c.config(state=DISABLED)
                    button_var_d.config(state=DISABLED)
                    button_pass.config(state=DISABLED)
                    countdown(2)

            def check_c():
                if button_var_c.cget('text') == dct[qn]['ans']:
                    button_var_a.config(state=DISABLED)
                    button_var_b.config(state=DISABLED)
                    button_var_c.config(bg='green', fg='black', state=DISABLED)
                    button_var_d.config(state=DISABLED)
                    button_pass.config(state=ACTIVE)
                else:
                    button_var_a.config(state=DISABLED)
                    button_var_b.config(state=DISABLED)
                    button_var_c.config(bg='red', state=DISABLED)
                    button_var_d.config(state=DISABLED)
                    button_pass.config(state=DISABLED)
                    countdown(2)

            def check_d():
                if button_var_d.cget('text') == dct[qn]['ans']:
                    button_var_a.config(state=DISABLED)
                    button_var_b.config(state=DISABLED)
                    button_var_c.config(state=DISABLED)
                    button_var_d.config(bg='green', fg='black', state=DISABLED)
                    button_pass.config(state=ACTIVE)
                else:
                    button_var_a.config(state=DISABLED)
                    button_var_b.config(state=DISABLED)
                    button_var_c.config(state=DISABLED)
                    button_var_d.config(bg='red', state=DISABLED)
                    button_pass.config(state=DISABLED)
                    countdown(2)

            # FOR JOKER
            var1 = random.randint(70, 100)
            var2 = random.randint(0, 100 - var1)
            var3 = random.randint(0, 100 - var1 - var2)
            var4 = random.randint(0, 100 - var1 - var2 - var3)
            ans = f"'{dct[qn]['ans']}' -- {var1}%\n" \
                  f"'{dct[qn]['var1']}' -- {var2}%\n" \
                  f"'{dct[qn]['var2']}' -- {var3}%\n" \
                  f"'{dct[qn]['var3']}' -- {var4}%\n"

        ask()

        # JOKER ANSWERS
        def show_call():
            button_call.config(image=image_callX, state=DISABLED)
            label_ans = Label(text=f'Hello. ... ...\nHm... That\'s a tricky one..\nLemme think.\n'
                                   f"I think answer is..\n'{dct[qn]['ans']}'", font='Boulder 14',
                              bg='black', fg='white')
            label_ans.place(relx=0.35, rely=0.02, relwidth=0.3, relheight=0.45)

            label_ans.after(5000, lambda: label_ans.destroy())

        def show_5050():
            button_5050.config(image=image_5050X, state=DISABLED)
            label_ans = Label(text=f"Variant 1 is ..\n '{dct[qn]['var1']}'\n"
                                   f"Variant 2 is ..\n '{dct[qn]['ans']}'\n"
                                   f"Only one correct...", font='Boulder 14', bg='black', fg='white')
            label_ans.place(relx=0.35, rely=0.02, relwidth=0.3, relheight=0.45)
            label_ans.after(5000, lambda: label_ans.destroy())

        def show_audience():
            button_audience.config(image=image_audienceX, state=DISABLED)
            label_ans = Label(text=ans, font='Boulder 14', bg='black', fg='white')
            label_ans.place(relx=0.35, rely=0.02, relwidth=0.3, relheight=0.45)

            label_ans.after(5000, lambda: label_ans.destroy())

        # JOKER BUTTONS
        button_call = Button(font='Boulder 14', image=image_call, bg='black', fg='white',
                             activebackground='#1c6ab8', command=lambda: show_call())
        button_call.place(relx=0.23, rely=0.02, relwidth=0.08, relheight=0.15)
        button_5050 = Button(font='Boulder 14', image=image_5050, bg='black', fg='white',
                             activebackground='#1c6ab8', command=lambda: show_5050())
        button_5050.place(relx=0.23, rely=0.19, relwidth=0.08, relheight=0.15)
        button_audience = Button(font='Boulder 14', image=image_audience, bg='black', fg='white',
                                 activebackground='#1c6ab8', command=lambda: show_audience())
        button_audience.place(relx=0.23, rely=0.36, relwidth=0.08, relheight=0.15)

        # RESULTS
        def result():
            global name

            def back_menu():
                label3.pack_forget()
                image_menu()

            label2.pack_forget()

            result_frame = Frame()

            label3 = Label()
            label3.config(image=image4)
            label3.pack()

            label4 = Label(font='Boulder 16 bold', text=f'CONGRATULATIONS!!!\nYOU WON {scores[qns_asked_num - 1]}$ '
                                                        f'DOLLARS.', bg='#1a2047', fg='white')
            label4.place(relx=0.24, rely=0.25, relwidth=0.52, relheight=0.2)

            button_back = Button(font='Arial 14 bold', text='BACK TO MENU', bg='#f5ae20',
                                 activebackground='#f5ae20', activeforeground='#33374d', command=lambda: back_menu())
            button_back.place(relx=0.25, rely=0.495, relwidth=0.5, relheight=0.073)

            file = open('users.txt', 'rb')
            user = pickle.load(file)
            file.close()
            if user[name]['score'] < scores[qns_asked_num - 1]:
                user[name]['score'] = scores[qns_asked_num - 1]
            file = open('users.txt', 'wb')
            pickle.dump(user, file)
            file.close()

            result_frame.mainloop()

        frame.mainloop()
        menu_frame.mainloop()

    def add_qn():
        global name, passw
        if name != 'Admin' or passw != 'mrd2003':
            messagebox.showwarning('Warning!', 'Only Admin can add question.')
        else:
            label.pack_forget()

            label2 = Label()
            label2.config(image=image3)
            label2.pack()

            label_score = Label(text='Score', font='Arial 14', bg='black', fg='white')
            label_score.place(relx=0.72, rely=0.1, relwidth=0.16, relheight=0.055)

            button_lvl1 = Button(font='Boulder 14', text='Level 1', bg='black', fg='white',
                                 activebackground='#1c6ab8', command=lambda: add_qn_lvl1())
            button_lvl1.place(relx=0.8, rely=0.2, relwidth=0.15, relheight=0.07)
            button_lvl2 = Button(font='Boulder 14', text='Level 2', bg='black', fg='white',
                                 activebackground='#1c6ab8', command=lambda: add_qn_lvl2())
            button_lvl2.place(relx=0.8, rely=0.3, relwidth=0.15, relheight=0.07)
            button_lvl3 = Button(font='Boulder 14', text='Level 3', bg='black', fg='white',
                                 activebackground='#1c6ab8', command=lambda: add_qn_lvl3())
            button_lvl3.place(relx=0.8, rely=0.4, relwidth=0.15, relheight=0.07)

            button_back = Button(font='Boulder 14', text='Back to menu', bg='black', fg='white',
                                 activebackground='#1c6ab8', command=lambda: back_menu())
            button_back.place(relx=0.05, rely=0.03, relwidth=0.18, relheight=0.07)

            entry_qn = Entry(font='Boulder 14', bg='grey', fg='black')
            entry_qn.place(relx=0.2, rely=0.55, relwidth=0.6, relheight=0.1)
            entry_var_a = Entry(font='Boulder 14', bg='grey', fg='black')
            entry_var_a.place(relx=0.17, rely=0.72, relwidth=0.29, relheight=0.07)
            entry_var_c = Entry(font='Boulder 14', bg='grey', fg='black')
            entry_var_c.place(relx=0.17, rely=0.83, relwidth=0.29, relheight=0.07)
            entry_var_b = Entry(font='Boulder 14', bg='grey', fg='black')
            entry_var_b.place(relx=0.585, rely=0.72, relwidth=0.29, relheight=0.07)
            entry_var_d = Entry(font='Boulder 14', bg='grey', fg='black')
            entry_var_d.place(relx=0.585, rely=0.83, relwidth=0.29, relheight=0.07)

            def back_menu():
                label2.pack_forget()
                image_menu()

            def add_qn_lvl1():
                global x
                x = dict_qns1['count']
                x += 1
                dict_qns1['count'] = x

                dict_qns1[x] = {'qn': entry_qn.get(), 'ans': entry_var_a.get(), 'var1': entry_var_b.get(),
                                'var2': entry_var_c.get(), 'var3': entry_var_d.get()}
                label2.pack_forget()
                add_qn()

                file = open('dict1.txt', 'wb')
                pickle.dump(dict_qns1, file)
                file.close()

            def add_qn_lvl2():
                global x
                x = dict_qns2['count']
                x += 1
                dict_qns2['count'] = x

                dict_qns2[x] = {'qn': entry_qn.get(), 'ans': entry_var_a.get(), 'var1': entry_var_b.get(),
                                'var2': entry_var_c.get(), 'var3': entry_var_d.get()}
                label2.pack_forget()
                add_qn()

                file = open('dict2.txt', 'wb')
                pickle.dump(dict_qns2, file)
                file.close()

            def add_qn_lvl3():

                x = dict_qns3['count']
                x += 1
                dict_qns3['count'] = x

                dict_qns3[x] = {'qn': entry_qn.get(), 'ans': entry_var_a.get(), 'var1': entry_var_b.get(),
                                'var2': entry_var_c.get(), 'var3': entry_var_d.get()}
                label2.pack_forget()
                add_qn()

                file = open('dict3.txt', 'wb')
                pickle.dump(dict_qns3, file)
                file.close()


WIDTH = 750
HEIGHT = 400

users = {}

window = Tk()

window.title('Who wants to be a millionaire?')
window.geometry(f'{WIDTH}x{HEIGHT}')
window.resizable(False, False)
window.config(bg='#76a3e3')

image1 = PhotoImage(file='img/img_b.ppm')
image2 = PhotoImage(file='img/menu_img.ppm')
image3 = PhotoImage(file='img/m_qn.ppm')
image4 = PhotoImage(file='img/result_1.ppm')
image_dict = {1: PhotoImage(file='img/Picture1.ppm'),
              2: PhotoImage(file='img/Picture2.ppm'),
              3: PhotoImage(file='img/Picture3.ppm'),
              4: PhotoImage(file='img/Picture4.ppm'),
              5: PhotoImage(file='img/Picture5.ppm'),
              6: PhotoImage(file='img/Picture6.ppm'),
              7: PhotoImage(file='img/Picture7.ppm'),
              8: PhotoImage(file='img/Picture8.ppm'),
              9: PhotoImage(file='img/Picture9.ppm'),
              10: PhotoImage(file='img/Picture10.ppm'),
              11: PhotoImage(file='img/Picture11.ppm'),
              12: PhotoImage(file='img/Picture12.ppm'),
              13: PhotoImage(file='img/Picture13.ppm'),
              14: PhotoImage(file='img/Picture14.ppm'),
              15: PhotoImage(file='img/Picture15.ppm')}

image_call = PhotoImage(file='img/call.ppm')
image_callX = PhotoImage(file='img/callX.ppm')
image_5050 = PhotoImage(file='img/50_50.ppm')
image_5050X = PhotoImage(file='img/50_50X.ppm')
image_audience = PhotoImage(file='img/audience.ppm')
image_audienceX = PhotoImage(file='img/audienceX.ppm')

scores = {0: 0, 1: 100, 2: 200, 3: 300, 4: 500, 5: 1000,
          6: 2000, 7: 4000, 8: 8000, 9: 16000, 10: 32000,
          11: 64000, 12: 125000, 13: 250000, 14: 500000, 15: 1000000}

sign()

window.mainloop()
