class UnderAgeError(Exception):
    pass

class SeatAlreadyBookedError(Exception):
    pass

class InvalidPromoCodeError(Exception):
    pass

class TicketBookingSystem:
    def __init__(self, movie_title, minimum_age, valid_promo):
        self.movie_title = movie_title
        self.minimum_age = minimum_age
        self.booked_seats = []
        self.valid_promo = valid_promo

    def check_age_requirement(self, user_age):
        if user_age < self.minimum_age:
            raise UnderAgeError(f"Invalid, Umur penonton {user_age} tahun, di bawah batas minimal yaitu {self.minimum_age}+ untuk film {self.movie_title}.")

    def book_seat(self, user_id, seat_number, user_age):
        self.check_age_requirement(user_age)
        
        if seat_number in self.booked_seats:
            raise SeatAlreadyBookedError(f"Maaf, Kursi {seat_number} sudah dipesan oleh pelanggan lain.")
        
        self.booked_seats.append(seat_number)
        print(f"Sukses, Penonton '{user_id}' berhasil memesan kursi {seat_number}.")

    def apply_promo(self, promo_code):
        if promo_code not in self.valid_promo:
            raise InvalidPromoCodeError(f"Invalid, Kode promo '{promo_code}' tidak valid.")
        
        print(f"Sukses, Kode promo '{promo_code}' berhasil digunakan, Anda mendapat diskon.")

cinema = TicketBookingSystem("Deadpool & Wolverine", 17, ["NONTONHEMAT", "DISKONWEEKEND"])

try:
    cinema.book_seat(user_id="Aldyto", seat_number="A1", user_age=22)
    cinema.apply_promo("NONTONHEMAT")
    cinema.apply_promo("CASHBACK100")

except UnderAgeError as e:
    print(e)
except SeatAlreadyBookedError as e:
    print(e)
except InvalidPromoCodeError as e:
    print(e)

try:
    cinema.book_seat(user_id="Joko", seat_number="A1", user_age=16)
    
except UnderAgeError as e:
    print(e)
except SeatAlreadyBookedError as e:
    print(e)
