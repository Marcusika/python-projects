#i made this myself
import random
value = 0
while value < 1: #input how many usernames you want to generate
    name_1 = ['Smooth', 'Fluffy', 'Slimy', 'Greasy', 'Sharp', 'Soft', 'Rough', 'Shiny', 'Fast', 'Lazy', 'Blue', 'Red', 'Yellow', 'Green', 'Purple', 'Orange']
    name_2 = ['Snail', 'Fox', 'Potato', 'Lettuce', 'Turtle', 'Mouse', 'Bacteria', 'Feline', 'Canine', 'Mosquito','Pebble','Melon' ,'Fish' ,'Snake' ,'Hedgehog' ,'Cloud']
    number = random.randint(0, 999)
    number = str(number)
    rname_1 = random.choice(name_1)
    rname_2 = random.choice(name_2)
    print(rname_1 + rname_2 + number)
    value += 1
