
<h1 align="center"> ☣️ Simulador Educacional de Malware (Ransomware) </h1>

Este diretório contém o `Ransomware.py`, um script Python para demonstrar os conceitos de criptografia e sequestro de arquivos.

> **AVISO IMPORTANTE:** Este script é estritamente para fins educacionais. Ele foi projetado para criptografar **apenas** os arquivos de teste que eu mesmo criei (`Test_Files.txt`). **Nunca execute este script em arquivos pessoais ou em um sistema que você não possa formatar.**

## 🎯 Objetivo Educacional

O objetivo deste script é demonstrar de forma prática:
* Como a **criptografia simétrica** (usando a função `fernet` da biblioteca `cryptography`) funciona.
* A importância crítica da **gestão de chaves** (o arquivo key.key`).
* O processo de leitura e escrita de dados binários em arquivos.
* O impacto imediato que a criptografia tem sobre um arquivo, tornando-o ilegível.

## 🚀 Como Usar

### 1. Pré-requisitos

Certifique-se de ter o Python 3 e a biblioteca `cryptography` instalados:
`pip install cryptography`

### 2. Executando o Simulador
No seu terminal, dentro desta pasta (/Ransomware), execute o script:
```Bash
python Ransomware.py
```
  - O script criará um arquivo chamado key.key. Esta é a "chave-mestra" da criptografia.
    - Ponto de aprendizado: Em um ataque real, o atacante geraria esta chave e a manteria em seu servidor, tornando impossível a descriptografia sem o pagamento.
  - O script usará a key.key para criptografar o Test_Files.txt.
  - Ele também criará a nota de resgate LEIA ISSO.txt
    
    - Ponto de aprendizado: Tente abrir o Test_Files.txt agora. Você verá dados binários ilegíveis. Os arquivos originais foram "sequestrados".
    - Obs: Lembre-se de retirar os arquivos key.key e os scripts do alvo de criptografia (Função já embutida)

### 4. Executando o simulador(Descriptografia)
  No seu terminal, dentro desta pasta (/Ransomware), execute o script:
```Bash
python Descriptografia.py
```
  - O script usará a key.key para reverter o processo e descriptografar o Test_Files.txt.
    - Ponto de aprendizado: Abra o arquivo novamente. O conteúdo original foi restaurado. Isso demonstra que, com a chave, o processo é totalmente reversível.
