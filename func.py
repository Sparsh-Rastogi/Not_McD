#main functions of the program
#default menu for customer
menuu = [("S.no","Item name","price"),("1","Mc Pizza","49"),("2","Mc Alloo Tikki","65"),("3","French fries","70"),("4","Pasta","115"),("5","Ice Cream","35")]
global_variables ={"status":"used to show user's status","form":"tkinter window that aids in inputting menu"}
#function that confirms the status of user... either customer or employee
def know_user():
  import tkinter
  passcode = "KFC"
  root = tkinter.Tk()  #root is the window where user will sign in
  root.geometry("450x400+425+200")
  root.title("Sparsh Vibhu project")
  nolabel = tkinter.Label(root,text="                   ") #to create an empty column 0
  nolabel.grid(column=0)
  h1 = tkinter.Label(root,text="Welcome to McDonalds",font=("Arial",22))
  h1.grid(row=0,column=2,columnspan=4)
  l1 = tkinter.Label(root,text="Are you an employee or a customer?",font=("Arial",10))
  l1.grid(row=1,column=2,columnspan=6)
  def statdef(a): #this function defines the global_var status
    global status
    if a == "employee":
      cust_butt["state"]= "disabled"
      askpass()
    if a == "customer":
      status = a
      tkinter.Label(root,text="Welcome",font=("Arial",20)).grid(row=5,column=2,columnspan=4)
      root.after(3000,root.destroy)
  emp_butt = tkinter.Button(root,text="Employee",command=lambda:statdef("employee"))
  emp_butt.grid(row=2,column=3,columnspan=2,padx=3,pady=3)
  cust_butt = tkinter.Button(root,text="Customer",command=lambda:statdef("customer"))
  cust_butt.grid(row=3,column=3,columnspan=2,padx=3,pady=3)
  def askpass(): #asks the password from user if he identifies oneself as employee
    pass_var = tkinter.StringVar()
    l2 = tkinter.Label(root,text="Kindly enter the employee password \n (press enter to submit)",font=("Arial",10))
    l2.grid(row=5,column=2,columnspan=4,rowspan=2)
    ent = tkinter.Entry(root,textvariable=pass_var,foreground="gray")
    ent.grid(row=7,column=3,columnspan=2)
    ent.insert(0,"The password is KFC :)")
    global error_ct
    error_ct = 0
    def temp_text(e):
      global error_ct
      if str(e) == "<FocusIn event>":
        ent.delete(0,"end")
        ent["foreground"]="black"
      else:
        password = pass_var.get()
        if password == passcode:
          if error_ct == 1:
            error_ct = 0
            global error
            error.destroy()
          global status
          status = "employee"
          l3 = tkinter.Label(root,text="You are now confirmed as an Employee \n LET'S CREATE A MENU")
          l3.grid(row=8,column=2,rowspan=2,columnspan=4)
          l4 = tkinter.Label(root,text="\U0001f600",font=("Arial",60))
          l4.grid(row=10,column=2,rowspan=3,columnspan=4)
          root.after(4000,root.destroy)
        elif error_ct == 0:
          error_ct = 1
          error = tkinter.Label(root,text="That is not the correct password... but KFC is :)")
          error.grid(row=8,column=2,columnspan=4)
    ent.bind("<FocusIn>",temp_text) #<FocusIn>event is triggered when the entry is clicked
    ent.bind("<Return>",temp_text) #<Return>event is triggered when the enter key is pressed
  root.mainloop()
  try:
    return status
  except:
    pass
#function that creates the form which is used to gather information about menu
def know_menu():
  import tkinter
  global form 
  form = tkinter.Tk()  #window that takes inputs from user
  form.title("Sparsh Vibhu Project")
  form.geometry("300x300+200+125")
  tkinter.Label(form,text="       ").grid(row=0,column=0)
  h1 = tkinter.Label(form,text="Menu Form",font=("Arial",25))
  h1.grid(row=0,column=1,columnspan=4)
  global q1 #variables are declared global for there use in later functions
  q1 = tkinter.Label(form,text="",font=("Arial",12))
  q1.grid(row=1,column=1,columnspan=4)
  global a1
  global ans1
  ans1 = tkinter.Variable()
  a1 = tkinter.Entry(form,textvariable=ans1)
  a1.grid(row=2,column=2,columnspan=2)
  return form 
#function that updates the question one after another
def q_a(q,clas):
  global q1
  global a1
  global ans1
  q1["text"] = q  #updates the question in the form window 
  def get_a1(self,clas):
    import tkinter
    global a1
    global x
    global ans1
    x = ans1.get()
    a1.delete(0,"end") 
    global error_ct
    if error_ct == 1:
      global error
      error_ct = 0
      error.destroy()
    try:
      if clas == "int":
        int(x)
      elif  clas == "str":
        str(x)
      form.quit()
    except:
      error_ct = 1
      error = tkinter.Label(form,text="Please enter a number")
      error.grid(row=4,column=1)
  a1.bind("<Return>",lambda self,obj=clas: get_a1(self,obj)) #self is used to handle the default input given by the <Return> event
  form.mainloop()
  try:
    global x  
    return x   #will return the text which is inside the entry box present in form window
  except:
    pass
#function that displays the menu and takes the order
def take_order():
  import tkinter
  global status
  global order2
  global my_order,my_ordercount
  my_order = {}
  my_ordercount = []
  order2 = tkinter.Tk() 
  order2.title("Your Order")
  order2.geometry("+600+300")
  tkinter.Label(order2,text="Your current order is:").grid(row = 0,column=0,columnspan=2)
  print_menu(menuu)
  order2.mainloop()
def print_menu(menuu):
  import tkinter
  global menu
  global status
  menu = tkinter.Tk()
  menu.geometry("396x570+850+80")
  tkinter.Label(menu,text="McDonalds",font=("Arial",25)).grid(row=0,rowspan=2,column=4,columnspan=4)
  tkinter.Label(menu,text="Menu",font=("Arial",20)).grid(row=2,column=4,columnspan=4)
  def menu_enter(self,obj):
    x = str(obj).lstrip(".!toplevel.!button")
    if x == "":
      x = "1"
    x = int(x)-1
    if x != 0:
      global my_order,my_ordercount
      items = list(my_order.keys())
      if menuu[x][1] not in items:
        tkinter.Label(order2,text=menuu[x][1],relief="flat").grid(row =len(items)+1,column=0)
        y = tkinter.Label(order2,text="1",relief = "flat")
        y.grid(row = len(items)+1,column=1)
        my_ordercount.append(y)
        my_order[menuu[x][1]] = "1"
        if len(items)==0:
          global order_button
          order_button = tkinter.Button(order2,text="Order now",command=lambda:print_bill(menuu,my_order))
          order_button.grid(row=len(items)+2,column=0,columnspan=2)
        else:
          order_button.grid_configure(row=len(items)+2)
      elif menuu[x][1] in items:
        i = items.index(menuu[x][1])
        y = my_ordercount[i]
        t = int(y["text"])+1
        y["text"] = str(t)
        my_order[menuu[x][1]] = str(t)
  but_list = []
  for i in range(len(menuu)):
    if status=="customer":
      x = tkinter.Button(menu,text=menuu[i][1],command = None,font=("Arial",12),borderwidth=2,relief="raised",width=20)
      x.bind("<1>",lambda event,obj=x:menu_enter(event,obj))
      but_list.append(x)
    elif status=="employee": 
      x = tkinter.Label(menu,text=menuu[i][1],font=("Arial",12),borderwidth=2,relief="raised",width=20)
    x.grid(row=3+i,column=4,columnspan=4)
    tkinter.Label(menu,text=menuu[i][0],font=("Arial",12),borderwidth=2,relief="raised",width=11).grid(row=3+i,column=0,columnspan=4)
    tkinter.Label(menu,text=menuu[i][2],font=("Arial",12),borderwidth=2,relief="raised",width=11).grid(row=3+i,column=8,columnspan=3)
def print_bill(list1,dict1=dict):
  import tkinter
  order2.destroy()
  menu.destroy()
  bill = tkinter.Tk()
  bill.title("Sparsh Vibhu Project")
  bill.geometry("+550+160")
  tkinter.Label(bill,text="McDonalds",font=("Arial",42,"normal")).grid(row=0,column=0,rowspan=2,columnspan=5)
  tkinter.Label(bill,text="Item name",font=("Arial",21,"normal")).grid(row=2,column=0,columnspan=2)
  tkinter.Label(bill,text="Quantity",font=("Arial",21,"normal")).grid(row=2,column=2,columnspan=1)
  tkinter.Label(bill,text="Amount",font=("Arial",21,"normal")).grid(row=2,column=3,columnspan=2)
  items = list(dict1.keys())
  item_info = list(dict1.values())
  total = 0
  for x in range(len(items)):
    for i in list1:
      if i[1] == items[x]:
        cost= int(i[2])
    tkinter.Label(bill,text=items[x],font=("Arial",14,"normal")).grid(row=x+3,column=0,columnspan=2)
    tkinter.Label(bill,text=item_info[x],font=("Arial",14,"normal")).grid(row=x+3,column=2,columnspan=1)
    tkinter.Label(bill,text=str(cost*int(item_info[x])),font=("Arial",14,"normal")).grid(row=x+3,column=3,columnspan=2)
    total = total + cost*int(item_info[x])
  tkinter.Label(bill,text=f"The total amount of your order is {total}",font=("Arial",14,"normal")).grid(row=len(items)+3,column=0,columnspan=5)
  bill.mainloop()