import unittest
from fgslpycnpj.cnpj.CNPJ import CNPJ
from fgslpycnpj.cnpj.DigitoVerificador import DigitoVerificador

class TestCNPJ(unittest.TestCase):

    def testCNPJ(self):
        numero = "12.ABC.345/01DE-35"
        cnpj = CNPJ(numero)        

        self.assertTrue(cnpj.valida())

    def testDigitoVerificador(self):
        base = "12.ABC.345/01DE"
        cnpj = CNPJ(base)
        dv = DigitoVerificador(base)        
        self.assertEqual(4,dv.calcula())
        self.assertEqual("35",cnpj.gera_dv())

if __name__ == '__main__':
    unittest.main()