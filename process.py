import importlib

import pathlib

src = pathlib.Path(__file__).parent

# create `prod` directory

proc_dir = src / 'prod'
proc_dir.mkdir(parents=True, exist_ok=True)

image_src = src / 'src'

for path in image_src.rglob("*.py"):
    libpath = ".".join(("src", *(p.removesuffix('.py') for p in path.relative_to(image_src).parts)))
    cls = importlib.import_module(libpath)
    cls.main()
