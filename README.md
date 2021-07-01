# cashback-api

> API desenvolvida utilizando FastAPI para Registrar/Autenticar um Usuário e Cadastrar/Listar/Editar/Deletar as compras feitas por esse Usuário. É possível também acompanhar o Cashback Acumulado a partir de uma requisição em outra API.

## Como utilizar com Docker

De forma mais simples, basta rodar estes comandos na raíz do projeto:

``` make dbuild ```

Para rodar os testes:

``` make dtest ```

* precisa ter o Docker instalado


## Endpoints 
Estão implementados endpoints para **autenticação** e **compras**. Para facilitar o uso, basta acessar o **Swagger** da aplicação (/docs), registrar um usuário (/auth/register) e utilizar o campo **Authorize** para gerar o token e passar para todos os endpoints de forma automática.

#### Authentication

- ``` /auth/register ``` - POST - Cria um usuário.

- ``` /auth/login ``` - POST - autentica o usuário gerando um token para utilizar nos endpoints.


#### Purchases
- ``` /purchases ``` - GET - Lista todas as compras cadastradas.

- ``` /purchases ``` - POST - Cria um usuário a partir da entrada abaixo

- ``` /purchases/acumCashback ``` - GET - Lista o cashback acumulado para o cpf do usuário autenticado a partir da consulta de uma **API Externa**.

- ``` /purchases/:id ``` - PUT - Atualiza uma compra cujo status é "Em avaliação".

- ``` /purchases/:id ``` - DELETE - Remove uma compra cujo status é "Em avaliação".

- ``` /docs ``` - Documentação da Api.


# Conclusão

Há validações que não foram possíveis serem feitas, dado o tempo para desenvolver. Também há mais testes que precisam ser implementados para corrigir algumas falhas.
