"""Number Guessing Game (CLI).

O computador sorteia um número secreto dentro de um intervalo e o jogador
tenta adivinhá-lo. A cada palpite o jogo informa se o número secreto é maior
ou menor. Cada nível de dificuldade limita o número de tentativas.

Conceitos: módulo random, loops while, operadores de comparação,
validação de input e cores ANSI para feedback visual.
"""

import random

# --- Cores ANSI (reaproveitando o conceito do projeto ansi-color-gen) ---
RESET = "\033[0m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"

# Intervalo padrão do número secreto.
LOW, HIGH = 1, 100

# Dificuldades: nome -> número máximo de tentativas.
DIFFICULTIES = {
    "1": ("Fácil", 10),
    "2": ("Médio", 7),
    "3": ("Difícil", 5),
}


def ask_int(prompt, low, high):
    """Lê um inteiro do usuário garantindo que esteja em [low, high]."""
    while True:
        raw = input(prompt).strip()
        try:
            value = int(raw)
        except ValueError:
            print(f"{RED}Digite um número inteiro válido.{RESET}")
            continue
        if not low <= value <= high:
            print(f"{RED}O número deve estar entre {low} e {high}.{RESET}")
            continue
        return value


def choose_difficulty():
    """Pergunta a dificuldade e retorna (nome, tentativas_maximas)."""
    print(f"\n{BOLD}Escolha a dificuldade:{RESET}")
    for key, (name, attempts) in DIFFICULTIES.items():
        print(f"  {CYAN}{key}{RESET} - {name} ({attempts} tentativas)")

    while True:
        choice = input("Opção: ").strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print(f"{RED}Opção inválida. Escolha 1, 2 ou 3.{RESET}")


def play_round():
    """Executa uma partida completa. Retorna True se o jogador venceu."""
    difficulty_name, max_attempts = choose_difficulty()
    secret = random.randint(LOW, HIGH)

    print(
        f"\nEstou pensando em um número entre {BOLD}{LOW}{RESET} e "
        f"{BOLD}{HIGH}{RESET}. Você tem {BOLD}{max_attempts}{RESET} tentativas "
        f"({difficulty_name})."
    )

    for attempt in range(1, max_attempts + 1):
        remaining = max_attempts - attempt + 1
        guess = ask_int(
            f"\nTentativa {attempt}/{max_attempts} ({remaining} restantes) — seu palpite: ",
            LOW,
            HIGH,
        )

        if guess == secret:
            print(f"\n{GREEN}{BOLD}🎉 Acertou! O número era {secret}.{RESET}")
            print(f"{GREEN}Você venceu em {attempt} tentativa(s).{RESET}")
            return True
        elif guess < secret:
            print(f"{YELLOW}📈 Muito baixo! Tente um número maior.{RESET}")
        else:
            print(f"{YELLOW}📉 Muito alto! Tente um número menor.{RESET}")

    print(f"\n{RED}{BOLD}💥 Fim das tentativas! O número era {secret}.{RESET}")
    return False


def main():
    print(f"{BOLD}{CYAN}=== Jogo de Adivinhação de Números ==={RESET}")

    wins = 0
    losses = 0
    while True:
        if play_round():
            wins += 1
        else:
            losses += 1

        print(f"\nPlacar: {GREEN}{wins} vitória(s){RESET} | {RED}{losses} derrota(s){RESET}")
        again = input("Jogar de novo? (s/n): ").strip().lower()
        if again not in ("s", "sim", "y", "yes"):
            print(f"\n{CYAN}Obrigado por jogar! Até a próxima. 👋{RESET}")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print(f"\n{CYAN}Jogo encerrado. Até mais!{RESET}")
