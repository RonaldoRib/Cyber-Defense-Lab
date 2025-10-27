# 🛡️ Guia de Prevenção e Defesa

Este documento detalha as medidas defensivas (Blue Team) contra as ameaças simuladas neste laboratório (e ameaças reais).

## 1. Defesa contra Ransomware

A defesa contra ransomware é feita em camadas (Defense in Depth).

### Prevenção (Antes do Ataque)

* **Backups (A Regra 3-2-1):** A defesa mais importante.
    * **3** cópias dos seus dados.
    * **2** tipos de mídia diferentes (ex: HD interno + nuvem).
    * **1** cópia "offline" ou "imutável" (desconectada da rede, para que o ransomware não possa alcançá-la).
* **Conscientização do Usuário:** Treinar usuários para não abrir anexos suspeitos (Phishing) ou clicar em links maliciosos, que são os vetores de entrada mais comuns.
* **Patch Management:** Manter sistemas operacionais e softwares (especialmente navegadores e clientes de e-mail) atualizados para corrigir vulnerabilidades.
* **Princípio do Menor Privilégio:** Usuários não devem ter permissões de administrador no dia-a-dia. Isso limita a capacidade do ransomware de se espalhar e criptografar arquivos de sistema.

### Detecção (Durante o Ataque)

* **Antivírus (AV) e EDR (Endpoint Detection & Response):**
    * **Detecção por Assinatura:** O AV reconhece o "hash" (impressão digital) de malwares conhecidos.
    * **Detecção Heurística/Comportamental:** O EDR monitora *comportamentos* suspeitos. Por exemplo: "Por que o 'Word.exe' está tentando criptografar centenas de arquivos .doc em segundos?". Ele bloqueia a ação com base nesse comportamento anômalo.
* **Canary Files (Arquivos "Canário"):** Ferramentas de EDR espalham arquivos "isca" (ex: `C:\Users\Admin\documento_secreto.docx.canary`) em locais comuns. Se algum processo modificar esse arquivo, o EDR sabe que é um ransomware e bloqueia o processo imediatamente.

## 2. Defesa contra Keyloggers

### Prevenção e Detecção

* **Antivírus (AV/EDR):** Assim como no ransomware, o AV/EDR é a principal defesa.
    * Eles detectam keyloggers conhecidos (assinaturas).
    * Eles monitoram APIs suspeitas. Um EDR pode se perguntar: "Por que este programa desconhecido está usando a API `SetWindowsHookEx` (uma API comum para keyloggers no Windows)?".
* **Firewall (Detecção de Exfiltração):**
    * É aqui que as funcionalidades como ("envio por e-mail") são pegas.
    * Um firewall de saída (Egress Firewall) monitora o tráfego que *sai* da sua rede.
    * Regras de firewall podem bloquear conexões SMTP (porta 25, 465, 587) para qualquer servidor, exceto o servidor de e-mail oficial da empresa. O keylogger tentando enviar dados seria bloqueado.
    * EDRs modernos também monitoram conexões de rede por processo, bloqueando tráfego suspeito.
* **Sandboxing:**
    * Navegadores modernos e leitores de PDF rodam em um "sandbox" (caixa de areia).
    * Isso significa que, mesmo que um site malicioso tente rodar um script, esse script fica "preso" dentro da caixa de areia do navegador e não pode acessar suas teclas, seus arquivos ou sua rede.
* **Teclados Virtuais:** Usados em sites de bancos. Como você clica com o mouse em vez de digitar, o keylogger não registra a senha.
* **Autenticação de Múltiplos Fatores (MFA):** A defesa final. Mesmo que um atacante roube sua senha, ele não pode logar sem o segundo fator (ex: o código do seu celular).
