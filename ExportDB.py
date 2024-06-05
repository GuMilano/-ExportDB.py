import psycopg2
import json
from datetime import datetime, timedelta
import os
import time
import glob 


# Função personalizada para serializar datas para JSON
def serialize_datetime(obj):
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S.%f')
    raise TypeError("Object of type datetime is not JSON serializable")


def log_error(error_message, error_directory, error_filename):
    with open(os.path.join(error_directory, error_filename), "a") as error_file:
        error_file.write(f"{datetime.now()} - {error_message}\n")


def execute_and_save_query(table_name, json_directory, error_directory, error_filename):
    connection = None
    error_occurred = False

    try:
        # Conectar ao PostgreSQL
        connection = psycopg2.connect(
            host="", # Nome do Host
            database="", # Nome do seu banco de dados
            user="", # Seu usuário de login
            password="" # Sua senha do banco
        )

        cursor = connection.cursor()

        # Executar a consulta SQL com base no nome da tabela
        if table_name in ["table1", "table2", "table3", "table4"]:
            query = f'SELECT * FROM "{table_name}" WHERE "isActive" = True'
        else:
            # Adicionar um JOIN com a tabela1 usando a coluna table2
            # Na linhaem seguida, ela está criando um filtro para a importação,
            # selecionando apenas os dados anteriores a '2024-07-01 09:00:00.000'
            query = f'''
                SELECT t.*, m.name as table2
                FROM "{table_name}" t
                LEFT JOIN "table1" m ON t."table2" = m.id 
                WHERE t."column2" <= '2024-07-01 09:00:00.000'
            '''
        cursor.execute(query)

        # Recuperar os resultados em um formato tabular
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        data = [dict(zip(columns, row)) for row in rows]

        # Exportar os resultados para JSON em formato tabular
        with open(os.path.join(json_directory, f"{table_name}.json"), "w", encoding="utf-8") as f:
            f.write(json.dumps(data, default=serialize_datetime, ensure_ascii=False))

    except (Exception, psycopg2.Error) as error:
        error_message = f"Erro ao conectar ou consultar a tabela {table_name}: {error}"
        print(error_message)
        log_error(error_message, error_directory, error_filename)
        error_occurred = True

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    if not error_occurred:
        success_message = f"A consulta {table_name} foi executada sem erros."
        log_error(success_message, error_directory, error_filename)


def rename_error_file(error_directory, error_filename):
    # Excluir arquivos existentes
    existing_txt_files = glob.glob(os.path.join(error_directory, "*.txt"))
    for existing_txt_file in existing_txt_files:
        os.remove(existing_txt_file)  # Exclua o arquivo existente

    # Criar um novo arquivo de log
    current_time = datetime.now()
    date_part = current_time.strftime('%Y-%m-%d')
    time_part = current_time.strftime('%H-%M-%S')

    new_error_filename = f"atualizacao_data_{date_part}_hora_{time_part}.txt"
    new_error_filepath = os.path.join(error_directory, new_error_filename)
    with open(new_error_filepath, "w") as new_error_file:
        new_error_file.write("")  # Cria um arquivo vazio


def main():
    json_directory = "\\\\servidor\\local1\\local2"
    error_directories = [
        "\\\\servidor\\local1\\local2",
        "\\\\servidor\\local3\\local4"
    ]
    tables_to_query = ["table1", "table2", "table3", "table4"]

    error_filename = "atualizacao_log.txt"  # Nome do arquivo de log de erro

    try:
        while True:
            current_time = datetime.now()
            print(f"Dados de lançamentos Atualizando em: {current_time.strftime('%Y-%m-%d %H:%M:%S')}",
                  end="\r")  # Adiciona \r para sobrescrever a linha

            for error_directory in error_directories:
                for table_name in tables_to_query:
                    execute_and_save_query(table_name, json_directory, error_directory, error_filename)

                # Renomear o arquivo de log de erro no final do loop
                rename_error_file(error_directory, error_filename)

            time.sleep(3600)  # Aguardar 1 minuto antes da próxima atualização
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpar a tela do CMD

    except KeyboardInterrupt:
        print("\nLoop interrompido manualmente.")


if __name__ == "__main__":
    main()
