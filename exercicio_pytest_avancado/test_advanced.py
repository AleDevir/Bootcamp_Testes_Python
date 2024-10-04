'''
Módulo Pytest Avançado
https://learn.microsoft.com/pt-br/training/modules/python-advanced-pytest/5-exercise
comando para executar o teste: pytest -v test_avanced.py
'''
import os
import pytest 


def str_to_bool(string):
    if string.lower() in ['yes', 'y', '1']:
        return True
    elif string.lower() in ['no', 'n', '0']:
        return False

