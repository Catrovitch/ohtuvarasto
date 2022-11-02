import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_index_tilavuus_is_under_0(self):

        varasto = Varasto(-1)

        self.assertEqual(varasto.tilavuus, 0)

    def test_index_saldo_is_under_0(self):

        varasto = Varasto(0,-1)

        self.assertEqual(varasto.saldo, 0)

    def test_maara_is_under_0(self):

        self.assertEqual(self.varasto.lisaa_varastoon(-1), None)

    def test_maara_is_more_than_tilavuus(self):

        self.varasto.lisaa_varastoon(15)

        self.assertEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_varastosta_under_0(self):

        self.assertEqual(self.varasto.ota_varastosta(-1), 0.0)

    def test_ota_varastosta_maara_is_more_than_saldo(self):

        kaikki_mita_voidaan = self.varasto.ota_varastosta(5)

        self.assertEqual((kaikki_mita_voidaan, self.varasto.saldo), (1.0, 0.0))

    def test_str(self):

        self.assertEqual(self.varasto.__str__(), f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}")


