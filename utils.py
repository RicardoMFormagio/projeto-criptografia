import hashlib

def gerar_hash_arquivo(caminho_arquivo):
    """Lê o arquivo em binário e gera o hash SHA-256."""

    sha256_hash = hashlib.sha256()

    # Abre o arquivo como "rb" (read binary)
    with open(caminho_arquivo, "rb") as file:
        # Lê em pedaços de 4KB para não travar a memória
        # Lambda transforma o file.read(4096) em uma função anônima
        # Essa função é executada até que o resultado dela seja b"" (binario vazio)
        for byte_block in iter(lambda: file.read(4096), b""):
            #A cada iteração o hash é atualizado, mas sempre mantendo o tamanho de 256bits
            sha256_hash.update(byte_block)
    # Converte o hash de binário para hexadecimal de 64 caracteres
    return sha256_hash.hexdigest()