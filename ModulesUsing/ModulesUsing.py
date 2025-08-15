import sys

import sales
# or:
from sales import calc_shipping, calc_tax
# import all objects: import *

# When complie this file ,a pyc binary file is created in ...\ModulesUsing\__pycache__\sales.cpython-313
calc_shipping()
calc_tax


sales.calc_tax()

print(sys.path)
