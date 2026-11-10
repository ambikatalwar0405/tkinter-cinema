import tkinter as tk 
from tkinter import ttk 


seat_variables = {} 
basket_widgets = []

prices = {"Adult": 12.00, "Child": 8.00, "Student":10.00, "Senior": 9.00}



def addtobasket():
    for widget in basket_widgets:  #clear any existing widgets. this program works by refreshing the list every time a new seat is selected
        widget.grid_forget()
        widget.destroy()
    basket_widgets.clear()

    selected_seats = []
    for seat_name, seat_status in seat_variables.items(): 
        if seat_status.get() == True: #if a seat is selected 
            selected_seats.append(seat_name) #append it to the list of selected seats

    for index, seat_name in enumerate(selected_seats): 
        basket_row = index + 1

        seat = ttk.Label(    #generate the text showing the selected seat
            panel, 
            text=seat_name
        )
        seat.grid(row=basket_row, column=6, padx=5, pady=2, sticky="w") #grid() has to occur on a seperate line here because buttons are assigned to a variable, else would return None

        basket_widgets.append(seat)

        ticket_type_var = tk.StringVar(value="Adult") 

        ticket_type = ttk.Combobox(  #create the ticket type dropdown
            panel,
            textvariable=ticket_type_var, 
            values=list(prices.keys()),
            width=10,
            state="readonly",
        )
        ticket_type.grid(row=basket_row, column=7, padx=5, pady=2)
        
        basket_widgets.append(ticket_type)


        price = tk.Label( #create the price display
            panel, 
            text="£0.00"
        )
        price.grid(row=basket_row, column=8, padx=5, pady=2, sticky="e")

        basket_widgets.append(price)

        #change the price when one of the dropdown options is selected
        ticket_type.bind(
            "<<ComboboxSelected>>",
            lambda event, pr=price, tt=ticket_type: change_price(
                event, pr, tt  #a nested function 
            ),
        )



    
    #added.set(selected_seats) #update the displayed list of added seats


def change_price(event, price_label, dropdown): #event needs to be a parameter because it's used by .bind()
    selected_type = dropdown.get()
    text_to_display = f"£{prices.get(selected_type):.2f}" #get the price ascribed to that ticket type, display with 2 decimal points
    price_label.config(text=text_to_display) #display the price in the price 


root = tk.Tk() 
root.title("Cinema Tickets") 
root.minsize(360, 170) 
root.columnconfigure(0, weight=1) 
root.rowconfigure(0, weight=1) #sets up the rows of the grid
panel = ttk.Frame(root, padding=16) #frame creates a container you can organise widgets in
panel.grid(row=0, column=0, sticky="nsew") #sticky here makes sure that the grid fills out the window

#added = tk.StringVar(master=root, value="When you choose a ticket, it will appear here.") 


#create all the seat buttons
for row in range(5):
    for col in range(5):
        seat_name = f"{chr(row+65)}{col+1}"

        seat_var = tk.BooleanVar(value=False) #each seat is either selected or not
        seat_variables[seat_name] = seat_var

        tk.Checkbutton(
            panel,
            text=seat_name,
            variable=seat_var,
            width=10,
            height=5,
            indicatoron=False, #makes the check buttons look like normal ones whilst letting us use checkbutton methods
            selectcolor="green",
            command=addtobasket,
        ).grid(row=row, column=col, padx=10, pady=10)

ttk.Label(panel, text="Basket").grid(row=0, column=6, columnspan=2, pady=10) #basket header

# ttk.Label(panel, textvariable=added).grid( 
#     row=1, column=6, columnspan=2 
# ) #list of added seats appears here

root.mainloop()

