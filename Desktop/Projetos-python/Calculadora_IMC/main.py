#
from pessoaIMC import Pessoa as P

p1 = P("João", "06-04-2007",48 ,174)
p1.calculoImc(58.00, 1.70)
print(
    f" Nome:{p1.nome}\n Data de Nascimento:{p1.nascimento}\n Peso:{p1.peso}\n Altura:{p1.altura}"
)
print(f" IMC:{p1.imc}")
p1.resultImc()
