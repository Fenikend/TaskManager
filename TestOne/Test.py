
def double_letters(s):
    i_beg=s.index('"')
    i_end=s.index('"',i_beg+1)
    print(f'{s[i_beg:i_end+1]}')

print(double_letters('"dfdfdfdfdf dfdfdf ffff" ffff'))