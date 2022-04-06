__version__ = '0.1.0'

from googletrans import Translator
translator = Translator()

test1 = translator.translate('Pythonプログラミング')
test2 = translator.translate('How do you do', dest='ja')

print(test1) # Python programming
print(test2) # ごきげんよう