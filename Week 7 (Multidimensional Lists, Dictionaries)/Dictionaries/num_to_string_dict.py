def num_to_string_dict(n):
    one_to_ten={'zero':0, 'one':1, 'two':2, 'three':3, 'four':4,
                'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    
    ten_to_nineteen={'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13,
                     'fourteen':14, 'fifteen':15, 'sixteen':16,
                     'seventeen':17, 'eighteen': 18, 'nineteen':19}
    
    twenty_to_ninety={'twenty':20, 'thirty':30, 'forty':40, 'fifty':50,
                      'sixty':60, 'seventy':70, 'eighty':80, 'ninety':90}
    temp_str=""

    if n==0:
        temp_str='zero'

    first_digit=n//1000
    second_digit=(n%1000)//100
    third_digit=(n%100)//10
    fourth_digit=(n%10)
    last_digit=int(str(third_digit)+str(fourth_digit))

    if first_digit>0:
        for number_string in one_to_ten:
            if one_to_ten[number_string]==first_digit:
                temp_str+=number_string+' thousand '

    if second_digit>0:
        for number_string in one_to_ten:
            if one_to_ten[number_string]==second_digit:
                temp_str+=number_string+' hundred '

    if third_digit>1:
        third_digit=third_digit*10
        for number_string in twenty_to_ninety:
            if twenty_to_ninety[number_string]==third_digit:
                temp_str+=number_string+' '

    if third_digit==1:
        for number_string in ten_to_nineteen:
            if ten_to_nineteen[number_string]==last_digit:
                temp_str+=number_string+' '

    else:
        if fourth_digit:
            for number_string in one_to_ten:
                if one_to_ten[number_string]==fourth_digit:
                    temp_str+=number_string+' '
                
    if temp_str[-1]==" ":
        temp_str=temp_str[0:-1]
    return temp_str
                  
number = 1019
print(num_to_string_dict(number))
