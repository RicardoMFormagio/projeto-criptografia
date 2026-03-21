from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.fernet import Fernet

def gerar_chaves_rsa():
    # 1. Gera o par de chaves (2048 bits é o padrão seguro atual)
    privada = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    # A chave pública é extraída a partir da chave privada
    publica = privada.public_key()

    # 2. Salva a Chave Privada
    with open("chave_privada.pem", "wb") as f:
        f.write(privada.private_bytes(
            encoding=serialization.Encoding.PEM, #Converte os dados binários em Base64
            format=serialization.PrivateFormat.PKCS8, #PKCS#8 é o padrão moderno e universal para armazenar chaves privadas. Pense nisso como o "formato do arquivo" (como .docx vs .pdf). Ele organiza os números da chave em uma ordem específica que outros programas (como OpenSSL ou Java) conseguem entender.
            encryption_algorithm=serialization.NoEncryption() # Isso define a segurança do arquivo no disco. Neste caso, salvar o arquivo sem uma senha (que caso tivesse, seria necessária para abrir o arquivo)
        ))

    # 3. Salva a Chave Pública (Pode ser distribuída)
    with open("chave_publica.pem", "wb") as f:
        f.write(publica.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo #Organiza os dados sob a norma SubjectPublicKeyInfo. Isso garante que qualquer sistema de segurança no mundo reconheça que o arquivo contém uma chave do tipo RSA.
        ))

def criptografar_rsa(caminho_arquivo):
    # Carrega a chave pública do arquivo
    with open("chave_publica.pem", "rb") as f:
        chave_publica = serialization.load_pem_public_key(f.read())

    # Gera uma chave simétrica (Fernet) temporária
    chave_simetrica = Fernet.generate_key()
    fernet = Fernet(chave_simetrica)

    with open(caminho_arquivo, "rb") as f:
        dados = f.read()

    # Criptografa os DADOS com a chave simétrica
    dados_cifrados = fernet.encrypt(dados)

    # Criptografa a CHAVE SIMÉTRICA usando a chave pública RSA
    # A chave simétrica é pequena, então cabe no RSA, que suporta somente 190bytes!
    # Criptografa usando Padding OAEP
    # O RSA puro é fraco contra ataques matemáticos; o OAEP adiciona dados aleatórios antes de criptografar para garantir que a mesma mensagem gere resultados diferentes toda vez.
    chave_simetrica_cifrada = chave_publica.encrypt(
        chave_simetrica,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Salva os dois no arquivo (Chave Cifrada + Dados Cifrados)
    with open(caminho_arquivo + ".rsa", "wb") as f:
        f.write(chave_simetrica_cifrada) 
        f.write(dados_cifrados)

def decriptografar_rsa(caminho_arquivo_rsa):
    # Carrega a Chave Privada
    with open("chave_privada.pem", "rb") as f:
        chave_privada = serialization.load_pem_private_key(
            f.read(),
            password=None # Se você tivesse colocado senha na chave, usaria aqui
        )

    with open(caminho_arquivo_rsa, "rb") as f:
        conteudo_total_arquivo_rsa = f.read()

    # Primeiros 256 bytes = Chave Simétrica trancada pelo RSA
    # O que sobrar = Dados do arquivo trancados pelo AES (Fernet)
    chave_simetrica_cifrada = conteudo_total_arquivo_rsa[:256]
    dados_cifrados_aes = conteudo_total_arquivo_rsa[256:]

    # Usa o RSA para "destrancar" a Chave Simétrica (Fernet)
    chave_simetrica = chave_privada.decrypt(
        chave_simetrica_cifrada,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Agora que temos a chave simétrica "pura", abrimos o arquivo grande
    fernet = Fernet(chave_simetrica)
    dados_decifrados = fernet.decrypt(dados_cifrados_aes)
    
    # Salva o arquivo original (removendo o .rsa)
    nome_arquivo_original = caminho_arquivo_rsa.replace(".rsa", "")
    nome_arquivo_decriptado = nome_arquivo_original.replace(".", "_decriptado_assimetrica.")
    
    with open(nome_arquivo_decriptado, "wb") as f:
        f.write(dados_decifrados)
    
    return nome_arquivo_decriptado