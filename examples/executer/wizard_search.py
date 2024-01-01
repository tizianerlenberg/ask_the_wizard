import logging
from ask_the_wizard.wizard_executer import WizardExecuter

logger = logging.getLogger('ask_the_wizard')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.WARNING)


def main():
    wizard_executer = WizardExecuter()

    # The window has a text field where you can enter a website. E.g. google.com
    # When clicking the "OPEN" button, the website will be opened. If the website does not exist, the text field will
    # be treated as a search query and the search query will be searched with google.com
    # When clicking the "CLOSE" button, the window will be closed.
    wizard_executer.basic_web_search_window_with_pysimplegui(window_title='Wizard Search')


if __name__ == '__main__':
    main()
