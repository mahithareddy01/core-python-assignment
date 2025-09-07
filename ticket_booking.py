def available(total, booked):
    return [s for s in range(1, total+1) if s not in booked]
def book(total, booked, seat):
    if seat in booked:
        print(f"Seat {seat} already booked")
    elif 1 <= seat <= total:
        booked.append(seat)
        print(f"Seat {seat} booked")
    else:
        print("Invalid seat")
def cancel(booked, seat):
    if seat in booked:
        booked.remove(seat)
        print(f"Seat {seat} cancelled")
    else:
        print(f"Seat {seat} not booked")
t = int(input("Total seats: "))
booked = list(map(int, input("Initially booked (space separated): ").split()))
while True:
    c = int(input("\n1.Show 2.Book 3.Cancel 4.Exit: "))
    if c == 1:
        print("Available:", available(t, booked))
    elif c == 2:
        book(t, booked, int(input("Seat to book: ")))
    elif c == 3:
        cancel(booked, int(input("Seat to cancel: ")))
    elif c == 4:
        break
