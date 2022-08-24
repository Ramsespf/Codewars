


class RomanNumerals:
    
    

    def to_roman(val):
       
        roman = ""
        list_vals = list(map(int, str(val)))
        for i in range(len(list_vals)):
            if len(list_vals) == 4:
                valor = list_vals[i]
                while valor > 0:
                    roman += "M"
                    valor -= 1
                list_vals.pop(0)
            elif len(list_vals) == 3:
                valor = list_vals[0]
                if valor == 9:
                    roman +="CM"
                elif valor >=5:
                    roman += "D"
                    while valor > 5:
                        roman += "C"
                        valor -= 1
                elif valor == 4:
                    roman += "CD"
                else:
                    while valor > 0:
                        roman += "C"
                        valor -= 1
                list_vals.pop(0)
            elif len(list_vals) == 2:
                valor = list_vals[0]
                if valor == 9:
                    roman += "XC"
                elif valor >=5:
                    roman += "L"
                    while valor > 5:
                        roman += "X"
                        valor -= 1
                elif valor == 4:
                    roman += "XL"
                else:
                    while valor > 0:
                        roman += "X"
                        valor -= 1
                list_vals.pop(0)
            elif len(list_vals) == 1:
                valor = list_vals[0]
                if valor == 9:
                    roman += "IX"
                elif valor >=5:
                    roman += "V"
                    while valor > 5:
                        roman += "I"
                        valor -= 1
                elif valor == 4:
                    roman += "IV"
                else:
                    while valor > 0:
                        roman += "I"
                        valor -= 1                         
            
        return roman
    """
    Optimized
    def to_roman(num):
        R2M = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1}
        string = ''
        for k, v in R2M.items():
            count = num // v
            num %= v
            string += count * k
    """

    def from_roman(roman_num):
        numeral_roman = {"I": 1,
                         "IV": 4,
                         "V": 5,
                         "IX": 9,
                         "X": 10,
                         "XL": 40,
                         "L": 50,
                         "XC": 90,
                         "C": 100,
                         "CD": 400,
                         "D": 500,
                         "CM": 900,
                         "M": 1000
                        }
        number = 0
        
        for i in range(len(roman_num)):
            if i != len(roman_num) - 1:
                if roman_num[i] == "I" and roman_num[i+1] == "V":
                    number += 4
                    if len(roman_num) == 2  or i >= len(roman_num) - 2:
                        break
            
                elif roman_num[i] == "V" and roman_num[i-1] == "I" and i != 0:
                    continue
            
                elif roman_num[i] == "I" and roman_num[i+1] == "X":
                    number += 9
                    if len(roman_num) == 2 or i >= len(roman_num) - 2:
                        break
            
                elif roman_num[i] == "X" and roman_num[i-1] == "I" and i != 0:
                    continue
            
                elif roman_num[i] == "X" and roman_num[i+1] == "L":
                    number += 40
                    if len(roman_num) == 2  or i >= len(roman_num) - 2:
                        break
            
                elif roman_num[i] == "L" and roman_num[i-1] == "X" and i != 0:
                    continue
            
                elif roman_num[i] == "X" and roman_num[i+1] == "C":
                    number += 90
                    if len(roman_num) == 2  or i >= len(roman_num) - 2:
                        break
            
                elif roman_num[i] == "C" and roman_num[i-1] == "X" and i != 0:
                    continue
            
                elif roman_num[i] == "C" and roman_num[i+1] == "D":
                    number += 400
                    if len(roman_num) == 2  or i >= len(roman_num) - 2:
                        break
            
                elif roman_num[i] == "D" and roman_num[i-1] == "C" and i != 0:
                    continue
            
                elif roman_num[i] == "C" and roman_num[i+1] == "M":
                    number += 900
                    if len(roman_num) == 2  or i >= len(roman_num) - 2:
                        break
            
                elif roman_num[i] == "M" and roman_num[i-1] == "C" and i != 0:
                    continue
                
                else:
                    number += numeral_roman[roman_num[i]]  
                    
            else:
                number += numeral_roman[roman_num[i]]     
        
        return number
    """
    Optimized
    def from_roman(roman):
        R2M = {'M':1000, 'i':900, 'D':500, 'j':400, 'C':100, 'k':90, 'L':50, 'l':40, 'X':10, 'm':9, 'V':5, 'n':4, 'I':1}
        roman = roman.replace('CM', 'i').replace('CD', 'j').replace('XC', 'k').replace('XL', 'l').replace('IX', 'm').replace('IV', 'n')
        return sum(R2M[i] for i in roman)
    """
    
numeral_to_roman = RomanNumerals
romano = numeral_to_roman.to_roman(1666)
print(romano)

numero = numeral_to_roman.from_roman("CLXXIX")
print(numero)
