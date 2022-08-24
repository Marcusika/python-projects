print("Welcome to my id maker!")

name = input("Type your first name (8 characters max) ")
while len(name) > 8:
  name = input("Type your first name (8 characters max) ")

name2 = input("Type your second name (8 characters max) ")
while len(name2) > 8:
  name2 = input("Type your second name (8 characters max) ")

day_of_birth = input("Type your day of birth (dd) ")
dat_of_birth = str(day_of_birth)
while not day_of_birth.isnumeric() or len(day_of_birth) > 2 or len(day_of_birth) < 2 or int(day_of_birth) > 31:
    day_of_birth = input("Type your day of birth (dd) ")
    dat_of_birth = str(day_of_birth)

month_of_birth = input("Type your month of birth (mm) ")
month_of_birth = str(month_of_birth)
while not month_of_birth.isnumeric() or len(month_of_birth) > 2 or  len(month_of_birth) < 2 or  int(month_of_birth) > 12:
    month_of_birth = input("Type your month of birth (mm) ")
    month_of_birth = str(month_of_birth)

year_of_birth = input("Type your year of birth (yyyy) ")
year_of_birth = str(year_of_birth)
while not year_of_birth.isnumeric() or len(year_of_birth) > 4 or len(year_of_birth) < 4:
    year_of_birth = input("Type your year of birth (yyyy) ")
    year_of_birth = str(year_of_birth)
#gendr = ["M", "F"]
#while gender not in gendr:
#gender = input("Gender (M/F))")
#gender = gender.upper()
#while not gender.isalpha() or len(gender) > 1 or gender != "F" or "M":
    #gender = input("Gender (M/F)) ")
    #gender = gender.upper()
gendr = ["M", "F"]
gender = input("Gender (M/F)) ")
while gender not in gendr:
    gender = input("Gender (M/F)) ")

#This whole thing is for adding the spaces after the name so that the line is straight
#This is the only way i could think of doing this at the moment
#namelen = len(name) 
#spacenum = 8 - len(name)
#spacelen = ("")
#if spacenum == 0:
#    spacelen == ("")
#elif spacenum == 1:
#    spacelen == (" ")    
#elif spacenum == 2:
#    spacelen == ("  ") 
#elif spacenum == 3:
#    spacelen == ("   ") 
#elif spacenum == 4:
#    spacelen == ("    ") 
#elif spacenum == 5:
#    spacelen = ("     ") 
#elif spacenum == 6:
#    spacelen == ("      ") 
#elif spacenum == 7:
#    spacelen == ("       ") 
#print(spacelen)
#nvm i found something better

spaceamount = 8 - len(name)
spaceamount2 = 8 - len(name2)



print("""__________________________________________""")
print("""|   _____   |                             |""")
print("""|  / 0  0\  |  First Name: """ + name + " "*spaceamount + """       |""")
print("""|  \_____/  |  Second Name: """ + name2 + " "*spaceamount2 + """      |""")
print("""|  |     |  |  Gender: """ + gender + """                  |""")
print("""|___________|  Date of birth: """ + day_of_birth +"." + month_of_birth + "." + year_of_birth +  """  | """)
print("""__________________________________________|""")

