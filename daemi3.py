texti = input("texti: ")
hastafir = 0
lagstafir = 0
lagstafur_eftir_hastaf = 0
sidast_var_hastafur = 0
for x in texti:
    if x.isupper():
        hastafir += 1
        sidast_var_hastafur = 1
    elif x.islower():
        lagstafir += 1
        if sidast_var_hastafur == 1:
            lagstafur_eftir_hastaf += 1
        sidast_var_hastafur = 0
    else:
        sidast_var_hastafur = 0
print("i þessum texta eru %d hástafir, %d lágstafir og %d lágstafir koma strax á eftir hástaf." %(hastafir, lagstafir, lagstafur_eftir_hastaf))