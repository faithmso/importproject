from utils.common import file_operations
from utils.find import find_in

file_operations.save_to_file('Rolf', 'data.txt')

print(file_operations.read_file('data.txt'))