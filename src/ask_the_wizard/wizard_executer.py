import inspect

# noinspection PyUnresolvedReferences
from . import pip_importer
from .wizard_communication import WizardCommunication


class WizardExecuter:
    def __init__(self, wizard_communication: WizardCommunication = None, api_key: str = None, model: str = None):
        self.wizard_communication = wizard_communication or WizardCommunication(api_key=api_key, model=model)

    def __getattr__(self, key):
        def method(*args, **kwargs):
            # Extracting comments
            comments = []
            frame = inspect.currentframe().f_back
            source_code_lines = inspect.getsource(frame).splitlines()
            call_line_no = frame.f_lineno - frame.f_code.co_firstlineno

            # Traverse backwards from the current line to find comments
            for line in reversed(source_code_lines[:call_line_no]):
                stripped_line = line.strip()
                if stripped_line.startswith("#"):
                    comments.insert(0, stripped_line)
                else:
                    break

            function_details = 'Function details:\n'

            function_details += 'Comments before the function call : ' + '\n'.join(comments) + '\n'

            function_details += f'Function name: {key}\n'

            args_details = ', '.join([f'(value={arg}, type={type(arg)})' for arg in args])
            kwargs_details = ', '.join(
                [f'(name={name}, value={value}, type={type(value)})' for name, value in kwargs.items()])

            function_details += f'Positional arguments: {args_details}\n'
            function_details += f'Keyword arguments: {kwargs_details}\n'

            code = self.wizard_communication.request_function_code(function_details)
            exec_globals = {'result': None}
            exec(code, exec_globals)
            result = exec_globals['result']

            return result

        return method
