# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, hours, rate, bonus = argv
u_hours=int(hours)
u_rate=int(rate)
u_bonus=int(bonus)
def salary(hours,rate,bonus):
    return (hours*rate)+bonus
print(f"Заработная плата сотрудника = {salary(u_hours,u_rate,u_bonus)}")