class TicketBookingSystem:
    def __init__(self, total_vip, total_regular):
        self.total_vip = total_vip
        self.total_regular = total_regular
        self.available_vip = total_vip
        self.available_regular = total_regular
        self.booked_tickets = {}

    def display_available_seats(self):
        print(f"Available VIP Seats: {self.available_vip}")
        print(f"Available Regular Seats: {self.available_regular}")

    def book_ticket(self, name, seat_type, num):
        if seat_type == 'VIP':
            if self.available_vip > 0 and self.available_vip >= num:
                self.booked_tickets[name] = seat_type
                self.available_vip -= num
                print("VIP ticket booked successfully for ", name, "Price:", 2200 * num, "rs")
            else:
                print("Sorry, no VIP seats available!")
        elif seat_type == 'Regular':
            if self.available_regular > 0 and self.available_regular>=num:
                self.booked_tickets[name] = seat_type
                self.available_regular -= num
                print(f"Regular ticket booked successfully for {name}. Price: {1000*num}rs")
            else:
                print("Sorry, no Regular seats available!")
        else:
            print("Invalid seat type! Please choose either 'VIP' or 'Regular'.")

    def cancel_ticket(self, name,r):
        if name in self.booked_tickets:
            seat_type = self.booked_tickets[name]
            if seat_type=='VIP':
                self.available_vip += 1
            else:
                self.available_regular +=1
            del self.booked_tickets[name]
            print("Ticket canceled for", name)
            print("Reason for cancelling:",r)
            print("Thank You!!!!")
        else:
            print(f"No booking found for {name}.")

    def show_booked_tickets(self):
        if self.booked_tickets:
            print("Booked Tickets:")
            for name, seat_type in self.booked_tickets.items():
                print(f"- {name}: {seat_type}")
        else:
            print("No tickets booked yet.")

    def search_booking(self, name):
        if name in self.booked_tickets:
            seat_type = self.booked_tickets[name]
            print(f"Booking found: {name} has a {seat_type} ticket.")
        else:
            print(f"No booking found for {name}.")


def main():
    total_vip = int(input("Enter total number of VIP seats: "))
    total_regular = int(input("Enter total number of Regular seats: "))
    system = TicketBookingSystem(total_vip, total_regular)

    while True:
        print("\nMenu:")
        print("1. Display available seats")
        print("2. Book a ticket")
        print("3. Cancel a ticket")
        print("4. Show booked tickets")
        print("5. Search for a booking")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            system.display_available_seats()
        elif choice == '2':
            name = input("Enter the name for booking: ")
            seat_type = input("Choose seat type (VIP/Regular): ")
            num = int(input("Enter no of tickets to be booked:"))
            system.book_ticket(name, seat_type, num)
        elif choice == '3':
            name = input("Enter the name to cancel booking: ")
            r=input("Reason for cancelling:")
            system.cancel_ticket(name,r)
        elif choice == '4':
            system.show_booked_tickets()
        elif choice == '5':
            name = input("Enter the name to search booking: ")
            system.search_booking(name)
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice! Please choose again.")


if __name__ == "__main__":
    main()