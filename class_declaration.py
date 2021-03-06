"""
Class-declaration file.
"""
import random


class Hotel:
    def __init__(self):
        self.data = '01.03.18'
        self.clients = []
        self.bron = 0
        self.rooms = []
        self.profit = 0
        self.loss = 0
        self.percent = ''
        self.booked_single = 0
        self.booked_double = 0
        self.booked_junior = 0
        self.booked_luxury = 0

    def __str__(self):
        string = f'Итог за {self.data}\n\nКоличество занятых номеров:' \
            f'{len(self.clients)}\n\nКоличество свободных номеров: {len(self.rooms) - self.bron}\n\n' \
            f'Занятость по категориям\n\nОдноместный: {self.booked_single} из {Hotel.__room()["одноместный"]}\n\n' \
            f'Двухместный: {self.booked_double} из {Hotel.__room()["двухместный"]}\n\n' \
            f'Полулюкс: {self.booked_junior} из {Hotel.__room()["полулюкс"]}' \
            f'Люкс: {self.booked_luxury} из {Hotel.__room()["люкс"]}\n\n' \
            f'Доход за день: {self.profit}\n\n' \
            f'Упущенный доход: {self.loss}\n\n' \
            f'Процент загруженности гостиницы: {self.percent}'
        return string

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def __room():
        _dict = {'одноместный': 0, 'двухместный': 0, 'полулюкс': 0, 'люкс': 0}
        with open('fund.txt') as f:
            room_list = list(map(lambda each_room: each_room.rstrip(), f.readlines()))
        for room in room_list:
            _dict[room.split()[1]] += 1
        return _dict


class Client:
    def __init__(self, register_date, name, surname, middle_name, people, from_date, days, money, hotel):
        self.register_date = register_date
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.fullname = name + surname + middle_name
        self.from_date = from_date
        self.days = int(days)
        self.dates_list = self.__make_dates_list()
        self.people = int(people)
        self.money = int(money)
        self.hotel = hotel
        hotel.clients.append(self)

    def __make_dates_list(self):
        day_from, month_from, year_from = list(map(int, self.from_date.split('.')))
        years = list(range(year_from, year_from+self.days//365+1))
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
        time_list = time_list[start_index+1:][:self.days]
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
        if best_choice:
            if random.random() <= 0.7:
                best_choice.booking_time += self.dates_list
                max_profit += best_choice_price * self.people
                answer = True
            else:
                answer = False
        else:
            answer = False
        return {
            'best_choice': best_choice,
            'answer': answer,
            'best_choice_options': best_choice_options,
            'hotel': self.hotel,
        }


class Room:
    def __init__(self, number, type_room, comfort, capacity, hotel):
        self.number = number
        self.type_room = type_room
        self.comfort = comfort
        self.capacity = capacity
        self.variants = self.__room_variants()
        self.booking_time = []
        self.hotel = hotel

    @staticmethod
    def __room_variants():
        massive_list = []
        price_type = {'одноместный': 2900, 'двухместный': 2300, 'полулюкс': 3200, 'люкс': 4100}
        comfort_rate = {'стандарт': 1, 'апартамент': 1.5, 'стандарт_улучшенный': 1.2}
        with open('fund.txt') as f:
            room_list = list(map(lambda each_room: each_room.rstrip(), f.readlines()))
            for room in room_list:
                room_dict = {
                    'number': room.split()[0],
                    'type_room': room.split()[1],
                    'capacity': room.split()[-2],
                    'comfort': room.split()[-1]
                }
                massive_list.append(room_dict)
        for room in massive_list:
            room['price'] = price_type[room['type_room']] * comfort_rate[room['comfort']]
        finish_list = []
        for el in massive_list:
            s_1, s_2, s_3 = el.copy(), el.copy(), el.copy()
            s_1['food'] = 'No meals'
            finish_list.append(s_1)
            s_2['food'] = 'Breakfast'
            s_2['price'] += 280
            finish_list.append(s_2)
            s_3['food'] = 'Half board'
            s_3['price'] += 1000
            finish_list.append(s_3)
        return finish_list
