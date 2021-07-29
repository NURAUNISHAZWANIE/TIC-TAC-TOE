#Define Reset
def reset():
	global b1, b2, b3, b4, b5, b6, b7, b8, b9, frame1, app, player1_score, player2_score
	global clicked, count, create_option
	if create_option == 0:

my_menu.add_cascade(label="Options", menu=options_menu)

options_menu.add_command(label="Reset Game", command=reset)