import importlib
import importlib.abc
import sys
import subprocess

class PipImporterFinder(importlib.abc.MetaPathFinder):
    def __init__(self):
        pass
    def find_spec(self, fullname, path, target=None):
        subprocess.call(["pip", "install", fullname])
        module = importlib.import_module(fullname)
        return module
    def register(self):
        sys.meta_path.append(self)
    @classmethod
    def register_importer(cls):
        obj = cls()
        obj.register()()

PipImporterFinder.register_importer()
