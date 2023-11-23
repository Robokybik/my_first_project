from PIL import Image
from filters import (BreakingBadFilter, TheMatrixFilter, BarbieFilter,BladeRunnerFilter,OppenheimerFilter,
                     HorrorArgFilter)
import os


def main():
    filter_names = [
        "Во все тяжкие👨‍🔬",
        "Матрица🕹",
        "Барби👱‍♀️",
        "Бегущий по лезвию🔪",
        "Оппенгеймер🤯🏃‍♂️",
        "ХорорАрг🦴",
    ]
    filters = [
        BreakingBadFilter(),
        TheMatrixFilter(),
        BarbieFilter(),
        BladeRunnerFilter(),
        OppenheimerFilter(),
        HorrorArgFilter(),
    ]

    print("Добро пожаловать в меню кинофильтров! Какой фильтр предпочитаете?")
    is_finished = False
    while not is_finished:
        path = input("Введите нужный путь к файлу: ")
        while not os.path.exists(path):
            path = input("Файл не найден 😥. Попробуйте еще раз: ")

        img = Image.open(path).convert("RGB")

        print("Какой кинофильтр вы хотите применить?")
        for i in range(len(filter_names)):
            print(f"{i} - {filter_names[i]}")

        choice = input("Выберите фильтр (введите номер): ")
        while not choice.isdigit() or int(choice) >= len(filters) or int(choice) < 0:
            choice = input("Некорректный ввод💣. Попробуйте еще раз(введите номер): ")

        filt = filters[int(choice)]
        img = filt.apply_to_image(img)

        save_path = input("Выберите путь, куда сохранить файл: ")
        img.save(save_path)
        is_finished = input("Ещё раз? (да/нет): ").lower() == "нет"


if __name__ == "__main__":
    main()