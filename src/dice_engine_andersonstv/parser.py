from dice import Dice

# TO DO: Better error handling, instead of raising exceptions and stoping, continue parsing and list errors at the end.

# TO DO: Remove getters and setters, unnecessary not pythonic

class SyntaxTree():
    def __init__(self):
        self.root = None
    def set_root(self, node):
        self.root = node
    def get_root(self):
        return self.root
    def __str__(self):
        return str(self.root)

class Node():
    def __init__(self, token):
        self.token = token
        self.child_L = None
        self.child_R = None
        self.parent = None
    def add_child(self, node):
        if (self.child_L == None):
            self.child_L = node
        elif (self.child_R == None):
            self.child_R = node
        else:
            raise Exception("Error while parsing: Trying to add children to a full node")
    def set_parent(self, node):
        self.parent = node
    def get_token(self):
        return self.token
    def __str__(self):
        s = "Node: " + str(self.token)
        c1 = str(self.child_L) if self.child_L == None else str(self.child_L.get_token())
        c2 = str(self.child_R) if self.child_R == None else str(self.child_R.get_token())

        s+= " Children: [ L: " + c1 + " | R: " + c2 + "]"
        return s

def parse_and_eval(tokens):
    tokens_dice, annotated_str = evaluate_dice(tokens)
    tree = parse(tokens_dice)
    return annotated_str, evaluate_tree(tree)
def parse(tokens):
    tree = SyntaxTree()
    last_token = None

    for t in tokens:

        node = Node(t)
        root = tree.get_root()
        if t[1] == "NUMBER":
            if root == None:
                tree.set_root(node)
            elif root.get_token()[1] == "OPERATOR":
                node.set_parent(root)
                root.add_child(node)
                tree.set_root(root)
            elif root.get_token()[1] == "NUMBER":
                raise Exception("Error while parsing: Subsequent numbers. Ex: 2 +4 3")
        
        elif t[1] == "OPERATOR":
            if root == None: # +6 = 0 + 6
                new_node = Node((0, "NUMBER")) # Obs: Only works for + and -. Has to be updated when new operators are added
                new_node.set_parent(node)
                node.add_child(new_node)
                tree.set_root(node)
            elif root.get_token()[1] == "NUMBER" or root.get_token()[1] == "OPERATOR":
                root.set_parent(node)
                node.add_child(root)
                tree.set_root(node)
            
        last_token = t
    return tree


# Returns a list tokens after evaluating dice, replacing the dice tokens with the number obtained.
# Does not alter the original token list
def evaluate_dice(tokens):
    new_tokens = []
    reconst = ""

    for t in tokens:
        new_token = t

        if t[1] == "DICE":
            [q, s] = t[0].split("d")
            d = Dice(int(q), int(s))

            reconst += t[0] + str(d.get_result()) +" " 
            new_token = (d.get_total(), "NUMBER")
        else:
            reconst += str(t[0]) + " "
        new_tokens.append(new_token)
    return new_tokens, reconst

def evaluate_tree(tree):
    return evaluate(tree.root)
def evaluate(node):
    token = node.get_token()
    if token[1] == "NUMBER": 
        return token[0]
    if token[1] == "OPERATOR":
        if token[0] == "+":
            return evaluate(node.child_L) + evaluate(node.child_R)
        elif token[0] == "-":
            return evaluate(node.child_L) + evaluate(node.child_R)
