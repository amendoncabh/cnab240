
try:
    import unittest2 as unittest
except ImportError:
    import unittest

# import os
# import codecs

from cnab import errors
from cnab.bancos import bancodobrasil
from cnab.tipos import Arquivo
from tests.data_bancobrasil import (
    get_banco_brasil_data_from_dict,
    # get_banco_brasil_file_remessa,
    # ARQS_DIRPATH
)


class TestBancoBrasilPagamentoCnab240(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBancoBrasilPagamentoCnab240, self).__init__(*args, **kwargs)
        self.maxDiff = None

    def setUp(self):
        self.data = get_banco_brasil_data_from_dict()
        self.arquivo = Arquivo(bancodobrasil, **self.data['header'])

    def test_banco_do_brasil_pagamento(self):

        for evento in self.data['pagamento']:
            self.arquivo.incluir_debito_pagamento(
                **evento
            )
        # TODO: FIXME
        # self.assertEqual(
        #     unicode(self.arquivo),
        #     get_banco_brasil_file_remessa()
        # )

    def test_banco_do_brasil_arquivo_vazio(self):
        arquivo = Arquivo(bancodobrasil)
        self.assertRaises(errors.ArquivoVazioError, unicode, arquivo)

    # TODO: FIXME
    # def test_leitura(self):
    #     return_file_path = os.path.join(
    #         ARQS_DIRPATH,
    #         'pagamento.bancodobrasil.ret'
    #     )
    #     ret_file = codecs.open(return_file_path, encoding='ascii')
    #     arquivo = Arquivo(bancodobrasil, arquivo=ret_file)
    #     ret_file.seek(0)
    #     self.assertEqual(ret_file.read(), unicode(arquivo))

if __name__ == '__main__':
    unittest.main()
