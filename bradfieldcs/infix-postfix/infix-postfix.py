"""
Converts an infix expression to a postfix expression
for token in expression
	if token is not an operator:
		append the token to output_list
	if token is an operator:
		peek at the top of the op_list
		compare token to top of op_list
		if priority of token is greater than priority of top of op_list:
			append token to op_list
		else:
			while priority token is < priority top:
				pop top of op_list
				append top to output_list
			append token to op_list

for token in op_list:
	pop operator from op_list
	append operator to output_list

Example:
A + B * C  - D-> ABC*+D-

"""
import sys


class Stack:

    def __init__(self):
        self.stack = []

    def __str__(self):
        return "{}".format(self.stack)

    def is_empty(self):
        """
        Checks if the Stack is empty
        """
        return True if len(self.stack) == 0 else False

    def peek(self):
        """
        View top of stack without removing token
        """
        return None if self.is_empty() else self.stack[-1]

    def pop(self):
        """
        Remove an token from the top of the stack
        """
        return None if self.is_empty() else self.stack.pop()

    def push(self,token):
        """
        Push an token to the top of the stack
        """
        self.stack.append(token)



def infix_to_postfix(expression):
    """
    """
    print expression
    output_list = []
    op_stack = Stack()
    PRECEDENCE = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
        None: 0
    }
    LEFT_PARENS = '('
    RIGHT_PARENS = ')'
    PARENS = [LEFT_PARENS,RIGHT_PARENS]
    operators = ['+', '-', '*','/']
    for token in expression:
        if token not in PARENS and token not in operators:
            output_list.append(token)
        elif token == LEFT_PARENS:
            op_stack.push(token)
        elif token == RIGHT_PARENS:
            top = op_stack.pop()
            while top in operators:
                output_list.append(top)
                top = op_stack.pop()
        else:
            top = op_stack.peek()
            if top in operators and PRECEDENCE[token] > PRECEDENCE[top]:
                op_stack.push(token)
            elif top == LEFT_PARENS:
                op_stack.push(token)
            else:
                top = op_stack.pop()
                while top and top != LEFT_PARENS:
                    output_list.append(top)
                    top = op_stack.pop()
                op_stack.push(token)

    while not op_stack.is_empty():
        output_list.append(op_stack.pop())

    return " ".join(output_list)




if __name__ == '__main__':
    infix = sys.argv[1]
    expression = infix.split(" ")
    print infix_to_postfix(expression)
