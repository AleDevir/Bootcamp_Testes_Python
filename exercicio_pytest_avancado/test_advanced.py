'''
Módulo Pytest Avançado
https://learn.microsoft.com/pt-br/training/modules/python-advanced-pytest/5-exercise

execução na raiz do projeto 'Bootcamp_Testes_Python': pytest exercicio_pytest_avancado -v

execução no diretório 'exercicio_pytest_avancado': pytest -v test_advanced.py
'''
import os
import pytest 


def str_to_bool(string):
    if string.lower() in ['yes', 'y', '1']:
        return True
    elif string.lower() in ['no', 'n', '0']:
        return False

