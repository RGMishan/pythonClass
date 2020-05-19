magician = True
expert = False

# Checking if the person is magicaian and expert both
if magician and expert:
 print("You are an expert magicain.")

#Check if magician but not an expert
elif magician and not expert:
 print("You are not and expert magician")

#Check if he is magician or expert     (-- above and this is different --)
elif magician or expert:
 print("You are either magician or an expert")

else:
 print("Learn some magic power and come")