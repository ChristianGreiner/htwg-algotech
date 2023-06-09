def wechselgeld(betrag: float):
    herausgegeben = 0
    geld = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

    while herausgegeben < betrag:
        for i in range(len(geld)):
            if herausgegeben + geld[i] <= betrag:
                herausgegeben += geld[i]
                print(geld[i])
                break

wechselgeld(17.69)