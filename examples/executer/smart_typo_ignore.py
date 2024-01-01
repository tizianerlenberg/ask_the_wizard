import logging
from ask_the_wizard.wizard_executer import WizardExecuter

logger = logging.getLogger('ask_the_wizard')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.WARNING)


def main():
    wizard_executer = WizardExecuter()

    result = wizard_executer.a__fuDncthion_tshat_addas_two_nuhmbers(1, 2)
    print(result)


if __name__ == '__main__':
    main()
