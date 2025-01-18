#import openpyxl 
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Scouting Registration Form")
root.geometry('400x400')

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

#School Name
school_name_label = Label(root, text="Team Number: ", font=NORM_FONT)
school_name_label.place(x=5, y=5)
school_name_label = Entry(root)
school_name_label.place(x=150, y=5)

#Locations
location_label = Label(root, text="Competition Location: ", font=NORM_FONT)
location_label.place(x=5, y=40)

options = [
    "Mcmaster",
    "NewMarket",
    "Districts"
]

clicked = StringVar()
clicked.set("Select Location")

drop = OptionMenu( root, clicked, *options)
drop.place(x=150, y= 40)

#Match Number
match_label = Label(root, text="Match Number: ", font=NORM_FONT)
match_label.place(x=5, y= 65)
match_label = Entry(root)
match_label.place(x= 150, y= 65)

score = IntVar()
def increase_score(event=None, score=None):
    score.set(score.get() + 1)
def decrease_score(event=None, score=None):
    score.set(score.get() - 1)

rnum = 180
cnum = 5
counters = [IntVar() for _ in range(3)]

for idx, stat in enumerate(["Score", "Autonomous", "Endgame"]):
    scorelabel = Label(root, text = stat).place(x=30, y=rnum)
    scorelabel = Label(root, textvariable = counters[idx]).place(x=55, y= rnum+22)
    scorelabel = Button(root, text = "+", command = lambda score=counters[idx]: increase_score(score=score)).place(x=30, y= rnum+22)
    scorelabel = Button(root, text= "-", command=lambda score=counters[idx]: decrease_score(score=score)).place(x=70, y= rnum+22)
    rnum += 60

#Additional Comments
comments_label = Label(root, text= "Additional Comments: ", font=NORM_FONT)
comments_label.place(x=5, y= 300)
comments_label = Entry(root)
comments_label.place(x= 150, y= 300)

def register():
    school_name = school_name_label.get()
    location_name = location_label.get()

    new_row = [location_name, school_name]

    """
    workbook = openpyxl.load_workbook("registration_data.xlsx")
    sheet = workbook.active
    sheet.append(new_row)
    workbook.save("registration_data.xlsx")
    messagebox.showinfo("Success", "Registration successful!")

"""
"""
register_button = Button(root, text="Register", command=register)
register_button.pack()
"""
root.mainloop()
