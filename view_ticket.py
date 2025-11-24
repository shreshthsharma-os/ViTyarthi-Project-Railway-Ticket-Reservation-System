def check_pnr_status(bookings_db):
    print("Check Your PNR Status")
    pnr_input=int(input("Enter your PNR number: "))
    
    if pnr_input in bookings_db:
        ticket=bookings_db[pnr_input]
        
        print("Ticket Details:")
        print("PNR:", pnr_input)
        print("Passenger:", ticket['name'])
        print("Train No:", ticket['train_no'])
        print("Train Name:", ticket['train_name'])
        print("Time:", ticket['time'])
        print("Route:", ticket['route'])
        print("Class:", ticket['class'])
        print("Price:", ticket['price'])
    else:
        print("PNR not found in system.Please enter correct PNR.")