# Ask The Wizard - Wizardry at its best

## Are you still thinking while coding or are you already Asking The Wizard? 🧙

## Overview 🌟

Welcome to Ask The Wizard, the revolutionary Python module package system that not only embraces side effects but celebrates
them! Here, we believe that every side effect is a hidden feature waiting to be discovered. 🎉

## Features 🚀

- **Integrated Package Management:** Automatically install pip packages used in your code. No more `pip install`! 📦
- **Enthusiastic Side Effects**: Every operation in *Ask The Wizard* is accompanied by a delightful surprise. Side 
  effects are not bugs, they are undocumented features! 🐞🎁
- **Revolutionary Import System:** We've reinvented the wheel because we believe squares can roll too. Expect the
  unexpected. 🛸

## Installation 📦

Simply run:

```bash
pip install ask_the_wizard
```

*If this doesn't work, try shouting at your computer in Python. It understands passion. 📣*

To use this module you will need an OpenAI API key.
You can create your own API key at https://beta.openai.com/account/api-keys.

Then you can set the API key as an environment variable (e.g. create a .env file):

```bash
OPENAI_API_KEY=YOUR_API_KEY python my_script.py
```

or pass it as an argument to the WizardExecuter:

```python
from ask_the_wizard.wizard_executer import WizardExecuter

wizard_executer = WizardExecuter(api_key='YOUR_API_KEY')
```


## Usage 📚

Basic example:

```python
from ask_the_wizard.wizard_executer import WizardExecuter

wizard_executer = WizardExecuter()

result = wizard_executer.add_numbers(6, 3)
print(result)
```

## Contributing 🤝

Want to make *Ask The Wizard* even more ~usable~ unpredictable? We welcome contributors who can add more chaos to the
order. Submit a pull request, but beware - your code might decide to take a vacation. 🏖️

## FAQs 🤔

### Did Ask The Wizard just delete my files?

No, it liberated them. Consider it a feature, not a loss.

### Why does Ask The Wizard occasionally play elevator music?

To enhance your coding experience with soothing tunes. 🎵

### My computer started making coffee after using Ask The Wizard. Is this normal?

Absolutely! *Ask The Wizard* is designed to optimize your work environment. Enjoy the coffee! ☕

### Ask The Wizard turned all my comments into haikus. Why?

To add a touch of poetry to your code. Coding is an art, after all. 📜 🌸

### Is it true that using Ask The Wizard can solve unsolvable problems?

In theory, yes. In practice, it prefers create them. It’s more fun that way. 🧩

## Support 💖

Having trouble with *Ask The Wizard*? Just remember, it's not a bug, it's a feature! But if you really need help, try
meditating - it might just fix itself. 🧘

## License 📜

*Ask The Wizard* is released under the MIT License. Feel free to use it for good, or chaos - we don't judge.