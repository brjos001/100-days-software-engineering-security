import ast
import dis

source = """
def multiply(x):
    return x * 2
"""

# 1. Inspect the source structure
tree = ast.parse(source)
print("AST:")
print(ast.dump(tree, indent=4))

# 2. Compile the source
code = compile(source, "<experiment>", "exec")
print("\nCode object:")
print(type(code))

function_code = code.co_consts[0]
print(type(function_code))
print(function_code.co_name)
print(function_code.co_varnames)

dis.dis(function_code)

# 3. Inspect the compiled instructions
print("\nBytecode:")
dis.dis(code)

def multiply(x):
    return x * 2

print("Function:", multiply)
print("GFunction type:", type(multiply))

print("Code object:", multiply.__code__)
print("Code type:", type(multiply.__code__))

print("Same code object:", multiply.__code__ is multiply.__code__)