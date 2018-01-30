def Hello4(ArgCount, *VarArgs):
    print("Je gebruikte ", ArgCount, " argumenten.")
    for Arg in VarArgs:
        print(Arg)


Hello4(1, "Een teststring.")
Hello4(3, "Een", "Twee", "Drie")
