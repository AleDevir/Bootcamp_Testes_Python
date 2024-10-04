'''
Módulo Pytest
https://learn.microsoft.com/pt-br/training/modules/test-python-with-pytest/5-exercise

execução na raiz do projeto 'Bootcamp_Testes_Python': pytest exercicio_pytest -v

execução no diretório 'exercicio_pytest': pytest -v test_exercise.py
'''
import pytest


def admin_command(command, sudo=True):
    """
    Prefix a command with `sudo` unless it is explicitly not needed. Expects
    `command` to be a list.
    """
    if not isinstance(command, list):
        raise TypeError(f"was expecting command to be a list, but got a {type(command)}")
    if sudo:
        return ["sudo"] + command
    return command

