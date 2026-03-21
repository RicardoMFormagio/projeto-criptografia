from PIL import Image
import stepic

def ocultar_arquivo_em_imagem(caminho_imagem, caminho_arquivo_dados):
    # Abre a imagem de suporte
    img = Image.open(caminho_imagem)
    
    # Lê os bytes do arquivo que será escondido
    with open(caminho_arquivo_dados, "rb") as f:
        dados = f.read()
    
    # Codifica os dados na imagem
    img_pixelada = stepic.encode(img, dados)
    
    # Define o nome da imagem de saída
    nome_saida = caminho_imagem.rsplit(".", 1)[0] + "_secreta.png"
    img_pixelada.save(nome_saida, "PNG")
    
    return nome_saida

def revelar_arquivo_de_imagem(caminho_imagem_secreta):
    # Abre a imagem com dados ocultos
    img = Image.open(caminho_imagem_secreta)
    
    # Decodifica os bytes
    dados_extraidos = stepic.decode(img)

    # --- CORREÇÃO DE ACENTUAÇÃO (ENCODING) ---
    # Se o stepic te entregou uma String (que está com acentos vindo errados)
    if isinstance(dados_extraidos, str):
        # Tentamos converter para bytes usando latin-1 (que preserva os bits originais)
        # e depois decodificamos corretamente para utf-8
        try:
            dados_extraidos = dados_extraidos.encode('latin-1')
        except UnicodeEncodeError:
            dados_extraidos = dados_extraidos.encode('utf-8')
    
    # Define um nome padrão para o arquivo extraído
    nome_saida = "extraido_da_imagem.txt" 
    
    with open(nome_saida, "wb") as f:
        f.write(dados_extraidos)
        
    return nome_saida