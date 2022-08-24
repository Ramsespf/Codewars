def to_roman(num):
        R2M = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
        string = ''
        for k, v in R2M.items():
            count = num // v
            num %= v
            string += count * k
            
num = 2469

valor = to_roman(num)

print(valor)