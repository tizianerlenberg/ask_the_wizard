from src.impraise.wizard_communication import WizardCommunication
# TODO: Import pip_importer


class WizardExecuter:
    def __init__(self, wizard_communication: WizardCommunication):
        self.wizard_communication = wizard_communication or WizardCommunication()

    def __getattr__(self, item):
        # TODO: Implement
        return exec(self.wizard_communication.request_function_code(item))
