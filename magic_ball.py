import random

answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print('Привет Мир, Я магический шар, и я знаю ответ на любой твой вопрос.')

name = input('Как тебя зовут: ')
print('Привет',  name)

again = 'д'

while again.lower() == 'д':
    question = input('Задай мне свой вопрос: ')
    print(random.choice(answers))
    again = input('Задать еще один вопрос? (д = да, н = нет): ')
    
    if not again.lower() == 'д':
        print('Возвращайся если возникнут вопросы!')