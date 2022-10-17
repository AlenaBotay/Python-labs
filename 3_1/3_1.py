import os
import os.path
import shutil
os.getcwd()
if (os.path.exists("hw3") == False):
    os.mkdir("hw3")              # Пункт 1, создали папку

    
if (os.path.exists("hw3/file.txt") == False):
    with open('hw3/file.txt', 'x') as f1:
        f1.write("Do you believe in Heaven above? Do you believe in love? Don't tell a lie, don't be false or untrueIt all comes back to you")
    
with open('hw3/file.txt', 'w') as f1:
    f1.write("Do you believe in Heaven above? Do you believe in love? Don't tell a lie, don't be false or untrueIt all comes back to you")

# Пункт 2 выполнен, текстовый файл

import json
 
film1 = {
            "name": "Полночь в Париже",
            "release_year": 2011,
            "director": "Вуди Аллен"
}
film2 = {
            "name": "Гравити Фолз",
            "release_year": 2012,
            "creator": "Алекс Хирш"
}
film3 = {
            "name": "Окно во двор",
            "release_year": 1954,
            "director": "Альфред Хичкок"
}    
    

movies = [film1, film2, film3]


if (os.path.exists("hw3/file.json")== False):
    with open("hw3/file.json", "x") as f2:
        json.dump(movies, f2, indent = 4, sort_keys = True)

with open("hw3/file.json", "w") as f2:
    json.dump(movies, f2, indent = 4, sort_keys = True, ensure_ascii=False)
        
# Пункт 3 выполнен

import csv

tabls = [
    ["Cancer Type", "D-Loop", "mRNAs", "tRNAs", "rRNAs", "Nucleotide Position of Deletions", "Increase of mtDNA copy"],
    ["Bladder", 1, 1, 0, 1, 15642-15662, 0, 0],
    ["Breast", 1, 1, 1, 1, 8470-13447 and 8482-13459, 0, 1],
    ["Oral", 1, 1, 0, 0, 8470-13447 and 8482-13459, 0, 0]
        ]

if (os.path.exists("hw3/file.json")== False):
    with open("hw3/file.csv", "x") as f3:
        writer = csv.writer(f3)
        writer.writerows(tabls)
with open("hw3/file.csv", "w") as f3:
    writer = csv.writer(f3)
    writer.writerows(tabls)
    
# Пункт 4 выполнен    
    
if (os.path.exists("hw3/folder") == False):
    os.mkdir("hw3/folder")    
    
    
 # Пункт 5 выполнен   




cwd = os.getcwd()
#Получаем путь в текущую директорию

search_dir = "C:/Users/bagda/Python-labs/lab3/hw3/" #Вот путь
os.chdir(search_dir)
files = filter(os.path.isfile, os.listdir(search_dir))
#Cобрали

files = [os.path.join(search_dir, f) for f in files] # Добавим путь, нужен для сортировки

files.sort(key=lambda x: os.path.getmtime(x))
print(files)       #6
os.chdir("..") 
shutil.rmtree("hw3") #7 удаление папки
