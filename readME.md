# 📊 ExportDB.py

# Descrição

ExportDB.py é um programa de automação (RPA) que acessa um banco de dados, seleciona e filtra tabelas com consultas SQL baseadas em datas especificadas no código, relaciona tabelas com JOIN e exporta os resultados como arquivos JSON. Além disso, ele cria um arquivo de log em formato TXT em cada pasta especificada no código, registrando a última atualização dos dados com um nome de arquivo baseado na data e hora da atualização.

## Funcionalidades
- 🔗 **Acesso ao Banco de Dados:** Conecta-se ao banco de dados e executa consultas SQL para selecionar e filtrar tabelas.

- 🔍 **Relacionamento de Tabelas:** Utiliza JOIN para relacionar tabelas conforme necessário.

- 💾** Exportação de Dados:** Exporta os dados das tabelas como arquivos JSON, nomeando-os com base no nome das tabelas do banco de dados.

- 📝 **Geração de Logs:** Cria arquivos de log TXT em pastas especificadas, com nomes baseados na data e hora da última atualização, para facilitar a visualização rápida.

- 🔄 **Execução Contínua:** O código é executado em loop contínuo, mantendo os dados sempre atualizados e informando a última atualização no console.

- 📊 **Integração com Power Query e Power BI:** Facilita a integração com Power Query, Excel, Power BI e outras ferramentas de análise de dados, mantendo os dados sempre atualizados.

- ⚡ **Resiliência a Reinicializações:** Pode ser configurado como um executável e adicionado a uma tarefa do Windows para garantir que seja reiniciado automaticamente após uma queda de energia ou reinicialização do servidor.

## Requisitos
- Python 3.x
- Bibliotecas Python:
    - pandas
    - sqlalchemy
    - json
    - datetime

## Como Usar
🛠️ **Configuração do Banco de Dados:**
- Configure os detalhes de conexão do banco de dados no código.

🔧 **Configuração das Consultas SQL:**
- Especifique as consultas SQL para filtrar e relacionar tabelas com base em datas no código.

🚀 **Execução do Código:**

- Execute o código no CMD:
 
 ```
 python ExportDB.py
 ```
-  programa informará a última atualização no console e manterá a execução contínua.

📂 **Logs e Arquivos JSON:**

- Os arquivos JSON exportados e os logs TXT serão salvos nas pastas especificadas no código.

- Os arquivos de log terão nomes no formato atualizacao_data_YYYY-MM-DD_hora_HH-MM-SS.txt.

## 🖥️ Exemplo de Configuração de Tarefa do Windows
Para garantir que o programa seja reiniciado automaticamente após uma queda de energia ou reinicialização do servidor:

⚙️ **Crie um Executável:**

Use pyinstaller para criar um executável:

```
pyinstaller --onefile ExportDB.py
```

📅 **Configuração da Tarefa do Windows:**

- Abra o Agendador de Tarefas do Windows.

- Crie uma nova tarefa básica.

- Configure a tarefa para iniciar o executável criado na inicialização do sistema.

## Considerações Finais
ExportDB.py é uma solução robusta para manter os dados do banco de dados sempre atualizados e prontos para análise em ferramentas como Power Query, Excel e Power BI. A configuração de logs detalhados e a capacidade de reinicialização automática garantem que você nunca perca uma atualização, mesmo em caso de falhas de energia ou reinicializações do sistema.
#

**Autor**

Gustavo Milano Silva