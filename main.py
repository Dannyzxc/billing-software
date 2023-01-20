from tkinter import *
import random
import math
from tkinter import messagebox
import os

class Bill_app:
          def __init__(self,root):
                    self.root=root
                    self.root.geometry("1350x700+0+0")
                    self.root.title("billing software")
                    bg_color = "#FFBD33"
                    fg_color_1 = "black"

                    
                    # variables 
                    self.soap = IntVar()
                    self.face_cream = IntVar()
                    self.face_wash = IntVar()
                    self.hair_wash =IntVar()

                    
                    self.tomato = IntVar()
                    self.carrot = IntVar()
                    self.onion = IntVar()
                    self.bean = IntVar()

                    
                    self.milk = IntVar()
                    self.orange_juice = IntVar()
                    self.water = IntVar()
                    self.soda = IntVar()

                    
                    self.cosmetice_price = StringVar()
                    self.grocerry_price = StringVar()
                    self.drinks_price = StringVar()

                    self.cosmetice_tax = StringVar()
                    self.grocerry_tax = StringVar()
                    self.drinks_tax = StringVar()

                    
                    self.c_name = StringVar()
                    self.c_phone = StringVar()

                    self.bill_num = StringVar()
                    x = random.randint(1000,9999)
                    self.bill_num.set(str(x))
                    self.search_bill = StringVar()
                  
                  




                    title= Label(self.root,text="Billing software",bd=5,relief=GROOVE,bg=bg_color,fg="black",  font=("times new roman",27,"bold"),pady=6).pack(fill=X)

                    # customer detail frame
                    F1 = LabelFrame(self.root,text="customer details",font=("times new roman",15,"bold"),fg="black",bg=bg_color)
                    F1.place(x=0,y=50,relwidth=1)

                    cname_lable1 = Label(F1,text="Customer Name",bg=bg_color,fg="black" ,font=("times new roman",18,"bold")).grid(row=0,column=0,padx=20,pady=20)
                    cname_txt = Entry(F1,width=14,font="arial 15",textvariable=self.c_name ,bd=4,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=6)

                    cphone_lable1 = Label(F1,text="Phone",bg=bg_color,fg="black" ,font=("times new roman",18,"bold")).grid(row=0,column=2,padx=20,pady=20)
                    cphone_txt = Entry(F1,width=14,font="arial 15",textvariable=self.c_phone ,bd=4,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=6)

                    cbill_lable1 = Label(F1,text="Bill number",bg=bg_color,fg="black" ,font=("times new roman",18,"bold")).grid(row=0,column=4,padx=20,pady=20)
                    cbill_txt = Entry(F1,width=14,font="arial 15",textvariable=self.search_bill ,bd=4,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=6)

                    bill_btn = Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=5)


                    # cosmetic frame 
                    F2 = LabelFrame(self.root,text="Cosmetics",font=("times new roman",15,"bold"),fg="black",bg=bg_color)
                    F2.place(x=5,y=150,width=325,height=380)


                    bath_lb = Label(F2,text="Bath Soap",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")

                    bath_txt = Entry(F2,width=10,textvariable=self.soap ,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)



                    face_cream_lb = Label(F2,text="Face cream",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")

                    face_cream_txt = Entry(F2,width=10,textvariable=self.face_cream,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)



                    face_wash_lb = Label(F2,text="Face Wash",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")

                    face_wash_txt = Entry(F2,width=10,textvariable=self.face_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)



                    hair_wash_lb = Label(F2,text="Hair wash",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")

                    hair_wash_txt = Entry(F2,width=10,textvariable=self.hair_wash,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)



                    # grocerries 

                    F3 = LabelFrame(self.root,text="Grocerries",font=("times new roman",15,"bold"),fg="black",bg=bg_color)
                    F3.place(x=320,y=150,width=325,height=380)


                    tomato_lb = Label(F3,text="Tomato",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=2,padx=10,pady=10,sticky="w")

                    tomato_txt = Entry(F3,width=10,textvariable=self.tomato,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=10)



                    carrot_lb = Label(F3,text="Carrot",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=2,padx=10,pady=10,sticky="w")

                    carrot_txt = Entry(F3,width=10,textvariable=self.carrot,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=10)



                    onion_lb = Label(F3,text="Onion",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=2,padx=10,pady=10,sticky="w")

                    onion_txt = Entry(F3,width=10,textvariable=self.onion,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=10)



                    beans_lb = Label(F3,text="Beans",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=2,padx=10,pady=10,sticky="w")

                    beans_txt = Entry(F3,width=10,textvariable=self.bean,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=3,padx=10,pady=10)





                    # Drinks 

                    F4 = LabelFrame(self.root,text="Drinks",font=("times new roman",15,"bold"),fg="black",bg=bg_color)
                    F4.place(x=640,y=150,width=325,height=380)


                    milk_lb = Label(F4,text="Milk",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=0,column=2,padx=10,pady=10,sticky="w")

                    milk_txt = Entry(F4,width=10,textvariable=self.milk,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=10)



                    orrange_juice_lb = Label(F4,text="orange juice",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=1,column=2,padx=10,pady=10,sticky="w")

                    orange_juice_txt = Entry(F4,width=10,textvariable=self.orange_juice,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=10)



                    water_lb = Label(F4,text="Water",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=2,column=2,padx=10,pady=10,sticky="w")

                    water_txt = Entry(F4,width=10,textvariable=self.water,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=10)



                    soda_lb = Label(F4,text="Soda",font=("times new roman",16,"bold"),bg=bg_color,fg="black").grid(row=3,column=2,padx=10,pady=10,sticky="w")

                    soda_txt = Entry(F4,width=10,textvariable=self.soda,font=("times new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=3,padx=10,pady=10)



                    # bill area

                    F5 = Frame(self.root,bd=5,relief=GROOVE)
                    F5.place(x=960,y=150,width=390,height=380)

                    bill_title = Label(F5,text="Bill Area",font="arial 15 bold",fg="black",bd=5,relief=RIDGE).pack(fill=X)
                    scroll_y = Scrollbar(F5,orient=VERTICAL)
                    self.txtarea = Text(F5,yscrollcommand=scroll_y)
                    scroll_y.pack(side=RIGHT,fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.pack(fill=BOTH,expand=1)


                    # button print

                    F6 =  LabelFrame(self.root,text="Bill Menu" ,font=("times new roman",15,"bold"),bd=6,fg="black",relief=GROOVE ,bg=bg_color)
                    F6.place(x=0,y=530,relwidth=1,height=150)
                    

                    m1_lb = Label(F6,text="Total Cosmetic Price",font=("times new roman",12,"bold"),bg=bg_color,fg=fg_color_1).grid(row=0,column=0,padx=5,pady=5,sticky="w")

                    m1_txt = Entry(F6,width=10,textvariable=self.cosmetice_price,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=5,pady=5)



                    m2_lb = Label(F6,text="Total grocceries price",font=("times new roman",12,"bold"),bg=bg_color,fg=fg_color_1).grid(row=1,column=0,padx=5,pady=5,sticky="w")

                    m2_txt = Entry(F6,width=10,textvariable=self.grocerry_price,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=5,pady=5)

                    m3_lb = Label(F6,text="Total drinks price",font=("times new roman",12,"bold"),bg=bg_color,fg=fg_color_1).grid(row=2,column=0,padx=5,pady=5,sticky="w")

                    m3_txt = Entry(F6,width=10,textvariable=self.drinks_price,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=5,pady=5)

# 

                    m4_lb = Label(F6,text="-- Tax ",font=("times new roman",12,"bold"),bg=bg_color,fg=fg_color_1).grid(row=0,column=2,padx=5,pady=5,sticky="w")




                    m4_txt = Entry(F6,width=10,textvariable=self.cosmetice_tax,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=3,padx=5,pady=5)

                    m4_lb = Label(F6,text="-- Tax",font=("times new roman",12,"bold"),bg=bg_color,fg=fg_color_1).grid(row=1,column=2,padx=5,pady=5,sticky="w")

                    m4_txt = Entry(F6,width=10,textvariable=self.grocerry_tax,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=3,padx=5,pady=5)

                    m4_lb = Label(F6,text="-- Tax",font=("times new roman",12,"bold"),bg=bg_color,fg=fg_color_1).grid(row=2,column=2,padx=5,pady=5,sticky="w")

                    m4_txt = Entry(F6,width=10,textvariable=self.drinks_tax,font=("arial",12,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=3,padx=5,pady=5)


                    # btns menu

                    btn_1 = Frame(F6,bd=7,relief=GROOVE)
                    btn_1.place(x=450,width=888,height=120)


                    total_btn = Button(btn_1,command=self.total ,text="Total",bg="blue",fg="white",pady=15,padx=15,width=11,font="arial 15 bold").grid(row=0,column=0,padx=35,pady=5)
                    generate_bill = Button(btn_1,command=self.bill_area, text="Generate",bg="green",fg="white",pady=15,padx=15,width=11,font="arial 15 bold").grid(row=0,column=1,padx=10,pady=5)
                    clear_btn = Button(btn_1,command=self.clear_data, text="Clear",bg="orange",fg="white",pady=15,padx=15,width=11,font="arial 15 bold").grid(row=0,column=2,padx=5,pady=10)
                    exit_btn = Button(btn_1,command=self.exit_app,text="Exit",bg="red",fg="white",pady=15,padx=15,width=11,font="arial 15 bold").grid(row=0,column=3,padx=5,pady=10)

                    self.welcome_bill()




          def total(self):
                    self.c_s_p = int(self.soap.get())*36
                    self.c_fc_p = self.face_cream.get()*100
                    self.c_fw_p = self.face_wash.get()*150
                    self.c_hw_p = self.soap.get()*70

                    self.g_t_p = self.tomato.get()*20
                    self.g_c_p = self.carrot.get()*40
                    self.g_o_p = self.onion.get()*30
                    self.g_b_p = self.bean.get()*50


                    self.d_m_p = self.milk.get()*20
                    self.d_o_p = self.orange_juice.get()*10
                    self.d_w_p = self.water.get()*15
                    self.d_s_p = self.soda.get()*8
                    


                    self.total_cosmetice_price  = float(
                              self.c_s_p + self.c_fc_p + self.c_fw_p + self.c_hw_p
                  
                    )

                    self.cosmetice_price.set("Rs." + str(self.total_cosmetice_price))
                    self.c_tax = round((self.total_cosmetice_price * 0.10),2)
                    self.cosmetice_tax.set( "Rs." + str(self.c_tax))


                    self.total_grocceries_price  = float(
                            
                             ( self.tomato.get()*20) + 
                             ( self.carrot.get()*40) + 
                             ( self.onion.get()*30) + 
                             ( self.bean.get()*50)
                            
                    )

                    self.grocerry_price.set("Rs." + str(self.total_grocceries_price))
                    self.g_tax = round((self.total_grocceries_price * 0.05),2)
                    self.grocerry_tax.set( "Rs." + str(self.g_tax ))

                    self.total_drinks_price  = float(
                           
                             ( self.milk.get()*20) + 
                             ( self.orange_juice.get()*10) + 
                             ( self.water.get()*15) + 
                             ( self.soda.get()*8) 
                    )

                    self.drinks_price.set("Rs." + str(self.total_drinks_price))
                    self.d_tax = round((self.total_drinks_price * 0.28),2)
                    self.drinks_tax.set( "Rs." + str(self.d_tax ))


                    

                    self.Total_bill = float(self.total_cosmetice_price + self.total_grocceries_price   + self.total_drinks_price + self.c_tax + self.g_tax + self.d_tax)


          def welcome_bill(self):
                    self.txtarea.delete('1.0',END)
                    self.txtarea.insert(END,"\tWelcome to shopify")
                    self.txtarea.insert(END,"\n============================================\n")
                    self.txtarea.insert(END,f"\n Bill Number : {self.bill_num.get()}")
                    self.txtarea.insert(END,f"\n Customer Name : {self.c_name.get()}")
                    self.txtarea.insert(END,f"\n Phone : {self.c_phone.get()}")
                    self.txtarea.insert(END,"\n============================================\n")
                    self.txtarea.insert(END,"\nProducts \t\tQty\t\tPrice")
                    self.txtarea.insert(END,"\n--------------------------------------------\n")


                    


          def bill_area(self):

                    if self.c_name.get()=="" or self.c_phone.get()=="":
                              messagebox.showerror("Error","Customer details are must")
                    
                    elif self.cosmetice_price.get() == "Rs.0.0" and self.grocerry_price.get() =="Rs.0.0" and self.drinks_price.get():
                              messagebox.showerror("Error","No product added")
                    else:
                              
                              self.welcome_bill()

                              # cosmetics
                              if self.soap.get() != 0:
                                        self.txtarea.insert(END,f"\n  Bath Soap\t\t\t{self.soap.get()}\t{self.c_s_p}")
                              if self.face_cream.get() != 0:
                                        self.txtarea.insert(END,f"\n  face cream\t\t\t{self.face_cream.get()}\t{self.c_fc_p}")
                              if self.face_wash.get() != 0:
                                        self.txtarea.insert(END,f"\n  face wash\t\t\t{self.face_wash.get()}\t{self.c_fw_p}")
                              if self.hair_wash.get() != 0:
                                        self.txtarea.insert(END,f"\n  hair wash\t\t\t{self.hair_wash.get()}\t{self.c_hw_p}")
                              # grocerries
                              if self.tomato.get() != 0:
                                        self.txtarea.insert(END,f"\n   tomato\t\t\t{self.tomato.get()}\t{self.g_t_p}")
                              if self.carrot.get() != 0:
                                        self.txtarea.insert(END,f"\n   carrot\t\t\t{self.carrot.get()}\t{self.g_c_p}")
                              if self.onion.get() != 0:
                                        self.txtarea.insert(END,f"\n   onion\t\t\t{self.onion.get()}\t{self.g_o_p}")
                              if self.bean.get() != 0:
                                        self.txtarea.insert(END,f"\n   bean\t\t\t{self.bean.get()}\t{self.g_b_p}")
                              # drinks
                              if self.milk.get() != 0:
                                        self.txtarea.insert(END,f"\n   milk\t\t\t{self.milk.get()}\t{self.d_m_p}")
                              if self.orange_juice.get() != 0:
                                        self.txtarea.insert(END,f"\n   orange juice\t\t\t{self.orange_juice.get()}\t{self.d_o_p}")
                              if self.water.get() != 0:
                                        self.txtarea.insert(END,f"\n   water\t\t\t{self.water.get()}\t{self.d_w_p}")
                              if self.soda.get() != 0:
                                        self.txtarea.insert(END,f"\n   soda\t\t\t{self.soda.get()}\t{self.d_s_p}")

                              self.txtarea.insert(END,f"\n--------------------------------------------")
                              if self.cosmetice_tax.get() != "Rs.0.0":
                                        self.txtarea.insert(END,f"\nCosmetic Tax \t\t\t\t{self.cosmetice_tax.get()}")
                              if self.grocerry_tax.get() != "Rs.0.0":
                                        self.txtarea.insert(END,f"\nGrocceries Tax \t\t\t\t{self.grocerry_tax.get()}")
                              if self.drinks_tax.get() != "Rs.0.0":
                                        self.txtarea.insert(END,f"\nDrinks Tax \t\t\t\t{self.drinks_tax.get()}")
                              
                              self.txtarea.insert(END,f"\nTotal Bill  \t\t\t\tRs.{self.Total_bill}")
                              self.txtarea.insert(END,f"\n==========================================")
                              self.save_bill()
          

          def save_bill(self):
                    op=messagebox.askyesno("save bill","Do you want to save the Bill?")
                    if op > 0:
                              
                              self.bill_data = self.txtarea.get('1.0',END)
                              f1 = open("bills/" + str(self.bill_num.get())+ ".txt","w")
                              f1.write(self.bill_data)
                              f1.close()
                              messagebox.showinfo("saved","Bill saved successfully")

                    else:
                              return


          def find_bill(self):
                    present = "no"
                    for i in os.listdir("bills/"):
                              if i.split(".")[0] == self.search_bill.get():
                                        f1 = open(f"bills/{i}","r")
                                        self.txtarea.delete('1.0',END)
                                        for d in f1:
                                                  self.txtarea.insert(END,d)
                                        f1.close()
                                        present = "yes"

                    if present == "no":
                              messagebox.showerror('error','invalid bill number')


          def clear_data(self):
                    op=messagebox.askyesno("confirm","do you really want to clear data")
                    if op>0:
                              # variables 
                              self.soap.set(0)
                              self.face_cream.set(0)
                              self.face_wash.set(0)
                              self.hair_wash.set(0)

                              
                              self.tomato.set(0)
                              self.carrot.set(0)
                              self.onion.set(0)
                              self.bean.set(0)

                              
                              self.milk.set(0)
                              self.orange_juice.set(0)
                              self.water.set(0)
                              self.soda.set(0)

                              
                              self.cosmetice_price.set("")
                              self.grocerry_price.set("")
                              self.drinks_price.set("")

                              self.cosmetice_tax.set("")
                              self.grocerry_tax.set("")
                              self.drinks_tax.set("")

                              
                              self.c_name.set("")
                              self.c_phone.set("")

                              self.bill_num.set("")
                              x = random.randint(1000,9999)
                              self.bill_num.set(str(x))
                              self.search_bill.set("")
                              self.welcome_bill()


          def exit_app(self):
                    op=messagebox.askyesno("confirm","do you really want to exit")
                    if op>0:
                              self.root.destroy()
                    



                    


root = Tk()
obj = Bill_app(root)
root.mainloop()




