from function import *
import pytest

def test_calculate_total_cost_0topping():
    input = []
    expected_result = 25
    actual_result = calculate_total_cost(input)
    assert expected_result == actual_result
    
def test_calculate_total_cost_1topping_Bubble():
    input = ["Bubble"]
    expected_result = 30
    actual_result = calculate_total_cost(input)
    assert expected_result == actual_result

def test_calculate_total_cost_1topping_GrassJelly():
    input = ["Grass Jelly"]
    expected_result = 35
    actual_result = calculate_total_cost(input)
    assert expected_result == actual_result

def test_calculate_total_cost_1topping_RedBean():
    input = ["Red Bean"]
    expected_result = 40
    actual_result = calculate_total_cost(input)
    assert expected_result == actual_result

def test_calculate_total_cost_1topping_WipCream():
    input = ["Wip Cream"]
    expected_result = 40
    actual_result = calculate_total_cost(input)
    assert expected_result == actual_result
 
def test_calculate_total_cost_2topping_Bubble_and_RedBean():
    input = ["Bubble","Red Bean"]
    expected_result = 45
    actual_result = calculate_total_cost(input)
    assert expected_result == actual_result

def test_calculate_total_cost_2topping_GrassJelly_and_WipCream():
    input = ["Grass Jelly","Wip Cream"]
    expected_result = 50
    actual_result = calculate_total_cost(input)
    assert expected_result == actual_result

def test_check_bill_0topping():
    input1 = 25
    input2 = []
    expected_result = "Great! Your order with  costs $25. Enjoy your milk tea!"
    actual_result = check_bill(input1,input2)
    assert expected_result == actual_result
    
def test_check_bill_1toppin_bubble():
    input1 = 30
    input2 = ["Bubble"]
    expected_result = "Great! Your order with Bubble costs $30. Enjoy your milk tea!"
    actual_result = check_bill(input1,input2)
    assert expected_result == actual_result
    
def test_check_bill_1topping_jelly():
    input1 = 35
    input2 = ["Grass Jelly"]
    expected_result = "Great! Your order with Grass Jelly costs $35. Enjoy your milk tea!"
    actual_result = check_bill(input1,input2)
    assert expected_result == actual_result

def test_check_bill_2topping():
    input1 = 40
    input2 = ["Bubble","Grass Jelly"]
    expected_result = "Great! Your order with Bubble, Grass Jelly costs $40. Enjoy your milk tea!"
    actual_result = check_bill(input1,input2)
    assert expected_result == actual_result
