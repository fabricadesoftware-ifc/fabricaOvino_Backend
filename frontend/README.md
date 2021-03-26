# Ovino - Frontend

O objetivo do frontend é apresentar uma interface amigável e intuitiva para o usuário, e realizar chamadas para o backend para consultar e alterar o estado do sistema. O backend usa o framework Nuxt.js, que extende a funcionalidade do Vue.js, facilitando a realização de server-side rendering (SSR).

**Leia a documentação dos frameworks, e todo esse documento, antes de começar a desenvolver.**

## Server-side rendering

Operando no modo SSR, existem dois componentes: o cliente, que executa no navegador do usuário; e o servidor, que executa lado-a-lado com o backend.

Quando o usuário abre o navegador em uma página, o servidor renderiza todo o HTML e CSS, poupando processamento do navegador. As interações posteriores do usuário com a página são processadas localmente pelo cliente.

Escolhemos implementar SSR para, entre outros motivos:

* Melhor desempenho, principalmente em dispositivos móveis

* Melhor search engine optimization

## Linting

Para identificar e corrigir erros de programação e de formatação, utilizamos o ESLint junto do Prettier.

## Debugging

Para diagnosticar erros durante a execução do código, é preciso configurar o debugging tanto para o cliente como para o servidor. As instruções a seguir se aplica para o editor VSCode e o navegador Firefox.

**Etapas para configurar o Firefox:**

1. Instale o Firefox Developer Edition, que já vem com remote debugging habilitado.

2. Execute-o com a opção `--ProfileManager` e crie um novo perfil com o nome `eventos2`.

O projeto já contém um arquivo `launch.json` com as configurações de debug para o VSCode. No menu de debug, selecione `fullstack: nuxt` para iniciar o cliente e o servidor simultâneamente.

## Internationalization (i18n)

Os arquivos de tradução do projeto se encontram no diretório `locales/`. Eles podem ser editados à mão, com a ajunda do `npm run lintfix` para consertar erros.

Para uma experiência mais "sofisticada, este editor pode ser usado: https://github.com/jcbvm/i18n-editor. Basta usar a função "Import project" e escolher o diretório `locales/`.


## Diagrama de como estão organizados nossos módulos

Alguns dos itens que estão ali ainda não estão totalmente prontos ou criados, sendo assim é necessário verificar e realizar a criação/atualização deles. 

* https://drive.google.com/file/d/1wILZtGvS_hRvXy6-bPWsgKBBYo_fWyhT/view?usp=sharing
