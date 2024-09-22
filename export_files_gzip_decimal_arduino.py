import os
import sys
import gzip
import io
import shutil
from datetime import datetime

if __name__ == '__main__':

    caminho_recebido_bootstrap = sys.argv[1]

    path_arduino_include_folder = None

    if not os.path.exists(caminho_recebido_bootstrap + "\\___config_export.txt"):
        with open(caminho_recebido_bootstrap + "\\___config_export.txt", 'w') as configFileCreate:
            configFileCreate.write('PATH_ARDUINO_INCLUDE_FOLDER=\n')

    with open(caminho_recebido_bootstrap + "\\___config_export.txt", 'r') as configFile:
        linhas = configFile.readlines()
        for linha in linhas:
            if 'PATH_ARDUINO_INCLUDE_FOLDER' in linha:
                try:
                    path_arduino_include_folder = linha.split('=')[1].strip() or None
                    if not os.path.exists(path_arduino_include_folder):
                        path_arduino_include_folder = None
                except:
                    path_arduino_include_folder = None

    if path_arduino_include_folder != None:
        path_folder_export_gzip = path_arduino_include_folder

        if os.path.exists(caminho_recebido_bootstrap + "\\data"):
            shutil.rmtree(caminho_recebido_bootstrap + "\\data")

    else:
        path_folder_export_gzip = caminho_recebido_bootstrap + "\\data"

        if os.path.exists(caminho_recebido_bootstrap + "\\data"):
            shutil.rmtree(caminho_recebido_bootstrap + "\\data")

        if not os.path.exists(caminho_recebido_bootstrap + "\\data"):
            os.makedirs(caminho_recebido_bootstrap + "\\data")

    try:
        with open(path_folder_export_gzip + "\\" + "web_gzip.h", 'w') as web_gzip:

            web_gzip.write(f'#ifndef WEB_GZIP_h' + '\n')
            web_gzip.write(f'#define WEB_GZIP_h' + '\n\n')
            web_gzip.write("#include \"Arduino.h\"\n\n")
            web_gzip.write("namespace web_gzip\n{")

            for diretorio, subpastas, arquivos in os.walk(caminho_recebido_bootstrap):
                for arquivo in arquivos:
                    if arquivo != 'script.bat' and arquivo != 'export_files_gzip_decimal_arduino.py' and arquivo != 'export_files_gzip_decimal_arduino.exe' and arquivo != '___config_export.txt' and arquivo != 'web_gzip.h':
                        path_relative_file = diretorio.replace(caminho_recebido_bootstrap, '') + '\\' + arquivo
                        caminho_completo = caminho_recebido_bootstrap + path_relative_file
                        nome_arquivo = arquivo.split(".")[0]
                        extensao_arquivo = arquivo.replace(nome_arquivo, "")
                        caminho_header_file = path_folder_export_gzip + path_relative_file.replace(extensao_arquivo,
                                                                                                   ".h")

                        with open(caminho_completo, 'rb') as fileData:
                            data = fileData.read()

                            # Criar um buffer para armazenar os dados gzip compactados
                            buffer = io.BytesIO()

                            # Compactar os bytes da string HTML usando gzip
                            with gzip.GzipFile(fileobj=buffer, mode='wb') as f:
                                f.write(data)

                            # Obter os bytes compactados
                            gzip_bytes = buffer.getvalue()

                            # Converter os bytes compactados para uma lista de decimais
                            decimal_array = list(gzip_bytes)

                            nome_namespace_formatado = path_relative_file.replace('\\', '_').replace('-', '_').replace(
                                '.', '_').replace(' ', '_').upper()

                            file_comprimido = f"\n\tnamespace {nome_namespace_formatado}\n\t" + "{\n"

                            file_comprimido += f'\t\tconst uint32_t size = {len(decimal_array)};' + '\n'

                            file_comprimido += f'\t\tconst uint8_t content[] PROGMEM = ' + '{\n\t\t\t'
                            for i, byte in enumerate(decimal_array):
                                file_comprimido += f'{byte},' + ' '

                            file_comprimido += '\n\t\t};\n'
                            file_comprimido += "\t}\n"

                            web_gzip.write(file_comprimido)

            web_gzip.write('}\n\n#endif')
            print(
                "Export completed successfully. Generated file path: " + path_folder_export_gzip + "\\" + "web_gzip.h")
    except PermissionError:
        date_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with open(caminho_recebido_bootstrap + "\\error.log", 'a') as file_error_log:
            file_error_log.write(f"[{date_time}] Unable to export files in folder '{path_folder_export_gzip}'\n")

        print(f"[{date_time}] Unable to export files in folder '{path_folder_export_gzip}'\n")