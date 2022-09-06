# congenial-couscous
# sign up page
from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector


class Newbie:
    def __init__(self, new):
        self.sinup = new
        self.sinup.geometry("100x200")
        self.sinup.state("zoomed")
        self.sinup.title("Sign Up Page")
        self.icon2 = PhotoImage(file="lift.png")
        self.sinup.iconphoto(False, self.icon2)
        self.frame2 = Frame(self.sinup, height=900, width=500, background="sky blue")
        self.frame2.place(x=0, y=0)
        self.frame3 = Frame(self.sinup, height=800, width=1000, background="pink")
        self.frame3.place(x=500, y=0)
        Label(self.frame2, text="Sign Up ", background="sky blue", foreground="black",
              font=("MV Boli", 35)).place(x=100, y=200)
        Label(self.frame3, text="First Name:", background="pink", foreground="black",
              font=("MV Boli", 20)).place(x=10, y=100)
        Label(self.frame3, text="Last Name:", background="pink", foreground="black",
              font=("MV Boli", 20)).place(x=10, y=150)
        Label(self.frame3, text="Email:", background="pink", foreground="black",
              font=("MV Boli", 20)).place(x=10, y=200)
        Label(self.frame3, text="Phone Number:", background="pink", foreground="black",
              font=("MV Boli", 20)).place(x=10, y=250)
        Label(self.frame3, text="Password:", background="pink", foreground="black",
              font=("MV Boli", 20)).place(x=10, y=300)
        Label(self.frame3, text="Domain:", background="pink", foreground="black",
              font=("MV Boli", 20)).place(x=10, y=350)
        Label(self.frame3, text="Shop Name:", background="pink", foreground="black",
              font=("MV Boli", 20)).place(x=10, y=400)
        Label(self.frame3, text="GST Number:", background="pink", foreground="black",
              font=("MV Boli", 20)).place(x=10, y=450)
        Label(self.frame3, text="Location:", background="pink", foreground="black",
              font=("MV Boli", 20)).place(x=10, y=500)
        self.D1 = Entry(self.frame3, width=15, font=("MV Boli", 15))
        self.D1.place(x=260, y=110)
        self.D2 = Entry(self.frame3, width=15, font=("MV Boli", 15))
        self.D2.place(x=260, y=160)
        self.D3 = Entry(self.frame3, width=15, font=("MV Boli", 15))
        self.D3.place(x=260, y=210)
        self.D4 = Entry(self.frame3, width=15, font=("MV Boli", 15))
        self.D4.place(x=260, y=260)
        self.D5 = Entry(self.frame3, width=15, font=("MV Boli", 15))
        self.D5.place(x=260, y=310)
        self.D6 = ttk.Combobox(self.frame3, height=4, width=12, font=("MV Boli", 13), state="readonly")
        self.D6["values"] = ("select", "Medical", "Foods & Beveargs", "Statinary", "others")
        self.D6.place(x=260, y=360)
        self.D6.current(0)
        self.D6_0 = Entry(self.frame3, width=15, font=("MV Boli", 13))
        self.D6_0.place(x=440, y=360)
        self.D7 = Entry(self.frame3, width=15, font=("MV Boli", 15))
        self.D7.place(x=260, y=410)
        self.D8 = Entry(self.frame3, width=15, font=("MV Boli", 15))
        self.D8.place(x=260, y=460)
        self.D9 = Entry(self.frame3, width=15, font=("MV Boli", 15))
        self.D9.place(x=260, y=510)


# ========================BUTTONS============================

        Button(self.frame3, text="Sign Up", font=("MV Boli", 15), command=self.enter).place(x=260, y=580)
        Button(self.frame3, text="Edit", font=("MV Boli", 15), command=self.updatesp).place(x=160, y=580)
        Label(self.frame2, text="note:", background="red", fg="white").place(x=20, y=450)
        Label(self.frame2, text="For Edit the profile data please enter the registered phoneNumber.\nThis page can't change the password, use forget password to change.\n Thank you for your cooperation", background="sky blue").place(x=20, y=470)

# =========================ENTER CODE=============================

    def enter(self):
        name = self.D1.get()
        lname = self.D2.get()
        emid = self.D3.get()
        con = self.D4.get()
        pw = self.D5.get()
        do = self.D6.get()
        do2 = self.D6_0.get()
        sh = self.D7.get()
        gst = self.D8.get()
        loc = self.D9.get()

        self.hell = mysql.connector.connect(host="localhost", user="root", passwd="Admin@123", database="inventory_sos")
        self.heaven = self.hell.cursor()
        try:
            self.vql = "insert into details(First_Name, Last_Name, EmailID, PhoneNumber, PassWord, Domain, Domain_Others, Shop_Name, GST_Number, Location) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            self.mql = name, lname, emid, con, pw, do, do2, sh, gst, loc
            self.heaven.execute(self.vql, self.mql)
            messagebox.showinfo("info", "SIGN UP Complete\nPlease Restart the Application..!")
            self.hell.commit()
            self.sinup.quit()

        except Exception as e:
            print(e)
            messagebox.showerror("info", "The user number already exists..!")
            self.hell.rollback()
            self.hell.close()

# ============================================UPDATE THE PROFILE=========================================

    def updatesp(self):
        try:
            hell = mysql.connector.connect(host="localhost", user="root", passwd="Admin@123", database="inventory_sos")
            hea = hell.cursor(buffered=True)
            three = "update details set First_Name=%s, Last_Name=%s, EmailID=%s,Domain=%s, Domain_Others=%s, Shop_Name=%s, GST_Number=%s, Location=%s  where PhoneNumber=%s;"
            four = self.D1.get(), self.D2.get(), self.D3.get(), self.D6.get(), self.D6_0.get(), self.D7.get(), self.D8.get(), self.D9.get(), self.D4.get()
            hea.execute(three, four)
            messagebox.showinfo("", "Details Updated successfully..!")
            # Label(self.frame3, text="Database Updated successfully....", foreground="yellow", font=(None, 12)).place(x=900, y=280)
            hell.commit()
            hell.rollback()
            hell.close()

        except Exception as e:
            messagebox.showerror("updatesp", f"{e}")
            print(e)


if __name__ == "__main__":
    new = Tk()
    obj1 = Newbie(new)
    new.mainloop()

