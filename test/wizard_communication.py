from src.impraise.wizard_communication import WizardCommunication

if __name__ == '__main__':
    wc = WizardCommunication()

    code = wc.request_function_code('A function that adds two numbers.')

    print(code)
