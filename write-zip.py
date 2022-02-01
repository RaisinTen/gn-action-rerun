import sys
from zipfile import ZipFile

input_file = sys.argv[1]
output_zip = sys.argv[2]

with ZipFile(output_zip, 'w') as zip:
    print('Writing ' + input_file + ' to ' + output_zip)
    zip.write(input_file)
