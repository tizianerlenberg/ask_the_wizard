from functools import cache

from src.impraise.wizard_communication import WizardCommunication
# noinspection PyUnresolvedReferences
import src.impraise.pip_importer


class WizardExecuter:
    def __init__(self, wizard_communication: WizardCommunication = None):
        self.wizard_communication = wizard_communication or WizardCommunication()

    def __getattr__(self, key):
        def method(*args, **kwargs):
            function_details = 'Function details:\n'
            function_details += f'Function name: {key}\n'

            args_details = ', '.join([f'(value={arg}, type={type(arg)})' for arg in args])
            kwargs_details = ', '.join(
                [f'(name={name}, value={value}, type={type(value)})' for name, value in kwargs.items()])

            function_details += f'Positional arguments: {args_details}\n'
            function_details += f'Keyword arguments: {kwargs_details}\n'

            code = self.wizard_communication.request_function_code(function_details)
            locals_dict = {}
            exec(code, {}, locals_dict)
            result = locals_dict['result']

            print(code)
            # Return the result
            return result

        return method
