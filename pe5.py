
# pe5.py
def generate_table(row=None, col=None):
    multi_table = [["X".rjust(5)] + [str(i).rjust(5) for i in range(1, 13)]] + [[str(j).rjust(5)] + [str(i * j).rjust(5) for i in range(1, 13)] for j in range(1, 13)]
    if row is None or col is None:
        return multi_table
    if row > 12 or col > 12:
        raise IndexError("Row or Column index is out of range!")
    return multi_table[row][col]

def print_table():
    multi_table = generate_table()
    for row in multi_table:
        print(''.join(row))



