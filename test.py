def arithmetic_arranger(problems, solve=True):
    first = ""
    second = ""
    result = ""
    lines = ""
    string = ""
    for k in problems:
        if len(k) > 5:
            return "Error: Too many problems."

        pieces = k.split(" ")
        firstnumber = pieces[0]
        operator = pieces[1]
        secondnumber = pieces[2]

    
        if len(firstnumber) > 4 or len(secondnumber) > 4:
            return "Error: Numbers cannot be more than four digits."
        if not firstnumber.isnumeric() or secondnumber.isnumeric():
            return "Error: Numbers must only contain digits."
        if (operator == '/') or (operator == '*'):
            return "Error: Operator must be '+' or '-'."

        new = ""
        if (operator == '+'):
            new = str(int(firstnumber)) + int(secondnumber)

        elif (operator == '-'):
            new = str(int(firstnumber)) - int(secondnumber)

        length = max(len(firstnumber), len(secondnumber)) + 2
        top = str(firstnumber).rjust(length)
        bottom = operator + str(secondnumber).rjust(length)
        line = ""
        final = str(new).rjust(length)
        
        for s in range(length):
            line += "-"

        if k != k[-1]:
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            result += final + '    '
        else:
            first += top
            second += bottom
            lines += line
            result += final


    if solve:
        string = first + '\n' + second + '\n' + lines + '\n' + result
    else:
        string = first + '\n' + second + '\n' + lines 
    return string

#print(type(sign))