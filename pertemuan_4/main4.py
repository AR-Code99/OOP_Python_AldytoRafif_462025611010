class Gamer:
    username = ''
    skor = 0
    level = 0

    def cek_username(self):
        print(f'Halo {self.username}, Skor Anda adalah {self.skor}, sekarang level {self.level}')

    def __init__(self, username='', skor=0, level=0):
        if skor < 0:
            raise ValueError('Skor tidak boleh negatif')
        self.username = username
        self.level = level
        self.skor = skor
        print('Username anda aktif')

    def __str__(self):
        return f'Player: {self.username} - Level: {self.level}, Skor: {self.skor}'

    def __eq__(self, other):
        return self.username == other.username and self.skor == other.skor and self.level == other.level

    def __ge__(self, other):
        return self.skor >= other.skor
    
    def __le__(self, other):
        return self.skor <= other.skor

user1 = Gamer('Kiboy969', 67890, 41)
user1.cek_username()
user2 = Gamer('karltzy', 54321, 35)
user2.cek_username()
user3 = Gamer('Alex', 60890, 38)
user3.cek_username()

print(user1)
print(user3 <= user1)
print(user1 == user2)
print(user1 >= user2)

