from crip_simetrica import gerar_e_salvar_chave, criptografar_arquivo, decriptografar_arquivo
from crip_assimetrica import decriptografar_rsa, gerar_chaves_rsa, criptografar_rsa
from utils import gerar_hash_arquivo
import logging
from esteganografia import revelar_arquivo_de_imagem,  ocultar_arquivo_em_imagem

# Configuração do Log
logging.basicConfig(filename='operacoes.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def exibir_menu():
    print("\n-*-*-*-*-*-*-*-* SISTEMA DE SEGURANÇA -*-*-*-*-*-*-*-*")
    print("1. Gerar Nova Chave Simétrica")
    print("2. Criptografar Arquivo (Simétrica)")
    print("3. Decriptografar Arquivo (Simétrica)")
    print("--------------------------------------------------")
    print("4. Gerar Par de Chaves RSA (Pública/Privada)")
    print("5. Criptografar Arquivo (Assimétrica - RSA)")
    print("6. Decriptografar Arquivo (Assimétrica)")
    print("--------------------------------------------------")
    print("7. Ocultar Arquivo em Imagem (Esteganografia)")
    print("8. Revelar Arquivo de Imagem (Esteganografia)")
    print("--------------------------------------------------")
    print("0. Sair")
    print("--------------------------------------------------")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        gerar_e_salvar_chave()
        print("Chave gerada com sucesso e salva em 'chave_simetrica.key'!")
        logging.info("Chave gerada com sucesso e salva em 'chave_simetrica.key'!")
    
    elif opcao == "2":
        arquivo = input("Caminho do arquivo para criptografar: ")

        hash_antes = gerar_hash_arquivo(arquivo)
        print(f"Hash do arquivo original: {hash_antes}")
        logging.info(f"HASH ARQUIVO ORIGINAL: {hash_antes}")

        criptografar_arquivo(arquivo)
        print("Arquivo criptografado com sucesso!")
        logging.info(f"ARQUIVO CRIPTOGRAFADO (SIMETRICA): {arquivo}.enc")

    elif opcao == "3":
        arquivo_encriptado = input("Caminho do arquivo encriptado '.enc': ")
        arquivo_decriptado = decriptografar_arquivo(arquivo_encriptado)
        print("Arquivo decriptado!")
        logging.info(f"ARQUIVO DECRIPTADO (SIMETRICA): {arquivo_decriptado}")

        hash_depois = gerar_hash_arquivo(arquivo_decriptado)
        print(f"Hash do arquivo decriptado: {hash_depois}")
        logging.info(f"HASH ARQUIVO DECRIPTADO (SIMETRICA): {hash_depois}\n\n")

    elif opcao == "4":
        gerar_chaves_rsa()
        print("Par de chaves RSA gerado com sucesso!")
        logging.info("Par de chaves RSA gerado com sucesso!")

    elif opcao == "5": 
        arquivo = input("Arquivo para criptografar com RSA: ")

        hash_antes = gerar_hash_arquivo(arquivo)
        print(f"Hash do arquivo original: {hash_antes}")
        logging.info(f"HASH ARQUIVO ORIGINAL: {hash_antes}")

        criptografar_rsa(arquivo)
        print("Arquivo criptografado com a sua Chave Pública!")
        logging.info(f"ARQUIVO CRIPTOGRAFADO (ASSIMETRICA): {arquivo}.rsa")

    elif opcao == "6": 
        arquivo_rsa = input("Caminho do arquivo '.rsa': ")
        # Captura o nome gerado pela função RSA
        arquivo_decriptado = decriptografar_rsa(arquivo_rsa)
        print("Arquivo decriptado!")
        logging.info(f"ARQUIVO DECRIPTADO (ASSIMETRICA): {arquivo_decriptado}")

        hash_depois = gerar_hash_arquivo(arquivo_decriptado)
        print(f"Hash do arquivo decriptado: {hash_depois}")
        logging.info(f"HASH ARQUIVO DECRIPTADO (ASSIMETRICA): {hash_depois} \n\n")

    elif opcao == "7":
        img_origem = input("Caminho da imagem base (ex: foto.png): ")
        arquivo_esconder = input("Caminho do arquivo para ocultar: ")
        
        hash_interno = gerar_hash_arquivo(arquivo_esconder)
        logging.info(f"INICIANDO ESTEGANOGRAFIA - HASH ARQUIVO ORIGINAL: {hash_interno}")
        
        imagem_final = ocultar_arquivo_em_imagem(img_origem, arquivo_esconder)
        
        print(f"Sucesso! Arquivo ocultado em: {imagem_final}")
        logging.info(f"ESTEGANOGRAFIA CONCLUIDA: {imagem_final}")

    elif opcao == "8":
        img_secreta = input("Caminho da imagem secreta: ")
        
        arquivo_extraido = revelar_arquivo_de_imagem(img_secreta)
        
        print(f"Arquivo extraído com sucesso: {arquivo_extraido}")
        logging.info(f"ARQUIVO EXTRAIDO DA IMAGEM: {arquivo_extraido}")
        
        hash_extraido = gerar_hash_arquivo(arquivo_extraido)
        print(f"Hash do arquivo extraído: {hash_extraido}")
        logging.info(f"HASH ARQUIVO EXTRAIDO (ESTEGANOGRAFIA): {hash_extraido}\n\n")
        
    elif opcao == "0":
        break