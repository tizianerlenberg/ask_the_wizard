import logging

# noinspection PyUnresolvedReferences
import ask_the_wizard.wizard_importer

# noinspection PyUnresolvedReferences
import \
    a_function_named_search_window_that_does_the_following_The_window_created_with_pysimplegui_has_a_text_field_where_you_can_enter_a_website_Eg_google_com_When_clicking_the_OPEN_button_the_website_will_be_opened_If_the_website_does_not_exist_the_text_field_will_be_treated_as_a_search_query_and_the_search_query_will_be_searched_with_google_com_When_clicking_the_CLOSE_button_the_window_will_be_closed as wizardry

logger = logging.getLogger('ask_the_wizard')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.WARNING)


def main():
    wizardry.search_window()


if __name__ == '__main__':
    main()
