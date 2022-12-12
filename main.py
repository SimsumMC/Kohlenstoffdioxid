"""
Programm zur Berechnung von der Masse des Kohlenstoffdioxids sowie der vollständigen Reaktionsgleichung anhand der
C-Atome.

von Niklas Möller 10B
"""


def calculate(c_atoms: int):
    even = (c_atoms % 2) == 0
    c_prefix = 2 if even else 1

    h_atoms = 2 * c_atoms + 2
    o_prefix = c_atoms + h_atoms - 1 if even else h_atoms - c_atoms + 2

    carbon_dioxide = c_atoms * 2 if even else c_atoms
    water = h_atoms if even else h_atoms / 2

    carbon_dioxide_value = rem_dec(carbon_dioxide * 44.01)

    output = f"""
    
{rem_dec(c_prefix)}C{index(rem_dec(c_atoms))} + H{index(rem_dec(h_atoms))} + {rem_dec(o_prefix)}O{index(2)} → {rem_dec(carbon_dioxide)}CO{index(2)} + {rem_dec(water)}H{index(2)}O
    
Kohlenstoffdioxid: {carbon_dioxide_value}g ({rem_dec(carbon_dioxide)} x 44,01g/mol)
    
    """

    print(output)


def rem_dec(value: int or float) -> str:
    if isinstance(value, int):
        return str(value)

    if value % 1 == 0:
        return str(int(value))
    else:
        return str(value)


def index(value: int or str) -> str:
    value = str(value)

    indexes = {
        "1": "₁",
        "2": "₂",
        "3": "₃",
        "4": "₄",
        "5": "₅",
        "6": "₆",
        "7": "₇",
        "8": "₈",
        "9": "₉",
        "0": "₀",
    }

    for letter in value:
        if letter not in indexes:
            continue
        value = value.replace(letter, indexes[letter])

    return value


def main():
    while True:
        print("Anzahl der C Atome: ", end="")
        value = input().strip()
        try:
            int(value)
        except ValueError:
            print("Fehler: Gib eine Nummer ein!")
            return
        calculate(int(value))


if __name__ == "__main__":
    main()
