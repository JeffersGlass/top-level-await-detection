import ast
class TopLevelAsyncFinder(ast.NodeVisitor):
    def is_source_async(self, source):
        self.async_found = False
        node = ast.parse(source)
        self.generic_visit(node)
        return self.async_found

    def visit_Await(self, node):
        self.async_found = True

    def visit_AsyncFor(self, node):
        self.async_found = True

    def visit_AsyncWith(self, node):
        self.async_found = True

    def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef):
        pass # Do not visit children of async function defs

if __name__ == "__main__":
    import sys
    file = sys.argv[1]

    with open(file, 'r') as f:
        source = f.read()
    
    print(f"File {file} {'uses' if TopLevelAsyncFinder().is_source_async(source) else 'does not use'} top level await")