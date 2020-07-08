#necessary imports

import tkinter as tk
import tkinter.font as font
import webbrowser

#create lists for player-entered info
names = []
phrases = []

#function that creates title screen
def title_screen():
    #clear screen first
    for widget in window.winfo_children():
        widget.destroy()

    #what happens when buttons are clicked
    #clicking play button starts game
    def play_click(self):
        play_game()
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

#function that plays game
def play_game():
    
    #clear screen first
    for widget in window.winfo_children():
        widget.destroy()

    #what happens when buttons are clicked
    #clicking submit adds name + phrases to lists
    def submit_click(self):
        if len(names) >= 10:
            game_message["text"]="You already have 10 players."
        else:
            if name_entry.get() != "" and len(phrase_entry1.get().split()) <= 5 and phrase_entry1.get() != "" and len(phrase_entry2.get().split()) <= 5 and phrase_entry2.get() != "" and len(phrase_entry3.get().split()) <= 5 and phrase_entry3.get() != "":
                names.append(name_entry.get())
                phrases.append(phrase_entry1.get())
                phrases.append(phrase_entry2.get())
                phrases.append(phrase_entry3.get())
                game_message["text"]="Phrases submitted!"
                name_entry.delete(0, tk.END)
                phrase_entry1.delete(0, tk.END)
                phrase_entry2.delete(0, tk.END)
                phrase_entry3.delete(0, tk.END)

            elif len(phrase_entry1.get().split()) > 5 or phrase_entry1.get() == "" or len(phrase_entry2.get().split()) > 5 or phrase_entry2.get() == "" or len(phrase_entry3.get().split()) > 5 or phrase_entry3.get() == "":
                game_message["text"]="All phrases must be 1-5 words."
            elif name_entry.get() == "":
                game_message["text"]="You need to enter a name."
        print(names)
        print(phrases)
    def move_on_click(self):
        if len(names) == 6 or len(names) == 8 or len(names) == 10:
            game_message["text"]="You're ready to move on."
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



window = tk.Tk()
window.title("Charades Manager")
title_screen()
window.mainloop()