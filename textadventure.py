from random import randint
stone = 0
stick = 0
rose = 0
tulip = 0

print("(you wake up to the sound of humming)")
print("(you are laying on a path leading into a forest)")
print("(behind u is a wall, there is nowhere else to go)")
print("(you realise the humming sound is coming from a cat, it's standing on top of you)")
print("Unknown: Hello there")
print("(it can talk??")
name = input("Unknown: What's your name? ")
print(name + "?")
print("Cat: cool, my name is Cat")
print("Cat: umm.. so.. i need help with something..")
answer1 = input("can you help me? ")
if answer1 == "no":
  print("Cat: oh...")
  print("Cat: that's okay..")
  print("(Cat stabs you and you die)")
  exit()
if answer1 == "yes":
  print("Cat: oh thank you, thank you!")


answer2 = input("Cat: just follow me okay? (you can answer either no or ok) ")
if answer2 == "no":
    print("Cat: but..")
    print("Cat: how are you gonna help me then?")
    print("(you say nothing so Cat stabs you and you die)")
    print("(you should of seen that coming..)")
    exit()
if answer2 == "ok":
    print("Cat: good good")
    print("Cat: let's go :D")


print("(you and Cat wander into the forest)")
answer3 = input("(ask what Cat needs help with?)" )
if answer3 == "yes":
  print("umm so.. what do you need help with?")
  print("(Cat says nothing)")
  answer3a = input("ask again? ")
  if answer3a == "no":
    print("you keep walking in silence")
  if answer3a == "yes":
    print("wh-what do you need help with?")
    print("(Cat stops)")
    print("(she turns to you, she looks angry)")
    print("Cat: just follow me.")
    print("(you start to suspect her)")
    print("(you see a stick and a stone on the path)")
    answer3b = input("(what do you want to pick up?) (stick, stone, nothing? ")
    if answer3b == "stick":
      stick += 1
      print("(you picked up the stick)")
    if answer3b == "stone":
      stone += 1
      print("(you picked up the stone)")
    if answer3b == "nothing":
      print("(you picked up nothing)")
if answer3 == "no":
  print("(you don't ask and keep walking in silence)")

print("(you walk for a few minutes and the path ends up splitting)")
print("Cat: you have to pick what path we're gonna walk")
print("don't you know the right one?")
print("Cat: I forgot")
print("ok..")
answer4 = input("walk the right or left path?")
if answer4 == "right":
  print("we can try the right path i guess")
  print("Cat: right is always right!")
  print("(you walk down the right path)")
  print("(the path leads into a flower meadow")
  print("(on the other side of the meadow is a small castle, there's a young girl atanding in front of the doors)")
  print("Cat: that is princess Rose")
  print("Cat: let's go talk to her, maybe she can help us!")
  print("(help us with what?..)")
  print("as you walk through you're thinking of picking a flower")
  answer4a = input("(pick a rose, a tulip or nothing?)")
  if answer4a == "rose":
    rose += 1
    print("(you pick a rose)")
  if answer4a == "tulip":
    tulip += 1
    print("(you pick a tulip)")
  if answer4a == "nothing":
    print("(you pick nothing)")
  print("(you get to the castle doors")
  print("Rose: hello there")
  print("Rose: what brings you to my castle?")
  print("Cat: we were wondering if you could help us")
  print("Rose: oh? what do you need help with?")
  print("Cat: there are dogs invading my homeland")
  print("Rose: I could help, but only if you have a gift for me")
  print("(Cat looks at you, you have to give the princess something)")
  print("what do you give the princess?", stone,"stone", stick,"stick", rose,"rose", tulip,"tulip?")
  answer4b = input()
  if answer4b == "stone":
    stone -= 1
    print("(you give Rose a stone)")
    print("Rose: A STONE?!?")
  if answer4b == "stick":
    stick -= 1
    print("(you give Rose a stick)")
    print("Rose: A STICK?!?")
  if answer4b == "rose":
    rose -= 1
    print("(you give Rose a rose)")
    print("Rose: is that.. FROM MY GRADEN?!?")
  if answer4b == "tulip":
    tulip -= 1
    print("(you give Rose a tulip)")
    print("is that.. FROM MY GARDEN?!?")
  print("Rose: HOW DARE YOU?!?")
  print("Rose: GUARDS! BEHEAD THEM RIGHT NOW!!!")
  answer4c = input("(run or try to talk to Rose?) (Answer 'run' or 'talk') ")
  if answer4c == "talk":
    print("princess, i didn't mean to offend you, i'm sorry")
    print("(you and Cat were killed by the guards)")
    print("(you fucked up lol)")
    exit()
  if answer4c == "run":
    print("RUN!")
    print("Rose: NO! WAIT!!!")
    print("(you and Cat get away from the guards)")
    print("Cat: YOU ALMOST GOT US KILLED!!")
    print("Cat: ARE YOU STUPID??")
    print("I didn't have anything else..")
    print("Cat: whatever, we have to keep going")
    print("(you keep walking for another 10 minutes without saying anything)")
    print("sooo.. dogs are invading your homeland?")
    print("(Cat doesn't answer)")
    print("is that what you need help with?")
    print("Cat: yea sure")
    print("(somehow i don't believe her)")
    print("(you keep walking, you have to walk over a river)")
    print("Cat: i wanna drink a little bit")
    answer4d = input("drown her?")
    if answer4d == "yes":
      print("(you get behind her and push her face down in the river)")
      print("she's strong and may manage to get up")
      answer4e = input("(knock her out with a stone?)")
      if answer4e == "no":
        print("(Cat gets up and push you off)")
        print("(Cat stabs you and you die)")
        print("(not the smartest move)")
        exit()
      if answer4e == "yes":
        print("(you hit her on the head with a stone and she falls uncontious)")
        print("(you sucsessfully drown her)")

if answer4 == "left":
  print("we can try the left path i guess")
  print("left is best!")
  print("(you walk down the left path)")
  print("(the path leads into a cave)")