import pathlib
import shutil

src = pathlib.Path(__file__).parent
prod_src = src.parent.parent.parent / "prod" / "ribbons"

def process_133x51():
    for file in (src / "133x51" / "replace").rglob("*.png"):
        shutil.copyfile(str(file), str(prod_src / file.name))

def main():
    prod_src.mkdir(parents=True, exist_ok=True)
    process_133x51()

if __name__ == "__main__":
    main()
