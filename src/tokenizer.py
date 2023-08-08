separators = ["+", "-"," "]
operators = ["+", "-"]

def notEmpty(s):
    return not (s.isspace() or len(s) == 0)

def extract_lexeme(raw_string): 
    lexemes = []
    lexeme = ""

    for c in raw_string:
        if c in separators:
            if notEmpty(lexeme):
                lexemes.append(lexeme)
            if notEmpty(c): 
                lexemes.append(c)
            lexeme = ""
        else:
            lexeme += c
    if notEmpty(lexeme): lexemes.append(lexeme) 
    
    return lexemes

def isDice(s):
    if s.count("d") == 1:
        [l, r] = s.split("d")
        return l.isnumeric() and r.isnumeric()
    return False

def extract_tokens(lexeme_list):
    tokens = []
    for l in lexeme_list:
        if isDice(l):
            tokens.append((l, "DICE"))
        elif l in operators:
            tokens.append((l, "OPERATOR"))
        elif l.isnumeric():
            tokens.append((int(l), "NUMBER"))
    return tokens

def tokenize(s):
    return extract_tokens(extract_lexeme(s))

def reconstruct(tokens):
    s = ""
    first = True
    for t in tokens:
        if first: 
            first = False
        else:
            s += " "
        s += str(t[0])
    return s
