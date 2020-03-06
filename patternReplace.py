import re

text = 'My name is Cristian. Hi Cristian.'
print(f'The text before pattern replace is:\n{text}\n\n')

pattern = r'Cristian'
newPattern = re.sub(pattern, 'Hellsing', text)

print(f'The text after pattern replace is:\n{newPattern}')
