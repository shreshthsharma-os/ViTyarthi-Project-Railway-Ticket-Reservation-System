Problem Statement & Scope

1. Problem Statement
The manual railway ticketing system involves great inconvenience to passengers in terms of long queues, paper-based record-keeping, and no real-time information related to the availability of seats. Manual processing is highly error-prone, time-consuming, and inefficient for administrators trying to manage dynamic train schedules and cancellation requests.

This project therefore seeks to address these problems by digitizing the process, offering immediate booking, automatic checking of availability, and error-free data management.

2. Scope of the Project

The aim of this project is to construct a console-based application, capable of simulating a functional railway reservation environment. The system shall focus on:

Computerized Record Keeping: Replace manual registers with persistent storage (File Handling/Database) for data regarding trains and passengers.

Transaction Management: This is to handle the logic of booking and cancellation, ensuring that the seat count updates automatically. For example, cancellation should increase the count of available seats.

Verification: To provide a mechanism to verify the status of bookings using unique identifiers for each, known as PNR.

Administration: Providing administrative control to handle the fleet of trains-addition/deletion of trains.

3. Target Users

The system targets two major groups of users:

The end-users are passengers who want to know the availability of trains, book tickets for their travel, and cancel tickets when necessary.

Administrators: railway staff who are responsible for adding trains, removing obsolete routes, and keeping track of bookings.

4. High-Level Features

According to functional requirements, the system implements the following features:

Train Management (Admin):

Add Train: capability to define new trains with Source, Destination, and Seat Capacity.

Delete Train: ability to delete trains from the network.

Reservation System (User)

Book Ticket: The user can provide travel details, and the system allocates seats if available along with a unique PNR.

Cancel Ticket: The user can enter the PNR to cancel a booking, which automatically updates the seat availability of a particular train. Query System: PNR Status : Get and display passenger and booking status by using Ticket ID. Show All Trains: List all the trains available along with the seat count for each.
