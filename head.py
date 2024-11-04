try:
    import tkinter
except:
    print("You must install tkinter using pip to use this program")
    exit()
import func
status = func.know_user()
print(status)
if status.lower() == "employee":
    form = func.know_menu()
    n_items = int(func.q_a("Number of items in your menu is?","int"))
    mylist = [("S.no","Items","Price")]
    for i in range(n_items):
        tup = (i+1,)
        x1 = (func.q_a(f"What is item number {i+1} name?","str")).capitalize()
        tup = tup + (x1,)
        x1 = func.q_a(f"What is the price for {x1}?","int")
        tup = tup + (x1,)
        mylist.append(tup)
        try:
            func.menu.destroy()
        except:
            pass
        func.print_menu(mylist)
    form.destroy()
    from func import menu
    menu.geometry("396x570+425+40")
    menu.mainloop()
if status.lower() == "customer":
    func.take_order()