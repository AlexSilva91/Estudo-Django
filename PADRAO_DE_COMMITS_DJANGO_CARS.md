# 📘 Padrão de Commits -- Projeto Django_Cars

Este documento define o padrão oficial de commits do projeto
**Django_Cars**. O objetivo é manter consistência, legibilidade e
facilitar versionamento semântico.

------------------------------------------------------------------------

## 🎯 Estrutura do Commit

Formato padrão:

    <tipo>(escopo opcional): descrição curta

    [corpo opcional]

    [rodapé opcional]

------------------------------------------------------------------------

## 🏷 Tipos de Commit

  Tipo       Quando usar
  ---------- -----------------------------------------------
  feat       Nova funcionalidade
  fix        Correção de bug
  refactor   Refatoração sem mudança de comportamento
  chore      Tarefas internas (configuração, dependências)
  docs       Alterações na documentação
  style      Formatação, lint, sem alteração lógica
  test       Criação ou alteração de testes
  perf       Melhoria de performance
  build      Alterações de build ou dependências
  ci         Configurações de integração contínua

------------------------------------------------------------------------

## 🧩 Exemplos

### Nova funcionalidade

    feat(cars): adiciona modelo Car com campos básicos

### Correção de bug

    fix(auth): corrige erro de autenticação no login

### Refatoração

    refactor(views): simplifica lógica de listagem de carros

### Documentação

    docs(readme): adiciona instruções de instalação

------------------------------------------------------------------------

## 📌 Regras Gerais

-   Use verbo no **imperativo**
    -   Correto: "adiciona validação"
    -   Errado: "adicionando validação"
-   Descrição curta com até 72 caracteres
-   Não use ponto final
-   Seja objetivo e técnico

------------------------------------------------------------------------

## 🚀 Versionamento Semântico (SemVer)

Seguimos o padrão:

    MAJOR.MINOR.PATCH

| Tipo de Commit \| Impacto na versão \|

\|---------------\|------------------\| feat \| Incrementa MINOR \| \|
fix \| Incrementa PATCH \| \| BREAKING CHANGE \| Incrementa MAJOR \|

------------------------------------------------------------------------

## 🔥 Breaking Changes

Quando houver alteração incompatível:

    feat(api): altera estrutura de resposta da API

    BREAKING CHANGE: campo "price" agora retorna decimal

------------------------------------------------------------------------

## 📂 Fluxo Sugerido de Branches

-   master → Produção
-   develop → Desenvolvimento
-   feature/\* → Novas funcionalidades
-   hotfix/\* → Correções urgentes

------------------------------------------------------------------------

## ✅ Checklist Antes do Commit

-   Código testado?
-   Lint validado?
-   Nome do commit segue o padrão?
-   Sem arquivos desnecessários (venv, db.sqlite3)?

------------------------------------------------------------------------

Documento criado para padronização interna do projeto.
