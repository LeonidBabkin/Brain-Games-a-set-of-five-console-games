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
        us_input = prompt.string('Your answer: ')
        if answer == str(us_input):
            print('Correct!')
            counter += 1
        else:
            print(f'{us_input} is wrong answer ;(. Correct answer was {answer}')
            return print(f'Let\'s try again, {name}!')
    print(f'Congratulations, {name}!')
