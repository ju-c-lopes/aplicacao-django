# Pi-Votorantim-2024

URL da aplicação em produção: [https://aplicacao-django.onrender.com](https://aplicacao-django.onrender.com)

Aplicação em produção no **Render Cloud** (render.com), usando **Postgres** como banco de dados, e servidor de arquivos estáticos e mídia em **Bucket da AWS S3**.

Para testar a aplicação para registro de aulas, está disponibilizado o um usuário com _nickname:_ **usuario-teste**, e _password:_ **kufx0%Q3Sc0GUo**

Este usuário é limitado a registrar até 15 aulas, sendo imposibilitado de fazer novos registros, se limitando a fazer apenas consultas das aulas registradas.


## Pré-Requisitos
---
* [Python >= 3.10](https://www.python.org/downloads/)
* [Django >= 5.0.4](https://docs.djangoproject.com/en/5.0/intro/install/)

## Iniciando o projeto
---
Para baixar o repositório:  
`git clone https://github.com/Projeto-Integrador-Univesp-Votorantim/aplicacao-django.git`

Após baixar o repositório, usar o comando: `pip install -r requirements.txt`

*OBS: este comando irá instalar as dependências python (pacotes necessários) para a execução da aplicação* 

## Integrando com o banco de dados
--- 

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlite/sqlite-original-wordmark.svg" style="width: 200px;" alt="SQLite3 Logo" />

O banco de dados utilizado no projeto atualmente está sendo o SQLite3, para facilitar o compartilhamento do BD entre a equipe, evitando complexidades de instalações.

A aplicação já está configurada, então é necessário apenas ligar o servidor que pode ser executado a partir da raiz da aplicação com o seguinte comando:

```
python manage.py runserver
```

Para então, no seu navegador, digitar o endereço ```127.0.0.1:8000```


Para verificar os dados do BD através da linha de comando, pode usar os seguintes comando:

``` python
python manage.py shell
from gerenciaAula.models import Habilidade
Habilidade.objects.all()
```

Com isso, vemos que todos os dados do banco estão presentes

<hr>
