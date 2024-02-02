import random

global variables, operators, negations, max_length
    # Beispielaufruf
variables = ['A', 'B', 'C', 'D','E']
operators = ['∧', '∨']
negations = ['','¬']
max_length = 5


def generate_random_boolean_formula():
    if max_length < 1:
        raise ValueError("Maximale Länge muss mindestens 1 sein.")
    if not variables:
        raise ValueError("Es müssen mindestens einige Variablen vorhanden sein.")
    def generate_subformula(length):
        if length == 1:
            return random.choice(negations)+random.choice(variables)
        else:
            operator = random.choice(operators)
            if operator == '¬':
                subformula = generate_subformula(length - 1)
            else:
                left_length = random.randint(1, length - 1)
                right_length = length - left_length
                left_subformula = generate_subformula(left_length)
                right_subformula = generate_subformula(right_length)
                subformula = f"({left_subformula} {operator} {right_subformula})"
            return subformula

    return generate_subformula(max_length)

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def parse_boolean_formula(formula):
    # Hilfsfunktion, um die Position des Hauptoperators zu finden
    def find_main_operator_position(formula):
        stack = []
        for i, char in enumerate(formula):
            if char == '(':
                stack.append(i)
            elif char == ')':
                stack.pop()
            elif char in {'and', 'or', 'not'} and not stack:
                return i
        return -1

    # Hilfsfunktion, um den Hauptoperator und seine Position zu extrahieren
    def extract_main_operator_and_position(formula):
        position = find_main_operator_position(formula)
        if position != -1:
            return formula[position:position + 3], position
        return None, -1

    main_operator, position = extract_main_operator_and_position(formula)

    if main_operator is None:
        # Das bedeutet, dass die Formel nur eine Variable ist
        return TreeNode(formula)

    left_formula = formula[1:position].strip()
    right_formula = formula[position + 3:-1].strip() if main_operator != 'not' else None

    return TreeNode(main_operator,
                    parse_boolean_formula(left_formula),
                    parse_boolean_formula(right_formula))

def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left is not None or node.right is not None:
            print_tree(node.left, level + 1, "Left: ")
            print_tree(node.right, level + 1, "Right: ")

# Beispielaufruf
formula = "(A and (B or C))"
tree = parse_boolean_formula(generate_random_boolean_formula())
print_tree(tree)
