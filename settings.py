# Colors
RED = '#CE0000'
GREEN = '#00CC00'
BLUE = '#378DF7'
YELLOW = '#FFFF2B'

# Texts
bits = ('Bit', 'Byte', 'KiloByte', 'MegaByte', 'GigaByte', 'TeraByte', 'PetaByte', 'ExaByte', 'ZettaByte', 'YottaByte')
number_system = ('Bin 2', 'Oct 8', 'Dec 10', 'Hex 16')
infotext = """
Конвертер единиц памяти компьютера
содержит 10 единиц измерения:
бит, байт, килобайт, мегабайт, гигабайт,
терабайт, петабайт, эксабайт, зеттабайт, йоттабайт.

Инструкции:
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

Инструкции:
1. Введите число в желтом поле ввода.
2. Выберите текущую систему счисления (двоичная (Bin),
восьмеричная (Oct), десятичная (Dec) или шестнадцатеричная (Hex)).
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
    if from_ == 'Bit':
        return num
    elif from_ == 'Byte':
        return num * 8
    elif from_ == 'KiloByte':
        return num * (8 * 1024)
    elif from_ == 'MegaByte':
        return num * (8 * 1024 * 1024)
    elif from_ == 'GigaByte':
        return num * (8 * 1024 * 1024 * 1024)
    elif from_ == 'TeraByte':
        return num * (8 * 1024 * 1024 * 1024 * 1024)
    elif from_ == 'PetaByte':
        return num * (8 * 1024 * 1024 * 1024 * 1024 * 1024)
    elif from_ == 'ExaByte':
        return num * (8 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024)
    elif from_ == 'ZettaByte':
        return num * (8 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024)
    elif from_ == 'YottaByte':
        return num * (8 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024)

def from_bit(num, to_):
    if to_ == 'Bit':
        return num
    elif to_ == 'Byte':
        return num / 8
    elif to_ == 'KiloByte':
        return num / (8 * 1024)
    elif to_ == 'MegaByte':
        return num / (8 * 1024 * 1024)
    elif to_ == 'GigaByte':
        return num / (8 * 1024 * 1024 * 1024)
    elif to_ == 'TeraByte':
        return num / (8 * 1024 * 1024 * 1024 * 1024)
    elif to_ == 'PetaByte':
        return num / (8 * 1024 * 1024 * 1024 * 1024 * 1024)
    elif to_ == 'ExaByte':
        return num / (8 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024)
    elif to_ == 'ZettaByte':
        return num / (8 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024)
    elif to_ == 'YottaByte':
        return num / (8 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024 * 1024)

def to_dec(num, from_):
    if from_ == 'Bin 2':
        return int('0b' + str(num), 2)
    elif from_ == 'Oct 8':
        return int('0o' + str(num), 8)
    elif from_ == 'Dec 10':
       return int(num)
    elif from_ == 'Hex 16':
        return int('0x' + str(num), 16)

def from_dec(num, to_):
    if to_ == 'Bin 2':
        return str(bin(int(num)))[2:]
    elif to_ == 'Oct 8':
        return str(oct(int(num)))[2:]
    elif to_ == 'Dec 10':
        return str(num)
    elif to_ == 'Hex 16':
        return str(hex(int(num)))[2:]

def transform(number, fr, to):
    return from_bit(to_bit(number, fr), to)

def transformBinOctDecHex(number, fr, to):
    return from_dec(to_dec(number, fr), to)
