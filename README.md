# Projeto Ovino

Projeto de ovinocultura, desenvolvimento em parceria entre a Fábrica de Software e o NEPPA

## Setup para desenvolvimento

O sistema é composto por duas partes: o **backend**, construído em Django, implementa a persistência de dados e regras de negócio, e disponibiliza uma API que segue os princípios REST; e o **frontend**, feito com o framework Nuxt.js.

### Backend

Requisitos:

* [Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [Docker Compose](https://docs.docker.com/compose/install/)
* [Poetry](https://poetry.eustace.io/docs/)

```sh
# Inicializar o banco de dados
sudo docker-compose up -d

# Configurações (editar se necessário)
cp .env.sample .env

# Instalar as dependências
poetry install
# Executar os comandos dentro do virtualenv (criado automaticamente)
poetry run python manage.py migrate
poetry run python manage.py runserver
```

O backend responde localmente na porta 8000: http://localhost:8000/api/v1/swagger/. Para mais detalhes sobre o seu funcionamento, leia o [README do diretório backend](backend/README.md).

**Para fazer um commit, você deve estar dentro do virtualenv do backend.**

Use o poetry para isso:
```sh
poetry shell
```

Configure os hooks de commit para executar verificações de código antes de fazer um commit.

```sh
pre-commit install
```

### Frontend

Requisitos:

* [Node.js](https://nodejs.org/)

```sh
# Todas as operações do frontend devem ser feitas a partir deste diretório
cd frontend

# Instalar as dependências
npm install
# Executar em modo de desenvolvimento
npm run dev
```

O frontend responde localmente na porta 3000: http://localhost:3000/. Para mais detalhes sobre o seu funcionamento, leia o [README do diretório frontend](frontend/README.md).

