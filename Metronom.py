import time
from winsound import Beep

Antwort = False
while not Antwort:
    try:
        Tacktzahl = int(input("Wie viele Tackte hat das Lied?"))
        Schlagzahl = int(input("Wie viele Schläge hat ein Tackt?"))
        Antwort = True
    except ValueError:
        print("Versuch es nochmal")

frequencyhigh = 700
frequency = 500 # Hertz
duration = 50 # ms
Tackt = 1

while Tackt < Tacktzahl + 1:
    Schlag = 1
    print(f"Tackt: {Tackt}")
    while Schlag < Schlagzahl + 1:
        print("\tSchlag: {Schlag}")
        if Schlag == 1:
            Beep(frequencyhigh, duration)
        else:
            Beep(frequency, duration)

        Schlag += 1
        time.sleep(0.25)
    Tackt += 1
