# Independent reference for "Base64 encode data" (Python 3, standard library only).
# expected.txt is this program's stdout; omc never produced it.
import base64
for s in ['M', 'Ma', 'Man', 'Hello, World!', 'To err is human, but to really foul things up you need a computer.\n    -- Paul R. Ehrlich']:
    print(base64.b64encode(s.encode()).decode())
