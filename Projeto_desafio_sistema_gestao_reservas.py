import os
from datetime import datetime
import json


# ================== ARQUIVOS ==================

def carregar_dados(arquivo="salas.json"):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_dados(salas, arquivo="salas.json"):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(salas, f, ensure_ascii=False, indent=4)
    print("💾 Dados salvos com sucesso!")


# ================== UTILIDADES ==================

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def hora_valida(hora):
    try:
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False


def data_valida(data):
    try:
        return datetime.strptime(data, "%d/%m/%Y").date() >= datetime.now().date()
    except ValueError:
        return False


# ================== SALAS ==================

def cadastrar_sala(salas):
    try:
        id_sala = int(input("ID da sala: "))
    except ValueError:
        return

    for s in salas:
        if s['sala']['id'] == id_sala:
            print("❌ ID já existente.")
            input("ENTER...")
            return

    nome = input("Nome da sala: ").strip()
    capacidade = int(input("Capacidade (1 a 5): "))

    salas.append({
        "sala": {
            "id": id_sala,
            "nome": nome,
            "capacidade": capacidade,
            "reservas": []
        }
    })

    salvar_dados(salas)
    input("ENTER...")


def listar_sala(salas):
    limpar_tela()
    for s in salas:
        sala = s['sala']
        print("=-=-" * 8)
        print(f"ID: {sala['id']}")
        print(f"Nome: {sala['nome']}")
        print(f"Capacidade: {sala['capacidade']}")
    input("\nENTER...")


# ================== RESERVAS ==================

def reserva(salas):
    id_sala = int(input("ID da sala: "))

    sala = next((s['sala'] for s in salas if s['sala']['id'] == id_sala), None)
    if not sala:
        print("❌ Sala não encontrada.")
        input("ENTER...")
        return

    id_reserva = int(input("ID da reserva: "))
    responsavel = input("Responsável: ").strip()

    data = input("Data (DD/MM/AAAA): ")
    if not data_valida(data):
        print("❌ Data inválida ou passada.")
        input("ENTER...")
        return

    hora_inicio = input("Hora início (HH:MM): ")
    hora_fim = input("Hora fim (HH:MM): ")

    inicio = datetime.strptime(hora_inicio, "%H:%M")
    fim = datetime.strptime(hora_fim, "%H:%M")

    if fim <= inicio:
        print("❌ Horário inválido.")
        input("ENTER...")
        return

    # BLOQUEIO DE HORÁRIO
    for r in sala['reservas']:
        if r['data'] == data:
            i = datetime.strptime(r['hora_inicio'], "%H:%M")
            f = datetime.strptime(r['hora_fim'], "%H:%M")
            if inicio < f and fim > i:
                print("❌ Conflito de horário.")
                input("ENTER...")
                return

    sala['reservas'].append({
        "id_reserva": id_reserva,
        "nome_responsavel": responsavel,
        "data": data,
        "hora_inicio": hora_inicio,
        "hora_fim": hora_fim
    })

    salvar_dados(salas)
    input("✅ Reserva realizada! ENTER...")


def listar_reservas(salas):
    id_sala = int(input("ID da sala: "))
    sala = next((s['sala'] for s in salas if s['sala']['id'] == id_sala), None)

    if not sala or not sala['reservas']:
        print("⚠️ Nenhuma reserva.")
        input("ENTER...")
        return

    for r in sala['reservas']:
        print("=-=-" * 8)
        print(r)

    input("ENTER...")


def cancelar_reserva(salas):
    id_sala = int(input("ID da sala: "))
    id_reserva = int(input("ID da reserva: "))

    for s in salas:
        if s['sala']['id'] == id_sala:
            reservas = s['sala']['reservas']
            for r in reservas:
                if r['id_reserva'] == id_reserva:
                    reservas.remove(r)
                    salvar_dados(salas)
                    print("✅ Reserva cancelada.")
                    input("ENTER...")
                    return

    print("❌ Reserva não encontrada.")
    input("ENTER...")


# ================== MENU ==================

salas = carregar_dados()

while True:
    limpar_tela()
    print("[1] Cadastrar sala")
    print("[2] Listar salas")
    print("[3] Reservar")
    print("[4] Listar reservas")
    print("[5] Cancelar reserva")
    print("[9] Sair")

    op = input("Opção: ")

    if op == "1":
        cadastrar_sala(salas)
    elif op == "2":
        listar_sala(salas)
    elif op == "3":
        reserva(salas)
    elif op == "4":
        listar_reservas(salas)
    elif op == "5":
        cancelar_reserva(salas)
    elif op == "9":
        break
