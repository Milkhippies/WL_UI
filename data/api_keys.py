import random


class CreateKey:
    # безлимитный ключ
    UnlimKey = {
        'Prefix': "Test key unlim",
        'KeyName': f"Test key unlim #{random.randint(0,10000)}",
        'Spot': True,
        'Future': True,
        'Limit': False,
    }

    # ключ с одним адресом
    LimitedKey = {
        'Prefix': "Test key limit",
        'KeyName': f"Test key limit #{random.randint(0, 10000)}",
        'Spot': True,
        'Future': False,
        'Limit': True,
        'Multi': 1,
        'IpName': [f"Name #{random.randint(0, 1000)}"],
        'IpAddr': [f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"]
    }

    # ключ с несколькими адресами
    MultiLimitedKey = {
        'Prefix': 'Test key multilim ',
        'KeyName': f"Test key multilim #{random.randint(0, 10000)}",
        'Spot': False,
        'Future': True,
        'Limit': True,
        'Multi': 3,
        'IpName': [f"Name #{random.randint(0, 1000)}",
                   f"Name #{random.randint(0, 1000)}",
                   f"Name #{random.randint(0, 1000)}"],
        'IpAddr': [f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
                   f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
                   f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}", ]
    }

    # ключ с универсальным названием
    AnyKey = {
        'Prefix': "Test key",
        'KeyName': "Test key",
        'Spot': False,
        'Future': False,
        'Limit': False,
    }


class EditKey:
    # ключ для тестов на изменение параметров
    BaseKey = {
        'Prefix': "Test key base",
        'KeyName': f"Test key base #{random.randint(100, 1000)}",
        'Spot': False,
        'Future': False,
        'Limit': True,
        'Multi': 1,
        'IpName': [f"Name #{random.randint(0, 1000)}"],
        'IpAddr': [f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"]
    }

    # в базовом ключе добавим адрес
    ChangeLimit = {
        'Prefix': "Test key base",
        'KeyName': f"Test key base #{random.randint(100, 1000)}",
        'Spot': False,
        'Future': False,
        'Limit': True,
        'Multi': 2,
        'IpName': [f"Name #{random.randint(0, 1000)}",
                   f"Name #{random.randint(0, 1000)}"],
        'IpAddr': [f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}",
                   f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"]
    }

    # в базовом ключе поменяем параметры
    ChangeParams = {
        'Prefix': "Test key base",
        'KeyName': f"Test key base #{random.randint(100, 1000)}",
        'Spot': False,
        'Future': False,
        'Limit': False,
        'Multi': 1,
    }

    # в базовом ключе поменяем имя
    ChangeName = {
        'Prefix': "Test key renamed",
        'KeyName': f"Test key renamed #{random.randint(100, 1000)}",
        'Spot': False,
        'Future': False,
        'Limit': True,
        'Multi': 1,
        'IpName': [f"Name #{random.randint(0, 1000)}"],
        'IpAddr': [f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"]
    }
