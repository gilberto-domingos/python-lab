class TaxRegime:
    def __init__(self, cod_tax_regime, descr_tax_regime, id=None):
        self.id = id
        self.cod_tax_regime = cod_tax_regime
        self.descr_tax_regime = descr_tax_regime

    def get_cod_tax_regime(self):
        return self.cod_tax_regime

    def set_cod_tax_regime(self, cod_tax_regime):
        self.cod_tax_regime = cod_tax_regime

    def get_descr_tax_regime(self):
        return self.descr_tax_regime

    def set_descr_tax_regime(self, descr_tax_regime):
        self.descr_tax_regime = descr_tax_regime

    def display_info(self):
        print(f"Código: {self.cod_tax_regime}, "
              f"Descrição: {self.descr_tax_regime}, "
              f"ID: {self.id}")
