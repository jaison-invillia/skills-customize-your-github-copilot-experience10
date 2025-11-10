# Instruções do GitHub Copilot

## Mensagens de Commit

Todas as mensagens de commit devem seguir o padrão **Conventional Commits**.

### Formato

```
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé(s) opcional(is)]
```

### Tipos Principais

- **feat**: Uma nova funcionalidade
- **fix**: Correção de bug
- **docs**: Mudanças apenas na documentação
- **style**: Mudanças que não afetam o significado do código (espaços, formatação, ponto e vírgula, etc)
- **refactor**: Mudança de código que não corrige bug nem adiciona funcionalidade
- **perf**: Mudança de código que melhora performance
- **test**: Adição ou correção de testes
- **chore**: Mudanças no processo de build ou ferramentas auxiliares

### Exemplos

#### Commits Simples
```
feat: adiciona validação de email no formulário de login
fix: corrige erro ao salvar dados do usuário
docs: atualiza README com instruções de instalação
style: formata código com prettier
refactor: reorganiza estrutura de pastas do projeto
perf: otimiza consulta ao banco de dados
test: adiciona testes para módulo de autenticação
chore: atualiza dependências do projeto
```

#### Commits com Escopo
```
feat(auth): implementa autenticação com JWT
fix(dashboard): corrige exibição de gráficos
docs(api): documenta endpoints de usuário
refactor(database): migra de MySQL para PostgreSQL
```

#### Commits com Corpo
```
feat: adiciona integração com API de pagamento

Implementa integração completa com Stripe incluindo:
- Processamento de cartão de crédito
- Webhooks para confirmação de pagamento
- Tratamento de erros
```

#### Commits com Breaking Changes
```
feat!: altera estrutura da API de usuários

BREAKING CHANGE: o endpoint /users agora retorna um objeto paginado
em vez de um array simples. Clientes devem atualizar para acessar
users.data para obter a lista de usuários.
```

### Regras

1. Use o imperativo no tempo presente: "adiciona" não "adicionado" ou "adicionando"
2. Não capitalize a primeira letra da descrição
3. Não use ponto final na descrição
4. A descrição deve ter no máximo 72 caracteres
5. Use o corpo para explicar o "o quê" e "por quê", não o "como"
6. Separe o corpo da descrição com uma linha em branco

# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados
- **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes