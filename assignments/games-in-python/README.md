
# 🎮 Jogo da Forca (Hangman)

Objetivo
--------

Crie uma versão do clássico jogo da forca em Python para praticar manipulação de strings, estruturas de controle e entrada do usuário.

O que você vai construir
------------------------

Um jogo onde o jogador tenta adivinhar uma palavra letra por letra antes de esgotar o número de tentativas. A palavra deve ser escolhida aleatoriamente a partir de uma lista predefinida.

Habilidades praticadas
----------------------

- Manipulação de strings
- Estruturas de repetição e decisão (loops e condicionais)
- Tratamento de entrada do usuário
- Uso do módulo random

Tarefas
-------

1. Implementar a lógica principal do jogo:
	- Selecionar uma palavra aleatória de uma lista
	- Mostrar o estado atual da palavra com letras descobertas e underscores para letras não adivinhadas
	- Ler palpites do usuário (letras)
	- Controlar letras já tentadas e número de tentativas restantes
	- Verificar condições de vitória e derrota

2. Tratar entradas inválidas (mais de uma letra, caracteres não alfabéticos, palpites repetidos)

3. (Opcional) Melhorias extras:
	- Carregar palavras de um arquivo `words.txt` em vez de uma lista interna
	- Suporte a dicas (hint)
	- Interface simples no terminal com cores

Requisitos (critério de aceitação)
---------------------------------

O programa concluído deve:

- Selecionar palavras aleatoriamente a partir de uma lista ou arquivo
- Aceitar palpites de letras e atualizar o estado visível da palavra (ex.: _ a _ _ a _ )
- Controlar e exibir o número de tentativas restantes
- Evitar que o jogador repita palpites já feitos
- Encerrar com mensagem de vitória quando a palavra for adivinhada
- Encerrar com mensagem de derrota quando as tentativas se esgotarem

Arquivos fornecidos
-------------------

- `starter-code.py` — ponto de partida com esqueleto do jogo (não entregue aqui? verifique a pasta)
- `README.md` — este arquivo

Como executar
-------------

1. Abra um terminal na pasta `assignments/games-in-python`
2. Execute:

```bash
python3 starter-code.py
```

Dicas
-----

- Teste com palavras curtas durante o desenvolvimento
- Faça validação das entradas para melhorar a experiência do usuário
- Use funções pequenas e bem nomeadas para organizar a lógica

Critérios de avaliação
----------------------

- Código claro e legível
- Tratamento de entradas inválidas
- Cobertura das funcionalidades obrigatórias listadas em "Requisitos"

Próximos passos (extras recomendados)
----------------------------------

- Adicionar testes automatizados simples para as funções que manipulam o estado do jogo
- Criar um arquivo `words.txt` com uma lista de palavras e alterar o código para carregá-lo

Licença e atribuição
--------------------

Conteúdo educativo — use e adapte para fins de aprendizagem
