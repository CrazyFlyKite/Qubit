# Colors
RED = '#CE0000'
GREEN = '#00CC00'
BLUE = '#378DF7'
YELLOW = '#FFFF2B'

# Strings
bits = ('Bit', 'Byte', 'KiloByte', 'MegaByte', 'GigaByte', 'TeraByte', 'PetaByte', 'ExaByte', 'ZettaByte', 'YottaByte')
number_system = ('Binary', 'Octal', 'Decimal', 'Hexadecimal')

infotext = """
Конвертер единиц памяти компьютера
содержит следующие единицы измерения:
бит, байт, килобайт, мегабайт, гигабайт,
терабайт, петабайт, эксабайт, зеттабайт и йоттабайт.

Инструкция:
1. Введите число в желтом поле ввода.
2. Выберите текущую единицу измерения
числа(бит, байт и т.д.).
3. Выберите целевую единицу измерения для конвертации.
4. Получите результат конвертации.
"""

infotext2 = """
2 - Конвертер систем счисления

Конвертер систем счисления поддерживает несколько
систем, включая двоичную, восьмеричную, десятичную и шестнадцатеричную.

Инструкция:
1. Введите число в желтом поле ввода.
2. Выберите текущую систему счисления (двоичная (Binary),
восьмеричная (Octal), десятичная (Decimal) или
шестнадцатеричная (Hexadecimal)).
3. Выберите целевую систему счисления для конвертации.
4. Получите результат конвертации.

Спасибо Каргину Евгению за помощь в разработке этого проекта.

Qubit                                                                                                                                                          2021-2023
"""

# Window Settings
name = 'Qubit'
icon = 'icon.ico'

# Images
img_info = 'info.png'
img_info2 = 'info2.png'
img_go_back = 'close.png'


# Functions
def to_bit(num, from_):
    conversion_factors = {
        'Bit': 1,
        'Byte': 8,
        'KiloByte': 8 * 1024,
        'MegaByte': 8 * 1024 * 1024,
        'GigaByte': 8 * 1024 * 1024 * 1024,
        'TeraByte': 8 * 1024 * 1024 * 1024 * 1024,
        'PetaByte': 8 * 1024 * 1024 * 1024 * 1024 * 1024,
        'ExaByte': 8 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
        'ZettaByte': 8 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
        'YottaByte': 8 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024
    }

    return num * conversion_factors[from_]


def from_bit(num, to_):
    conversion_factors = {
        'Bit': 1,
        'Byte': 8,
        'KiloByte': 8 * 1024,
        'MegaByte': 8 * 1024 * 1024,
        'GigaByte': 8 * 1024 * 1024 * 1024,
        'TeraByte': 8 * 1024 * 1024 * 1024 * 1024,
        'PetaByte': 8 * 1024 * 1024 * 1024 * 1024 * 1024,
        'ExaByte': 8 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
        'ZettaByte': 8 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024,
        'YottaByte': 8 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024
    }

    return num / conversion_factors[to_]


def to_dec(num, from_):
    conversion_functions = {
        'Binary': lambda x: int('0b' + str(x), 2),
        'Octal': lambda x: int('0o' + str(x), 8),
        'Decimal': lambda x: int(x),
        'Hexadecimal': lambda x: int('0x' + str(x), 16)
    }

    return conversion_functions[from_](num)


def from_dec(num, to_):
    conversion_functions = {
        'Binary': lambda x: bin(x)[2:],
        'Octal': lambda x: oct(x)[2:],
        'Decimal': lambda x: str(x),
        'Hexadecimal': lambda x: hex(x)[2:]
    }

    return conversion_functions[to_](int(num))


def transform(number, from_, to_):
    return from_bit(to_bit(number, from_), to_)


def transformBinOctDecHex(number, from_, to_):
    return from_dec(to_dec(number, from_), to_)
