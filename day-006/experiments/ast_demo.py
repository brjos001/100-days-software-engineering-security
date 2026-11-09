
import ast

source = "x = 10 + 20"

tree = ast.parse(source)

print(ast.dump(tree, indent=4))