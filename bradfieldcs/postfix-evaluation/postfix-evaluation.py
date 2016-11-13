"""
Postfix evaluation
"""
import sys



def add(op1,op2):
    return op1 + op2

def subtract(op1,op2):
    return op1 - op2

def divide(op1,op2):
    return (op1 * 1.0) / op2

def multiply(op1,op2):
    return op1 * op2

operator_map = {
    '*': multiply,
    '+': add,
    '-': subtract,
    '/': divide
}

operators = operator_map.keys()


def postfix_evaluation(expression):
    token_stack = []
    for token in expression:
        if token not in operators:
            token_stack.append(int(token))
        else:
            op2 = token_stack.pop()
            op1 = token_stack.pop()
            op3 = operator_map[token](op1,op2)
            token_stack.append(op3)

    return token_stack.pop()


def postfix_evaluation_recur(expression):
    """
    Recursive solution to the Postfix evaluation function
    """
    if len(expression) == 1:
        return float(expression[0])
    else:
        for index, token in enumerate(expression):
            if token in operators:
                op1_index = index - 2
                op2_index = index - 1
                op2 = float(expression[op2_index])
                op1 = float(expression[op1_index])
                op3 = str(operator_map[token](op1,op2))
                new_expression = expression[:op1_index] + [op3] + expression[index+1:]
                return postfix_evaluation_recur(new_expression)





if __name__ == '__main__':
    postfix = sys.argv[1]
    expression = postfix.split(" ")
    print postfix_evaluation_recur(expression)
