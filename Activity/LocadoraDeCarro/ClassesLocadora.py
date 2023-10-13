# O aluno deverá desenvolver uma aplicação em Python utilizando PyQt ou PySide, 
# para uma locadora de veículos, comunicando com o banco de dados no qual deverá ter as seguintes funcionalidades: 

# - Opções para locar o carro por diária 
# - Opções para locar o carro mensalista 
# - Opções de compra do carro 

# Categorias (aluguel-diario, compra, Mensalista)

# O sistema deverá permitir cadastrar os veículos e em qual categoria ele se enquadra. 
# (Cadastrar, R(mostrar os dados), U(editar os dados), D(deletar se o carro nunca foi alugado ou vendido)). 
# Cadastrar usuário para realizar a venda ou a locação. 

from Crud import Conexao # para importar uma classe de outro arquivo
#from pasta1 import arquivo1

conexao = Conexao.conexao_banco()


