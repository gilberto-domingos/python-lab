from ..p_model.operator_model import Operator


operator_obj = Operator("5665", "5985699", "Leandro")

print(operator_obj.get_cod_operator())
print(operator_obj.get_cnpj_operator())
print(operator_obj.get_name_operator())

operator_obj.set_name_operator("Ricardo")

print(operator_obj.get_name_operator())
