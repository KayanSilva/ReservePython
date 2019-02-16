import diviner
import gallows

print("*******************************")
print("Games in Python by Kayan Silva.")
print("*******************************")

game = int(input("Choice a game ---> (1) Gallows or (2) Diviner: "))

if(game == 1):
    print("Playing Gallows!")
    gallows.play()
elif(game == 2):
    print("Playing Diviner!")
    diviner.play()