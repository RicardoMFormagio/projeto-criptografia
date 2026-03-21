from cryptography.fernet import Fernet

def gerar_e_salvar_chave():

    # Gera a chave secreta
    chave = Fernet.generate_key() 
    # Cria um arquivo para salvar a chave secreta usando "wr" (write binary)
    with open("chave_simetrica.key", "wb") as f:
        f.write(chave)
    return chave

def carregar_chave():
    return open("chave_simetrica.key", "rb").read()

def criptografar_arquivo(caminho_origem):
    chave = carregar_chave()
    f = Fernet(chave)
    
    with open(caminho_origem, "rb") as file:
        dados = file.read()
    
    dados_cifrados = f.encrypt(dados)
    
    with open(caminho_origem + ".enc", "wb") as file:
        file.write(dados_cifrados)

def decriptografar_arquivo(caminho_cifrado):
    chave = carregar_chave()
    f = Fernet(chave)
    
    with open(caminho_cifrado, "rb") as file:
        dados_cifrados = file.read()
    
    dados_decifrados = f.decrypt(dados_cifrados)
    
    # Define o novo nome com o sufixo
    nome_base = caminho_cifrado.replace(".enc", "")
    nome_final = nome_base.replace(".", "_decriptado_simetrica.")
    
    with open(nome_final, "wb") as file:
        file.write(dados_decifrados)
    
    return nome_final
        