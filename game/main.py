import random

def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()
    
    if not user_option in options:
        print('Esa opción no es valida, intente de nuevo!')
        return None, None
    
    computer_option = random.choice(options)
    
    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    
    return user_option, computer_option

def check_rules(user_option, computer_option, user_wins, computer_wins): 
    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a Tijera')
            print('User gana!')
            user_wins += 1
        else:
            print('Papel gana a Piedra')
            print('Computer gana!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('User gana!')
            user_wins += 1
        else:
            print('Tijera gana a Papel')
            print('Computer gana!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a Papel')
            print('User gana!')
            user_wins += 1
        else:
            print('Piedra gana a Tijera')
            print('Computer gana!')
            computer_wins += 1
    
    return user_wins, computer_wins
    
def check_winner(user_wins, computer_wins):
    if computer_wins == 2:
        print('El ganador es Computer!')
        exit()
    
    if user_wins == 2:
        print('El ganador es User!')
        exit()
    
    
def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1
         
    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
        print('computer_wins', computer_wins)
        print('user_wins', user_wins)
        
        rounds += 1
        
        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        check_winner(user_wins, computer_wins)

run_game()