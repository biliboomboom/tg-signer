import re
import ast

with open('tg_signer/core.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the broken f-string pattern
content = re.sub(
    r'self\.log\(f"问题: \n\{text\}"\)',
    'self.log(f"问题: \\\\n{text}")',
    content
)

with open('tg_signer/core.py', 'w', encoding='utf-8') as f:
    f.write(content)

# Verify
try:
    ast.parse(open('tg_signer/core.py', encoding='utf-8').read())
    print("Syntax OK!")
except SyntaxError as e:
    print(f"Still has error: {e}")
