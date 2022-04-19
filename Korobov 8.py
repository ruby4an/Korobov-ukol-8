class Human:
    def __init__(self, person_id):
        first_part = person_id.split('/')[0]
        self.year = int(first_part[:2])
        self.month = int(first_part[2:4])
        if self.month > 12:
            self.gender = 'Female'
            self.month -= 50
        else:
            self.gender = 'Male'
        self.day = int(first_part[4:6])

    def __str__(self):
        return f'Day {self.day} Month {self.month} Year {self.year} \n Gender: {self.gender}'


def input_id():
    while True:
        number_id = input('Input number')
        try:
            number_id = int(number_id)
            if number_id < 0:
                print('Wrong ID. Try again')
                continue  # we didn't study this, but I found it by myself...
            return number_id
        except ValueError:
            print('Wrong ID. Try again')


num = input_id()
Dima = Human(str(num))
print(Dima)
