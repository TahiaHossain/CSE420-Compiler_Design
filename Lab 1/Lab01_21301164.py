f_in = open('input.txt', 'r')

kw = ['int', 'float', 'while', 'for', 'if', 'else', 'True', 'false', 'bool', 'and', 'or', 'print', 'in', 'pass']
op = ['+','-','*', '/', '=']
log = ['<','>', '==', '!=', '<=', '>=']
other = [',', ';', '(', ')', '{', '}', '[', ']']
n = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

keywords = []
id = []
mat = []
logical = []
num = []
others = []

def check(s):
    if s in kw :
        # print('found a keyword', s)
        keywords.append(s)
    elif s in op :
        # print('found an operator', s)
        if s not in mat :
            mat.append(s)
    elif s in log :
        # print('found a logical operator', s)
        if s not in logical :
            logical.append(s)

    else :
        is_id = False
        is_num = False

        if s != '' and s[0].isalpha():
            is_id = True
        elif (s != '' and s[0] in n) or (s != '' and s[0] == '-' and s[1] in n):
            is_num = True
            # print(is_num)

        if is_id :
            # print('found an identifier', s)
            if s not in id :
                id.append(s)

        elif is_num :
            # print('found a number', s)
            if s not in num :
                num.append(s)
                

for line in f_in.readlines() :
    s = ''
    for i in line :
        # print(i)
        if i == ' ' or i == '\n':
            check(s)
            s = ''

        elif i in other :
            # print('found an other', i)
            if i not in others :
                others.append(i)
            check(s)
            s = ''
        
        elif i in op and i != '-':
            # print('found an operator', i)
            if i not in mat :
                mat.append(i)
            check(s)
            s = ''
        
        elif i in log:
            # print('found a logical operator', i)
            if i not in logical :
                logical.append(i)
            check(s)
            s = ''
        
        else :
            s += i
            # print(s)

print('Keywords: ', ', '.join(keywords))
print('Identifiers: ', ', '.join(id))
print('Math Operators: ', ', '.join(mat))
print('Logical Operators: ', ', '.join(logical))
print('Numerical Values: ', ', '.join(num))
print('Others: ', ' '.join(others))