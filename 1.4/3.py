import math

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.axes import Subplot

fields = ["age", "sex", "weight", "childs", "smoker", "region", "price"]

dct = {}
for f in fields:
    dct[f] = []

sex_cl = {"male": 0, "female": 1}

region_cl = {"northwest": 0, "southwest": 1, "southeast": 2, "northeast": 3}

with open("./files/dataset_home.txt", "r") as f:
    for l in f.readlines():
        l = l.strip()
        lspl = l.split(',')

        dct["age"].append(int(lspl[fields.index("age")]))
        dct["sex"].append(sex_cl[lspl[fields.index("sex")]])
        dct["weight"].append(float(lspl[fields.index("weight")]))
        dct["childs"].append(int(lspl[fields.index("childs")]))
        dct["smoker"].append(0 if lspl[fields.index("smoker")] == "no" else 1)
        dct["region"].append(int(region_cl[lspl[fields.index("region")]]))
        dct["price"].append(float(lspl[fields.index("price")]))

arr = np.empty((len(dct[fields[0]]), 0))
for f in fields:
    arr = np.c_[arr, np.array(dct[f])]

# print(arr.shape)


# def c_n_k(v: int):
# return math.factorial(v) / (math.factorial(2) * math.factorial(v - 2))


# cols = 5
# rows = math.ceil(c_n_k(len(fields)) / cols)
# print("rows ", rows)

# fig, axs = plt.subplots(rows, cols, figsize=(20, 15), dpi=60)

# cntr = 0
# for i in range(len(fields)):
#     i_f = fields[i]
#     for j in range(i + 1, len(fields)):
#         j_f = fields[j]
#         print(cntr, math.floor(cntr / cols), cntr % cols)
#         ax = axs[math.floor(cntr / cols), cntr % cols]
#         ax.scatter(arr[:, i], arr[:, j], )
#         ax.set_xlabel(fields[i])
#         ax.set_ylabel(fields[j])
#
#         plt.sca(ax)
#         if i_f == "sex":
#             plt.xticks([0, 1], ["male", "female"], color='red')
#         elif i_f == "smoker":
#             plt.xticks([0, 1], ["no", "yes"], color='red')
#         elif i_f == "region":
#             keys_idx = sorted(region_cl.values())
#             plt.xticks(range(len(region_cl)), [list(region_cl.keys())[idx] for idx in keys_idx], color='red')
#
#         if j_f == "sex":
#             plt.yticks([0, 1], ["male", "female"], color='red')
#         elif j_f == "smoker":
#             plt.yticks([0, 1], ["no", "yes"], color='red')
#         elif j_f == "region":
#             keys_idx = sorted(region_cl.values())
#             plt.yticks(range(len(region_cl)), [list(region_cl.keys())[idx] for idx in keys_idx], color='red')
#
#         cntr += 1
# plt.show()


# Отношение возраста к цене
# plt.scatter(dct["age"],dct["price"])
# plt.xlabel("age")
# plt.ylabel("price")
# plt.show()

# Отношение курильщик - к количеству детей
# plt.figure()
# s = [np.count_nonzero((arr[:,  fields.index("childs")] == dct["childs"][i])&(arr[:,  fields.index("smoker")] == dct["smoker"][i])) for i in
#      range(len(dct["smoker"]))]
# plt.scatter(dct["smoker"], dct["childs"],s=s)
# plt.xlabel("is smoker")
# plt.xticks([0, 1], ["no", "yes"], color='red')
# plt.ylabel("childs")
# plt.show()
# можно сделать вывод, что курильщик с меньшей вероятностью доживает до количества детей некурящего человека


# Отношение региона к цене
# plt.scatter(dct["region"],dct["price"])
# plt.xlabel("region")
# plt.ylabel("price")
# plt.show()
# не заморачиваясь с xtick для региона видим, что корелляции практически нет


#Количество курящих к возрасту
# print(arr[arr[:,4]==0][:,0])
# plt.hist(arr[arr[:,4]==0][:,0],label="no smoke")
# plt.hist(arr[arr[:,4]==1][:,0],label="smoke")
# plt.legend()
# plt.ylabel("age")
# plt.show()

#Отношение курения к массе тела
# plt.hist(arr[arr[:,4]==0][:,2],label="no smoke")
# plt.hist(arr[arr[:,4]==1][:,2],label="smoke")
# plt.legend()
# plt.ylabel("weigth")
# plt.show()
#Как будто бы есть корелляция - у курильщиков масса тела меньше

#Отношение курения к полу
# plt.hist(arr[arr[:,4]==0][:,1],label="no smoke")
# plt.hist(arr[arr[:,4]==1][:,1],label="smoke")
# plt.legend()
# plt.ylabel("weight")
# plt.show()
#Распределено равномерно


#Количество курящих к цене страховки
# print(arr[arr[:,4]==0][:,0])
# plt.hist(arr[arr[:,4]==0][:,6],label="no smoke")
# plt.hist(arr[arr[:,4]==1][:,6],label="smoke")
# plt.legend()
# plt.ylabel("price")
# plt.show()
#Как будто бы страховка у курильщиков дороже


# plt.scatter(dct["weight"],dct["price"])
# plt.show()
#у людей с небольшим индексом массы страховка стоит дешевле


#Пол к цене страховки
# plt.hist(arr[arr[:,1]==0][:,6],label="male")
# plt.hist(arr[arr[:,1]==1][:,6],label="female")
# plt.legend()
# plt.ylabel("price")
# plt.show()
#Нет корелляции


#Количество детей к цене страховки
# plt.scatter(dct["childs"],dct["price"])
# plt.show()
#у людей с 5ю детьми почему-то страховка дешевле

#Средняя цена от количества детей
barx=np.arange(np.max(arr[:,fields.index("childs")]))
prices=[arr[arr[:,fields.index("childs")]==i][:,6] for i in barx]
# plt.bar(barx,[np.mean(t) for t in prices])
# plt.show()
#Можно пренебречь

#Максимальная цена от количества детей
# plt.bar(barx,[np.max(t) for t in prices])
# plt.show()


plt.scatter(dct["age"],dct["price"])
plt.show()
#При повышении возраста цена линейно растет