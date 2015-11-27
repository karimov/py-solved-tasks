#/usr/bin/python

def r_sum(list):
    if len(list) == 1:
       return list[0]
    else:
       return list[0] + r_sum(list[1:])
       
attr = 'Attributes'

def reverse(str):
    if len(str)==1:
       return str[0]
    else:
       return reverse(str[1:]) + str[0]

def main():
    
main()



