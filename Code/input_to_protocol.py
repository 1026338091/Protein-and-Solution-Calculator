final_vol = float(input("please enter the final volume of the solution(ml):"))
Nacl_stock =  float(input("please enter the Nacl stock(mM):"))
Nacl_final = float(input("please enter the Nacl final(mM):"))
MgCl2_stock = float(input("please enter the MgCl2 stock(mM):"))
MaCl2_final = float(input("please enter the MgCl2 final(mM):"))
Nacl_add = final_vol * Nacl_final / Nacl_stock
MgCl2_add = final_vol * MaCl2_final / MgCl2_stock
print(f'Add {Nacl_add} ml Nacl')
print(f'Add {MgCl2_add} ml MgCl2')
print(f'Add water to a final volume of {final_vol} ml and mix')