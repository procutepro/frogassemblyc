import re
import json
import app.lexalc as lexalc

KEYWORD_MAP = {
    "OUT": "print",
    "VAL": "variable",
    "ADD": "ADD",
    "SUB": "SUB",
    "MUL": "MUL",
    "DIV": "DIV",
    "PRINT": "printval",
    "SET": "redefine",
    "JIC": "jic",
    "LABEL": "label",
    "EXIT": "exit"
}

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

def tokenize_line(line):
    # Remove comments
    line = line.split('#')[0].strip()
    if not line:
        return []
    # Match strings as one token, then everything else
    return re.findall(r'"[^"]*"|\'[^\']*\'|\S+', line)

def parse_value(token):
    if token.startswith('"') and token.endswith('"'):
        return {"type": "string", "value": token[1:-1]}
    elif token.isdigit():
        return {"type": "number", "value": int(token)}
    else:
        return {"type": "identifier", "value": token}

def parse_file(filename):
    lines = read_file(filename)
    ast = {"children": []}

    for line in lines:
        tokens = tokenize_line(line)
        if not tokens:
            continue

        keyword = tokens[0].upper()
        if keyword not in KEYWORD_MAP:
            raise ValueError(f"Unknown keyword: {keyword}")

        node_type = KEYWORD_MAP[keyword]
        children = [parse_value(tok) for tok in tokens[1:]]
        node = {"type": node_type, "children": children}
        ast["children"].append(node)

    return ast

if __name__ == "__main__":
    source_file = input("frog ")
    ast = parse_file(source_file)
    with open("ast.json", "w") as f:
        json.dump(ast, f, indent=4)
    
    lexalc.doit()
