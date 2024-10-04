'''
Módulo unittest
https://learn.microsoft.com/pt-br/training/modules/python-get-started-testing/3-exercise
Execução do teste: python test_exercise.py 
'''
import unittest

def str_to_bool(value):
    '''
    String para bool
    '''
    try:
        value = value.lower()
    except AttributeError:
        raise AttributeError(f"{value} must be of type string")
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False

class TestStrToBool(unittest.TestCase):
    '''
    Classe de teste unittest
    '''

    def test_y_is_true(self):
        '''
        Teste usando bool
        '''
        result = str_to_bool('y')
        self.assertTrue(result)

    def test_yes_is_true(self):
        '''
        Teste usando bool
        '''
        result = str_to_bool('Yes')
        self.assertTrue(result)

    def test_invalid_input(self):
        '''
        Teste tratamento de exceção
        '''
        with self.assertRaises(AttributeError):
            str_to_bool(1)













if __name__ == '__main__':
    unittest.main()
