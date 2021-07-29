from tkinter import *
from tkinter import messagebox
#from PIL import ImageTk,Image

app = Tk()
app.title('Tic-Tac-Toe')
app.iconbitmap('C:/Users/USER/Desktop/MiniProject/tic tac toe.ico')


frame1 = Label(app, bd = 2, relief = SUNKEN)
frame1.pack(side = "top", fill = BOTH, expand = 1)
frame2 = Label(app)
frame2.pack(side = "bottom", fill = BOTH, expand = 1)
frame1.configure(background='Powder Blue')

#my_img = ImageTk.PhotoImage(Image.open("Sir Iszaidy.png"))
#my_img2 = ImageTk.PhotoImage(Image.open("Pn Mas.png"))

create_option = 0

player_score = [0, 0]
player_name = ['', '']

player1_score = None
player2_score = None

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


#Define Reset
def reset():
	global b1, b2, b3, b4, b5, b6, b7, b8, b9, frame1, app, player1_score, player2_score
	global clicked, count, create_option
	if create_option == 0:

my_menu.add_cascade(label="Options", menu=options_menu)

options_menu.add_command(label="Reset Game", command=reset)

page1()
app.mainloop()
