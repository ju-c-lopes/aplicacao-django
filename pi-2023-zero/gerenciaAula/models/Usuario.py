from gerenciaAula.models import *

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=45, blank=True, null=True)
    nivel_usuario = models.IntegerField(choices=ROLE_CHOICE, default=3)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=255, null=True, blank=True)
    eventual_doc = models.BooleanField(blank=True, null=True)  # This field type is a guess.
    cod_turma = models.ManyToManyField('Turma', db_column='cod_turma', blank=True, null=True)
    cod_disc = models.ManyToManyField('Disciplina', db_column='cod_disc', blank=True, null=True)

    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}'
    
    # Quando houver um post na classe User, deverá ser chamado o método create_user_profile

    # Ao criar este método, já foi criado o superuser, por isso o uso do try
    # para não quebrar o app ao fazer login com admin
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Usuario.objects.create(user=instance)
        except:
            pass
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.usuario.save()
        except:
            pass

    class Meta:
        db_table = 'Usuario'
