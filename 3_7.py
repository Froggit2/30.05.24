#Я сделал так что бы можно было любые переменые задавать :)
team1_num = int(input('Кол-во участников команды 1:'))
team2_num = int(input('Кол-во участников команды 2:'))
team1_time = int(input('Время на задания 1 команда:'))
team2_time = int(input('Время на задания 2 команда:'))
score_1 = int(input('Сделано 1 командой задач:'))
score_2 = int(input('Сделано 2 командой задач:'))
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'
print("В команде Мастера кода участников: %s!" % team1_num)
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))
print()
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {} с !".format(team1_time))
print()
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {challenge_result}")
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time)/2
print(f"Сегодня было решенно {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")