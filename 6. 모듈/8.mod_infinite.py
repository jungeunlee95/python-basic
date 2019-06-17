import sys

import mod_a

print('import infinite')

for key in sys.modules.keys():
    print(key)