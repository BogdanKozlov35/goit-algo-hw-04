    #fh = open("cats.txt", "w", encoding="UTF-8")
#fh.write(
#         "60b90c1c13067a15887e1ae1,Tayson,3\n"
#         "60b90c2413067a15887e1ae2,Vika,1\n"
#         "60b90c2e13067a15887e1ae3,Barsik,2\n"
#         "60b90c3b13067a15887e1ae4,Simon,12\n"
#         "60b90c4613067a15887e1ae5,Tessi,5\n"
#         )
#fh.close()

import pathlib
def get_cats_info(path):
    try:
        with open("cats.txt", "r", encoding="UTF-8") as fh:
            cats_list = fh.readlines()
            cats_info = []

            for line in cats_list:
                line = line.strip().split(',')
                if len(line) == 3:
                    cats_info.append({"id": line[0], "name":line[1], "age":line[2]})
                else:
                    return f"невірно введені дані в строці: {line}"
            return cats_info

    except FileNotFoundError:
        return "Не вдалося знайти файл"

cats_info = get_cats_info("/goit-algo-hw-04/cats.txt")
print(cats_info)