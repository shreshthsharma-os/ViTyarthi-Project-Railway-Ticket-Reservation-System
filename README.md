# ViTyarthi-Project-Railway-Ticket-Reservation-System

Railway Ticket Reservation System - RTRS

Overview of the Project

RTRS is an integrated information system designed to replace manual, paper-based processes for ticketing. It provides a secure and efficient interface to passengers and railway administrators. The system can maintain, in real time, data related to train schedules and bookings and allows the user to access information regarding train seat/berth availability and to manage railway reservations in a very user-friendly manner.

Features

The system carries out modular functions for major railway activities including:

Train/User Setup: Add_Train / Register_User - This module allows an administrator to add a new train to the database, including details such as the train number, source, destination, and total seats. It also allows new users to persistently register their profiles.

Book Ticket(Book_Ticket): This is similar to depositing money, which reserves a seat for the user on the already existing train. It contains logic to check the availability of seats and updates the count after confirmation of the booking.

Cancel Ticket (Cancel_Ticket): A user can cancel a certain booking. It provides logic to verify the PNR/Ticket ID and refunds the seat back to the pool of availability, which means incrementing the available seat count.

Display Status(Display_PNR): Through this, the current status of the booking (Confirmed/Waiting) and passenger details for a given PNR or Ticket ID will be fetched and presented.

Remove Train (Delete_Train): This option allows the administrator to irreversibly remove a train from the schedule, once confirmed; useful for managing obsolete routes.

Main Menu - main.py: This contains a simple, interactive, console-based menu for the user to navigate to major functionalities (Booking, Cancelling, Status, Admin).

Technologies Used:

1)Language: Python 3.13.3
2)Tools: VS Code, Git

Steps to Install & Run:

1)Make sure Python is installed on your system.
2)Clone the repository to your local machine.
