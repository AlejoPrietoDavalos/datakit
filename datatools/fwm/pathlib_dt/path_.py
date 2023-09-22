""" Emprolijar, gpteado.
- TODO: Se me ocurre poner unos validadores con `attr`.
- Me gusta el __str__ y repr, quizas usar el de attr, ver como queda.
- También ver la estructura base, preprocess y processed me parece que
está bueno depende que proyecto.
- Quizás hacer un `ABC` para características que tengan todos los
proyectos de data sciente en general, y después si querés hacer algo rápido,
para ver un resultado por que estás scripteando, que también haya una clase
que pueda hacer eso y no sea tan molesto definir de entrada.
- Idea: También podría crearte la estructura de carpetas automáticamente
con ejecutar una función en python, o q si no exista la cree, algo asi. Y si existe
la usa como propia...
"""

import argparse
from pathlib import Path

class ProjectPaths:
    def __init__(self, root: Path = None):
        if not root:
            # Parse command line arguments
            parser = argparse.ArgumentParser(description="Set up project paths.")
            parser.add_argument("--root", default=".", help="Root directory of the project.")
            args = parser.parse_args()
            root = Path(args.root)
        
        self.root = root
        self.data = self.root / "data"
        self.raw = self.data / "raw"
        self.preprocess = self.data / "preprocess"
        self.processed = self.data / "processed"
        self.models = self.root / "models"
        self.reports = self.root / "reports"
        self.notebooks = self.root / "notebooks"

    def __str__(self):
        return f"""
        Project Paths:
        Root: {self.root}
        Data: {self.data}
        Raw Data: {self.raw}
        Preprocessed Data: {self.preprocess}
        Processed Data: {self.processed}
        Models: {self.models}
        Reports: {self.reports}
        Notebooks: {self.notebooks}
        """

if __name__ == "__main__":
    paths = ProjectPaths()
    print(paths)
