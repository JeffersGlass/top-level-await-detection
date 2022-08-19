import ast
from typing import Any

class asyncVisitor(ast.NodeVisitor):
    def __init__(self):
        self.async_found = False

    def visit_Await(self, node):
        self.async_found = True

    def visit_AsyncFor(self, node):
        self.async_found = True

    def visit_AsyncWith(self, node):
        self.async_found = True

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        pass # Do not visit children of async function defs
           
def is_async_visit(source: str) -> bool:
    node = ast.parse(source)
    visitor = asyncVisitor()
    visitor.generic_visit(node)
    return visitor.async_found

async_statement_node_types = (ast.Await, ast.AsyncFor, ast.AsyncWith)
async_allowed_contexts = (ast.AsyncFunctionDef, )

def is_async_walk(source: str) -> bool:
    node = ast.parse(source)
    print(ast.dump(node, indent=2))
    
    for n in ast.walk(node):
        if n.__class__ in async_statement_node_types:
            return True
    return False

if __name__ == "__main__":

    filename = "async_finder_tests/helloworld.py"

    with open(filename, 'r') as f:
        source = f.read()

    #print(f"Is {filename} using top-level await? {is_async_walk(source)= }")
    print(f"Is {filename} using top-level await? {is_async_visit(source)= }")