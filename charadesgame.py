#necessary imports

import tkinter as tk
import tkinter.font as font
import webbrowser
import random

#create lists for player-entered info
names = []
phrases_dictionary = {}
phrases_list = []
used_phrases = []
scores = []
current_phrase = ""
current_player = ""
current_player_num = 0
#function that creates title screen
def title_screen():
    #clear screen first
    for widget in window.winfo_children():
        widget.destroy()

    #what happens when buttons are clicked
    #clicking play button starts game
    def play_click(self):
        accept_inputs()
    #clicking rules button opens rules in pastebin
    def rules_click(self):
        webbrowser.open("https://pastebin.com/WPXtPBig")
    #clicking credits button opens credits
    def credits_click(self):
        credits_screen()

    #create widgets
    title = tk.Label(master=window, text="CHARADES", fg="#FFC0CB",)
    title["font"] = font.Font(size="36", weight="bold")
    fr_buttons = tk.Frame(master=window, bg="white")
    play_button = tk.Button(master=fr_buttons,text="Play")
    rules_button = tk.Button(master=fr_buttons,text="Rules")
    credits_button = tk.Button(master=fr_buttons,text="Credits")

    #place buttons in button frame
    play_button.grid(row="0", column="0", sticky="ew")
    rules_button.grid(row="1", column="0", sticky="ew")
    credits_button.grid(row="2", column="0", sticky="ew")

    #place all widgets
    title.grid(row="0", column="0")
    fr_buttons.grid(row="1", column="0")


    #bind buttons
    play_button.bind("<Button-1>", play_click)
    rules_button.bind("<Button-1>", rules_click)  
    credits_button.bind("<Button-1>", credits_click)

#function that creates credits screen
def credits_screen():
    #clear screen first
    for widget in window.winfo_children():
        widget.destroy()
        
    #what happens when buttons are clicked
    #clicking home button returns to home
    def home_click(self):
        title_screen()

    #create widgets
    credits_label = tk.Label(master=window,text="Credits",fg="#FFC0CB")
    credits_label["font"] = font.Font(size="24", weight="bold")
    credits_text = tk.Label(master=window, text="Coding: Raymond Goslow\nTimer: Ostcrom\nRules: Carson Claud\n\nFor IS3020 Summer 2020\nKennesaw State University")
    home_button = tk.Button(master=window,text="Back")
    #place all widgets
    credits_label.pack()
    credits_text.pack()
    home_button.pack()

    #bind buttons
    home_button.bind("<Button-1>", home_click)

#function that starts game by allowing players to input names and phrases
def accept_inputs():
    
    #clear screen first
    for widget in window.winfo_children():
        widget.destroy()

    #what happens when buttons are clicked
    #clicking submit adds name + phrases to lists
    def submit_click(self):
        if len(names) >= 10:
            game_message["text"]="You already have 10 players."
        else:
            if name_entry.get() in names:
                game_message["text"]="Someone else is using that name."
            elif phrase_entry1.get() in phrases_dictionary or phrase_entry2.get() in phrases_dictionary or phrase_entry3.get() in phrases_dictionary:
                game_message["text"]="One of those phrases already exists."
            elif phrase_entry1.get() == phrase_entry2.get() or phrase_entry3.get() == phrase_entry1.get() or phrase_entry2.get() == phrase_entry3.get():
                game_message["text"]="You can't use the same phrase twice."
            else: 
                if name_entry.get() != "" and len(phrase_entry1.get().split()) <= 5 and phrase_entry1.get() != "" and len(phrase_entry2.get().split()) <= 5 and phrase_entry2.get() != "" and len(phrase_entry3.get().split()) <= 5 and phrase_entry3.get() != "":
                    names.append(name_entry.get())
                    phrases_dictionary[phrase_entry1.get()] = name_entry.get()
                    phrases_dictionary[phrase_entry2.get()] = name_entry.get()
                    phrases_dictionary[phrase_entry3.get()] = name_entry.get()
                    game_message["text"]="Phrases submitted!"
                    name_entry.delete(0, tk.END)
                    phrase_entry1.delete(0, tk.END)
                    phrase_entry2.delete(0, tk.END)
                    phrase_entry3.delete(0, tk.END)
                elif len(phrase_entry1.get().split()) > 5 or phrase_entry1.get() == "" or len(phrase_entry2.get().split()) > 5 or phrase_entry2.get() == "" or len(phrase_entry3.get().split()) > 5 or phrase_entry3.get() == "":
                    game_message["text"]="All phrases must be 1-5 words."
                elif name_entry.get() == "":
                    game_message["text"]="You need to enter a name."
    def move_on_click(self):
        if len(names) == 6 or len(names) == 8 or len(names) == 10:
            play_game()
        else:
            game_message["text"]="You need more players."
    #create widgets
    game_label = tk.Label(master=window, text="Enter Information")
    game_message = tk.Label(master=window,text="")
    fr_entry = tk.Frame(master=window, bg="white")
    name_label = tk.Label(master=fr_entry, text="Name:")
    name_entry = tk.Entry(master=fr_entry)
    phrase_label1 = tk.Label(master=fr_entry, text="Secret Phrase:")
    phrase_label2 = tk.Label(master=fr_entry, text="Secret Phrase:")
    phrase_label3 = tk.Label(master=fr_entry, text="Secret Phrase:")
    phrase_entry1 = tk.Entry(master=fr_entry)
    phrase_entry2 = tk.Entry(master=fr_entry)
    phrase_entry3 = tk.Entry(master=fr_entry)
    submit_button = tk.Button(master=window, text="Submit")
    move_on_button = tk.Button(master=window, text="Move On")
    #place entry widgets in entry frame
    name_label.grid(row="0", column="0", sticky="e")
    name_entry.grid(row="0", column="1")
    phrase_label1.grid(row="1",column="0", sticky="e")
    phrase_entry1.grid(row="1", column="1", sticky="w")
    phrase_label2.grid(row="2",column="0", sticky="e")
    phrase_entry2.grid(row="2", column="1", sticky="w")
    phrase_label3.grid(row="3",column="0", sticky="e")
    phrase_entry3.grid(row="3", column="1", sticky="w")
    #place all widgets
    game_label.grid(row="0", column="0",columnspan="2")
    fr_entry.grid(row="1", column="0",columnspan="2")
    game_message.grid(row="2", column="0",columnspan="2")
    submit_button.grid(row="3", column="0")
    move_on_button.grid(row="3",column="1")
    #bind button
    submit_button.bind("<Button-1>", submit_click)
    move_on_button.bind("<Button-1>",move_on_click)

def play_game():
    #clear screen first
    for widget in window.winfo_children():
        widget.destroy()

    
    #create 0 scores for number of players
    for x in range(0,len(names)):
        scores.append(0)
    #create phrase list
    for x in phrases_dictionary:
        phrases_list.append(x)
    #start with first player
    current_player = names[current_player_num]
    #choose random phrase to start
    current_phrase = "Click Pass to begin"


    #what happens when buttons are clicked
    def correct_click(self):
        global current_phrase
        global current_player_num
        global current_player
        global scores
        used_phrases.append(current_phrase)
        phrases_list.remove(current_phrase)
        scores[current_player_num] += 1
        if phrases_list:
            current_phrase = random.choice(phrases_list)
            phrase_widget["text"] = current_phrase
        else:
            results_screen()
        if current_player_num == (len(names) - 1):
            current_player_num = 0
        else:
            current_player_num +=1
        current_player = names[current_player_num]
        player_widget["text"] = current_player
    def pass_click(self):
        global current_phrase
        global current_player_num
        global current_player
        current_phrase = random.choice(phrases_list)
        phrase_widget["text"] = current_phrase
        if current_player_num == (len(names) - 1):
            current_player_num = 0
        else:
            current_player_num +=1
        current_player = names[current_player_num]
        player_widget["text"] = current_player
    #create widgets
    phrase_widget = tk.Label(master=window,text=current_phrase)
    timer_widget = tk.Label(master=window,text="")
    player_widget = tk.Label(master=window,text="")
    correct_button = tk.Button(master=window, text="Correct")
    pass_button = tk.Button(master=window, text = "Pass")
    #place widgets
    phrase_widget.grid(row="0",column="0", columnspan="2")
    timer_widget.grid(row="1",column="0", columnspan="2")
    player_widget.grid(row="2",column="0", columnspan="2")
    correct_button.grid(row="3",column="0")
    pass_button.grid(row="3",column="1")

    #bind button
    correct_button.bind("<Button-1>", correct_click)
    pass_button.bind("<Button-1>",pass_click)

def results_screen():
    #clear screen first
    for widget in window.winfo_children():
        widget.destroy()

    def home_click(self):
        names = []
        phrases_dictionary = {}
        phrases_list = []
        used_phrases = []
        scores = []
        current_phrase = ""
        current_player = ""
        current_player_num = 0
        title_screen()
    for num in range(0,int(len(names)/2)):
        team_names = names[num],"and",names[num+int(len(names)/2)]
        team_score = scores[num] + scores[num+int(len(names)/2)]
        team_names_widget = tk.Label(master=window, text=team_names)
        team_score_widget = tk.Label(master=window, text=team_score)
        team_names_widget.pack()
        team_score_widget.pack()
    home_button = tk.Button(master=window,text="Home")
    home_button.pack()

    #bind buttons
    home_button.bind("<Button-1>", home_click)

window = tk.Tk()
window.title("Charades Manager")
title_screen()
window.mainloop()