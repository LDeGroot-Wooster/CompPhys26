# import numpy
import pytest
from testbook import testbook

#@testbook('/Users/ldegroot/CompPhys26/Labs/LabAssignment3_S26.ipynb', execute=True)
#@testbook('/Users/ldegroot/OneDrive - The College of Wooster/a_PHYS230_S26/Labs/LabAssignment3_Solutions_S26.ipynb', execute=True)
#@testbook('/path/to/notebook.ipynb', execute=True)

@pytest.fixture(scope='module')
def tb():
    with testbook('/Users/ldegroot/OneDrive - The College of Wooster/a_PHYS230_S26/Labs/LabAssignment3_Solutions_S26.ipynb', execute=True) as tb:
        yield tb

def test_first_error_cell(tb):
    # Execute specific cell
    #tb.execute_cell('Error1')
    #out_vals = tb.cell_output('Error1')
    out_val = tb.execute_cell('Error1')
    #out_vals = tb.execute_cell()

    # assert the output 
    output_list = out_val["outputs"][0]["text"].splitlines()
    assert len(output_list) == 10
    assert float(output_list[-1]) == 9


def test_second_error_cell(tb):
    # Execute specific cell
    #tb.execute_cell('Error1')
    #out_vals = tb.execute_cell('Error2')
    tb.execute_cell('Error2')

  

def test_third_error_cell(tb): 
    tb.execute_cell('Error3')
    #result = tb.execute_cell('Error3')
    calc = tb.ref("calculate")
    assert calc(5) == -50


def test_fourth_error_cell(tb): 
    tb.execute_cell('Error4')
    #result = tb.execute_cell()
    #assert result[0] > 0
    #assert result[1] < 0
    quad = tb.ref("quadratic")
    assert round(quad(2,6,-35)[0],3) == 2.944



def test_first_snippet(tb):
    out_val = tb.execute_cell('Snippet1')

    # assert the output 
    output_list = out_val["outputs"][0]["text"].splitlines()
    assert len(output_list) == 13
    assert (output_list[-1]) == 's'


def test_second_snippet(tb):
    tb.execute_cell('Snippet2')
    # assert the output 
    output_list = out_val["outputs"][0]["text"].splitlines()
    assert len(output_list) == 1
    # which one of these is correct? or neither? 
    assert isinstance(output_list[0], numpy.ndarray)
    assert type(output_list[0]) == numpy.ndarray 
    # <class 'numpy.ndarray'>

def test_third_snippet(tb):
    tb.execute_cell('Snippet3')
    output_list = out_val["outputs"][0]["text"].splitlines()
    assert len(output_list) == 25


def test_fourth_snippet(tb):
    tb.execute_cell('Snippet4')
    #result = tb.execute_cell()
    magnitude = tb.ref("mag")
    assert round(magnitude(38.5),3) == 21.996

def test_Script1(tb): 
    tb.execute_cell('Script1')
    # assert the output 
    output_list = out_val["outputs"][0]["text"].splitlines()
    assert len(output_list) == 2
    assert (output_list[-1][-1]) == 11


def test_Script2(tb): 
    tb.execute_cell('Script2')
    #result = tb.execute_cell()
    #odd_sum = tb.ref("odd_sum")
    #assert odd_sum(1000000)[0] == 250000000000
    output_list = out_val["outputs"][0]["text"].splitlines()
    assert len(output_list) == 2


def test_Script3(tb): 
    tb.execute_cell('Script3')
    output_list = out_val["outputs"][0]["text"].splitlines()
    assert round((output_list[-1]),3) == 5.069
    assert round((output_list[-2]),3) == 5.069



