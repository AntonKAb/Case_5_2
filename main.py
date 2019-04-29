"""
Case 5.
Developers: Kabaev A., Anufrienko K.
"""

from class_declaration import Hotel, Client, Room


def main():
    hotel = Hotel()
    rooms_list = []
    with open('fund.txt') as f:
        rooms_list = list(map(lambda rooms_data: rooms_data.rstrip(), f.readlines()))
    rooms = [Room(*room_info) for room_info in rooms_list]
    clients_list = []
    clients_amount = []
    money_earn = []
    money_lose = []
    with open('booking.txt') as f:
        clients_list = list(map(lambda client_data: client_data.rstrip(), f.readlines()))
    clients = [Client(*client_info, hotel=hotel) for client_info in clients_list]
    for hotel_client in clients:
        reg_params = hotel_client.registration()
        print('Поступила заявка на бронирование:\n')
        print('{} {} {} {} {} {} {} {}\n').format(hotel_client.register_date, hotel_client.surname,
                                                  hotel_client.name, hotel_client.middle_name,
                                                  hotel_client.people, hotel_client.from_date,
                                                  hotel_client.days, hotel_client.money)
        reg_options = reg_params['best_choice_options']
        if reg_params['best_choice'] is None:
            print('Предложений по данному запросу не найдено. В бронировании отказано.\n')
        else:
            print('Найден:\n')
            outinfo = [
                reg_params['best_choice'].number,
                reg_options['type_room'],
                reg_options['comfort'],
                reg_params['best_choice'].capacity,
                hotel_client.people,
                f' {reg_options["food"]}',
                reg_options['price']
            ]
            print('номер {} {} {} рассчитан на {} чел. фактически {} чел.{} стоимость {} руб./сутки'.format(*outinfo))
            (print('Клиент согласен. Номер забронирован.\n',
             clients_amount.append(hotel_client), money_earn.append(reg_options['price'] * int(hotel_client.days)))
             if reg_params['answer'] is True else
                (print('Клиент отказался от варианта'),
                 (money_lose.append(reg_options['price'] * int(hotel_client.days)))))
        # hotel_condition = Hotel(rooms=len(rooms), clients=len(clients_amount),
        #                         profit=sum(money_earn), loss=sum(money_lose),
        #                         data='01.03.2018 Any data',
        #                         percent=str(round((len(rooms) - clients_amount) * 100 / len(rooms), 2)) + ' %')
        # print(hotel_condition)


if __name__ == '__main__':
    main()
