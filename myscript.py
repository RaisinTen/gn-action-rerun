import datetime
import sys

filename = sys.argv[1]

print('Writing to ' + filename)

with open(filename, 'w') as out:
    out.write(str(datetime.datetime.now()) + '\n')
