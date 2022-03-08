# Obs: Tanto professores quanto alunos estudam

class Pessoa:
    def falar(self):
        print('Falando como Pessoa')


class Aluno(Pessoa):
    def falar(self):
        print('Falando como Aluno')


class Professor(Pessoa):
    def falar(self):
        print('Falando como Professor')
        

# Estou herdando tanto a classe Professor quanto a classe Aluno
class Estudante01(Professor, Aluno):
    pass


class Estudante02(Aluno, Professor):
    pass

estudante01 = Estudante01()
estudante02 = Estudante02()

# Busca na classe Estudante se este método existe, caso exista ele exibe o da própria classe, caso não exista ele procura uma classe pai que possua este método
# Como os dois pais possuem uma classe com o mesmo nome, ele busca o pai que foi informado primeiro e após isso ele executa a função deste pai

estudante01.falar()  # Falando como Professor
estudante02.falar()  # Falando como Aluno
