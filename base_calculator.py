def is_float(floating):
    # used to test if an element is a number
    try:
        floating = float(floating)
    except:
        return False
    return True


def is_operator(operator):
    # takes in a single operator and checks if it's an operator
    symbols = '!^*/+-'
    return operator in symbols


def is_paren(operator):
    # takes in a single operator and checks if it's a paren
    return operator in '()'


def is_alphabet(variable):
    return variable in 'fghxyzstuvwnabcdlmopqrijke'

def is_keyword(key):
    return


def stringIntoList(string):
    # got off of stackoverflow
    # https://stackoverflow.com/questions/53418844/turning-a-string-into-a-nested-list
    output = []
    token = ''
    index = 0
    while index < len(string):
        char = string[index]
        index += 1
        if char in '() ' and token:
            '''
            if is_float(token):
                output.append(float(token))
            else:
                output.append(token)
            '''
            output.append(token)
            token = ''
        if char == '(':
            lst, offset = stringIntoList(string[index:])
            output.append(lst)
            index += offset
        elif char == ')':
            break
        elif char != ' ':
            token += char
    return output, index


def get_operand_operator(str_num, give_num=True):
    math = list(str_num)
    numbers = ''
    operators = []
    for num in math:
        if is_float(num) or is_paren(num) or is_alphabet(num):
            numbers += num
        if is_operator(num):
            operators.append(num)
            numbers += ' '

    if give_num:
        try:
            numbers.remove('')
        except (ValueError, AttributeError):
            return stringIntoList(numbers)[0]
        return stringIntoList(numbers)[0]
    else:
        return operators


def valid_expression(str_num):
    def list_count(stringy):
        count = 0
        for i in stringy:
            if type(i) is list:
                count += list_count(i)
            else:
                count += 1
        return count
    return list_count(get_operand_operator(str_num, False)) == list_count(get_operand_operator(str_num)) - 1


operators = {'+': lambda a,b: a + b,
             '-': lambda a,b: a - b,
             '*': lambda a,b: a * b,
             '/': lambda a,b: a / b,
             '^': lambda a,b: pow(a,b),
             '!': lambda a,b: b*a(a, b-1) if b > 0 else 1}


def do_operators(number, operator, debugging=False):
    debug_print('outer|||:', number, operator, debugging=debugging)

    def do_no_paren(inner_number, inner_operator):

        for op in '!^*/+-':
            if len(inner_number) == 1:
                return inner_number
            elif inner_operator == []:
                return 'Error empty list'
            debug_print('|||inner:', inner_number, inner_operator, op, debugging=debugging)
            if op in inner_operator:
                op_index = inner_operator.index(op)
                oper = inner_operator.pop(op_index)
                arg = inner_number.pop(op_index)
                debug_print('before operating: operators[', oper, '](', arg, ',', inner_number[op_index], ')',
                            debugging=debugging)
                number[op_index] = operators[oper](arg, inner_number[op_index])
                debug_print('after operating:', number[0], debugging=debugging)
                do_no_paren(number, operator)
                # break
        return inner_number

    # check if there are lists inside lists
    has_list = False
    for num in number:
        debug_print('Is list?:', num, type(num) is list)
        if type(num) is list:
            has_list = True  # to detect if should just operate assuming no paren
            num_index = number.index(num)

            # extracting string to paren
            prior, post = operator[:num_index], operator[num_index + len(num) - 1:]
            inner_op = operator[num_index: num_index + len(num) - 1]
            operator = prior + post
            debug_print('outer list: operator[', operator, ']', debugging=debugging)
            debug_print('inner list: operator[', inner_op, ']', debugging=debugging)

            number[num_index] = do_operators(num, inner_op)  # function call to reassign list into a number
    # if no list, send to be calculated
    if not has_list:
        do_no_paren(number, operator)

    if len(number) > 1:
        debug_print('still left to calculate')
        do_operators(number, operator)
        '''
    if len(operator) < 1:
        print('done calculating')
        return number[0]
        '''
    debug_print('final:', number, operator, debugging=debugging)
    return number[0]

def debug_print(*stringy_stuff, debugging = False):
    if debugging:
        print(*stringy_stuff)

def get_answer(sentence):
    number = get_operand_operator(sentence)
    operator = get_operand_operator(sentence, False)
    #print(number, operator)
    answer = do_operators(number, operator)
    return answer



