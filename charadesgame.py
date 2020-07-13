#necessary imports

import tkinter as tk
import tkinter.font as font
from tkinter.filedialog import asksaveasfilename
import webbrowser
import random
import tktimerwidget

#create variables/lists for
names = []
phrases_list = []
used_phrases = []
scores = []
current_phrase = ""
current_player = ""
current_player_num = 0
round_counter = 1

#function that clears screen when moving to new screen
def clear_screen():
    for widget in window.winfo_children():
        widget.destroy()

#function that creates title screen
def title_screen():
    #clear screen first
    clear_screen()

    #reset variables for a new game
    global names
    global phrases_list
    global used_phrases
    global scores
    global current_phrase
    global current_player
    global current_player_num
    global round_counter
    names = []
    phrases_list = []
    used_phrases = []
    scores = []
    current_phrase = ""
    current_player = ""
    current_player_num = 0
    round_counter = 1

    #what happens when buttons are clicked
    #clicking play button starts game
    def play_click(self):
        accept_inputs()
    #clicking rules button opens rules webpage
    def rules_click(self):
        webbrowser.open("http://studentweb.kennesaw.edu/~rgoslow/charades.html")
    #clicking credits button opens credits page
    def credits_click(self):
        credits_screen()

    #create widgets
    title = tk.Label(master=window, text="CHARADES", fg="#FFC0CB", bg="#42F548", height="1", font="Impact 60 bold")
        #this frame contains the buttons
    fr_buttons = tk.Frame(master=window, pady="75")
    play_button = tk.Button(master=fr_buttons,text="Play", font="sans-serif 30 bold", fg="#FFFFFF", bg="#000000")
    rules_button = tk.Button(master=fr_buttons,text="Rules", font="sans-serif 30 bold", fg="#FFFFFF", bg="#000000")
    credits_button = tk.Button(master=fr_buttons,text="Credits", font="sans-serif 30 bold", fg="#FFFFFF", bg="#000000")
    

    #place buttons in button frame
    play_button.grid(row="0", column="1", sticky="ew")
    rules_button.grid(row="0", column="0", sticky="ew")
    credits_button.grid(row="0", column="2", sticky="ew")

    #place all widgets
    title.pack(fill=tk.X)
    fr_buttons.pack()

    #bind buttons
    play_button.bind("<Button-1>", play_click)
    rules_button.bind("<Button-1>", rules_click)  
    credits_button.bind("<Button-1>", credits_click)

#function that creates credits screen
def credits_screen():
    #clear screen first
    clear_screen()
        
    #what happens when buttons are clicked
    #clicking home button returns to home
    def home_click(self):
        title_screen()

    #create widgets
    credits_label = tk.Label(master=window,text="Credits",fg="#FFC0CB", bg="#42F548", height="1", font="Impact 60 bold")
    credits_text = tk.Label(master=window, text="Coding: Raymond Goslow\nTimer: Ostcrom\nRules: Carson Claud\n\nFor IS3020 Summer 2020\nKennesaw State University", font="sans-serif 15 bold")
    home_button = tk.Button(master=window,text="Back", font="sans-serif 15 bold", fg="#FFFFFF", bg="#000000")
    
    #place all widgets
    credits_label.pack(fill=tk.X)
    credits_text.pack()
    home_button.pack()

    #bind buttons
    home_button.bind("<Button-1>", home_click)

#function that starts game by allowing players to input names and phrases
def accept_inputs():
    #clear screen first
    clear_screen()

    #what happens when buttons are clicked
    #clicking submit adds name + phrases to lists
    def submit_click(self):
        #don't allow more than 10 players
        if len(names) >= 10:
            game_message["text"]="You already have 10 players."
        else:
            #don't allow duplicate names
            if name_entry.get() in names:
                game_message["text"]="Someone else is using that name."
            #don't allow duplicating other players' phrases
            elif phrase_entry1.get() in phrases_list or phrase_entry2.get() in phrases_list or phrase_entry3.get() in phrases_list:
                game_message["text"]="One of those phrases already exists."
            #don't allow duplicating your own phrase
            elif phrase_entry1.get() == phrase_entry2.get() or phrase_entry3.get() == phrase_entry1.get() or phrase_entry2.get() == phrase_entry3.get():
                game_message["text"]="You can't use the same phrase twice."
            else: 
                #if all conditions are met, add phrases and name to lists
                if name_entry.get() != "" and len(phrase_entry1.get().split()) <= 5 and phrase_entry1.get() != "" and len(phrase_entry2.get().split()) <= 5 and phrase_entry2.get() != "" and len(phrase_entry3.get().split()) <= 5 and phrase_entry3.get() != "":
                    names.append(name_entry.get())
                    phrases_list.append(phrase_entry1.get()) 
                    phrases_list.append(phrase_entry2.get())
                    phrases_list.append(phrase_entry3.get())
                    game_message["text"]="Phrases submitted!"
                    #clear for next player
                    name_entry.delete(0, tk.END)
                    phrase_entry1.delete(0, tk.END)
                    phrase_entry2.delete(0, tk.END)
                    phrase_entry3.delete(0, tk.END)
                #don't allow blank phrase or >5 word phrases
                elif len(phrase_entry1.get().split()) > 5 or phrase_entry1.get() == "" or len(phrase_entry2.get().split()) > 5 or phrase_entry2.get() == "" or len(phrase_entry3.get().split()) > 5 or phrase_entry3.get() == "":
                    game_message["text"]="All phrases must be 1-5 words."
                #force entering a name
                elif name_entry.get() == "":
                    game_message["text"]="You need to enter a name."
    def move_on_click(self):
        #only allow moving on if there are 6, 8 or 10 players
        if len(names) == 6 or len(names) == 8 or len(names) == 10:
            #circumvent pass glitch by moving current_player_num back by 1
            global current_player_num
            current_player_num = len(names) - 1
            play_game()
        else:
            game_message["text"]="You need more players."
            
    #create widgets
    game_label = tk.Label(master=window, text="Enter Information", fg="#FFC0CB", bg="#42F548", height="1", font="Impact 36 bold")
        #game message changes to give player context
    game_message = tk.Label(master=window,text="", font="sans-serif 15 bold")
        #these frames are for the entries and buttons
    fr_entry = tk.Frame(master=window)
    fr_buttons = tk.Frame(master=window)
    name_label = tk.Label(master=fr_entry, text="Name:", font="sans-serif 15 bold")
    name_entry = tk.Entry(master=fr_entry)
    phrase_label1 = tk.Label(master=fr_entry, text="Secret Phrase:", font="sans-serif 15 bold")
    phrase_label2 = tk.Label(master=fr_entry, text="Secret Phrase:", font="sans-serif 15 bold")
    phrase_label3 = tk.Label(master=fr_entry, text="Secret Phrase:", font="sans-serif 15 bold")
    phrase_entry1 = tk.Entry(master=fr_entry, width="40")
    phrase_entry2 = tk.Entry(master=fr_entry, width="40")
    phrase_entry3 = tk.Entry(master=fr_entry, width="40")
    submit_button = tk.Button(master=fr_buttons, text="Submit", font="sans-serif 20 bold", fg="#FFFFFF", bg="#000000")
    move_on_button = tk.Button(master=fr_buttons, text="Move On", font="sans-serif 20 bold", fg="#FFFFFF", bg="#000000")
    

    #place entry widgets in entry frame
    name_label.grid(row="0", column="0", sticky="e")
    name_entry.grid(row="0", column="1")
    phrase_label1.grid(row="1",column="0", sticky="e")
    phrase_entry1.grid(row="1", column="1", sticky="w")
    phrase_label2.grid(row="2",column="0", sticky="e")
    phrase_entry2.grid(row="2", column="1", sticky="w")
    phrase_label3.grid(row="3",column="0", sticky="e")
    phrase_entry3.grid(row="3", column="1", sticky="w")

    #place button widgets in button frame
    submit_button.grid(row="0", column="0")
    move_on_button.grid(row="1",column="0")

    #pack all widgets
    game_label.pack(fill=tk.X)
    fr_entry.pack()
    game_message.pack()
    fr_buttons.pack()

    #bind buttons
    submit_button.bind("<Button-1>", submit_click)
    move_on_button.bind("<Button-1>", move_on_click)

def play_game():
    #clear screen first
    clear_screen()

    #if first round, create scores  - else recycle phrases
    global round_counter
    global phrases_list
    global scores
    global used_phrases
    if round_counter == 1:
        #create 0 scores for all players
        for x in range(0,len(names)):
            scores.append(0)
    else:
        #recycle all phrases back into pile
        phrases_list = used_phrases
        used_phrases = []

    #start with first player
    current_player = names[current_player_num]
    #circumvent pass glitch by adding "begin" screen
    current_phrase = "Press Begin when you're ready."


    #what happens when buttons are clicked
    #if guess is correct
    def correct_click(self):
        global current_phrase
        global current_player_num
        global current_player
        global scores
        #phrase moves from phrases_list to used_phrases
        used_phrases.append(current_phrase)
        phrases_list.remove(current_phrase)
        #player's score increases
        scores[current_player_num] += 1
        #if there are still phrases left, pass to next player
        if phrases_list:
            current_phrase = random.choice(phrases_list)
            phrase_widget["text"] = current_phrase
            #loop back to player 1 at end of circle
            if current_player_num == (len(names) - 1):
                current_player_num = 0
            else:
                current_player_num +=1
            current_player = names[current_player_num]
            player_widget["text"] = current_player
        #if no phrases left, move to results
        else:
            results_screen()
    
    #if player passes
    def pass_click(self):
        global current_phrase
        global current_player_num
        global current_player
        #new phrase chosen
        current_phrase = random.choice(phrases_list)
        phrase_widget["text"] = current_phrase
        #loop back to player 1 at end of circle
        if current_player_num == (len(names) - 1):
            current_player_num = 0
        else:
            current_player_num +=1
        current_player = names[current_player_num]
        player_widget["text"] = current_player
        #circumvent pass glitch by changing from "begin" to "pass" and starting timer
        pass_button["text"] = "Pass"
        reset_button.grid(row="0",column="1")
        correct_button.grid(row="0",column="2")
        timer_widget.start_countdown(120)
    #reset timer
    def reset_click(self):
        timer_widget.stop()
        timer_widget.reset()
        timer_widget.start_countdown(120)

    #create widgets
    phrase_widget = tk.Label(master=window,text=current_phrase)
    timer_widget = tktimerwidget.TkTimer(window, buttons=True)
        #frame for buttons
    fr_buttons = tk.Frame(master=window)
    player_widget = tk.Label(master=window,text="")
    correct_button = tk.Button(master=fr_buttons, text="Correct")
    pass_button = tk.Button(master=fr_buttons, text = "Begin")
    reset_button = tk.Button(master=fr_buttons, text="Reset Timer")


    #place widgets
    #tktimerwidget is placed automatically
    #pass button is originally "begin", starts beneath
    pass_button.grid(row="0",column="0")
    phrase_widget.pack()
    player_widget.pack()
    fr_buttons.pack()

    #bind buttons
    correct_button.bind("<Button-1>", correct_click)
    pass_button.bind("<Button-1>", pass_click)
    reset_button.bind("<Button-1>", reset_click)

def results_screen():
    #clear screen first
    clear_screen()

    #what happens when buttons are clicked
    #move to next round or end
    def next_click(self):
        global round_counter
        #if round 1 or 2, move to next round
        if round_counter < 3:
            round_counter += 1
            play_game()
        #if round 3, finish
        else:
            done_screen()
    
    #iterate through all teams and display their scores by creating and packing widgets
    for num in range(0,int(len(names)/2)):
        team_names = names[num],"and",names[num+int(len(names)/2)]
        team_score = scores[num] + scores[num+int(len(names)/2)]
        team_names_widget = tk.Label(master=window, text=team_names)
        team_score_widget = tk.Label(master=window, text=team_score)
        team_names_widget.pack()
        team_score_widget.pack()

    #create and place button
    next_button = tk.Button(master=window,text="Next")
    next_button.pack()

    #bind button
    next_button.bind("<Button-1>", next_click)

def done_screen():
    #clear screen first
    clear_screen()

    #what happens when buttons are clicked
    #export all phrases from game as txt file
    def export_click(self):
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = "\n".join(used_phrases)
            output_file.write(text)
        window.title(f"Charades - {filepath}")
        #return to title screen after exporting
        title_screen()
    #return to title screen without exporting
    def quit_click(self):
        title_screen()

    #create widgets
    export_question = tk.Label(master=window, text="Thanks for playing! Would you like to export your phrases as a .txt file?")
    export_button = tk.Button(master=window, text="Export")
    quit_button = tk.Button(master=window, text="No Thanks")

    #pack all widgets
    export_question.pack()
    export_button.pack()
    quit_button.pack()

    #bind buttons
    quit_button.bind("<Button-1>",quit_click)
    export_button.bind("<Button-1>",export_click)

#create window and define its title/size
window = tk.Tk()
window.title("Charades Manager")
window.geometry("500x350")

#call title screen and begin program
title_screen()
window.mainloop()