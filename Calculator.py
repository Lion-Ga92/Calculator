from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("700x500")
root.resizable(False, False)
frame_1 = ttk.Frame(root)
frame_1.grid(row=1, column=1)
frame_2 = ttk.Frame(root)
frame_2.grid(row=2, column=1)
frame_3 = ttk.Frame(root)
frame_3.grid(row=3, column=1)
frame_4 = ttk.Frame(root)
frame_4.grid(row=4, column=1)

lbl_greet = ttk.Label(frame_1, text="Welcome user...")
lbl_greet.grid(row=1, column=2)
#THE LAY OUT FOR DISPLAY
display_txt = Text(frame_2, width=50, height=7)
display_txt.grid(row=1, column=1)
#END OF DISPLAY SECTION 

#OPERAND BUTTONS


sum_bttn = ttk.Button(frame_3, text="+", command=lambda: display_txt.insert(END, "\n+\n"))
sum_bttn.grid(row=1, column=1)
minus_bttn = ttk.Button(frame_3, text="-", command=lambda: display_txt.insert(END, "\n-\n"))
minus_bttn.grid(row=1, column=2)
tims_bttn = ttk.Button(frame_3, text="X", command=lambda:  display_txt.insert(END, "\n*\n"))
tims_bttn.grid(row=1, column=3)
div_bttn = ttk.Button(frame_3, text="0/0", command=lambda: display_txt.insert(END, "\n/\n"))
div_bttn.grid(row=1, column=4)

def clr_all():
    display_txt.delete("1.0", END)

clr_bttn = ttk.Button(frame_4, text="Clr.", command=clr_all)
clr_bttn.grid(row=1, column=5)

#start of buttons section row 1
bttn_1 = ttk.Button(frame_4, text="1", command=lambda: display_txt.insert(END, "1"))
bttn_1.grid(row=1, column=1)
bttn_2 = ttk.Button(frame_4, text="2", command=lambda: display_txt.insert(END, "2"))
bttn_2.grid(row=1, column=2)
bttn_3 = ttk.Button(frame_4, text="3", command=lambda: display_txt.insert(END, "3"))
bttn_3.grid(row=1, column=3)


#start of buttons section row 3
bttn_4 = ttk.Button(frame_4, text="4", command=lambda: display_txt.insert(END, "4"))
bttn_4.grid(row=2, column=1)
bttn_5 = ttk.Button(frame_4, text="5", command=lambda: display_txt.insert(END, "5"))
bttn_5.grid(row=2, column=2)
bttn_6 = ttk.Button(frame_4, text="6", command=lambda: display_txt.insert(END, "6"))
bttn_6.grid(row=2, column=3)

#start of buttons section row 9
bttn_7 = ttk.Button(frame_4, text="7", command=lambda: display_txt.insert(END, "7"))
bttn_7.grid(row=3, column=1)
bttn_8 = ttk.Button(frame_4, text="8", command=lambda: display_txt.insert(END, "8"))
bttn_8.grid(row=3, column=2)
bttn_9 = ttk.Button(frame_4, text="9", command=lambda: display_txt.insert(END, "9"))
bttn_9.grid(row=3, column=3)
bttn_0 = ttk.Button(frame_4, text="0", command=lambda: display_txt.insert(END, "0"))
bttn_0.grid(row=4, column=2)

def ins_exp():
    display_txt.insert(END, "\nE\n")

exp_bttn = ttk.Button(frame_4, text="Exp", command=ins_exp)
exp_bttn.grid(row=4, column=3)


def ins_equals():
    var_op = display_txt.get("2.0")
    var_1 = display_txt.get("1.0", "1.9")
    var_3= display_txt.get("3.0", "3.9")

    if var_op == "+":
        solve_sum = (int(var_1) + int(var_3))
        display_txt.delete("1.0", END)
        display_txt.insert("1.0", solve_sum)
    elif var_op == "-":
        solve_minus = (int(var_1) - int(var_3))
        display_txt.delete("1.0", END)
        display_txt.insert("1.0", solve_minus)
    elif var_op == "*":
        solve_time = (int(var_1) * int(var_3))
        display_txt.delete("1.0", END)
        display_txt.insert("1.0", solve_time)
    elif var_op == "/":
        solve_div = (int(var_1) / int(var_3))
        display_txt.delete("1.0", END)
        display_txt.insert("1.0", solve_div)
    elif var_op == "E":
        solve_exp = (int(var_1) ** int(var_3))
        display_txt.delete("1.0", END)
        display_txt.insert("1.0", solve_exp)
    elif display_txt.get("4.1", END):
        print("Hello")

    
equals_bttn = ttk.Button(frame_4, text="=", command=ins_equals)
equals_bttn.grid(row=4, column=1)
root.mainloop()

# i am trying to solve an issue with my ability to push things to github 
# SO IGNORE THESE COMMENTS