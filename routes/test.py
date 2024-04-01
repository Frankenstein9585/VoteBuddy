string = """name:
faculty:
augustine
university
programme:
matric. no:
level:
llara-fne, lagos
student identification card
o
olufeso omowonuola atinuke
humanities, management and social sciences
accounting
au202200584
200 session: 2023/2024"""

matric_number = 'AU202200584 '

print(matric_number.casefold().strip() in string)
