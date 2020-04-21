# Ovinos - Backend

O objetivo do backend é a prover uma API que o frontend possa interagir com os dados do sistema. O backend usa a framework Django com o pacote Django Rest Framework (DRF) para facilitar a construção da API seguindo os princípios REST.

**Leia a documentação dos frameworks, e todo esse documento, antes de começar a desenvolver.**

## API

### Autenticação

A identificação dos clientes ocorre por JSON Web Tokens (JWT). Um token é obtido por meio do endpoint `/signin/` e deve ser enviado em cada requisição subsequente, no cabeçalho `Authorization`, prefixado com `Bearer ` (com espaço).

### Documentação

A interface do Swagger localizada em http://localhost:8000/api/v1/swagger/ é usada para explorar a API.

Para usar endpoints que necessitam de autenticação:

1. Utilize o endpoint `/signin/` para obter um access token
2. Pressione o botão _Authorize_ no topo da página.
3. Preencha o campo de texto com o token, prefixado com a palavra Bearer, seguida de um espaço. Por exemplo: `Bearer eyJ0eXAiO...`

## Gerenciamento de dependências

Os pacotes necessários para o funcionamento estão especificados no arquivo `pypoetry.toml`. Os requisitos não devem ser alterados manualmente. Em vez disso, o gestor de pacotes [Poetry](https://poetry.eustace.io/docs/) deve ser usado, pois verifica de forma mais rígida os requisitos de versão.

## Configurações

O arquivo de configurações normal do Django é utilizado: `settings.py`. Algumas variáveis, no entanto, são parametrizados para aceitar valores de variáveis de ambiente, facilitando a sua modificação em diferentes ambientes (desenvolvimento, produção).

## Organização do código

_TODO_

### Serializers

A função dos serializers é traduzir objetos JSON enviados pelo cliente para uma representação interna, e vice-versa.

Não é função dos serializers:

* Criar/alterar dados no banco.
* Implementar regras de negócio. Por exemplo: não permitir usuários com e-mail duplicado, utilizando um UniqueValidator. Isso deve ser implementado apenas em services.

### Views

A função das views é tratar as requisições dos clientes, retornando uma resposta adequada. Sua principal preocupação é lidar com os métodos e códigos de status do HTTP. Para tal: utiliza os serializers para interpretar os dados de entrada; faz chamadas à algum service caso necessário; e utiliza serializers novamente para gerar uma resposta.

Evitamos as views genéricas, pois causam a realização de consultas ao banco diretamente nas views, causando acoplação. 

### URLs / rotas

Tiramos proveito do uso de viewsets, para gerar URLs de forma padronizada, por meio de routers. Cada app define um router, que mapeia as actions de cada viewset registrado para uma URL. Esses routers são adicionados a um roteador global, no arquivo `urls.py`.

## Linting

Para identificar e corrigir erros de programação e de formatação, utilizamos as ferramentas `flake8`, `black`, e `isort`.

## Testing

Para executar os testes, utilizamos o `pytest`:

```sh
poetry run pytest
```
