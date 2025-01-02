def number_to_words(n):
    one_to_ten=['zero','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    ten_to_nineteen=['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    twenty_to_ninety=['','','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    temp_str=""

    if n==0:
        temp_str='zero'

    first_digit=n//1000
    second_digit=(n%1000)//100
    third_digit=(n%100)//10
    fourth_digit=(n%10)

    if first_digit>0:
        temp_str+=one_to_ten[first_digit]+' thousand '

    if second_digit>0:
        temp_str+=one_to_ten[second_digit]+' hundred '

    if third_digit>1:
        temp_str+=twenty_to_ninety[third_digit]+" "

    if third_digit==1:
        temp_str+=ten_to_nineteen[fourth_digit]+" "

    else:
        if fourth_digit:
            temp_str+=one_to_ten[fourth_digit]+" "

    if temp_str[-1]==" ":
        temp_str=temp_str[0:-1]
    return temp_str

inputNumber=int(input('please enter an integer between 1 and 9999: '))
print (number_to_words(inputNumber))





