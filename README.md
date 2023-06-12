![image](https://github.com/Quezia-Moura/P2-Estrutura-de-Dados/assets/102929131/145be61a-2121-45f3-ba86-b1c9efa86c68)


<h1>SOFTWARE PARA ADOÇÃO DE ANIMAIS</h1>
<h2>Alunos: João Victor Lopes dos Santos e Quézia Trindade Moura</h2>
<h3>Professor: 

[Marcio Alexandre Dias Garrido][identificador]

[identificador]: https://github.com/marciogarridoLaCop
</h3>
<h3>Disciplina: Estrutura de Dados</h3>
<hr>

<h4>ENUNCIADO</h4>

  A Universidade de Vassouras do Campus 1 foi convidada pela prefeitura de Maricá para promover uma solução tecnológica em um dos problemas sociais da cidade, o abandono de animais. Mesmo considerado crime (O abandono de animais é crime, previsto na Lei de Crimes Ambientais - Lei Federal n° 9.605 de 1998), e notório que o índice de abandono vem crescendo a cada ano.
  
  Os alunos do curso de Engenharia de Software foram convocados para a reunião com a secretaria da cidade para entender a demanda solicitada e alguns pontos foram levantados. A prefeitura precisa de um sistema que possa cadastrar todos os animais por tipo (canino, felino, etc.) e para tanto, é uma premissa que seja possível inserir novos tipos dinamicamente. Precisa ainda, que sejam classificados por idade aproximada, cor, porte e se possui alguma particularidade. No mesmo sistema, deverá ter também um cadastro de
pessoas interessadas na adoção, contendo os dados principais de contato e qual espécie teria o interesse de adotar. Ao escolher a espécie, deve também informar se possui alguma preferência do animal. Por fim, no final do mês a prefeitura emitirá um relatório de cruzamento de espécies disponíveis x possíveis candidatos, ou quando um candidato a adoção ligar, que o atendente possa pesquisar se há algum animal com as características informadas.

  Os alunos anotaram atentamente a todas as observações, criaram o fluxograma do estudo de caso, e posteriormente o primeiro protótipo em Python, ainda que em modo texto, e sem requisitos gráficos. A ideia foi apenas validar a proposta do programa junto ao solicitante.
<hr>

<h4>FLUXOGRAMA</h4>

![image](https://github.com/Quezia-Moura/P2-Estrutura-de-Dados/assets/133873524/c26cd1cf-1ae9-46e7-addc-c5b1e6187e8b)

<hr>

<h4>CÓDIGO</h4>

  Foi dividido em 4 (quatro) arquivos <b>.py</b> para melhor manipulação do conteúdo do código.
 
 
 - Menu

  Neste arquivo fazemos a inicialização do código com opções para o usuário escolher. De acordo com a opção escolhida, uma nova função é chamada para continuar o código, em um arquivo diferente.
  
![image](https://github.com/Quezia-Moura/P2-Estrutura-de-Dados/assets/125207561/0b3d511f-6ae5-4faf-ab52-91dd495ea5c9)

  
 - Cadastro de Animais

  Neste arquivo foram determinadas variáveis, onde cada uma recebe 1 (um) <b>arquivo.txt</b> que armazena os dados de espécies específicas. Exemplo: variável dados_caninos recebe o arquivo.txt que guarda todas as informações de cada canino.
  
![image](https://github.com/Quezia-Moura/P2-Estrutura-de-Dados/assets/125207561/b8b9eadb-468b-47fb-b840-fe09eac40c19)


 - Cadastro de Pessoas

  Aqui fizemos o mesmo que o anterior, porém com apenas uma variável recebendo um arquivo.txt responsável por armazenar todos os dados de cada pessoa que se cadastrar tanto para adotar um animal quanto para colocar animais para a adoção.

![image](https://github.com/Quezia-Moura/P2-Estrutura-de-Dados/assets/125207561/254e55ad-9d10-440a-ba86-e24ccf3985ae)


 - Consulta

  Neste arquivo é onde é possível realizar consultas dos animais disponíveis para adoção.
Como os dados foram salvos em arquivos de texto, para conseguirmos acessar e manipular melhor os dados, armazenamos-os em listas fazendo um tratamento de string, tornando assim possível a consulta e relação entre o que o cliente gostaria de adotar e o que temos disponível.

![image](https://github.com/Quezia-Moura/P2-Estrutura-de-Dados/assets/125207561/bde0adf3-ad56-406e-9302-5f985c4d3164)
<hr>

<h4>PROGRAMA RODANDO</h4>
  
  Por fim, abaixo se encontra o terminal com o código rodando no momento de consulta, onde por exemplo, a pessoa interessada na adoção informa o animal desejado e uma característica e conforme esses dados conseguimos mostrar o que está disponível para adoção. Logo em seguida é mostrado o início do código com o menu, caso a pessoa queira usa-lo novamente.
  
![image](https://github.com/Quezia-Moura/P2-Estrutura-de-Dados/assets/125207561/852fd6cd-7b35-43ed-aca7-c95ed0e9df68)

