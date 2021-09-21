import time
from winsound import Beep
Tacktzahl = input("Wie viele Tackte hat das Lied?")
Schlagzahl = input("Wie viele Schläge hat ein Tackt?")
frequencyhigh = 700
frequency = 500 # Herz
duration = 50 # ms
Tackt = 1

while Tackt <int(Tacktzahl) +1:
    Schlag = 1
    print("Tackt: " , Tackt)
    while Schlag <int(Schlagzahl) + 1: 
        print("\tSchlag: " , Schlag)
        if Schlag == 1:
            Beep( frequencyhigh, duration )
        else:
            Beep( frequency, duration )
        Schlag = Schlag + 1
        time.sleep(0.25)
    Tackt = Tackt + 1 
input("Enter zum Beenden")