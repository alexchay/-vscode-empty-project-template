import os
import pprint
import sys

if __name__ == '__main__':
    #
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(sys.path)
    #
    print(os.environ.get('ENVIRONMENT'))