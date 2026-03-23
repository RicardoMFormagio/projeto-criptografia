# ProjetoCripto

O **ProjetoCripto** é uma ferramenta desenvolvida para demonstrar a aplicação prática de protocolos de segurança da informação. O sistema integra criptografia simétrica de alta performance, criptografia assimétrica híbrida e ocultação de dados via esteganografia, garantindo a tríade da segurança: **Confidencialidade, Integridade e Disponibilidade.**

## Funcionalidades

O sistema opera em três frentes principais de proteção de dados:

1.  **Criptografia Simétrica (AES-128):** Utiliza o protocolo *Fernet* para cifras rápidas de grandes volumes de dados (testado com arquivos de até 500MB).
2.  **Criptografia Assimétrica Híbrida (RSA-2048):** Implementa o padrão de mercado onde o RSA protege a chave de sessão, enquanto o AES processa o arquivo, unindo segurança e performance.
3.  **Esteganografia LSB (Least Significant Bit):** Oculta arquivos (textos, chaves ou mensagens cifradas) dentro de imagens PNG sem alteração visual perceptível.
4.  **Auditoria de Integridade (SHA-256):** Gera e valida hashes antes e depois de cada operação para garantir que nenhum bit foi corrompido.
5.  **Logging e Telemetria:** Registro detalhado de operações com medição de latência (tempo de execução) para análise de performance.

## Tecnologias Utilizadas

* **Linguagem:** Python 3.10+
* **Criptografia:** `cryptography.hazmat` (RSA, Padding OAEP, SHA-256) e `cryptography.fernet`.
* **Imagem e Esteganografia:** `Pillow` (PIL) e `stepic`.
* **Logs:** Biblioteca nativa `logging` configurada para monitoramento de latência em milissegundos.

## Como Instalar e Usar

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/seu-usuario/projeto-criptografia.git](https://github.com/seu-usuario/projeto-criptografia.git)
    cd projeto-criptografia
    ```

2.  **Instale as dependências:**
    ```bash
    pip install cryptography stepic Pillow
    ```

3.  **Execute o sistema:**
    ```bash
    python main.py
    ```

## Estrutura do Projeto

* `main.py`: Interface de usuário, menu de opções e centralização de logs/auditoria.
* `crip_simetrica.py`: Lógica de chaves e cifragem AES.
* `crip_assimetrica.py`: Implementação do par de chaves RSA e lógica híbrida.
* `esteganografia.py`: Algoritmos de ocultação e extração de dados em imagens.
* `utils.py`: Funções utilitárias como geração de Hash SHA-256 e cálculos de tempo.
* `operacoes.log`: Histórico completo de trans