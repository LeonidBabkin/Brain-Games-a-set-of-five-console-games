import prompt
ROUNDS = 3


def start(game):
    print("Welcome to The Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.TASK)
    counter = 1
    while counter <= ROUNDS:
        question, answer = game.generate_round()
        print(question)
        user_ans = prompt.string('Your answer: ')
        if answer == str(user_ans):
            print('Correct!')
            counter += 1
        else:
            print(f'{user_ans} is wrong answer ;(. Correct answer was {answer}')
            return print(f'Let\'s try again, {name}!')
    print(f'Congratulations, {name}!')
