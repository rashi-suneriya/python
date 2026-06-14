# write a program to fill in a letter template give below with name and date

letter = '''Dear <|Name|>,
you are selected!
<|Date|>'''

print(letter.replace("<|Name|>", "Rashi").replace("<|Date|>", "20/06/2024"))


# letter = '''Dear rashi,
# you are selected!
# 20/06/2024'''

# print(letter)