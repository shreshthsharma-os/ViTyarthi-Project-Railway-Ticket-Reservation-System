def cancel_booking(trains_db, bookings_db):
    print("\nCancel Ticket")
    pnr_input=int(input("Enter PNR number to cancel: "))
    
    if pnr_input in bookings_db:
        
        booking=bookings_db[pnr_input]
        train_num=booking["train_no"]
        travel_class=booking["class"]
        confirm=input(f"Confirm cancellation for PNR {pnr_input}? (yes/no): ").lower()
        
        if confirm=='yes':
            if train_num in trains_db:
                trains_db[train_num]["classes"][travel_class]["seats"]+=1
            del bookings_db[pnr_input]
            print("Ticket cancelled successfully. Refund will be isssued within 24 hours.")
        else:
            print("Cancellation aborted.")
    else:
        print("PNR not found.")