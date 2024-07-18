import pathlib
import cv2
import numpy as np

src = pathlib.Path(__file__).parent
prod_src = src.parent.parent.parent / "prod" / "ribbons" / "subribbons"


def process_51x51():
    for file in (src / "51x51" / "replace").rglob("*.png"):
        img = cv2.imread(str(file), cv2.IMREAD_UNCHANGED)
        img2 = cv2.resize(img, (51, 51))
        cv2.imwrite(str(prod_src / file.name), img2)


def process_65x51():
    for file in (src / "65x51" / "replace").rglob("*.png"):
        img = cv2.imread(str(file), cv2.IMREAD_UNCHANGED)
        img2 = cv2.resize(img, (51, 51))
        img_final = np.zeros((51, 65, 4), np.uint8)
        img_final[0:51, 7:58] = img2
        cv2.imwrite(str(prod_src / file.name), img_final)


def main():
    prod_src.mkdir(parents=True, exist_ok=True)
    process_51x51()
    process_65x51()
    
if __name__ == "__main__":
    main()
