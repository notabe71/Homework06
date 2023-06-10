import shutil
from pathlib import Path
import sys

CATEGORIES = {"Audio": [".mp3", ".aiff", ".ogg", ".wav", ".amr"],
              "Documents": [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"],
              "Images": [".jpeg", ".png", ".jpg", ".svg"],
              "Video": [".avi", ".mp4", ".mov", ".mkv"],
              "Archives": [".zip", ".gz", ".tar"],
              "Other": []
              }


def get_categories(path: Path) -> str:
    ext = path.suffix.lower()
    for cat, exts in CATEGORIES.item():
        if ext in exts:
            return cat
    return "Other"


def move_file(file: Path, root_dir: Path, category: str):
    target_dir = root_dir.joinpath(category)
    if not target_dir.exist():
        target_dir.mkdir

    new_name = target_dir.joinpath(f"normalize({new_name.stem}){file.suffix}")


def main():
    try:
        path = Path(sys.argv[1])
    except IndexError:
        return "You must point the Folder's name!"

    if not path.exists():
        return f"The folder {path} doesn't exist !"


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
