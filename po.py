import os

packages = [
    "asgiref=*",
    "beautifulsoup4=*",
    "contourpy=*",
    "coverage=*",
    "cycler=*",
    "Django=*",
    "django-bootstrap4=*",
    "fonttools=*",
    "kiwisolver=*",
    "matplotlib=*",
    "numpy=*",
    "packaging=*",
    "pandas=*",
    "pillow=*",
    "pyparsing=*",
    "python-dateutil=*",
    "pytz=*",
    "six=*",
    "soupsieve=*",
    "sqlparse=*",
    "typing_extensions=*",
    "tzdata=*",
    "psycopg2-binary=*",
    "django-dotenv=*",
    "dj-database-url=*",
    "whitenoise[brotli]=*",
    "gunicorn=*",
    "uvicorn=*",
]

for package in packages:
    os.system(f'poetry add "{package}"')

print("\nFim da instalação dos pacotes.\n")
