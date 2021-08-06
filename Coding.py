from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk,Image

app = Tk()
app.title('Tic-Tac-Toe')
#app.iconbitmap('C:/Users/aunis/Desktop/TIC TAC TOE/tic tac toe.ico')
app.iconbitmap('C:/Users/USER/Desktop/MiniProject/tic tac toe.ico')
#app.iconbitmap('C:/Users/Asus/Desktop/HAIQAL/tic tac toe.ico')

frame1 = Label(app, bd = 2, relief = SUNKEN)
frame1.pack(side = "top", fill = BOTH, expand = 1)
frame2 = Label(app)
frame2.pack(side = "bottom", fill = BOTH, expand = 1)
frame1.configure(background='Powder Blue')

create_option = 0

player_score = [0, 0]
player_name = ['', '']

winPos = 0

player1_score = None
player2_score = None

my_img = Image.open("C:/Users/aunis/Desktop/TIC TAC TOE/winner.png")
my_img = my_img.resize((185,185), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(my_img)

#Function splashcreen(popup image if any player win the set)
def winnerPic(winPos):
    window = Toplevel(app)

    Label(window,image=my_img).grid(row=0, column=0)

    def msgbox(player_name):
        if winPos == 1:
            messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS! {player_name[0]} Wins!!")
        elif winPos ==2:
            messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS! {player_name[1]} Wins!!")

    def destroy():
        window.destroy()
        
    msgbox(player_name)
    window.after(2000,destroy)
#app.geometry("1200x710")
# X starts so true
#Define player name
def check_name(player1_entry, player2_entry):
 if player1_entry.get() != '' and player2_entry.get() != '':
  player_name[0] = player1_entry.get()
  player_name[1] = player2_entry.get()
  print(player1_entry.get())
  print(player2_entry.get())
  reset()

def page1():
 Label(frame1, text = "Tic-Tac-Toe", font = ("times new roman ", 12, "bold"), bg = "Cadet Blue").grid(row = 0, column = 0, columnspan = 2, pady = (70,50))
 Button(frame1, text = "PLAY", height ="2", width ="15", command = lambda: check_name(player1_entry, player2_entry)).grid(row= 3, column =  0, columnspan = 2)
 Label(frame1, text ="Player 1:").grid(row=4, column=0)
 Label(frame1, text ="Player 2:").grid(row=5, column=0)
 player1_entry = Entry(frame1)
 player1_entry.grid(row = 4, column = 1)
 player2_entry = Entry(frame1)
 player2_entry.grid(row = 5, column = 1)
 
 clicked = True
count = 0
# disable all the buttons
def disable_all_buttons():
 b1.config(state=DISABLED)
 b2.config(state=DISABLED)
 b3.config(state=DISABLED)
 b4.config(state=DISABLED)
 b5.config(state=DISABLED)
 b6.config(state=DISABLED)
 b7.config(state=DISABLED)
 b8.config(state=DISABLED)
 b9.config(state=DISABLED)

# Check to see if someone won
def checkifwon():
	global winner, player_name, player1_score, winPos
	winner = False
	if b1["text"] == "X" and b2["text"] == "X" and b3["text"]  == "X":
		b1.config(bg="Blue")
		b2.config(bg="Blue")
		b3.config(bg="Blue")
		winner = True
		winPos = 1
		player_score[0] += 1
		player1_score['text'] = f'{player_score[0]}'
		disable_all_buttons()
	elif b4["text"] == "X" and b5["text"] == "X" and b6["text"]  == "X":
		b4.config(bg="Blue")
		b5.config(bg="Blue")
		b6.config(bg="Blue")
		winner = True
		winPos = 1
		player_score[0] += 1
		player1_score['text'] = f'{player_score[0]}'
		disable_all_buttons()
	elif b7["text"] == "X" and b8["text"] == "X" and b9["text"]  == "X":
		b7.config(bg="Blue")
		b8.config(bg="Blue")
		b9.config(bg="Blue")
		winner = True
		winPos = 1
		player_score[0] += 1
		player1_score['text'] = f'{player_score[0]}'
		disable_all_buttons()
	elif b1["text"] == "X" and b4["text"] == "X" and b7["text"]  == "X":
		b1.config(bg="Blue")
		b4.config(bg="Blue")
		b7.config(bg="Blue")
		winner = True
		winPos = 1
		player_score[0] += 1
		player1_score['text'] = f'{player_score[0]}'
		disable_all_buttons()
	elif b2["text"] == "X" and b5["text"] == "X" and b8["text"]  == "X":
		b2.config(bg="Blue")
		b5.config(bg="Blue")
		b8.config(bg="Blue")
		winner = True
		winPos = 1
		player_score[0] += 1
		player1_score['text'] = f'{player_score[0]}'
		disable_all_buttons()
	elif b3["text"] == "X" and b6["text"] == "X" and b9["text"]  == "X":
		b3.config(bg="Blue")
		b6.config(bg="Blue")
		b9.config(bg="Blue")
		winner = True
		winPos = 1
		player_score[0] += 1
		player1_score['text'] = f'{player_score[0]}'
		disable_all_buttons()
	elif b1["text"] == "X" and b5["text"] == "X" and b9["text"]  == "X":
		b1.config(bg="Blue")
		b5.config(bg="Blue")
		b9.config(bg="Blue")
		winner = True
		winPos = 1
		player_score[0] += 1
		player1_score['text'] = f'{player_score[0]}'
		disable_all_buttons()
	elif b3["text"] == "X" and b5["text"] == "X" and b7["text"]  == "X":
		b3.config(bg="Blue")
		b5.config(bg="Blue")
		b7.config(bg="Blue")
		winner = True
		winPos = 1
		player_score[0] += 1
		player1_score['text'] = f'{player_score[0]}'
		disable_all_buttons()

	# CHECK FOR O's Win
	elif b1["text"] == "O" and b2["text"] == "O" and b3["text"]  == "O":
		b1.config(bg="Red")
		b2.config(bg="Red")
		b3.config(bg="Red")
		winner = True
		winPos = 2
		player_score[1] += 1
		player2_score['text'] = f'{player_score[1]}'
		disable_all_buttons()
	elif b4["text"] == "O" and b5["text"] == "O" and b6["text"]  == "O":
		b4.config(bg="Red")
		b5.config(bg="Red")
		b6.config(bg="Red")
		winner = True
		winPos = 2
		player_score[1] += 1
		player2_score['text'] = f'{player_score[1]}'
		disable_all_buttons()
	elif b7["text"] == "O" and b8["text"] == "O" and b9["text"]  == "O":
		b7.config(bg="Red")
		b8.config(bg="Red")
		b9.config(bg="Red")
		winner = True
		winPos = 2
		player_score[1] += 1
		player2_score['text'] = f'{player_score[1]}'
		disable_all_buttons()
	elif b1["text"] == "O" and b4["text"] == "O" and b7["text"]  == "O":
		b1.config(bg="Red")
		b4.config(bg="Red")
		b7.config(bg="Red")
		winner = True
		winPos = 2
		player_score[1] += 1
		player2_score['text'] = f'{player_score[1]}'
		disable_all_buttons()
	elif b2["text"] == "O" and b5["text"] == "O" and b8["text"]  == "O":
		b2.config(bg="Red")
		b5.config(bg="Red")
		b8.config(bg="Red")
		winner = True
		winPos = 2
		player_score[1] += 1
		player2_score['text'] = f'{player_score[1]}'
		disable_all_buttons()
	elif b3["text"] == "O" and b6["text"] == "O" and b9["text"]  == "O":
		b3.config(bg="Red")
		b6.config(bg="Red")
		b9.config(bg="Red")
		winner = True
		winPos = 2
		player_score[1] += 1
		player2_score['text'] = f'{player_score[1]}'
		disable_all_buttons()
	elif b1["text"] == "O" and b5["text"] == "O" and b9["text"]  == "O":
		b1.config(bg="Red")
		b5.config(bg="Red")
		b9.config(bg="Red")
		winner = True
		winPos = 2
		player_score[1] += 1
		player2_score['text'] = f'{player_score[1]}'
		disable_all_buttons()
	elif b3["text"] == "O" and b5["text"] == "O" and b7["text"]  == "O":
		b3.config(bg="Red")
		b5.config(bg="Red")
		b7.config(bg="Red")
		winner = True
		winPos = 2
		player_score[1] += 1
		player2_score['text'] = f'{player_score[1]}'
		disable_all_buttons()

# Check if tie
	if count == 9 and winner == False:
		messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
		disable_all_buttons()
	if winner == True:
		winnerPic(winPos)

# Button clicked function
def b_click(b):
 global clicked, count
 if b["text"] == " " and clicked == True:
  b["text"] = "X"
  clicked = False
  count += 1
  checkifwon()
 elif b["text"] == " " and clicked == False:
  b["text"] = "O"
  clicked = True
  count += 1
  checkifwon()
 else:
  messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box..." )



#Define Reset
def reset():
 global b1, b2, b3, b4, b5, b6, b7, b8, b9, frame1, app, player1_score, player2_score
 global clicked, count, create_option
 if create_option == 0:
  my_menu.add_cascade(label="Options", menu=options_menu)
  options_menu.add_command(label="Reset Game", command=reset)
  options_menu.add_command(label="New Game", command=newGame)

 create_option += 1
 frame1.destroy()
 score_frame = Label(frame2)
 score_frame.grid(row = 0, column = 3, rowspan = 3)
 clicked = True
 count = 0
 # Build our buttons
 b1 = Button(frame2, text=" ", font=("Arial Rounded MT Bold", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
 b2 = Button(frame2, text=" ", font=("Arial Rounded MT Bold", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
 b3 = Button(frame2, text=" ", font=("Arial Rounded MT Bold", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b3))
 b4 = Button(frame2, text=" ", font=("Arial Rounded MT Bold", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
 b5 = Button(frame2, text=" ", font=("Arial Rounded MT Bold", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
 b6 = Button(frame2, text=" ", font=("Arial Rounded MT Bold", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b6))
 b7 = Button(frame2, text=" ", font=("Arial Rounded MT Bold", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
 b8 = Button(frame2, text=" ", font=("Arial Rounded MT Bold", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
 b9 = Button(frame2, text=" ", font=("Arial Rounded MT Bold", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

 # Grid our buttons to the screen
 b1.grid(row=0, column=0)
 b2.grid(row=0, column=1)
 b3.grid(row=0, column=2)
 b4.grid(row=1, column=0)
 b5.grid(row=1, column=1)
 b6.grid(row=1, column=2)
 b7.grid(row=2, column=0)
 b8.grid(row=2, column=1)
 b9.grid(row=2, column=2)
 
 score_label = Label(score_frame, text = 'score', width = 20)
 score_label.grid(row=0, column=0)
 player1 = Label(score_frame, text = f'Player X ({player_name[0]}):')
 player1.grid(row = 1, column = 0)
 player1_score = Label(score_frame, text = f'{player_score[0]}')
 player1_score.grid(row = 1, column = 1)
 player2 = Label(score_frame, text = f'Player O ({player_name[1]}):')
 player2.grid(row = 2, column = 0)
 player2_score = Label(score_frame, text = f'{player_score[1]}')
 player2_score.grid(row = 2, column = 1)

#Function for New Game
def newGame():
 
 global player_score
 player_score[0]=0
 player_score[1]=0
 reset()
 
# Create menu
my_menu = Menu(app)
app.config(menu=my_menu)
Label(frame1, text ="Player 1").grid(row=4, column=0)
# Create Options Menu
options_menu = Menu(my_menu, tearoff=False)

page1()
app.mainloop()
