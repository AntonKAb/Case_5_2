"""
Class-declaration file.
"""
import random


# TODO
class Hotel:
    rooms = []
    clients = []
    profit = 0


# TODO
class Client:
    def __init__(self, name, surname, middle_name, from_date, days, people, money, hotel):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.fullname = name + surname + middle_name
        self.from_date = from_date
        self.days = days
        self.dates_list = Client._make_dates_list(from_date, days)
        self.days_number = len(self.dates_list)
        self.people = people
        self.money = money
        self.hotel = hotel
        hotel.clients.append(self)

    @staticmethod
    def _make_dates_list(from_date, days):
        day_from, month_from, year_from = list(map(int, from_date.split('.')))
        years = list(range(year_from, year_from+days//365+1))
        time_list = []
        for year in years:
            feb_days = (29 if not year % 400 else (28 if not year % 100 else (29 if not year % 4 else 28)))
            months = [31, feb_days, 31, 30,
                      31, 30, 31, 31,
                      30, 31, 30, 31]
            for month in range(12):
                for day in range(1, months[month]+1):
                    time_list.append((day, month+1, year))
        start_index = time_list.index((day_from, month_from, year_from))
        time_list = time_list[start_index+1:][:days]
        return time_list

    def registration(self):
        rooms = [room for room in self.hotel.rooms if room.capacity >= self.people and not
                 set(room.booking_time) & set(self.dates_list)]
        best_choice = None
        best_choice_price = 0
        best_choice_options = None
        max_profit = 0
        for room in rooms:
            for variant in room.variants:
                if variant['price'] < self.money:
                    if variant['price'] > best_choice_price:
                        best_choice = room
                        best_choice_price = variant['price']
                        best_choice_options = variant['options']
        if random.random() <= 0.7:
            best_choice.booking_time += self.dates_list
            max_profit += best_choice_price * self.people
            answer = True
        else:
            answer = False
        return {
            'answer': answer,
            'best_choice_options': best_choice_options,
            'hotel': self.hotel,
        }


# TODO
class Room:
    def __init__(self, number, type_room, comfort, capacity):
        self.number = number
        self.type_room = type_room
        self.comfort = comfort
        self.capacity = capacity
        self.variants = self.__room_variants()
        self.booking_time = []

    @staticmethod
    def __room_variants():
        massive_list = []
        with open('fund.txt') as f:
            rome_list = f.readlines()
            for i in rome_list:
                _dict = {}
                if i.split()[1] == 'одноместный' and i.split()[-1] == 'стандарт':
                    _dict['price'] = 2900
                    _dict['options'] = 'No meals'
                    massive_list.append(_dict)
                elif i.split()[1] == 'двухместный' and i.split()[-1] == 'стандарт':
                    _dict['price'] = 2300
                    _dict['options'] = 'No meals'
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'стандарт':
                    _dict['price'] = 3200
                    _dict['options'] = 'No meals'
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'стандарт':
                    _dict['price'] = 4100
                    _dict['options'] = 'No meals'
                    massive_list.append(_dict)

                if i.split()[1] == 'одноместный' and i.split()[-1] == 'стандарт_улучшенный':
                    _dict['price'] = 2900 * 1.2
                    _dict['options'] = 'No meals'
                    massive_list.append(_dict)
                elif i.split()[1] == 'двухместный' and i.split()[-1] == 'стандарт_улучшенный':
                    _dict['price'] = 2300 * 1.2
                    _dict['options'] = 'No meals'
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'стандарт_улучшенный':
                    _dict['price'] = 3200 * 1.2
                    _dict['options'] = 'No meals'
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'стандарт_улучшенный':
                    _dict['price'] = 4100 * 1.2
                    _dict['options'] = 'No meals'
                    massive_list.append(_dict)

                if i.split()[1] == 'одноместный' and i.split()[-1] == 'апартамент':
                    _dict['price'] = 2900 * 1.5
                    _dict['options'] = 'No meals'
                    massive_list.append(_dict)
                elif i.split()[1] == 'двухместный' and i.split()[-1] == 'апартамент':
                    _dict['price'] = 2300 * 1.5
                    _dict['options'] = 'No meals'
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'апартамент':
                    _dict['price'] = 3200 * 1.5
                    _dict['options'] = 'No meals'
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'апартамент':
                    _dict['price'] = 4100 * 1.5
                    _dict['options'] = 'No meals'
                    massive_list.append(_dict)

                if i.split()[1] == 'одноместный' and i.split()[-1] == 'стандарт':
                    _dict['price'] = 2900 + 280
                    _dict['options'] = 'Breakfast'
                    massive_list.append(_dict)
                elif i.split()[1] == 'двухместный' and i.split()[-1] == 'стандарт':
                    _dict['price'] = 2300 + 280
                    _dict['options'] = 'Breakfast'
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'стандарт':
                    _dict['price'] = 3200 + 280
                    _dict['options'] = 'Breakfast'
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'стандарт':
                    _dict['price'] = 4100 + 280
                    _dict['options'] = 'Breakfast'
                    massive_list.append(_dict)

                if i.split()[1] == 'одноместный' and i.split()[-1] == 'стандарт_улучшенный':
                    _dict['price'] = 2900 * 1.2 + 280
                    _dict['options'] = 'Breakfast'
                    massive_list.append(_dict)
                elif i.split()[1] == 'двухместный' and i.split()[-1] == 'стандарт_улучшенный':
                    _dict['price'] = 2300 * 1.2 + 280
                    _dict['options'] = 'Breakfast'
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'стандарт_улучшенный':
                    _dict['price'] = 3200 * 1.2 + 280
                    _dict['options'] = 'Breakfast'
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'стандарт_улучшенный':
                    _dict['price'] = 4100 * 1.2 + 280
                    _dict['options'] = 'Breakfast'
                    massive_list.append(_dict)

                if i.split()[1] == 'одноместный' and i.split()[-1] == 'апартамент':
                    _dict['price'] = 2900 * 1.5 + 280
                    _dict['options'] = 'Breakfast'
                    massive_list.append(_dict)
                elif i.split()[1] == 'двухместный' and i.split()[-1] == 'апартамент':
                    _dict['price'] = 2300 * 1.5 + 280
                    _dict['options'] = 'Breakfast'
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'апартамент':
                    _dict['price'] = 3200 * 1.5 + 280
                    _dict['options'] = 'Breakfast'
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'апартамент':
                    _dict['price'] = 4100 * 1.5 + 280
                    _dict['options'] = 'Breakfast'
                    massive_list.append(_dict)

                if i.split()[1] == 'одноместный' and i.split()[-1] == 'стандарт':
                    _dict['price'] = 2900 + 1000
                    _dict['options'] = 'Half board '
                    massive_list.append(_dict)
                elif i.split()[1] == 'двухместный' and i.split()[-1] == 'стандарт':
                    _dict['price'] = 2300 + 1000
                    _dict['options'] = 'Half board '
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'стандарт':
                    _dict['price'] = 3200 + 1000
                    _dict['options'] = 'Half board '
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'стандарт':
                    _dict['price'] = 4100 + 1000
                    _dict['options'] = 'Half board '
                    massive_list.append(_dict)

                if i.split()[1] == 'одноместный' and i.split()[-1] == 'стандарт_улучшенный':
                    _dict['price'] = 2900 * 1.2 + 1000
                    _dict['options'] = 'Half board '
                    massive_list.append(_dict)
                elif i.split()[1] == 'двухместный' and i.split()[-1] == 'стандарт_улучшенный':
                    _dict['price'] = 2300 * 1.2 + 1000
                    _dict['options'] = 'Half board '
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'стандарт_улучшенный':
                    _dict['price'] = 3200 * 1.2 + 1000
                    _dict['options'] = 'Half board '
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'стандарт_улучшенный':
                    _dict['price'] = 4100 * 1.2 + 1000
                    _dict['options'] = 'Half board '
                    massive_list.append(_dict)

                if i.split()[1] == 'одноместный' and i.split()[-1] == 'апартамент':
                    _dict['price'] = 2900 * 1.5 + 1000
                    _dict['options'] = 'Half board '
                    massive_list.append(_dict)
                elif i.split()[1] == 'двухместный' and i.split()[-1] == 'апартамент':
                    _dict['price'] = 2300 * 1.5 + 1000
                    _dict['options'] = 'Half board '
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'апартамент':
                    _dict['price'] = 3200 * 1.5 + 1000
                    _dict['options'] = 'Half board '
                    massive_list.append(_dict)
                elif i.split()[1] == 'полулюкс' and i.split()[-1] == 'апартамент':
                    _dict['price'] = 4100 * 1.5 + 1000
                    _dict['options'] = 'Half board '
                    massive_list.append(_dict)
        return massive_list
