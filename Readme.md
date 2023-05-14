# Pi-Votorantim-2023

Para baixar o repositório:

* git clone https://github.com/Projeto-Integrador-Univesp-Votorantim/aplicacao-django.git

Após baixar o repositório, usar o comando:
* pip install -r requirements.txt

OBS: este comando irá instalar as dependências python (pacotes necessários) para a execução da aplicação

Para verificar o banco de dados definido é necessário configurar o arquivo settings.py, presente no caminho ./projeto/settings.py

Encontre a linha com os códigos abaixo:<br>
<img src="configuracao.png"><br>

Para verificar os dados do BD:
<code>
* python manage.py shell<br>
\>\>\> from pi.models import Habilidades<br>
\>\>\> Habilidades.objects.all()
</code><br><br>
Com isso, vemos que todos os dados do banco estão presentes

<hr>

\- 07/maio/2023 - Adicionado templates base, arquivos estáticos como css, view home(para teste)<br>
\- 07/maio/2023 - Feito layout da home, header e footer<br>
\- 08/maio/2023 - Feito layout da página de cadastro de professores, com arquivo css e adição ao template<br>
