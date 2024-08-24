from pt_gt_dk import main_msg

def test_function1():
    r = main_msg.show_name()
    assert r == "Muhammad Saleh Saqib"

def test_function2():
    r = main_msg.show_name()
    assert r != "Pakistan"