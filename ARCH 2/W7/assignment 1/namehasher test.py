from namehasher import set_dict_key, encode_string, decode_string, encode_list, decode_list, validate_values


def test_encode_string():
    set_dict_key("A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@")
    # check if given the hashmap string, the correct output is given
    assert "**9 (?##*(;* :0;=?!5;" == encode_string("EEN CORRECTE UITKOMST")
    # check if case insesitive input is handle correctly
    assert "*en (orrecte :itkomst" == encode_string("Een Correcte Uitkomst")


def test_decode_string():
    set_dict_key("A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@")
    # check if given hasmap string, the correct decode output is given
    assert "ANDERSOM WERKT OOK" == decode_string("%9)*#5?! ]*#=; ??=")
    # check if case insesitive input is handle correctly
    assert "Ook Met Kleine Letters" == decode_string("?ok !et =leine 1etters")


def test_encode_list():
    set_dict_key("A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@")
    # check if given a list of values the encoded output is a list of encoded values
    assert [">0*;*#", ">%9"] == encode_list(["PIETER", "PAN"])


def test_decode_list():
    set_dict_key("A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@")
    # check if given a list of values the decoded output is a list of decoded values
    assert ["PIETER", "PAN"] == decode_list([">0*;*#", ">%9"])


def test_validate_values():
    set_dict_key("A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@")
    # check if the given values are equal based on the provided hashmap
    assert True == validate_values(">0*;*#", "PIETER")
    # check if the given values are not equal based on case sensitivity and the provided hashmap
    assert False == validate_values(">0*;*#", "Pieter")
