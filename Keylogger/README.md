<h1 align="center"> ⌨️ Demonstrador de Captura de Teclado (Keylogger)</h1>

Este diretório contém o `Keylogger.py`, um script Python para demonstrar os conceitos de capturas de teclas diretamente para um arquivo .txt.

> **AVISO IMPORTANTE:** Este script é estritamente para fins educacionais. **Nunca execute este script em computadores alheios ou em um sistema que você não tem autorização.**

## 🎯 Objetivo Educacional

O objetivo deste script é demonstrar de forma prática:
* Como bibliotecas de "hooking" (usando a biblioteca pynpunt) funcionam para interceptar eventos do sistema.
* A captura de eventos de hardware (como pressionar uma tecla) em tempo real.
* O processo de registro de dados (logging) contínuo em um arquivo de texto.
* Métodos de tornar o script mais furtivo.
* Envio automático dos logs por e-mail.

## 🚀 Como Usar

### 1. Pré-requisitos

Certifique-se de ter o Python 3 e a biblioteca `pynput` instalados:
```bash
pip install pynput
```

## 2. Executando o Simulador
No seu terminal, dentro desta pasta (/Keylogger), execute o script:
```bash
python Keylogger.py
```
  - Nota: Em alguns sistemas (Linux/macOS), você pode precisar de permissões de administrador (sudo) para permitir que o Python monitore os dispositivos de entrada. 

Enquanto o script estiver rodando, digite qualquer coisa. Você verá suas teclas sendo impressas no arquivo log.txt.

Para o funcionamento do keylogger é necessário deixar o terminal do python ligado(isso é o que o torna "não-furtivo").

## 3. Furtividade no keylogger
No Windows:
  - Apenas troque a extensão do keylogger de `.py` para `.pyw`, isso faz com que o terminal seja executado em segundo plano.

## 4. Transmissão via E-mail
  - Crie uma conta nova de email para teste (Segurança)
  - Para autorizar o envio automático de email é necessário realizar a verificação de dois fatores da sua conta google.
      ```bash
        Vá em gerenciamento de conta -> Segurança -> Verificação de duas etapas
      ```
  - Configurar as senhas de aplicativos:
    - Acesse: [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
    - Crie uma senha exclusiva para o aplicativo python.
  - Instale as bibliotecas necessário para exportação
    - `pip install secure-smtplib`
  - Execute o Script dentro da pasta (/keylogger)
  ```bash
    python Keylogger_email.py
  ```
  - Digite algumas informações no teclado. Em 1 minuto(Tempo setado no timestamp) o email chegará na sua caixa de entrada.

