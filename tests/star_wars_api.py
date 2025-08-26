import requests

def get_character_id(url):
    """Извлекаем ID персонажа из URL."""
    return url.strip('/').split('/')[-1]

def get_character_name(url):
    """Получаем данные персонажа по URL."""
    print(f"Получаем данные персонажа: {url}")
    response = requests.get(url, verify=True)

    if response.status_code != 200:
        print(f"Ошибка! Статус код: {response.status_code} для URL: {url}")
        return None

    print(f"Успешно получен персонаж: {url}")
    return response.json()['name']


def get_common_characters(main_char_url, output_file):
    """
    Находим всех персонажей, снимавшихся в фильмах с Дартом Вейдером,
    и сохраняем их имена в файл без дубликатов.
    """
    print("\nНачинаем поиск персонажей из фильмов с Дартом Вейдером...")

    vader_id = get_character_id(main_char_url) # Получаем ID Вейдера для сравнения
    print(f"ID Дарта Вейдера: {vader_id}")

    print(f"\nПолучаем данные основного персонажа по URL: {main_char_url}")
    response = requests.get(main_char_url, verify=True)

    if response.status_code != 200:
        print(f"Ошибка! Не удалось получить данные Вейдера. Статус код: {response.status_code}")
        return

    main_char_data = response.json()
    print(f"Получены данные Дарта Вейдера: {main_char_data['name']}")

    print(f"\nНайдено фильмов с Дартом Вейдером: {len(main_char_data['films'])}")
    characters = set()

    for i, film_url in enumerate(main_char_data['films'], 1):
        print(f"\nОбрабатываем фильм {i}/{len(main_char_data['films'])}: {film_url}")
        film_response = requests.get(film_url, verify=True)

        if film_response.status_code != 200:
            print(f"Пропускаем фильм. Ошибка {film_response.status_code} для URL: {film_url}")
            continue

        film_data = film_response.json()
        print(f"Фильм: {film_data['title']}")

        for char_url in film_data['characters']: # Добавляем только тех персонажей, чей ID не совпадает с Вейдером
            if get_character_id(char_url) != vader_id:
                characters.add(char_url)

        # characters.update(film_data['characters'])
        print(f"Текущее количество уникальных персонажей: {len(characters)}")

    print(f"\nНачинаем сбор имен {len(characters)} персонажей...")
    character_names = []

    for j, url in enumerate(characters, 1):
        name = get_character_name(url)
        if name:
            character_names.append(name)
            print(f"[{j}/{len(characters)}] Добавлен: {name}")
        else:
            print(f"[{j}/{len(characters)}] Пропущен персонаж по URL: {url}")

    print(f"\nСохраняем данные в файл: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(character_names)))

    print(f"\nГотово! Сохранено {len(character_names)} уникальных персонажей в файл '{output_file}'")
    print("Операция завершена успешно!")

DARTH_VADER_URL = "https://swapi.info/api/people/4/"
OUTPUT_FILE = "../test_results/star_wars_characters.txt"
get_common_characters(DARTH_VADER_URL, OUTPUT_FILE)