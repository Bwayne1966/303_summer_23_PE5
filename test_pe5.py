# test_pe5.py
import pytest
from pe5 import generate_table
from datetime import datetime

@pytest.fixture(autouse=True)
def timer():
    start = datetime.now()
    yield
    print(f"Test took: {datetime.now() - start}")

def test_generate_table_basic1():
    expected = [['    X', '    1', '    2', '    3', '    4', '    5', '    6', '    7', '    8', '    9', '   10', '   11', '   12'], 
                ['    1', '    1', '    2', '    3', '    4', '    5', '    6', '    7', '    8', '    9', '   10', '   11', '   12'], 
                ['    2', '    2', '    4', '    6', '    8', '   10', '   12', '   14', '   16', '   18', '   20', '   22', '   24'], 
                ['    3', '    3', '    6', '    9', '   12', '   15', '   18', '   21', '   24', '   27', '   30', '   33', '   36'], 
                ['    4', '    4', '    8', '   12', '   16', '   20', '   24', '   28', '   32', '   36', '   40', '   44', '   48'], 
                ['    5', '    5', '   10', '   15', '   20', '   25', '   30', '   35', '   40', '   45', '   50', '   55', '   60'], 
                ['    6', '    6', '   12', '   18', '   24', '   30', '   36', '   42', '   48', '   54', '   60', '   66', '   72'], 
                ['    7', '    7', '   14', '   21', '   28', '   35', '   42', '   49', '   56', '   63', '   70', '   77', '   84'], 
                ['    8', '    8', '   16', '   24', '   32', '   40', '   48', '   56', '   64', '   72', '   80', '   88', '   96'], 
                ['    9', '    9', '   18', '   27', '   36', '   45', '   54', '   63', '   72', '   81', '   90', '   99', '  108'], 
                ['   10', '   10', '   20', '   30', '   40', '   50', '   60', '   70', '   80', '   90', '  100', '  110', '  120'], 
                ['   11', '   11', '   22', '   33', '   44', '   55', '   66', '   77', '   88', '   99', '  110', '  121', '  132'], 
                ['   12', '   12', '   24', '   36', '   48', '   60', '   72', '   84', '   96', '  108', '  120', '  132', '  144']]
    assert generate_table() == expected


def test_generate_table_basic2():
    assert generate_table()[0][0] == '    X'
    assert generate_table()[1][0] == '    1'
    assert generate_table()[0][1] == '    1'
    assert generate_table()[1][1] == '    1'

@pytest.mark.xfail
def test_generate_table_xfail():
    assert generate_table()[0][0] == 'Y'  # This is expected to fail

def test_out_of_range():
    with pytest.raises(IndexError):
        result = generate_table()  # This should raise an IndexError as we're exceeding the size limit
        assert result[13][13]

@pytest.mark.parametrize( 
"row, col, expected", 
    [ 
    (0, 0, '    X'), 
    (1, 0, '    1'), 
    (0, 1, '    1'), 
    (1, 1, '    1'), 
    ] 
) 
def test_generate_table_basic3(row, col, expected): 
    assert generate_table()[row][col] == expected


