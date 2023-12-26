from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('Djalma', 46)

p1.comer('Maça')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.comer('alimento')
p1.parar_falar()
p1.falar("Assunto")

print(p1.ano_atual)
print(p2.ano_atual)

print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())




