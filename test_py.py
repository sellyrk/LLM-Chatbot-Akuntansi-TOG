print("test python! if it printed it means it worked!")
print("bismillah semua akan berlalu")

nama = input("ketik dulu nama luwh di sini, kocak: ")
weight = float(input("luwh ketik berat luwh sekarang di sini (kg): "))
height = float(input("luwh ketik tinggi luwh sekarang di sini (cm): "))

bmi = (weight/((height/100)**2))
#print(f"nih skor bmi luwh njir! : {bmi}.4f")

if bmi < 18.5:
    print("buset kurus banget, makan ngab!")
elif bmi < 24.9:
    print("luwh normal, luwh aman.")
elif bmi < 29.9:
    print("buset obes banget jir, workout woy!")
else:
    print("kalo kata gw mah mending lu tobat sekarang.")

print(f"{nama} nilai bmi luwh segini nih! {bmi}")

