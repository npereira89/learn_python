#! /bin/bash

# --- VARIAVEL DO DISPOSITIVO ---
# Altere 'eth0' para o nome do seu dispositivo (ex: enp2s0, wlp3s0, etc.)
DEVICE="Wi-Fi"

# --- VERIFICAÇÃO DO ESTADO ---
# `ip link show` mostra o estado de todas as interfaces.
# `grep` procura a linha que contém o nome do dispositivo e o estado "UP".
if ip link show $DEVICE | grep -q "state UP"; then
    echo "O dispositivo $DEVICE está ATIVADO."
else
    echo "O dispositivo $DEVICE está DESATIVADO. Vamos ativar..."
    netsh interface set interface "Wi-Fi" admin=enable
    echo "O dispositivo $DEVICE está ATIVADO."
fi
