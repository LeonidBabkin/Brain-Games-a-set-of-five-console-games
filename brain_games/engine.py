import prompt
CYCLES = 3


def gamestart_func(game):  # call a whole module:calc,even,progression and so on
    print("Welcome to The Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.TASK)  # call a constant from a module.
    counter = 1
    while counter <= CYCLES:
        question, answer = game.calc_func()  # call a function
        print(question)
        user_input = prompt.string('Your answer: ')
        if answer == user_input:
            print('Correct!')
            counter += 1
        else:
            print(f'{user_input} is wrong answer ;(. Correct answer was {answer}')
            return print(f'Let\'s try again, {name}!')


    print(f'Congratulations, {name}!')
