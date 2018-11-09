from django.db import models
from datetime import date

# Create your models here.

class Usuario(models.Model):

    dt_expiracao = models.DateField(default=date(year=1900, month=1, day=1))
    login        = models.TextField(max_length=30, unique=True)
    senha        = models.TextField(max_length=8) 
    def __str__(self):
        return self.login

class Coordenador(models.Model):
    
    usuario = models.OneToOneField(Usuario, null=True, on_delete=models.PROTECT)
    nome    = models.TextField(max_length=50)
    email   = models.EmailField(max_length=50, unique=True)  
    celular = models.TextField(max_length=11, unique=True)
    def __str__(self):
        return self.nome


class Aluno(models.Model):
    
    usuario = models.OneToOneField(Usuario, null=True, on_delete=models.PROTECT)
    nome    = models.TextField(max_length=50)
    email   = models.EmailField(max_length=50, unique=True)
    celular = models.TextField(max_length=11, unique=True)
    ra      = models.TextField(max_length=7, unique=True)
    foto    = models.TextField(max_length=100)
    def __str__(self):
        return self.nome

class Professor(models.Model):

    usuario = models.OneToOneField(Usuario, null=True, on_delete=models.PROTECT)

    nome    = models.TextField(max_length=50)
    email   = models.EmailField(max_length=50, unique=True)
    celular = models.TextField(max_length=11, unique=True)
    apelido = models.TextField(max_length=50)
    def __str__(self):
        return self.nome

class Curso(models.Model):

    curso = models.TextField(max_length=50, unique=True)
    def __str__(self):
        return self.curso

class Disciplina(models.Model):
    
    coordenador               = models.ForeignKey(Coordenador, on_delete=models.PROTECT)

    nome                      = models.TextField(max_length=30, unique=True)
    data                      = models.DateField(default=date.today)

    disciplina_status_choice = (('ABERTA','ABERTA'),('FECHADA','FECHADA'),)
    status                    = models.TextField(max_length=10, default="ABERTA",choices=disciplina_status_choice)
    
    plano_ensino              = models.TextField(max_length=1000)
    carga_horaria             = models.SmallIntegerField()
    competencias              = models.TextField(max_length=1000)
    habilidades               = models.TextField(max_length=1000)
    ementa                    = models.TextField(max_length=1000)
    conteudo_programatico     = models.TextField(max_length=1000)
    bibliografia_basica       = models.TextField(max_length=1000)
    bibliografia_complementar = models.TextField(max_length=1000)
    percentual_pratico        = models.SmallIntegerField()
    percentual_teorico        = models.SmallIntegerField()
    def __str__(self):
        return self.nome
    
       
class DisciplinaOfertada(models.Model):

    professor         = models.ForeignKey(Professor, on_delete=models.PROTECT)
    coordenador       = models.ForeignKey(Coordenador, on_delete=models.PROTECT)
    disciplina        = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
    curso             = models.ForeignKey(Curso, on_delete=models.PROTECT)

    dtiniciomatricula = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    dtfimmatricula    = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    ano               = models.SmallIntegerField()
    semestre          = models.SmallIntegerField()
    turma             = models.TextField(max_length=1)
    metodologia       = models.TextField(max_length=1000, null=True)
    recursos          = models.TextField(max_length=1000, null=True)
    criterioavaliacao = models.TextField(max_length=1000, null=True)
    planosdeaulas     = models.TextField(max_length=1000, null=True)
    
    class Meta:
       unique_together = ('curso', 'disciplina', 'turma', 'ano', 'semestre')
    def __str__(self):
        return self.disciplina

class SolicitacaoMatricula(models.Model):
      
    usuario = models.OneToOneField(Aluno, null=True, on_delete=models.PROTECT)
    disciplinaofertada = models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)
    coordenador        = models.ForeignKey(Coordenador, on_delete=models.PROTECT)

    dtresposta         = models.DateTimeField(auto_now_add=True, blank=True)
    status             = models.TextField(max_length=15)
    def __str__(self):
        return self.usuario

class Atividade(models.Model):

    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)

    titulo    = models.TextField(max_length=30) 
    descricao = models.TextField(max_length=100, null=True, unique=True) 
    conteudo  = models.TextField(max_length=8000) 
    tipo      = models.TextField(max_length=15) 
    extras    = models.TextField(max_length=100, null=True)    
    def __str__(self):
        return self.titulo


class AtividadeVinculada(models.Model):

    atividade     = models.ForeignKey(Atividade, on_delete=models.PROTECT)
    professor     = models.ForeignKey(Professor, on_delete=models.PROTECT)
    dofertada     = models.ForeignKey(DisciplinaOfertada, on_delete=models.PROTECT)

    rotulo        = models.TextField(max_length=500, unique=True)  
    status        = models.TextField(max_length=15)
    dtiniresposta = models.DateTimeField(auto_now_add=True, blank=True)
    dtfimresposta = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return self.atividade

class Entrega(models.Model):

    aluno               = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    professor           = models.ForeignKey(Professor, on_delete=models.PROTECT)
    atividade_vinculada = models.ForeignKey(AtividadeVinculada, on_delete=models.PROTECT)

    titulo              = models.TextField(max_length=100)
    resposta            = models.TextField(max_length=8000)
    dtentrega           = models.DateTimeField(auto_now_add=True, blank=True)
    dtavaliacao         = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    status              = models.TextField(max_length=10)
    nota                = models.DecimalField(max_digits=4,decimal_places=2, null=True)
    obs                 = models.TextField(max_length=500, null=True)
    def __str__(self):
        return self.aluno

class Mensagem(models.Model):
 
    aluno      = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    professor  = models.ForeignKey(Professor, on_delete=models.PROTECT)

    assunto    = models.TextField(max_length=100) 
    referencia = models.TextField(max_length=100) 
    conteudo   = models.TextField(max_length=500)
    status     = models.TextField(max_length=50) 
    dtenvio    = models.DateTimeField(auto_now_add=True, blank=True)
    dtresposta = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    resposta   = models.TextField(max_length=500, null=True)
    def __str__(self):
        return self.aluno


