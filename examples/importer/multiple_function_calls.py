import logging

# noinspection PyUnresolvedReferences
import ask_the_wizard.wizard_importer

# noinspection PyUnresolvedReferences
import function_that_takes_two_numbers_adds_them_and_returns_the_sqrt_of_the_result_called_wizard_math as wizardry

logger = logging.getLogger('ask_the_wizard')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.WARNING)


def main():
    result = wizardry.wizard_math(6, 3)

    print(result)


if __name__ == '__main__':
    main()
