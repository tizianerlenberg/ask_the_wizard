import importlib
import importlib.abc
import logging
import subprocess
import sys

logger = logging.getLogger(__name__)


class PipImporterFinder(importlib.abc.MetaPathFinder):
    def __init__(self):
        self._installing = set()
        self._logger = logger.getChild(str(id(self)))

    def find_spec(self, fullname, path, target=None):
        if path is None and fullname not in self._installing:
            package_name = fullname.split('.')[-1]
            self._installing.add(fullname)
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package_name])
            except subprocess.CalledProcessError:
                logger.info(f'Could not install {package_name}.', exc_info=True)
                return None
            self._installing.remove(fullname)
            module = importlib.import_module(fullname)
            spec = module.__spec__
            return spec
        return None

    def register(self):
        sys.meta_path.append(self)

    @classmethod
    def register_importer(cls):
        obj = cls()
        obj.register()


PipImporterFinder.register_importer()
