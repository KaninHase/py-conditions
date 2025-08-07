# Conditionals

a = 600
b = 700

if a > b:
    print("a ist größer als b")
    
elif a == b:
    print("a ist b gleich")

elif a != b:
    print("a ist nicht b gleich")
    
elif a >= b:
    print("a ist größer als oder b gleich")
    
elif a <= b:
    print("a ist kleiner als oder b gleich")

else:
    print("b ist größer als a")


a = 20
b = 10

print("a") if a > b else print("b")

# and conditional

a = 150
b = 140
c = 160

if a > b and c > a:
    print("Both conditions are true")

else:
    print("Both conditions are false")
# Hier wird nix angezeigt ,da nur einer der Sätze wahr ist (der erste)   

a = 150
b = 140
c = 160
# weswegen wird diesmal nicht funktionieren ? Denn weder b ist nicht größer als a und noch a größer als c
if b < a and a > c:
    print("Both conditions are true")
else:
    print("Both conditions are false")
    
# was ,wenn einer der Sätze wahr ist? ( mit or)
if a > b or a > c:
  print("At least one of the conditions is True")
#a ist größer als b