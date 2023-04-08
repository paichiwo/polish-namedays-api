# Polish Name Days API

import requests
from datetime import date


def polish_date():
    # Date - English to Polish translation

    # Get today's date
    today = date.today()
    # Get weekday and use dictionary for translation
    day = (today.strftime('%w'))
    days_translation = {
        '1': 'Poniedziałek',
        '2': 'Wtorek',
        '3': 'Środa',
        '4': 'Czwartek',
        '5': 'Piątek',
        '6': 'Sobota',
        '7': 'Niedziela'
    }
    # Get month day and use dictionary for translation
    month = (today.strftime('%m'))
    months_translation = {
        '01': 'Styczeń',
        '02': 'Luty',
        '03': 'Marzec',
        '04': 'Kwiecień',
        '05': 'Maj',
        '06': 'Czerwiec',
        '07': 'Lipiec',
        '08': 'Sierpień',
        '09': 'Wrzesień',
        '10': 'Październik',
        '11': 'Listopad',
        '12': 'Grudzień'
    }
    # Translate month, day
    month_pl = months_translation[month]
    day_pl = days_translation[day]

    return today.strftime(day_pl + ' %d ' + month_pl + ' %Y')


def get_name_day():
    # Free public API to get name days for number of countries
    url = "https://nameday.abalin.net/api/V1/today"
    response = requests.get(url)

    # Outputs dictionary of name days
    name_days = response.json()
    polish_name_day = name_days['nameday']['pl']  # ['pl'] can be changed to get name days for a different country

    return polish_name_day


print(polish_date())
print('Imieniny obchodzą dziś:')
print(get_name_day())
