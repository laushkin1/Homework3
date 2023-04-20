from datetime import datetime
from collections import defaultdict


def get_birthdays_per_week(users: list) -> None:
    corrent_datetime = datetime.now()
    containers = []

    for i in users:
        for j in i.items():
            if j[1].month == corrent_datetime.month:
                if j[1].day - corrent_datetime.day <= 7:

                    time_date = datetime(
                        year=corrent_datetime.year,
                        month=j[1].month,
                        day=j[1].day)
                    if time_date.strftime('%A') == 'Saturday' or time_date.strftime('%A') == 'Sunday':
                        containers.append('Monday' + ': ' + j[0])
                    else:
                        containers.append(
                            time_date.strftime('%A') + ': ' + j[0])

    containers_ddict = defaultdict(list)
    for element in containers:
        e = element.split(': ')
        char = e[0]
        containers_ddict[char].append(e[1])

    for k in dict(containers_ddict):
        time_string = ''
        for v in dict(containers_ddict)[k]:
            time_string += v + ', '
        t = time_string.removesuffix(', ')
        
        print(f'{k}: {t}')



if __name__ == '__main__':

    users = [
        {'Mike': datetime(year=2001, month=4, day=21)},
        {'John': datetime(year=2001, month=4, day=22)},
        {'Dave': datetime(year=2001, month=4, day=23)},
        {'Jack': datetime(year=2001, month=4, day=24)},
        {'Max': datetime(year=2001, month=4, day=25)},
        {'Leon': datetime(year=2001, month=4, day=26)},
        {'Bogdan': datetime(year=2001, month=4, day=27)}
    ]

    get_birthdays_per_week(users)
