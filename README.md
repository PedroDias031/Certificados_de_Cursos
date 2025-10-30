**🚀 Gerenciamento de Usuários com SQLAlchemy**

  Este é um script Python simples que demonstra operações básicas de CRUD (Create, Read, Update, Delete) em um banco de dados SQLite, utilizando a biblioteca SQLAlchemy como um Mapeador Objeto-Relacional (ORM).
  
**⚙️ Pré-requisitos**

  Para executar este código, você precisará ter o Python instalado e a biblioteca SQLAlchemy.InstalaçãoVocê pode instalar o SQLAlchemy usando pip:Bashpip install sqlalchemy
  
**📂 Estrutura do Projeto**

  O código está contido em um único arquivo, que configura a conexão com o banco de dados, define o modelo de dados e implementa as funções de manipulação de usuários.

**🛠️ Configuração e Modelo de Dados**

**🔗 Conexão com o Banco de Dados**
  O script configura a conexão com um banco de dados SQLite chamado datadabese.db. Se o arquivo não existir, ele será criado automaticamente.

**👤 Modelo Usuario**

  O modelo Usuario é mapeado para uma tabela chamada usuarios no banco de dados.

**🎯 Funções Principais (CRUD)**

  O script fornece quatro funções para gerenciar os dados dos usuários:
  1. Criar (Create)A função insert_usuario adiciona um novo registro de usuário à tabela.
  2. Ler (Read)A função select_usuarios consulta os usuários no banco de dados.
  3. Atualizar (Update)A função update_nome_usuario altera o nome de um usuário específico, buscando-o pelo seu id.
  4. Excluir (Delete) A função delete_usuario remove um usuário do banco de dados, buscando-o pelo seu id.
     
**🏃 Como Executar**

O bloco if __name__ == '__main__': é o ponto de entrada do script. Ele garante que a tabela usuarios seja criada no banco de dados se ainda não existir (Base.metadata.create_all(engine)).Para testar as funções, descomente as linhas 92 ate 95 para fazer a chamada de função, por exemplo:



92    #insert_usuario('Nome do usuario desejado', 'Função do usuario ex: Gerente,Operario,Convidado...')  ---> Cria um usuario novo

93    #select_usuarios('Nome do Usuario que ta salvo no Banco de Dados') ---> Proucura o usuario no Banco de dados

94   #update_nome_usuario('Informe o ID aqui', 'Informe o novo NOME') ---> Atualiza o nome de um usuario ja incluso no Banco de dados

95   #delete_usuario(coloca o numero do ID aqui)  ---> Deleta um usuario do banco de dados


NÃO ESQUEÇA DE TIRAR O SIMBLO '#' QUE ESTA A FRENTE DA FUNÇÃO, EXECUTE UM POR VEZ PARA ENTENDER O SCRIPT!

