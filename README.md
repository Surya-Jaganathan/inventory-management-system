# congenial-couscous
from tkinter import *
import Image
from PIL import ImageTk
from tkinter import ttk, messagebox
from designsp import Newbie
import mysql.connector


class Sos:
    def __init__(self, inv):
        self.item = inv
        self.item.geometry("100x200")
        self.item.state("zoomed")
        self.item.title("Inventory-Tamil Industries")
        self.icon = PhotoImage(file="lift.png")
        self.item.iconphoto(False, self.icon)
        self.bg = Image.open("planets.jpg")
        self.pic = ImageTk.PhotoImage(self.bg)
        Label(image=self.pic).pack()

# ==============FRAME=================
        self.fra = Frame(self.item, background="white", height=500, width=400)
        self.fra.place(x=800, y=120)
        self.top_frame = Frame(self.item, background="#6842A5", height=60, width=1500)
        self.top_frame.place(x=0, y=0)

# ===================TOP LABEL======================
        Label(self.top_frame, text="INVENTORY", font=("MV Boli", 25), background="#6842A5", fg="white", width=15).place(x=600, y=8)
        Label(self.top_frame, text="- Tamil Industries", background="#6842A5", fg="white").place(x=850, y=38)

# ===============LABEL================
        Label(self.fra, text="WELCOME", font=("Comic Sans MS", 25), foreground="black", background="white").place(x=120, y=20)
        Label(self.fra, text="PhoneNumber:", foreground="black", background="white", font=("Comic Sans MS", 15)).place(x=30, y=100)
        Label(self.fra, text="Password:", foreground="black", background="white", font=("Comic Sans MS", 15)).place(x=30, y=160)

# ================ENTRY BOX==========================
        datatype1 = IntVar()
        datatype2 = StringVar()
        self.e1 = Entry(self.fra, font=("Comic Sans MS", 15), fg="black", highlightthickness=0, relief=FLAT, textvariable=datatype1)
        self.e1.place(x=170, y=100)
        self.e1.delete(0)

        Canvas(self.fra, width=200, height=2, background="#6842A5", highlightthickness=0).place(x=170, y=125)

        self.e2 = Entry(self.fra, font=("Comic Sans MS", 15), fg="black", highlightthickness=0, relief=FLAT, textvariable=datatype2, show="*")
        self.e2.place(x=170, y=160)
        self.e2.delete(0)

        Canvas(self.fra, width=200, height=2, background="#6842A5", highlightthickness=0).place(x=170, y=185)

# ================BUTTONS====================
        self.c_v1 = IntVar(value=0)
        cb = Checkbutton(self.fra, text="Show Password", background="white",variable=self.c_v1, onvalue=1, offvalue=0, command=self.pwshow)
        cb.place(x=180, y=195)

        Button(self.fra, text="Login", background="#6842A5", foreground="white", width=10, height=1, font=("Comic Sans MS", 12),
               command=self.login).place(x=50, y=240)
        Button(self.fra, text="Sign Up", background="#6842A5", foreground="white", width=10, height=1,
               font=("Comic Sans MS", 12), command=self.rookie).place(x=230, y=240)
        Button(self.fra, text="EXIT", background="#6842A5", foreground="white", width=16, height=1,
               font=("Comic Sans MS", 12), command=self.item.quit).place(x=100, y=320)
        Button(self.fra, text="forget password", background="white", foreground="black", width=20, highlightthickness=0,
               relief=FLAT, font=("Comic Sans MS", 12), command=self.forget).place(x=80, y=280)

    def pwshow(self):
        if self.c_v1.get() == 1:
            self.e2.config(show='')
        else:
            self.e2.config(show='*')

# ======================================================SIGN UP PAGE=======================================================

    def rookie(self):
        self.item.destroy()
        new = Tk()
        hell = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123")
        heaven = hell.cursor(buffered=True)
        try:
            heaven.execute("create database if not exists inventory_sos;")
            heaven.execute("use inventory_sos;")
            heaven.execute("select database()")
            heaven.execute("create table if not exists details(First_Name varchar(20), Last_Name varchar(20), EmailID nvarchar(50), PhoneNumber bigint(40) primary key, PassWord nvarchar(21), Domain varchar(31), Domain_Others varchar(51), Shop_Name varchar(31), GST_Number nvarchar(31), Location varchar(151));")
            hell.commit()
        except Exception as e:
            print(e)
            hell.rollback()
            hell.close()

        obj1 = Newbie(new)
        new.mainloop()

# ==================================================================LOGIN PAGE===========================================

    def login(self):
        if self.e1.get() == "" and self.e2.get() == "":
            messagebox.showerror("invalid", "please! Fill the Required Form")
        elif self.e1.get() == "" or self.e2.get() == "":
            messagebox.showerror("Error", "please! Enter the Valid Data")
            self.clear()
        else:
            try:
                helld = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123", database="inventory_sos")
                heavend = helld.cursor()
                heavend.execute("select * from details where PhoneNumber=%s and PassWord=%s", (self.e1.get(), self.e2.get()))
                row = heavend.fetchone()
                if row is None:
                    messagebox.showerror("Error", "INVALID Phone Number and Password", parent=self.item)
                    self.clear()
                else:
                    helld.close()
                    self.new2 = Tk()
                    self.new2.geometry("400x600")
                    self.new2.state("zoomed")
                    self.new2.focus_set()
                    self.new2.grab_set()
                    print(self.e1.get())

                    try:
                        self.hell4 = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123", database="inventory_sos")
                        self.heaven4 = self.hell4.cursor()
                        self.vql = 'select shop_name from details where PhoneNumber=%s and PassWord=%s;'
                        self.eql = (self.e1.get(), self.e2.get())
                        self.heaven4.execute(self.vql, self.eql)       # ============ shopname =============
                        self.rp = self.heaven4.fetchone()
                        print(self.rp)
                        self.new2.title(self.rp)
                        Label(self.new2, height=4, width=1500, background="sky blue").place(x=0, y=0)
                        Label(self.new2, text=self.rp, font=("Comic Sans MS", 25, "bold"), background="sky blue", foreground="black").pack(anchor="n", pady=10)
                        # =================frame===============
                        frame = Label(self.new2, background="pink", height=24, width=50)
                        frame.place(x=0, y=66)
                        # Label(self.new2, background="white", height=40, width=1500).place(x=0, y=440)

                        try:
                            self.name = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123", database="inventory_sos")
                            self.firstname = self.name.cursor()
                            self.n1ql = 'select First_Name from details where PhoneNumber=%s and PassWord=%s;'
                            self.n2ql = (self.e1.get(), self.e2.get())
                            self.firstname.execute(self.n1ql, self.n2ql)         # =============firstname==================
                            self.n1 = self.firstname.fetchone()
                            print(self.n1)
                            Label(self.new2, text="name:", background="pink", font=("Comic Sans MS", 14)).place(x=10, y=80)
                            Label(self.new2, text=self.n1, font=("Comic Sans MS", 14), background="pink").place(x=80, y=80)

                            try:
                                self.name2 = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123", database="inventory_sos")
                                self.firstname2 = self.name2.cursor()
                                self.n1ql1 = 'select Last_Name from details where PhoneNumber=%s and PassWord=%s;'
                                self.n2ql2 = (self.e1.get(), self.e2.get())
                                self.firstname2.execute(self.n1ql1, self.n2ql2)         # ========= lastname =================
                                self.n2 = self.firstname2.fetchone()
                                print(self.n2)
                                Label(self.new2, text=self.n2, font=("Comic Sans MS", 14), background="pink").place(x=180, y=80)

                                try:
                                    self.hell5 = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123", database="inventory_sos")
                                    self.heaven5 = self.hell5.cursor()
                                    self.eql = 'select EmailID from details where PhoneNumber=%s and PassWord=%s;'
                                    self.eql2 = (self.e1.get(), self.e2.get())
                                    self.heaven5.execute(self.eql, self.eql2)           # =========== mailid ===================
                                    self.eid = self.heaven5.fetchone()
                                    print(self.eid)
                                    Label(self.new2, text="EmailID:", font=("Comic Sans MS", 14), background="pink").place(x=10, y=120)
                                    idmil = Listbox(self.new2, height=1, width=20, relief=FLAT, highlightthickness=0, font=("Comic Sans MS", 14), background="pink", )
                                    idmil.place(x=89, y=120)
                                    idmil.insert(0, self.eid)
                                    Label(self.new2, text="...", font=("Comic Sans MS", 14), background="pink", highlightcolor="pink").place(x=332, y=120)
                                    try:
                                        self.hell6 = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123", database="inventory_sos")
                                        self.heaven6 = self.hell6.cursor()
                                        self.pql = 'select PhoneNumber from details where PhoneNumber=%s and PassWord=%s;'
                                        self.pql2 = (self.e1.get(), self.e2.get())
                                        self.heaven6.execute(self.pql, self.pql2)      # ============= phone number=================
                                        self.pn = self.heaven6.fetchone()
                                        print(self.pn)
                                        Label(self.new2, text="PhoneNumber:", font=("Comic Sans MS", 14), background="pink").place(x=10, y=160)
                                        Label(self.new2, text=self.pn, font=("Comic Sans MS", 14), background="pink").place(x=140, y=160)

                                        try:
                                            self.hell7 = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123", database="inventory_sos")
                                            self.heaven7 = self.hell7.cursor()
                                            self.d = 'select Domain from details where PhoneNumber=%s and PassWord=%s;'
                                            self.d2 = (self.e1.get(), self.e2.get())
                                            self.heaven7.execute(self.d, self.d2)       # ===========domain==============
                                            self.dmain = self.heaven7.fetchone()
                                            print(self.dmain)
                                            Label(self.new2, text="Domain:", font=("Comic Sans MS", 14), background="pink").place(x=10, y=200)
                                            Label(self.new2, text=self.dmain, font=("Comic Sans MS", 14), background="pink").place(x=85, y=200)

                                            try:
                                                self.hell8 = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123", database="inventory_sos")
                                                self.heaven8 = self.hell8.cursor()
                                                self.o = 'select Domain_Others from details where PhoneNumber=%s and PassWord=%s;'
                                                self.o2 = (self.e1.get(), self.e2.get())
                                                self.heaven8.execute(self.o, self.o2)  # ==========domain others ================
                                                self.other = self.heaven8.fetchone()
                                                print(self.other)
                                                Label(self.new2, text="Other:", font=("Comic Sans MS", 14), background="pink").place(x=10, y=240)
                                                Label(self.new2, text=self.other, font=("Comic Sans MS", 14), background="pink").place(x=70, y=240)

                                                try:
                                                    self.hell9 = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123", database="inventory_sos")
                                                    self.heaven9 = self.hell9.cursor()
                                                    self.gst = 'select GST_Number from details where PhoneNumber=%s and PassWord=%s;'
                                                    self.gst2 = (self.e1.get(), self.e2.get())
                                                    self.heaven9.execute(self.gst, self.gst2)     # ===========gst number=================
                                                    self.gn = self.heaven9.fetchone()
                                                    print(self.gn)
                                                    Label(self.new2, text="GST Number:", font=("Comic Sans MS", 14), background="pink").place(x=10, y=280)
                                                    Label(self.new2, text=self.gn, font=("Comic Sans MS", 14), background="pink").place(x=140, y=280)

                                                    try:
                                                        self.hell9 = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123", database="inventory_sos")
                                                        self.heaven9 = self.hell9.cursor()
                                                        self.gst = 'select Location from details where PhoneNumber=%s and PassWord=%s;'
                                                        self.gst2 = (self.e1.get(), self.e2.get())
                                                        self.heaven9.execute(self.gst, self.gst2)     # ===========Location=================
                                                        self.gn = self.heaven9.fetchone()
                                                        print(self.gn)
                                                        Label(self.new2, text="Location:", font=("Comic Sans MS", 14), background="pink").place(x=10, y=320)
                                                        lb = Listbox(self.new2, height=3, width=26, background="pink", font=("Comic Sans MS", 14), relief=FLAT, highlightthickness=0)
                                                        lb.insert(0, self.gn)
                                                        lb.place(x=10, y=350)
                                                        Label(self.new2, text="...", font=("Comic Sans MS", 14), background="pink", highlightcolor="pink").place(x=330, y=350)

                                                    except Exception as e:
                                                        messagebox.showerror("location", f"{e}")

                                                except Exception as e:
                                                    messagebox.showerror("gst number", f"{e}")

                                            except Exception as e:
                                                messagebox.showerror("domain_others", f"{e}")

                                        except Exception as e:
                                            messagebox.showerror("domain", f"{e}")

                                    except Exception as e:
                                        messagebox.showerror("phonenumber", f"{e}")

                                except Exception as e:
                                    messagebox.showerror("email", f"{e}")

                            except Exception as e:
                                messagebox.showerror("Lastname", f"{e}")

                        except Exception as e:
                            messagebox.showerror("firstname", f'{e}')

                        try:
                            self.connection = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123")
                            self.cur = self.connection.cursor(buffered=True)
                            self.cur.execute("create database if not exists `%s` ;", (self.e1.get(),))
                            self.connection.commit()

                        except Exception as e:
                            messagebox.showerror("product_db", f'{e}')
                            print(e)
                            print(self.e1.get())

                        Label(self.new2, text="Please enter the Product Details", font=("Comic Sans MS", 12))

                        Label(self.new2, text="Brand Name:", font=("Comic Sans MS", 12)).place(x=400, y=100)
                        self.i1 = Entry(self.new2, font=("Comic Sans MS", 12))
                        self.i1.place(x=530, y=100)

                        Label(self.new2, text="Product Name:", font=("Comic Sans MS", 12)).place(x=400, y=140)
                        self.i2 = Entry(self.new2, font=("Comic Sans MS", 12))
                        self.i2.place(x=530, y=140)

                        Label(self.new2, text="Domain:", font=("Comic Sans MS", 12)).place(x=400, y=180)
                        self.ddb = ttk.Combobox(self.new2, height=4, width=15)
                        self.ddb["values"] = ("select", "medicines", "foods", "snacks", "juices", "Stationery", "others")
                        self.ddb.place(x=530, y=180)

                        Label(self.new2, text="Add Details about the product:", font=("Comic Sans MS", 12)).place(x=800, y=100)
                        self.i3 = Text(self.new2, height=8, width=40)
                        self.i3.place(x=850, y=140)

                        Label(self.new2, text="Type:", font=("Comic Sans MS", 12)).place(x=400, y=260)
                        self.i4 = Entry(self.new2, font=("Comic Sans MS", 12))
                        self.i4.place(x=530, y=260)

                        Label(self.new2, text="Product ID:", font=("Comic Sans MS", 12)).place(x=400, y=220)
                        self.i5 = Entry(self.new2, font=("Comic Sans MS", 12))
                        self.i5.place(x=530, y=220)

                        Label(self.new2, text="Status Report=", font=("Comic Sans MS", 13)).place(x=770, y=280)

                        Label(self.new2, text="eg:Biscuits,chocolates,Tablets,syrup....etc", font=("Comic Sans MS", 8), foreground="grey").place(x=530, y=284)
                        Button(self.new2, text="save  ", font=("Comic Sans MS", 12), background="green", command=self.save).place(x=400, y=320)
                        Button(self.new2, text="Update", font=("Comic Sans MS", 12), background="yellow", foreground="black", command=self.update).place(x=500, y=320)
                        Button(self.new2, text="Delete", font=("Comic Sans MS", 12), background="red", command=self.delete).place(x=600, y=320)
                        Button(self.new2, text="clear", font=("Comic Sans MS", 12), command=self.erase).place(x=840, y=380)

                        Label(self.new2, text="Choose the domain to view the lists:", font=("Comic Sans MS", 12)).place(x=400, y=380)
                        self.ddb1 = ttk.Combobox(self.new2, height=4, width=15)
                        self.ddb1["values"] = ("select", "medicines", "foods", 'snacks', "juices", "Stationery", "others")
                        self.ddb1.place(x=660, y=380)
                        Button(self.new2, text="view", font=("Comic Sans MS", 12), command=self.show).place(x=780, y=380)

                        sou = Menu(self.new2)
                        self.new2.config(menu=sou)
                        one10 = Menu(sou)
                        sou.add_cascade(label="PROFILE", menu=one10, background="pink", font=("Comic Sans MS", 14))
                        one10.add_command(label="sign up", command=self.rookie, font=("Comic Sans MS", 14))
                        one10.add_command(label="exit", command=self.new2.quit, font=("Comic Sans MS", 14))

                    except Exception as e:
                        messagebox.showerror("kind", f"{e}")
                        print(e)
                        self.item.destroy()

            except Exception as e:
                messagebox.showerror("mistake",  f"Error due to {str(e)}", parent=self.item)
                print(e)

# =============================================================FORGET PASSWORD==============================================

    def forget(self):
        if self.e1.get() == "":
            messagebox.showerror("error", "enter tha valid PhoneNumber....!")

        else:
            try:
                hell2 = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123", database="inventory_sos")
                heaven2 = hell2.cursor()
                heaven2.execute("select * from details where PhoneNumber=%s;", (self.e1.get(),))
                row2 = heaven2.fetchone()
                if row2 is None:
                    messagebox.showerror("error", "The given PhoneNumber is not Exists..!")
                else:
                    self.oot = Toplevel()
                    self.oot.title("Forget Password?")
                    self.oot.geometry("400x440+450+200")
                    one = PhotoImage(file="lift.png")
                    self.oot.iconphoto(False, one)
                    self.oot.config(bg="sky blue")

                    Label(self.oot, text="New Password:", background="sky blue").place(x=20, y=50)
                    Label(self.oot, text="Re-Enter the Password", background="sky blue").place(x=20, y=100)
                    # Label(self.oot, text=self.e1.get()).place(x=150, y=220)
                    self.p1 = Entry(self.oot, background="sky blue", relief=FLAT)
                    self.p1.place(x=150, y=50)
                    can = Canvas(self.oot, height=2, width=125, background="pink", highlightthickness=0)
                    can.place(x=150, y=70)
                    self.p2 = Entry(self.oot, background="sky blue", relief=FLAT)
                    self.p2.place(x=150, y=100)
                    can = Canvas(self.oot, height=2, width=125, background="pink", highlightthickness=0)
                    can.place(x=150, y=120)
                    Button(self.oot, text="Re-Set Password..", background="pink", command=self.reset).place(x=120, y=180)

            except Exception as e:
                messagebox.showerror("", f"{e}")
                print(e)

# ========================================================PASSWORD RESET BUTTON================================================

    def reset(self):
        if self.p1.get() == "" and self.p2.get() == "":
            messagebox.showerror("error", "Enter the New Password..!")
        elif self.p1.get() == "" or self.p2.get() == "":
            messagebox.showerror("error", "Both Values Doesn't Match..!")
        else:
            try:
                hell3 = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123", database="inventory_sos")
                heaven3 = hell3.cursor()
                heaven3.execute("update details set PassWord=%s where PhoneNumber=%s;", (self.p1.get(), self.e1.get(),))
                hell3.commit()
                messagebox.showinfo("", "New Password Updated..!")
                hell3.rollback()
                hell3.close()
                self.e1.delete(0)
                self.e2.delete(0)
                self.oot.destroy()

            except Exception as e:
                messagebox.showerror("three", f"{e}")

# ========================================================SAVE=============================================
    def clear(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
# =========================================SAVE LOGIN========================================

    def save(self):
        try:
            print(self.e1.get())
            print(self.ddb.get())
            self.s1 = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123")
            self.s2 = self.s1.cursor(buffered=True)
            self.s2.execute("use `%s`;", (self.e1.get(),))
            self.s2.execute("select database();")
            self.s2.execute("create table if not exists `%s` (Brand_Name varchar(41), Product_Name varchar(41), Domain varchar(20), Product_ID nvarchar(21) primary key, Type varchar(31),Details_of_the_Product varchar(500));", (self.ddb.get(),))
            one = "insert into `%s` (Brand_Name, Product_Name, Domain, Product_ID, Type, Details_of_the_Product) values (%s, %s, %s, %s, %s, %s)"
            two = self.ddb.get(), self.i1.get(), self.i2.get(), self.ddb.get(),  self.i5.get(), self.i4.get(), self.i3.get("1.0", "end-1c")
            self.s2.execute(one, two)
            # messagebox.showinfo("db", "database created", parent=self.new2)
            Label(self.new2, text="Database created successfully....", foreground="green", font=("Comic Sans MS", 12)).place(x=900, y=280)
            self.s1.commit()
            self.s1.rollback()
            self.i1.delete(0, END)
            self.i2.delete(0, END)
            self.ddb.delete(0, END)
            self.i4.delete(0, END)
            self.i3.delete('1.0', END)
            self.i5.delete(0, END)
            # self.item.destroy()
        except Exception as e:
            messagebox.showerror("save", f'{e}', parent=self.new2)
            print(e)
            print(self.e1.get())
            print(self.ddb.get())
            print(self.i3.get("1.0", "end-1c"))

# ======================================================UPDATE PRODUCT FILES==========================================================

    def update(self):
        try:
            hel = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123")
            hea = hel.cursor(buffered=True)
            hea.execute("use `%s`;", (self.e1.get(),))
            hea.execute("select database();")
            three = "update `%s` set Brand_Name=%s, Product_Name=%s, Domain=%s, Type=%s, Details_of_the_Product=%s  where Product_ID=%s;"
            four = self.ddb.get(), self.i1.get(), self.i2.get(), self.ddb.get(), self.i4.get(), self.i3.get("1.0", "end-1c"), self.i5.get()
            hea.execute(three, four)
            messagebox.showinfo("", "Updated..!", parent=self.new2)
            Label(self.new2, text="Database Updated successfully....", foreground="yellow", font=("Comic Sans MS", 12)).place(x=900, y=280)
            hel.commit()
            hel.rollback()
            hel.close()

        except Exception as e:
            messagebox.showerror("update", f"{e}")
            print(e)

# ================================================  DELETE THE DETAILS==========================================
    def delete(self):
        try:
            hel1 = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123")
            hea1 = hel1.cursor(buffered=True)
            hea1.execute("use `%s`;", (self.e1.get(),))
            hea1.execute("select database();")
            hea1.execute("delete from `%s` where Product_ID=%s", (self.ddb.get(), self.i5.get(),))
            # messagebox.showinfo("", "deleted..!", parent=self.new2)
            Label(self.new2, text="Database deleted successfully....", foreground="red", font=("Comic Sans MS", 12)).place(x=900, y=280)
            hel1.commit()
            hel1.rollback()
            hel1.close()

        except Exception as e:
            messagebox.showerror("update", f"{e}")
            print(e)

    def getinfo(self, event):
        self.i1.delete(0, END)
        self.i2.delete(0, END)
        self.i3.delete('1.0', END)
        self.ddb.delete(0, END)
        self.i4.delete(0, END)
        self.i5.delete(0, END)
        xql = self.lb.selection()[0]
        select = self.lb.set(xql)
        self.i1.insert(0, select["Brand_Name"])
        self.i2.insert(0, select["Product_Name"])
        self.ddb.insert(0, select["Domain"])
        self.i5.insert(0, select["Product_ID"])
        self.i4.insert(0, select["Type"])
        self.i3.insert(INSERT, select["Details_of_the_Product"])

# ===========================================================SHOW DETAILS LOGIN===============================================

    def show(self):
        if self.ddb1.get() == " ":
            messagebox.showerror("Empty field", "Please choose the following categories to view the stored product details", parent=self.new2)
        else:
            try:
                hell = mysql.connector.connect(host="127.0.0.1", user="root", password="Admin@123")
                heaven = hell.cursor(buffered=True)
                heaven.execute("use `%s`;", (self.e1.get(),))
                heaven.execute("select database();")
                heaven.execute("select Brand_Name, Product_Name, Domain, Product_ID, Type, Details_of_the_Product from `%s` ", (self.ddb1.get(),))
                view = heaven.fetchall()
                print(view)
                if view is None:
                    messagebox.showinfo("Empty data", "There is no such category in your shop data..!", parent=self.new2)
                else:
                    items = "Brand_Name", "Product_Name", "Domain", "Product_ID", "Type", "Details_of_the_Product"
                    self.lb = ttk.Treeview(self.new2, columns=items, show="headings", height=10)

                    for iql in items:
                        self.lb.heading(iql, text=iql, anchor=CENTER)
                        self.lb.pack(padx=0, pady=5)
                        self.lb.place(x=120, y=440)
                    for i, (Brand_Name, Product_Name, Domain, Product_ID, Type, Details_of_the_Product) in enumerate(view, start=1):
                        self.lb.insert("", "end", values=(Brand_Name, Product_Name, Domain, Product_ID, Type, Details_of_the_Product))

                        self.lb.bind("<Double-Button-1>", self.getinfo)
                        hell.close()
            except Exception as e:
                messagebox.showinfo("Dropdown Box", "There is no such category in your shop data..!", parent=self.new2)
                print(e)

    def erase(self):
        self.i1.delete(0, END)
        self.i2.delete(0, END)
        self.i3.delete('1.0', END)
        self.i4.delete(0, END)
        self.i5.delete(0, END)
        self.ddb.delete(0, END)


if __name__ == "__main__":
    inv = Tk()
    obj = Sos(inv)
    inv.mainloop()
