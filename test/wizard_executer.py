from src.impraise.wizard_executer import WizardExecuter


if __name__ == '__main__':
    wizard_executer = WizardExecuter()

    result = wizard_executer.basic_window_with_pysimplegui(title='Hello World!')
    print(result)
