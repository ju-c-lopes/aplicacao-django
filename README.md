# Pi-Votorantim-2024

URL da aplicação em produção: [https://aplicacao-django.onrender.com](https://aplicacao-django.onrender.com)

Aplicação em produção no **Render Cloud** (render.com), usando **Postgres** como banco de dados, e servidor de arquivos estáticos e mídia em **Bucket da AWS S3**.

Para testar a aplicação para registro de aulas, está disponibilizado o um usuário com _nickname:_ **usuario-teste**, e _password:_ **kufx0%Q3Sc0GUo**

Este usuário é limitado a registrar até 15 aulas, sendo imposibilitado de fazer novos registros, se limitando a fazer apenas consultas das aulas registradas.

## Pré-Requisitos

---

-   [Python >= 3.11](https://www.python.org/downloads/)
-   [Django >= 5.0.4](https://docs.djangoproject.com/en/5.0/intro/install/)

## Iniciando o projeto

---

### Opção 1: Setup Completo Automático (Recomendado)

Para setup completo do projeto após clonar o repositório:

```bash
git clone https://github.com/Projeto-Integrador-Univesp-Votorantim/aplicacao-django.git
cd aplicacao-django
./build.sh
```

O script `build.sh` irá automaticamente:

-   🔧 Instalar Poetry e dependências
-   📊 Coletar arquivos estáticos
-   🗄️ Criar e aplicar migrações do banco de dados
-   📋 Popular o banco com dados iniciais (Disciplinas, Turmas, Habilidades)
-   👤 Criar superusuário (se `CREATE_SUPERUSER=True` no arquivo `.env`)

### Opção 2: Setup Manual

Se preferir fazer o setup passo a passo:

1. **Clone o repositório:**

    ```bash
    git clone https://github.com/Projeto-Integrador-Univesp-Votorantim/aplicacao-django.git
    cd aplicacao-django
    ```

2. **Instale as dependências:**

    ```bash
    pip install poetry
    poetry install --no-root
    ```

3. **Configure o banco de dados:**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Popular banco com dados iniciais:**

    ```bash
    # Usando comando Django (recomendado)
    python manage.py init_db

    # OU usando script shell
    ./populate_db.sh
    ```

5. **Criar superusuário (opcional):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Iniciar o servidor:**
    ```bash
    python manage.py runserver
    ```

### Opção 3: Apenas Popular Banco de Dados

Se você já fez migrações e quer apenas popular o banco:

```bash
# Básico
./populate_db.sh

# Forçar inserção (ignorar duplicatas)
./populate_db.sh --force

# Usar comando Django
./populate_db.sh --django-command
```

### Configuração de Ambiente

O projeto usa um arquivo `.env` para configurações. Certifique-se de que existe e contém:

```env
SECRET_KEY=sua_chave_secreta_aqui
DEBUG=True
CREATE_SUPERUSER=False
```

## 🧹 Limpeza de Dívida Técnica - Import Refactoring

---

### Problema Identificado

O projeto originalmente continha vários problemas de importação que afetavam performance e manutenibilidade:

- **Importações Circulares**: Módulos importando uns aos outros criando loops de dependência
- **Wildcard Imports**: Uso excessivo de `from module import *` carregando código desnecessário
- **Importações Redundantes**: Módulos importando muito mais do que realmente precisavam

### Refatoração Realizada

Foi realizada uma refatoração completa eliminando todos os imports problemáticos:

#### 📁 **Models** (`gerenciaAula/models/`)
- ✅ Removidas todas as importações wildcard (`from gerenciaAula.models import *`)
- ✅ Implementadas referências string para ForeignKeys evitando dependências circulares
- ✅ Cada modelo agora importa apenas o que necessita

**Exemplo de melhoria:**
```python
# ❌ ANTES (problemático)
from gerenciaAula.models import *

class Disciplina(models.Model):
    aulas = models.ForeignKey(Aula, ...)  # Dependência circular!

# ✅ DEPOIS (limpo)
from django.db import models

class Disciplina(models.Model):
    aulas = models.ForeignKey('Aula', ...)  # Referência string
```

#### 📁 **Views** (`gerenciaAula/views/`)
- ✅ Eliminadas todas as importações circulares (`from gerenciaAula.views import *`)
- ✅ Cada view agora declara explicitamente suas dependências
- ✅ Imports específicos apenas do que é usado

**Exemplo de melhoria:**
```python
# ❌ ANTES (problemático)
from gerenciaAula.views import *
from gerenciaAula.models import *

# ✅ DEPOIS (limpo)
from django.shortcuts import render
from gerenciaAula.models import Aula, Usuario
from gerenciaAula.forms import LoginForm
```

#### 📁 **Forms** (`gerenciaAula/forms/`)
- ✅ Removidas importações circulares (`from gerenciaAula.forms import *`)
- ✅ Imports limpos apenas do Django e modelos necessários
- ✅ Zero dependências desnecessárias

### Benefícios Alcançados

#### 🚀 **Performance**
- **Carregamento mais rápido**: Módulos carregam apenas o necessário
- **Menos uso de memória**: Sem objetos desnecessários em memória
- **Startup mais rápido**: Django inicia sem resolver dependências circulares

#### 🛠️ **Manutenibilidade**
- **Dependências claras**: Cada arquivo mostra exatamente o que precisa
- **Debugging facilitado**: Mais fácil rastrear origem de problemas
- **Refatoração segura**: Mudanças não quebram dependências ocultas

#### 🔧 **Qualidade de Código**
- **Zero imports circulares**: Eliminado risco de runtime errors
- **Código mais limpo**: Imports organizados e explícitos
- **Melhor IDE support**: Autocompletar e análise estática funcionam melhor

### Verificação

Para confirmar que não há mais imports problemáticos:

```bash
# Verificar se não há mais wildcard imports
grep -r "import \*" gerenciaAula/

# Verificar se não há imports circulares
grep -r "from gerenciaAula\." gerenciaAula/ | grep "import \*"

# Verificar integridade do Django
python manage.py check
```

**Resultado esperado**: Todos os comandos devem retornar vazio ou "System check identified no issues".

### Impacto no Projeto

Esta refatoração transformou o projeto de um estado com múltiplas dependências circulares e imports desnecessários para um código base limpo, performático e manutenível. A aplicação agora segue as melhores práticas Python/Django para gestão de imports.

---

## Integrando com o banco de dados

---

<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/sqlite/sqlite-original-wordmark.svg" style="width: 200px;" alt="SQLite3 Logo" />

O banco de dados utilizado no projeto é o **SQLite3**, localizado em `./projeto/settings/db.sqlite3`, para facilitar o compartilhamento do BD entre a equipe, evitando complexidades de instalações.

### Executando a aplicação

A aplicação já está configurada. Para iniciar o servidor:

```bash
python manage.py runserver
```

Em seguida, acesse no navegador: `http://127.0.0.1:8000`

### Dados Iniciais do Banco

O banco é automaticamente populado com:

-   **📚 6 Disciplinas**: Matemática, Português, História, Geografia, Química, Física
-   **🎓 3 Turmas**: 1° Ano, 2° Ano, 3° Ano
-   **🎯 50+ Habilidades**: Códigos BNCC (EM13LGG101, EM13MAT101, etc.)

### Verificando os dados

Para verificar os dados através da linha de comando:

```python
python manage.py shell
from gerenciaAula.models import Habilidade, Disciplina, Turma
print(f"Disciplinas: {Disciplina.objects.count()}")
print(f"Turmas: {Turma.objects.count()}")
print(f"Habilidades: {Habilidade.objects.count()}")
```

### Scripts de População

-   **`./entrypoint.sh`** - Setup completo (migrations + população)
-   **`python manage.py init_db`** - Comando Django para popular banco
-   **`./populate_db.sh`** - Script shell independente

Para mais detalhes, consulte o arquivo [`DATABASE_POPULATION.md`](DATABASE_POPULATION.md)

<hr>

## ☁️ Deploy via Fly.io
A aplicação foi configurada para deploy automatizado em ambiente de produção com o serviço Fly.io, utilizando uma infraestrutura leve, escalável e gratuita.

### 📦 Destaques da Infraestrutura:

* 🐳 Docker: Imagem customizada com Poetry, SQLite e Gunicorn

* 🧪 Testes automatizados com pytest, rodando via GitHub Actions antes do deploy

* 🚀 CI/CD completo com GitHub Actions, integrado à branch main

* 💾 Banco SQLite com volume persistente no Fly.io (sem custos com PostgreSQL)

* ⚙️ Script de entrada (entrypoint.sh) responsável por:

Aplicar migrações (migrate)

Popular o banco com os dados iniciais (Disciplinas, Turmas, Habilidades)

Criar superusuário opcional

Rodar o servidor com Gunicorn

🔐 Gerenciamento de secrets via Fly.io, incluindo SECRET_KEY, ALLOWED_HOSTS, DEBUG e outros

🌐 Aplicação online (modo vitrine):
https://aplicacao-django.fly.dev

<hr>
