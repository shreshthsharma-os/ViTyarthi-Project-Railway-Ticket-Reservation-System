#import all files to access the user-defined functions
import railway_data
import show_trains
import book_ticket
import view_ticket
import cancel_ticket

def main():

    trains_db=railway_data.initialize_trains()
    bookings_db=railway_data.initialize_bookings()
    
    while True:
        print("\nRAILWAY RESERVATION SYSTEM")
        print("1.Show Available Trains")
        print("2.Book Ticket")
        print("3.Check PNR Status")
        print("4.Cancel Ticket")
        print("5.Exit")
        
        choice=input("Enter your choice(1-5): ")
        
        if choice=='1':
            show_trains.display_available_trains(trains_db)
        elif choice=='2':
            book_ticket.perform_booking(trains_db, bookings_db)
        elif choice=='3':
            view_ticket.check_pnr_status(bookings_db)
        elif choice=='4':
            cancel_ticket.cancel_booking(trains_db, bookings_db)
        elif choice=='5':
            print("THANK YOU FOR USING RAILWAY TICKET RESERVATION SYSTEM")
            break
        else:
            print("Invalid choice.Please enter from number 1 to 5.")

if __name__=="__main__":
    main()