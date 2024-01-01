import ast
import importlib.abc
import importlib.machinery
import sys
import types

from dotenv import load_dotenv

from .wizard_communication import WizardCommunication

load_dotenv()


class WizardFinder(importlib.abc.MetaPathFinder):
    def __init__(self, wizard_communication=None, api_key: str = None, model: str = None):
        self._wizard_communication = wizard_communication or WizardCommunication(api_key=api_key, model=model)

    @classmethod
    def is_valid_python_source(cls, code: str) -> bool:
        try:
            ast.parse(code)
            return True
        except SyntaxError:
            return False

    def find_spec(self, fullname, path, target=None):
        spec = self._find_py_file_spec(fullname)
        if spec is not None:
            return spec

        spec = self._find_package_init_spec(fullname)
        if spec is not None:
            return spec

        return None

    def _find_py_file_spec(self, fullname):
        location = f'unknown_wizard_location/{fullname}.py'
        source = self._get_wizardry(fullname)
        if source is None:
            return None
        loader = WizardLoader(fullname, source, location)
        return importlib.machinery.ModuleSpec(fullname, loader, origin=location)

    def _find_package_init_spec(self, fullname):
        location = f'unknown_wizard_location/{fullname}.py'
        source = self._get_wizardry(fullname)
        if source is None:
            return None
        loader = WizardLoader(fullname, source, location)
        spec = importlib.machinery.ModuleSpec(
            fullname, loader, origin=location, is_package=True,
        )
        return spec

    def _get_wizardry(self, request):
        source = self._wizard_communication.request_import_code(request)

        if not self.is_valid_python_source(source):
            return None
        return source


class WizardLoader(importlib.abc.Loader):
    def __init__(self, fullname, source_code, location):
        self._fullname = fullname
        self._source_code = source_code
        self._location = location

    def create_module(self, spec):
        module = sys.modules.get(spec.name)
        if module is None:
            module = types.ModuleType(spec.name)
            sys.modules[spec.name] = module
        return module

    def exec_module(self, module):
        module.__file__ = self._location
        exec(self._source_code, module.__dict__)
        return module

    def get_source(self, name):
        return self._source_code


########

def register_wizard():
    sys.meta_path.append(WizardFinder())


register_wizard()

########
