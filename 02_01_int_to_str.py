#take int as input, give output as string, dont use builtin str fuction

def int2str (num):
    digits= '0123456789'
    result = ""

    if num==0: return '0'

    while num>0:
        result = digits[ num % 10 ] + result
        num = num // 10   #whole div
    return result

print ( int2str(62) )

