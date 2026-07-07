from tkinter import *
import random
import pickle
from tkinter import messagebox


# ToDo: Debug from 'Image Between'
"""
How the game works:

1. All files of questions are read.
2. Tk window is created.
3. 'Sign' frame:
    a. 'Sign Up' frame
        1) Check
        2) Save
        3) Image Between ...
    b. 'Sign In' frame
        1) Check
        2) Image Between ...

... Image Between


Notes:
1. User data type is of the form: {'Admin': {'passw': 'mrd2003', 'score': 0}}
2. username, passw1, passw2 --> used for check up
   username, passw --> used for check in
   name, password --> used for the present account

"""

# READING ALL DICTIONARY QUESTIONS

with open("dict1.txt", "rb") as pickled_lvl1:
    dict_qns1 = pickle.load(pickled_lvl1)

with open("dict2.txt", "rb") as pickled_lvl2:
    dict_qns2 = pickle.load(pickled_lvl2)

with open("dict3.txt", "rb") as pickled_lvl3:
    dict_qns3 = pickle.load(pickled_lvl3)

global name, password
global qn_str, varA, varB, varC, varD, lvl, ans, qn, dct, x, qns_asked_num, asked_qns


def sign():
    frame_sign = Frame()

    button_signup = Button(
        window,
        font="Arial",
        text="Sign Up",
        command=sign_up,
        bg="#5179b5",
        fg="white",
        activebackground="#1d437a",
    )
    button_signup.place(relx=0.2, rely=0.1, relwidth=0.3, relheight=0.1)

    button_signin = Button(
        window,
        font="Arial",
        text="Sign In",
        command=sign_in,
        bg="#5179b5",
        fg="white",
        activebackground="#1d437a",
    )
    button_signin.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.1)
    frame_sign.mainloop()


def sign_up():
    """
    Creates interface of 'sign up'.

    Frame:
        1. labels: name, passw1, passw2
        2. entries: name, passw1, passw2
        3. button: continue
    """

    # Frame - labels, entries and buttons are located in the frame
    frame = Frame(window, bd=10)
    frame.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.6)

    # labels: name, passw1, passw2
    label = Label(frame, text="SIGN UP", font="Arial 16 bold")
    label.place(relwidth=1, relheight=0.1)

    label_name = Label(frame, text="Enter your name:", font="16")
    label_name.place(relx=0.1, rely=0.2, relwidth=0.4, relheight=0.1)

    label_password1 = Label(frame, text="Enter password:", font="16")
    label_password1.place(relx=0.1, rely=0.4, relwidth=0.4, relheight=0.1)

    label_password2 = Label(frame, text="Confirm password:", font="16")
    label_password2.place(relx=0.1, rely=0.6, relwidth=0.4, relheight=0.1)

    # entries: name, passw1, passw2
    entry_name = Entry(frame, font="Arial", bd=3)
    entry_name.place(relx=0.5, rely=0.2, relwidth=0.4, relheight=0.1)

    entry_password1 = Entry(frame, font="Arial", bd=3, show="*")
    entry_password1.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.1)

    entry_password2 = Entry(frame, font="Arial", bd=3, show="*")
    entry_password2.place(relx=0.5, rely=0.6, relwidth=0.4, relheight=0.1)

    # button: continue
    button_continue = Button(
        frame,
        font="Arial",
        text="Continue",
        bg="#c6daf5",
        activebackground="#8797ad",
        command=lambda: check_up(
            label, entry_name.get(), entry_password1.get(), entry_password2.get()
        ),
    )
    button_continue.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.2)


def check_up(label, username, passw1, passw2):
    """
    Tests password of 'sign up' and prints errors, if any;
    Defines the name and password of the current player.

    label_error will be on the label (which is passed as a parameter) of 'sign up'

    """

    global name, password

    label_error = Label(label, fg="#eb0c0c")
    label_error.place(rely=0.7)

    if len(username) == 0:
        label_error.config(text="*login error")

    elif len(passw1) == 0 or len(passw2) == 0:
        label_error.config(text="*password error")

    elif not 6 <= len(passw1) <= 14:
        label_error.config(
            text="*your password needs to be between 6 and 14 characters"
        )

    elif passw1 != passw2:
        label_error.config(text="*password error")

    else:
        label_error.config(text="not any errors")

        save(username, passw1)
        name, password = username, passw1
        image_between()


def save(username, passw1):
    """
    Adds and saves username and pass into 'users.txt'

    User is a dictionary of the following form:
    print(user) --> {'Admin': {'passw': 'mrd2003', 'score': 0}, ...}
    """

    with open("users.txt", "rb") as file:
        user = pickle.load(file)

    user[username] = {"passw": passw1, "score": 0}

    with open("users.txt", "wb") as file:
        pickle.dump(user, file)


def sign_in():
    """
    Creates interface of 'sign in'.

    Frame:
        1. labels: name, passw
        2. entries: name, passw
        3. button: continue
    """

    frame = Frame(window, bd=10)
    frame.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.6)

    # labels, entries, and 'continue' button
    label = Label(frame, text="SIGN IN", font="Arial 16 bold")
    label.place(relwidth=1, relheight=0.1)

    label_name = Label(frame, text="Enter your name:", font="16")
    label_name.place(relx=0.1, rely=0.2, relwidth=0.4, relheight=0.1)

    label_password = Label(frame, text="Enter password:", font="16")
    label_password.place(relx=0.1, rely=0.4, relwidth=0.4, relheight=0.1)

    entry_name = Entry(frame, font="Arial", bd=3)
    entry_name.place(relx=0.5, rely=0.2, relwidth=0.4, relheight=0.1)

    entry_password = Entry(frame, font="Arial", bd=3, show="*")
    entry_password.place(relx=0.5, rely=0.4, relwidth=0.4, relheight=0.1)

    button_continue = Button(
        frame,
        font="Arial",
        text="Continue",
        command=lambda: check_in(label, entry_name.get(), entry_password.get()),
        bg="#c6daf5",
        activebackground="#8797ad",
    )
    button_continue.place(relx=0.2, rely=0.8, relwidth=0.6, relheight=0.2)


def check_in(label, username, passw):
    """
    Tests password of 'sign in' and prints errors, if any;
    Defines the name and password of the current player.

    label_error will be on the label (which is passed as a parameter) of 'sign in'
    """
    global name, password

    with open("users.txt", "rb") as file:
        u = pickle.load(file)

    label_error = Label(label, fg="#eb0c0c")
    label_error.place(rely=0.7)

    if len(username) == 0:
        label_error.config(text="*login error")

    elif len(passw) == 0:
        label_error.config(text="*password error")

    elif username in u and passw == u[username]["passw"]:
        name, password = username, passw
        image_between()
    else:
        messagebox.showerror("Error", "Invalid login or password")


# ToDo: Countdown


def image_between():
    def countdown(count):
        if count > 0:
            frame.after(1000, countdown, count - 1)
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
    label = Label(image=image2)
    # label.config(image=image2)
    label.pack()

    label_top5 = Label(text="", bg="#1c1154", fg="gold", font="Arial 14 bold")
    label_top5.place(relx=0.75, rely=0.03, relwidth=0.24, relheight=0.5)

    show_top(label_top5)

    button_play = Button(
        font="Boilder 14",
        text="PLAY",
        fg="white",
        command=lambda: image_qns(menu_frame, label),
        bg="#eb9710",
        activebackground="#eb9710",
        activeforeground="#031145",
    )
    button_play.place(relx=0.25, rely=0.69, relwidth=0.52, relheight=0.08)

    button_add = Button(
        font="Boilder 12",
        text="ADD QUESTION",
        fg="white",
        command=lambda: add_qn_frame(label),
        bg="#031145",
        activebackground="#031145",
        activeforeground="#eb9710",
        state=ACTIVE,
    )
    button_add.place(relx=0.25, rely=0.8, relwidth=0.52, relheight=0.07)


# Todo: dct -> dct_
def show_top(label_top5):
    with open("users.txt", "rb") as file:
        dct_ = pickle.load(file)

    lst_n = list(dct_.keys())
    lst_s = list()

    for i in lst_n:
        lst_s.append(dct_[i]["score"])

    print(lst_n)  # List of names
    print(lst_s)  # List of scores

    def sort_scores(a, b):
        for j in range(len(lst_n)):
            max_score = max(b[j:])
            index = b[j:].index(max_score) + j
            if index != j:
                a[j], a[index] = a[index], a[j]
                b[j], b[index] = b[index], b[j]

    sort_scores(lst_n, lst_s)

    txt = []
    for i in range(len(lst_s)):
        txt.append(f"{i + 1}. {lst_n[i]} - {lst_s[i]}")
        print(f"{i + 1}. {lst_n[i]} - {lst_s[i]}")

    # Todo: use None type instead of predefined users
    # Initially: Admin: mrd2003, User1: user12003, User2: user22003, User3: user32003, User4: user42003
    label_top5.config(
        text=f"TOP 5:\n{txt[0]}$\n{txt[1]}$\n{txt[2]}$\n{txt[3]}$\n{txt[4]}$"
    )


class Answer:
    def __init__(self, variant, x, y, width, height):
        self.variant = variant
        self.x, self.y, self.width, self.height = x, y, width, height
        self.button = Button(
            font="Boulder 14",
            text=self.variant,
            bg="black",
            fg="white",
            activebackground="#1c6ab8",
            command=lambda: Answer.check,
        )
        self.button.place(
            relx=self.x, rely=self.y, relwidth=self.width, relheight=self.height
        )

    def check(self):
        if self.button.cget("text") == dct[qn]["ans"]:
            self.button.config(bg="green", fg="black", state=DISABLED)
        else:
            self.button.config(bg="red", state=DISABLED)


def image_qns(menu_frame, label):
    global qns_asked_num, asked_qns
    label.pack_forget()
    frame = Frame()

    label2 = Label()
    label2.config(image=image3)
    label2.pack()

    qns_asked_num = 0
    asked_qns = []

    ask(frame, label, label2)

    # JOKER BUTTONS

    # Call Joker
    button_call = Button(
        font="Boulder 14",
        image=image_call,
        bg="black",
        fg="white",
        activebackground="#1c6ab8",
        command=lambda: joker(
            button_call,
            image_callX,
            f"Hello. ... ...\nHm... That's a tricky one..\nLemme think.\n"
            f"I think answer is..\n'{dct[qn]['ans']}'",
        ),
    )
    button_call.place(relx=0.23, rely=0.02, relwidth=0.08, relheight=0.15)

    # Eliminate 2 variants
    button_5050 = Button(
        font="Boulder 14",
        image=image_5050,
        bg="black",
        fg="white",
        activebackground="#1c6ab8",
        command=lambda: joker(
            button_5050,
            image_5050X,
            f"Variant 1 is ..\n '{dct[qn]['var1']}'\n"
            f"Variant 2 is ..\n '{dct[qn]['ans']}'\n"
            f"Only one correct...",
        ),
    )
    button_5050.place(relx=0.23, rely=0.19, relwidth=0.08, relheight=0.15)

    # Ask the audience
    button_audience = Button(
        font="Boulder 14",
        image=image_audience,
        bg="black",
        fg="white",
        activebackground="#1c6ab8",
        command=lambda: joker(button_audience, image_audienceX, ans),
    )
    button_audience.place(relx=0.23, rely=0.36, relwidth=0.08, relheight=0.15)

    frame.mainloop()
    menu_frame.mainloop()


# Asks new question
def ask(frame, label, label2):
    print("asks")
    global qn_str, varA, varB, varC, varD, lvl, ans, qn, dct, qns_asked_num
    qns_asked_num += 1

    if qns_asked_num <= 5:
        with open("dict1.txt", "rb") as file:
            dct = pickle.load(file)

    elif 6 <= qns_asked_num <= 10:
        with open("dict2.txt", "rb") as file:
            dct = pickle.load(file)

    elif 11 <= qns_asked_num <= 15:
        with open("dict3.txt", "rb") as file:
            dct = pickle.load(file)

    count_add = dct["count"]
    qn = random.randint(1, count_add)  # question number
    qn_str = dct[qn]["qn"]

    if qn_str in asked_qns:
        qns_asked_num -= 1
        ask(frame, label, label2)
    else:
        asked_qns.append(qn_str)
        list_sq = [dct[qn]["ans"], dct[qn]["var1"], dct[qn]["var2"], dct[qn]["var3"]]

        random.shuffle(list_sq)
        varA = list_sq[0]
        varB = list_sq[1]
        varC = list_sq[2]
        varD = list_sq[3]
        print(dct[qn]["qn"], list_sq[0], list_sq[1], list_sq[2], list_sq[3])

    # SCORES
    image_sb = image_dict[qns_asked_num]
    label_sb = Label(
        text=scores[qns_asked_num],
        font="Arial 14",
        bg="black",
        fg="white",
        image=image_sb,
    )
    label_sb.place(relx=0.02, rely=0.02, relwidth=0.2, relheight=0.5)

    label_score = Label(
        text=f"{scores[qns_asked_num]} $", font="Arial 14", bg="black", fg="white"
    )
    label_score.place(relx=0.72, rely=0.1, relwidth=0.16, relheight=0.055)

    # QUESTION + VARIANTS
    label_qn = Label(font="Boulder 14", text=qn_str, bg="black", fg="white")
    label_qn.place(relx=0.2, rely=0.55, relwidth=0.6, relheight=0.1)

    button_var_a = Button(
        font="Boulder 14",
        text=varA,
        bg="black",
        fg="white",
        activebackground="#1c6ab8",
        command=lambda: check_answer(
            button_var_a, button_var_b, button_var_c, button_var_d, button_pass
        ),
    )
    button_var_a.place(relx=0.17, rely=0.72, relwidth=0.29, relheight=0.07)

    button_var_b = Button(
        font="Boulder 14",
        text=varB,
        bg="black",
        fg="white",
        activebackground="#1c6ab8",
        command=lambda: check_answer(
            button_var_b, button_var_a, button_var_c, button_var_d, button_pass
        ),
    )
    button_var_b.place(relx=0.585, rely=0.72, relwidth=0.29, relheight=0.07)

    button_var_c = Button(
        font="Boulder 14",
        text=varC,
        bg="black",
        fg="white",
        activebackground="#1c6ab8",
        command=lambda: check_answer(
            button_var_c, button_var_a, button_var_b, button_var_d, button_pass
        ),
    )
    button_var_c.place(relx=0.17, rely=0.83, relwidth=0.29, relheight=0.07)

    button_var_d = Button(
        font="Boulder 14",
        text=varD,
        bg="black",
        fg="white",
        activebackground="#1c6ab8",
        command=lambda: check_answer(
            button_var_d, button_var_a, button_var_b, button_var_c, button_pass
        ),
    )
    button_var_d.place(relx=0.585, rely=0.83, relwidth=0.29, relheight=0.07)

    button_pass = Button(
        font="Boulder 14",
        text="Continue",
        bg="black",
        fg="white",
        activebackground="#1c6ab8",
        state=DISABLED,
        command=lambda: ask(frame, label, label2),
    )
    button_pass.place(relx=0.7, rely=0.4, relwidth=0.25, relheight=0.07)

    if qns_asked_num == 15:
        button_pass.config(text="Finish", command=lambda: result(label2, qns_asked_num))

    # TIMER FOR QUESTIONS
    label_time = Label(text="Timer", bg="black", fg="white")
    label_time.place(relx=0.45, rely=0.48, relwidth=0.1, relheight=0.05)

    def count_time(sec):
        if sec >= 0:
            label_time.config(text=sec)
            label_time.after(1000, count_time, sec - 1)
        elif label != ".!label2":
            print("Done")
            return
        else:
            print(label)
            print(type(label))
            label.pack_forget()
            result(label2, qns_asked_num)

    count_time(10)

    # COUNTDOWN
    def countdown(count):
        if count > 0:
            frame.after(1000, countdown, count - 1)
            frame.mainloop()
        else:
            label.pack_forget()
            result(label2, qns_asked_num)

    # TODO
    # CHECKING ANSWER
    def check_answer(answer, other1, other2, other3, pass_):
        if answer.cget("text") == dct[qn]["ans"]:
            answer.config(bg="green", fg="black", state=DISABLED)
            other1.config(state=DISABLED)
            other2.config(state=DISABLED)
            other3.config(state=DISABLED)
            pass_.config(state=ACTIVE)

        else:
            answer.config(bg="red", state=DISABLED)
            other1.config(state=DISABLED)
            other2.config(state=DISABLED)
            other3.config(state=DISABLED)
            pass_.config(state=DISABLED)
            # TODO: the following function
            countdown(2)

    # FOR JOKER
    var1 = random.randint(70, 100)
    var2 = random.randint(0, 100 - var1)
    var3 = random.randint(0, 100 - var1 - var2)
    var4 = random.randint(0, 100 - var1 - var2 - var3)
    ans = (
        f"'{dct[qn]['ans']}' -- {var1}%\n"
        f"'{dct[qn]['var1']}' -- {var2}%\n"
        f"'{dct[qn]['var2']}' -- {var3}%\n"
        f"'{dct[qn]['var3']}' -- {var4}%\n"
    )


# JOKER ANSWERS
def joker(button_call, image, text):
    button_call.config(image=image, state=DISABLED)
    label_ans = Label(text=text, font="Boulder 14", bg="black", fg="white")
    label_ans.place(relx=0.35, rely=0.02, relwidth=0.3, relheight=0.45)
    label_ans.after(5000, lambda: label_ans.destroy())


# RESULTS
def result(label2, qns_asked_num):
    global name

    def back_menu():
        label3.pack_forget()
        image_menu()

    label2.pack_forget()

    result_frame = Frame()

    label3 = Label()
    label3.config(image=image4)
    label3.pack()

    label4 = Label(
        font="Boulder 16 bold",
        text=f"CONGRATULATIONS!!!\nYOU WON {scores[qns_asked_num - 1]}$ DOLLARS.",
        bg="#1a2047",
        fg="white",
    )
    label4.place(relx=0.24, rely=0.25, relwidth=0.52, relheight=0.2)

    button_back = Button(
        font="Arial 14 bold",
        text="BACK TO MENU",
        bg="#f5ae20",
        activebackground="#f5ae20",
        activeforeground="#33374d",
        command=lambda: back_menu(),
    )
    button_back.place(relx=0.25, rely=0.495, relwidth=0.5, relheight=0.073)

    with open("users.txt", "rb") as file:
        user = pickle.load(file)

    if user[name]["score"] < scores[qns_asked_num - 1]:
        user[name]["score"] = scores[qns_asked_num - 1]

    with open("users.txt", "wb") as file:
        pickle.dump(user, file)

    result_frame.mainloop()


def add_qn_frame(label):
    global name, password

    def back_menu():
        label2.pack_forget()
        image_menu()

    if name != "Admin" or password != "mrd2003":
        messagebox.showwarning("Warning!", "Only Admin can add question.")
    else:
        label.pack_forget()

        label2 = Label()
        label2.config(image=image3)
        label2.pack()

        label_score = Label(text="Score", font="Arial 14", bg="black", fg="white")
        label_score.place(relx=0.72, rely=0.1, relwidth=0.16, relheight=0.055)

        # ToDo: define a universal function
        def create_and_place_button(
            font, text, bg, fg, actvbg, cmd, relx, rely, relw, relh
        ):
            button = Button(
                font=font,
                text=text,
                bg=bg,
                fg=fg,
                activebackground=actvbg,
                command=lambda: cmd,
            )
            button.place(relx=relx, rely=rely, relwidth=relw, relheight=relh)

        # create_and_place_button('Boulder 14', 'Level 1', 'black', 'white', '#1c6ab8', add_qn(dict_qns1, 'dict1.txt'),
        #                         0.8, 0.2, 0.15, 0.07)

        button_lvl1 = Button(
            font="Boulder 14",
            text="Level 1",
            bg="black",
            fg="white",
            activebackground="#1c6ab8",
            command=lambda: add_qn(dict_qns1, "dict1.txt"),
        )
        button_lvl1.place(relx=0.8, rely=0.2, relwidth=0.15, relheight=0.07)
        button_lvl2 = Button(
            font="Boulder 14",
            text="Level 2",
            bg="black",
            fg="white",
            activebackground="#1c6ab8",
            command=lambda: add_qn(dict_qns2, "dict2.txt"),
        )
        button_lvl2.place(relx=0.8, rely=0.3, relwidth=0.15, relheight=0.07)
        button_lvl3 = Button(
            font="Boulder 14",
            text="Level 3",
            bg="black",
            fg="white",
            activebackground="#1c6ab8",
            command=lambda: add_qn(dict_qns3, "dict3.txt"),
        )
        button_lvl3.place(relx=0.8, rely=0.4, relwidth=0.15, relheight=0.07)

        button_back = Button(
            font="Boulder 14",
            text="Back to menu",
            bg="black",
            fg="white",
            activebackground="#1c6ab8",
            command=lambda: back_menu(),
        )
        button_back.place(relx=0.05, rely=0.03, relwidth=0.18, relheight=0.07)

        entry_qn = Entry(font="Boulder 14", bg="grey", fg="black")
        entry_qn.place(relx=0.2, rely=0.55, relwidth=0.6, relheight=0.1)

        entry_var_a = Entry(font="Boulder 14", bg="grey", fg="black")
        entry_var_a.place(relx=0.17, rely=0.72, relwidth=0.29, relheight=0.07)
        entry_var_c = Entry(font="Boulder 14", bg="grey", fg="black")
        entry_var_c.place(relx=0.17, rely=0.83, relwidth=0.29, relheight=0.07)

        entry_var_b = Entry(font="Boulder 14", bg="grey", fg="black")
        entry_var_b.place(relx=0.585, rely=0.72, relwidth=0.29, relheight=0.07)
        entry_var_d = Entry(font="Boulder 14", bg="grey", fg="black")
        entry_var_d.place(relx=0.585, rely=0.83, relwidth=0.29, relheight=0.07)

        def add_qn(dict_qns, filename):
            global x

            x = dict_qns["count"]
            x += 1
            dict_qns["count"] = x

            dict_qns[x] = {
                "qn": entry_qn.get(),
                "ans": entry_var_a.get(),
                "var1": entry_var_b.get(),
                "var2": entry_var_c.get(),
                "var3": entry_var_d.get(),
            }
            label2.pack_forget()
            # ToDO: Which label should i use? --- images file
            add_qn_frame(label2)

            with open(filename, "wb") as file:
                pickle.dump(dict_qns, file)


WIDTH = 750
HEIGHT = 400

window = Tk()

window.title("Who wants to be a millionaire?")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(False, False)
window.config(bg="#76a3e3")


# Converted all images into .ppm

image1 = PhotoImage(file="img/img_b.ppm")
image2 = PhotoImage(file="img/menu_img.ppm")
image3 = PhotoImage(file="img/m_qn.ppm")
image4 = PhotoImage(file="img/result_1.ppm")

image_dict = {}

for i in range(1, 16):
    ppm_file_name = f"img/Picture{i}.ppm"
    image_dict[i] = PhotoImage(file=ppm_file_name)

scores = {
    0: 0,
    1: 100,
    2: 200,
    3: 300,
    4: 500,
    5: 1000,
    6: 2000,
    7: 4000,
    8: 8000,
    9: 16000,
    10: 32000,
    11: 64000,
    12: 125000,
    13: 250000,
    14: 500000,
    15: 1000000,
}

image_call = PhotoImage(file="img/call.ppm")
image_callX = PhotoImage(file="img/callX.ppm")
image_5050 = PhotoImage(file="img/50_50.ppm")
image_5050X = PhotoImage(file="img/50_50X.ppm")
image_audience = PhotoImage(file="img/audience.ppm")
image_audienceX = PhotoImage(file="img/audienceX.ppm")

sign()

window.mainloop()
