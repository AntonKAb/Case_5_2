"""
Class-declaration file.
"""


# TODO
class Hotel:
    pass


# TODO
class Client:
    pass


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
