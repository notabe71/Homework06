import shutil
from pathlib import Path
import sys

if len(sys.argv) != 2:
    print("You must point the Folder's name!")
    sys.exit()
else:
    p = Path(sys.argv[1])
    if not p.exists():
        print("The folder "+sys.argv[1]+" doesn't exist !")
        sys.exit()


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = (
    "a",
    "b",
    "v",
    "g",
    "d",
    "e",
    "e",
    "j",
    "z",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "f",
    "h",
    "ts",
    "ch",
    "sh",
    "sch",
    "",
    "y",
    "",
    "e",
    "yu",
    "ya",
    "je",
    "i",
    "ji",
    "g",
)

TRANS = {}
for cyr, lat in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cyr)] = lat
    TRANS[ord(cyr.upper())] = lat.upper()


def normalize(in_name):
    in_name = in_name.translate(TRANS)
    out_name = ""

    for i in in_name:
        if i == '.' or (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57):
            out_name += i
        else:
            out_name += '_'
    return out_name


def get_Folder(p):

    file_list = []
    for i in p.iterdir():
        file_list.append(i.name)
        print(i.name)
        print(i.suffix)
    return file_list


file_list = get_Folder(p)

for i in file_list:
    print(normalize(i))
