import math
import re
import datetime
from collections import Counter
from subprocess import (
    run, PIPE
)

result_dict = {}
result_list = []
result_user_list = []
list_of_string = []
all_mem_used = 0
all_CPU_used = 0
file_name = datetime.datetime.now().strftime("%d-%m-%Y-%H:%M") + "-scan.txt"

result = run(["ps", "aux"], stderr=PIPE, stdout=PIPE)
result = result.stdout.decode("utf-8")
res_string = result.split("\n")
del res_string[-1]
del res_string[0]
for string in res_string:
    s = re.sub(r'\s+', ' ', string).split(" ")
    result_dict['USER'] = s[0]
    result_dict['PID'] = s[1]
    result_dict['%CPU'] = s[2]
    result_dict['%MEM'] = s[3]
    result_dict['VSZ'] = s[4]
    result_dict['RSS'] = s[5]
    result_dict['TTY'] = s[6]
    result_dict['STAT'] = s[7]
    result_dict['START'] = s[8]
    result_dict['TIME'] = s[9]
    result_dict['COMMAND'] = s[10]
    all_mem_used += float(s[3])
    all_CPU_used += float(s[2])
    result_list.append(dict(result_dict))
    result_user_list.append(s[0])

users = set(result_user_list)
user_dict = Counter(result_user_list)
after_sort = sorted(result_list, key=lambda mem: float(mem['%MEM']), reverse=True)
mem_app = str(after_sort[0]['COMMAND'])
after_sort = sorted(result_list, key=lambda cpu: float(cpu['%CPU']), reverse=True)
cpu_app = str(after_sort[0]['COMMAND'])
with open(file_name, "w") as f:
    f.write("Пользователи системы: " + str(list(users)) + "\n")
    f.write("Процессов запущено: " + str(len(result_user_list)) + "\n")
    f.write("Процессов по пользователям: " + str(user_dict) + "\n")
    f.write("Всего памяти используется: " + str(math.ceil(all_mem_used)) + "%\n")
    f.write("Больше всего памяти ест: " + mem_app + "\n")
    f.write("Всего CPU используется: " + str(math.ceil(all_CPU_used)) + "%\n")
    f.write("Больше всего CPU ест: " + cpu_app + "\n")

print("Пользователи системы: " + str(list(users)))
print("Процессов запущено: " + str(len(result_user_list)))
print("Процессов по пользователям: " + str(user_dict))
print("Всего памяти используется: " + str(math.ceil(all_mem_used)) + "%")
print("Больше всего памяти ест: " + mem_app)
print("Всего CPU используется: " + str(math.ceil(all_CPU_used)) + "%")
print("Больше всего CPU ест: " + cpu_app)
