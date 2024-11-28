# Python_Teste_para_tutores

**Desafio** é um jogo de plataforma simples desenvolvido em Python usando a biblioteca **pgzero**. O jogo apresenta um herói que deve evitar inimigos em movimento enquanto coleta itens e progride através de diferentes plataformas. O projeto inclui animações de sprite para o herói e inimigos, sons de fundo e de colisão, além de um menu inicial interativo.

## Requisitos

Este projeto foi desenvolvido com as seguintes bibliotecas:

- **pgzero**: Biblioteca principal para a criação de jogos em Python.
- **math**: Utilizada para operações matemáticas simples, como física e movimento.
- **random**: Para movimentação aleatória dos inimigos.

A biblioteca **Pygame** não foi utilizada, exceto pela classe **Rect** para detecção de colisões.

## Funcionalidades

- **Menu Principal**: Com opções para iniciar o jogo, ativar/desativar música e sair.
- **Movimento do Herói**: O herói pode se mover para a esquerda, direita e pular.
- **Inimigos em Movimento**: Inimigos se movem aleatoriamente pela tela e podem colidir com o herói.
- **Animação de Sprite**: O herói e os inimigos possuem animações de movimento (ex: pular e andar).
- **Música de Fundo e Sons**: O jogo toca uma música de fundo e efeitos sonoros para salto e colisão.
- **Colisões**: O jogo detecta colisões entre o herói e os inimigos, reiniciando o jogo ao colidir.

## Como Jogar

1. Ao iniciar o jogo, use as teclas **[seta para a esquerda]** e **[seta para a direita]** para mover o herói.
2. Pressione **[barra de espaço]** para fazer o herói pular.
3. Evite os inimigos e tente passar pelas plataformas.
4. Se colidir com um inimigo, o jogo será reiniciado.
5. No menu principal, pressione **[S]** para começar o jogo.

## Como Executar

1. Instale as dependências com o comando:

   ```bash
   pip install pgzero
