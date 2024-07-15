# Classe Pessoa: Crie uma super classe que modele uma Pessoa. Esta classe deve possuir os seguintes atributos:​
# Matricula; Nome; Idade;  ​
# Subclasses:​
# Defina as subclasses de Pessoa serão Aluno e Professor, estas devem conter além dos atributos herdados de Pessoa seus atributos identificadores, ex: Classe Aluno (NOTAS; MEDIA). ​
# Classe Professor (Formacao, Disciplina, Carga Horária e Salario)​
# Você deve criar métodos específicos para cada subclasse, ex: calcular_media, estudar, lecionar.​

from Ex2pessoa import Pessoa

pes1=Pessoa("665","Thiago",29)
pes1.getDados()
