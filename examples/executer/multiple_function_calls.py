import logging
from ask_the_wizard.wizard_executer import WizardExecuter

logger = logging.getLogger('ask_the_wizard')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.WARNING)


def main():
    wizard_executer = WizardExecuter()

    result = wizard_executer.add_numbers(6, 3)
    result = wizard_executer.sqrt_without_external_libraries(result)
    result = wizard_executer.times_two(result)
    result = wizard_executer.divide_by_the_sqrt_of(val_to_devide=result, sqrt_val=9)

    print(f'The result should be 2 and is {result}')


if __name__ == '__main__':
    main()
