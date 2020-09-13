def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


    
def step2_no_umbrella():
    print(
        'Начался дождь. '
        'Вернуться?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step1()
    return step3_wet()

def step2_umbrella():
    print(
        'Утка пришла в бар, но у нее нет денег. '
        'Заработать? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step4_earn()
    
    return step3_grenka()

def step3_wet():
    print(
        'Утка-маляр 🦆 промокла и заболела. '
        'Вернуться домой?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step1()
    return step2_umbrella()

def step4_earn():
    print(
        'Утка-маляр 🦆 идет красить стены?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        return step5_paint()
    print('Game Over: Утка подралась с бомжом за 3 рубля')
    return 0

def step5_paint():
    print(
        'Утка-маляр 🦆 заработала кучу денег и скупила весь бар вместе с сотрудниками. '
        'Заказывать что-нибудь будем?'
    )
    option = ''
    options = {'сок': True, 'горючее': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        print('WIN: Теперь утка довольна')
        return 0
    print('Game Over: Утка пропила все деньги и бар')
    return 1

def step3_grenka():
    print(
        'Утка-маляр 🦆 стащила гренку, ее поймал бармен. '
        'убежать или сдаться?'
    )
    option = ''
    options = {'убежать': True, 'сдаться': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    
    if options[option]:
        print('WIN: Теперь утка довольна')
        return 0
    print('Game Over: Утку посадили')
    return 1

if __name__ == '__main__':
    step1()
