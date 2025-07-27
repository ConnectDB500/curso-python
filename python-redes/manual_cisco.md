# 📘 Manual de Comandos Cisco (Switch/Roteador)

## 1. Acesso aos modos
enable                  # Acessa o modo privilegiado
configure terminal      # Entra no modo de configuração global
exit                    # Sai do modo atual
end                     # Volta ao modo privilegiado

## 2. Configuração de VLANs (Switch)
vlan <número>           # Cria uma VLAN
name <nome_da_vlan>     # Nomeia a VLAN

## 3. Atribuir VLAN à interface (Switch)
interface <interface_id>
switchport mode access
switchport access vlan <número_da_vlan>

## 4. Configuração de interface com IP (Roteador)
interface <interface_id>
ip address <IP> <máscara>
no shutdown

## 5. Ativar/desativar interface
shutdown            # Desativa a porta/interface
no shutdown         # Ativa a porta/interface

## 6. Nome do dispositivo
hostname <nome>

## 7. Salvar configurações
write memory            # Salva a configuração atual
ou
copy running-config startup-config

## 8. Verificações e diagnósticos
show running-config     # Mostra a config atual
show vlan brief         # Mostra resumo das VLANs
show ip interface brief # Mostra IPs e status das interfaces
show version            # Mostra versão do IOS
ping <ip>               # Testa conectividade


## 9. Acesso remoto via Telnet
line vty 0 4
password <senha>
login

## 10. Acesso remoto via SSH (requer configuração de domínio e usuário)
ip domain-name exemplo.com
crypto key generate rsa
username admin password <senha>
line vty 0 4
transport input ssh
login local