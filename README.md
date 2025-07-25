# Implementação do Padrão MVC

Um projeto Python de estudo das aulas da Rocketseat demonstrando a implementação do padrão arquitetural MVC (Model-View-Controller).

## Visão Geral do Projeto

Este projeto demonstra uma implementação limpa do padrão MVC, separando as responsabilidades em três componentes
principais:

- **View**: Lida com a interface do usuário e interação
- **Controller**: Contém a lógica de negócio e gerencia o fluxo de dados
- **Model**: Gerencia o armazenamento e manipulação de dados


1. **View**
    - Responsável por apresentar dados aos usuários
    - Gerencia elementos da interface do usuário
    - Encaminha entradas do usuário para o Presenter

2. **Controller**
    - Processa a entrada do usuário vinda da View
    - Contém a lógica de negócio
    - Atualiza o Model conforme necessário
    - Gerencia o fluxo de dados entre View e Model

3. **Model**
    - Gerencia os dados da aplicação
    - Fornece métodos para acesso e manipulação de dados
    - Mantém a integridade dos dados

## Configuração

1. Clone o repositório

