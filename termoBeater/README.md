Desenvolvi em #python um script para jogar o game term.ooo. O jogo é similar a uma "forca" e funciona da seguinte forma: você precisa adivinhar uma palavra de 5 letras gerada aleatoriamente pelo site. A cada tentativa, você recebe dicas sobre a posição das letras nessa palavra (imagem).

Utilizando essas informações, o script começa a filtrar as palavras a partir de uma lista de palavras importada do repo (https://lnkd.in/d_pvznmx).

Para melhorar a precisão das respostas e diminuir o número de tentativas, utilizei 4 filtros sendo;

1 - Filtra palavras que nescessáriamente contém a letra informada
2 - Filtra palavras que não possuem a letra informada
3 - Filtra palavras que possuem a letra informada pelo usuário em uma posição específica
4 - Filtra por negativa de posição, ou seja, caso o usuário informe a letra “C” na posição 2, todas as palavras que cumprem a condição são removidas dos possíveis resultados
