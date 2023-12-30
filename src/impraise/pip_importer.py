import importlib
import importlib.abc
import sys
import subprocess

class PipImporterFinder(importlib.abc.MetaPathFinder):
    def __init__(self):
        self.installing = set()
    def find_spec(self, fullname, path, target=None):
        if path is None and fullname not in self.installing:
            package_name = fullname.split('.')[-1]
            self.installing.add(fullname)
            print('before installing')
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
            self.installing.remove(fullname)
            print('importing')
            module = importlib.import_module(fullname)
            print('MODULE', module)
            spec = module.__spec__
            print('SPEC', spec)
            return spec
        return None
    def register(self):
        sys.meta_path.append(self)
    @classmethod
    def register_importer(cls):
        obj = cls()
        obj.register()

PipImporterFinder.register_importer()
