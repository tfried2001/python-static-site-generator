from pathlib import Path
import typer
from ssg.site import Site

class Site:
    def __init__(self, source, dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self, path):
        directory = self.dest / path.relative_to(self.source)

        directory.mkdir(parents=True, exist_ok=True)

    def build(self):
        self.dest.mkdir(parents=True, exist_ok=True)

        for path in self.source.rglob("*"):
            if path.is_dir():
                self.create_dir(path)

    def main(self, source="content", dest="dist"):
        config = {
            "source" : source,
            "dest" : dest
        }

        Site(**config).build()

typer.run(main)