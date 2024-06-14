from tkinter import *
import random
import os
import sys
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#5B2C6F")
        self.root.title("Billing Software")
        title = Label(self.root, text="Billing System", bd=12, relief=RIDGE, font=(
            "Arial Black", 20), bg="#A569BD", fg="white").pack(fill=X)
        # ===================================variables=======================================================================================
        self.nutella = IntVar()
        self.noodles = IntVar()
        self.lays = IntVar()
        self.oreo = IntVar()
        self.muffin = IntVar()
        self.silk = IntVar()
        self.namkeen = IntVar()
        self.atta = IntVar()
        self.pasta = IntVar()
        self.rice = IntVar()
        self.oil = IntVar()
        self.sugar = IntVar()
        self.dal = IntVar()
        self.tea = IntVar()
        self.soap = IntVar()
        self.shampoo = IntVar()
        self.lotion = IntVar()
        self.cream = IntVar()
        self.foam = IntVar()
        self.mask = IntVar()
        self.sanitizer = IntVar()
        self.total_sna = StringVar()
        self.total_gro = StringVar()
        self.total_hyg = StringVar()
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.c_name = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.phone = StringVar()
        # ==========================================customer details label frame=================================================
        details = LabelFrame(self.root, text="Customer Details", font=(
            "Arial Black", 12), bg="#A569BD", fg="white", relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)
        cust_name = Label(details, text="Customer Name", font=(
            "Arial Black", 14), bg="#A569BD", fg="white").grid(row=0, column=0, padx=15)
        cust_entry = Entry(details, borderwidth=4, width=30,
                           textvariable=self.c_name).grid(row=0, column=1, padx=8)
        contact_name = Label(details, text="Contact No.", font=(
            "Arial Black", 14), bg="#A569BD", fg="white").grid(row=0, column=2, padx=10)
        contact_entry = Entry(details, borderwidth=4, width=30,
                              textvariable=self.phone).grid(row=0, column=3, padx=8)
        bill_name = Label(details, text="Bill No.", font=(
            "Arial Black", 14), bg="#A569BD", fg="white").grid(row=0, column=4, padx=10)
        bill_entry = Entry(details, borderwidth=4, width=30,
                           textvariable=self.bill_no).grid(row=0, column=5, padx=8)
        # =======================================snacks label frame=================================================================
        snacks = LabelFrame(self.root, text="Snacks", font=(
            "Arial Black", 12), bg="#E5B4F3", fg="#6C3483", relief=GROOVE, bd=10)
        snacks.place(x=5, y=180, height=380, width=325)

        item1 = Label(snacks, text="Nutella Choco Spread", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483"). grid(row=0, column=0, pady=11)
        item1_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.nutella).grid(row=0, column=1, padx=10)
        item2 = Label(snacks, text="Noodles(1 Pack)", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=1, column=0, pady=11)
        item2_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.noodles).grid(row=1, column=1, padx=10)

        item3 = Label(snacks, text="Lays(10Rs)", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=2, column=0, pady=11)
        item3_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.lays).grid(row=2, column=1, padx=10)

        item4 = Label(snacks, text="Oreo(20Rs)", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=3, column=0, pady=11)
        item4_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.oreo).grid(row=3, column=1, padx=10)

        item5 = Label(snacks, text="Chocolate Muffin", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=4, column=0, pady=11)
        item5_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.muffin).grid(row=4, column=1, padx=10)

        item6 = Label(snacks, text="Dairy Milk Silk(60Rs)", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=5, column=0, pady=11)
        item6_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.silk).grid(row=5, column=1, padx=10)

        item7 = Label(snacks, text="Namkeen(15Rs)", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=6, column=0, pady=11)
        item7_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.namkeen).grid(row=6, column=1, padx=10)
        # ===================================GROCERY=====================================================================================
        grocery = LabelFrame(self.root, text="Grocery", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#E5B4F3", fg="#6C3483")
        grocery.place(x=340, y=180, height=380, width=325)

        item8 = Label(grocery, text="Aashirvaad Atta(1kg)", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=0, column=0, pady=11)
        item8_entry = Entry(grocery, borderwidth=2, width=15,
                            textvariable=self.atta).grid(row=0, column=1, padx=10)

        item9 = Label(grocery, text="Pasta(1kg)", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=1, column=0, pady=11)
        item9_entry = Entry(grocery, borderwidth=2, width=15,
                            textvariable=self.pasta).grid(row=1, column=1, padx=10)

        item10 = Label(grocery, text="Basmathi Rice(1kg)", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=2, column=0, pady=11)
        item10_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.rice).grid(row=2, column=1, padx=10)

        item11 = Label(grocery, text="Sunflower Oil(1ltr)", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=3, column=0, pady=11)
        item11_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.oil).grid(row=3, column=1, padx=10)

        item12 = Label(grocery, text="Refined Sugar(1kg)", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=4, column=0, pady=11)
        item12_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.sugar).grid(row=4, column=1, padx=10)

        item13 = Label(grocery, text="Daal(1kg)", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=5, column=0, pady=11)
        item13_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.dal).grid(row=5, column=1, padx=10)

        item14 = Label(grocery, text="Tea Powder(1kg)", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=6, column=0, pady=11)
        item14_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.tea).grid(row=6, column=1, padx=10)
        # ========================================beauty and hygine===============================================================================
        hygine = LabelFrame(self.root, text="Beauty & Hygine", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#E5B4F3", fg="#6C3483")
        hygine.place(x=677, y=180, height=380, width=325)

        item15 = Label(hygine, text="Bathing Soap", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=0, column=0, pady=11)
        item15_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.soap).grid(row=0, column=1, padx=10)

        item16 = Label(hygine, text="Shampoo(1ltr)", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=1, column=0, pady=11)
        item16_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.shampoo).grid(row=1, column=1, padx=10)

        item17 = Label(hygine, text="Body Lotion(1ltr)", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=2, column=0, pady=11)
        item17_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.lotion).grid(row=2, column=1, padx=10)

        item18 = Label(hygine, text="Face Cream", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=3, column=0, pady=11)
        item18_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.cream).grid(row=3, column=1, padx=10)

        item19 = Label(hygine, text="Shaving Foam", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=4, column=0, pady=11)
        item19_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.foam).grid(row=4, column=1, padx=10)

        item20 = Label(hygine, text="Face Mask(1piece)", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=5, column=0, pady=11)
        item20_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.mask).grid(row=5, column=1, padx=10)

        item21 = Label(hygine, text="Hand Sanitizer(50ml)", font=(
            "Arial Black", 11), bg="#E5B4F3", fg="#6C3483").grid(row=6, column=0, pady=11)
        item21_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.sanitizer).grid(row=6, column=1, padx=10)
        # =====================================================billarea==============================================================================
        bill_area = Frame(self.root, bd=10, relief=GROOVE, bg="#E5B4F3")
        bill_area.place(x=1010, y=188, width=330, height=372)

        bill_title = Label(bill_area, text="Bill Area", font=(
            "Arial Black", 17), bd=7, relief=GROOVE, bg="#E5B4F3", fg="#6C3483").pack(fill=X)

        scrol_y = Scrollbar(bill_area, orient=VERTICAL)
        self.txtarea = Text(bill_area, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        # =================================================billing menu=========================================================================================
        bill_menu = LabelFrame(self.root, text="Billing Summery", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#A569BD", fg="white")
        bill_menu.place(x=0, y=560, relwidth=1, height=137)

        total_snacks = Label(bill_menu, text="Total Snacks Price", font=(
            "Arial Black", 11), bg="#A569BD", fg="white").grid(row=0, column=0)
        total_snacks_entry = Entry(bill_menu, width=30, borderwidth=2, textvariable=self.total_sna).grid(
            row=0, column=1, padx=10, pady=7)

        total_grocery = Label(bill_menu, text="Total Grocery Price", font=(
            "Arial Black", 11), bg="#A569BD", fg="white").grid(row=1, column=0)
        total_grocery_entry = Entry(bill_menu, width=30, borderwidth=2,
                                    textvariable=self.total_gro).grid(row=1, column=1, padx=10, pady=7)

        total_hygine = Label(bill_menu, text="Total Beauty & Hygine Price", font=(
            "Arial Black", 11), bg="#A569BD", fg="white").grid(row=2, column=0)
        total_hygine_entry = Entry(bill_menu, width=30, borderwidth=2,
                                   textvariable=self.total_hyg).grid(row=2, column=1, padx=10, pady=7)

        tax_snacks = Label(bill_menu, text="Snacks Tax", font=(
            "Arial Black", 11), bg="#A569BD", fg="white").grid(row=0, column=2)
        tax_snacks_entry = Entry(bill_menu, width=30, borderwidth=2, textvariable=self.a).grid(
            row=0, column=3, padx=10, pady=7)

        tax_grocery = Label(bill_menu, text="Grocery Tax", font=(
            "Arial Black", 11), bg="#A569BD", fg="white").grid(row=1, column=2)
        tax_grocery_entry = Entry(bill_menu, width=30, borderwidth=2, textvariable=self.b).grid(
            row=1, column=3, padx=10, pady=7)

        tax_hygine = Label(bill_menu, text="Beauty & Hygine Tax", font=(
            "Arial Black", 11), bg="#A569BD", fg="white").grid(row=2, column=2)
        tax_hygine_entry = Entry(bill_menu, width=30, borderwidth=2, textvariable=self.c).grid(
            row=2, column=3, padx=10, pady=7)


root = Tk()
obj = Bill_App(root)
root.mainloop()
