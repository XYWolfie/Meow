from random import randint
stone = 0
stick = 0
rose = 0
tulip = 0
files_documents = 0
gun = 0
hallway_lights = 0
camera = 0
dead_bodies_pic = 0
enter_security_room = 0
cat_live = 1


print("//")
print("INSTRUCTIONS:")
print("Whenever you are asked a questin you can answer between the words inside '', exs: do you want 'ice cream' or brownies'. If no words are inside '' it's a yes or no question and can onlt be written as such.")
print("be careful not to use any capitals unless it is written so")
print("//")
print(" ")
def start_point():
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
   death_message()
  if answer1 == "yes":
   print("Cat: oh thank you, thank you!")

   answer2 = input("Cat: just follow me okay? ('no' 'ok') ")
  if answer2 == "no":
      print("Cat: but..")
      print("Cat: how are you gonna help me then?")
      print("(you say nothing so Cat stabs you and you die)")
      death_message()
  if answer2 == "ok":
    print("Cat: good good")
    print("Cat: let's go :D")
    forest1()

def forest1():
    global stick
    global stone
    print("(you and Cat wander into the forest)")
    answer3 = input("(ask what Cat needs help with?)" )
    if answer3 == "yes":
        print("umm so.. what do you need help with?")
        print("(Cat says nothing)")
        answer3a = input("(ask again?) ")
    if answer3a == "no":
        print("(you keep walking in silence)")
    if answer3a == "yes":
        print("wh-what do you need help with?")
        print("(Cat stops)")
        print("(she turns to you, she looks angry)")
        print("Cat: just follow me.")
        print("(you start to suspect her)")
        print("(you see a stick and a stone on the path)")
        answer3b = input("(what do you want to pick up?) ('stick', 'stone', 'nothing'?) ")
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
    path()

def path():
  global rose, stick, tulip, stone
  print("(the path leads into a flower meadow")
  print("(on the other side of the meadow is a small castle, there's a young girl standing in front of the doors)")
  print("Cat: that is princess Rose")
  print("Cat: let's go talk to her, maybe she can help us!")
  print("(help us with what?..)")
  print("as you walk through you're thinking of picking a flower")
  answer4a = input("(pick a 'rose', a 'tulip' or 'nothing'?)")
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
  print("what do you give the princess?", stone,"'stone'", stick,"'stick'", rose,"'rose'", tulip,"'tulip'?")
  answer4b = input()
  if answer4b == "stone" and stone > 0:
    stone -= 1
    print("(you give Rose a stone)")
    print("Rose: A STONE?!?")
  elif answer4b == "stick" and stick > 0:
     stick -= 1
     print("(you give Rose a stick)")
     print("Rose: A STICK?!?")
  elif answer4b == "rose" and rose > 0:
    rose -= 1
    print("(you give Rose a rose)")
    print("Rose: is that.. FROM MY GRADEN?!?")
  elif answer4b == "tulip" and tulip > 0:
    tulip -= 1
    print("(you give Rose a tulip)")
    print("is that.. FROM MY GARDEN?!?")
  else:
    print("(you have nothing to give her)")
    print("Rose:YOU CAME HERE WITHOUT A GIFT?!?")

  print("Rose: HOW DARE YOU?!?")
  print("Rose: GUARDS! BEHEAD THEM RIGHT NOW!!!")
  answer4c = input("(run or try to talk to Rose?) (Answer 'run' or 'talk') ")
  if answer4c == "talk":
     print("princess, i didn't mean to offend you, i'm sorry")
     print("(you and Cat were killed by the guards)")
     print("(you fucked up lol)")
     death_message()
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
        answer4d = input("(drown her?)")
        if answer4d == "yes":
          kill_ending()
        if answer4d == "no":
          kill_ending2()

def kill_ending():
  print("(you get behind her and push her face down in the river)")
  print("she's strong and may manage to get up")
  print("you have",stone, "stones" )
  answer4e = input("(knock her out with a stone?)")
  if answer4e == "no":
        print("(Cat gets up and push you off)")
        print("(Cat stabs you and you die)")
        print("(not the smartest move)")
        death_message()
  if answer4e == "yes":
        print("(you hit her on the head with a stone and she falls unconcious)")
        print("(you successfully drown her)")
        print("(you keep walking alone down the path)")
        print("(you end up by a huge cliff and you don't know where to go)")
        print("(the guards catch up to you and kill you)")
        death_message()

def kill_ending2():
  global cat_live
  print("(you decide not to drown her)")
  print("(She drinks some water and you continue walking)")
  print("(you get to a huge cliff)")
  print("(Cat shows you a secret path to get down)")
  print("You can hear the guards over you, but they don't know where to go and give up)")
  print("(you get safely to the other side")
  print("Cat: phew, we got lucky with that one")
  print("yeah.. thanks to you")
  print("Cat: of course")
  print("(I don't know what that's supposed to mean..)")
  print("(Cat looks down the cliff)")
  answer4f = input("(push her?)")
  if answer4f == "yes":
    cat_live -= 1
    print("(you push her off the cliff)")
    print("(you look over to see her dead body, you don't know how to feel about yourself)")
    print("(you breathe in, you have to keep moving)")
    print("(but where do you go? You were only following Cat, you don't know where you are.")
    print("(you hear cars..")
    print("(the sound isn't following the path)")
    answer4g = input("(Follow the sound of cars?)")
    if answer4g == "yes": 
      print("(you follow the sound and see a road)")
      answer4h = input("(hitchhike?)")
      if answer4h == "yes":
        print("(you stand by the road and a car stops for you)")
        print("(a dog is driving, he's wearing a weird coat)")
      if answer4h == "no":
        answer4n = input("(go back to the path?)")
        if answer4n == "no":
          print("(you stand by the road)")
          print("(you see a car coming, the driver is rolling down the window)")
          print("(he shoots you while still driving)")
          print("(you died)")
          exit()
      answer4i = input("(get in?)")
      if answer4i == "yes":
        print("(you get in the car with the dog)")
        print("(you ask him where you are, but he doesn't answer)")
        print("(You get a weird feeling about this)")
      if answer4i == "no":
          print("sorry, i don't need a hike")
          print("(the driver shoots you and you die)")
          death_message()
      answer4j = input("(ask him to stop the car?)")
      if answer4j == "yes":
            print("please stop the car here")
            print("(he looks at you grimly)")
            print("(he pulls out a gun and shoots you)")
            print("(you died)")
            death_message()
      if answer4j == "no":
            print("(he drives you to a big factory")
            print("(he pulls out a gun and tells you to go in the backdoors)")
            answer4k = input("(comply?)")
            if answer4k == "no":
              print("(He shoots you)")
              print("(you died)")
              death_message()
            if answer4k == "yes":
              print("(you carefully walk in the backdoors, he has his gun pointed at you the entire time)")
              print("(inside you are met by two dogs, both wearing the same coat the driver was wearing)")
              print("(they both raise their guns and point them at you)")
              print("Dog1: Do as we say or you will be killed")
              print("(you nod)")
              print("dog2: good, now follow us")
              answer4l = input("(comply again?)")
              if answer4l == "no":
                print("(the dogs shoots you and you die)")
                print("(you really don't understand this huh?)")
                death_message()
              if answer4l == "yes":
                print("(they start walking down the hallway and you follow)")
                print("(there is a room on both sides of the hallway, the dogs walk past them)")
                answer4m = input("(Sneak into the 'right' room, the 'left' room or keep 'follow'ing them? )")
                if answer4m == "follow":
                  print("(you keep following them into a dark room)")
                  print("dog1: go in")
                  print("(you have no choice but to follow their orders)")
                  print("(you walk in to the room)")
                  print("(just as you notice hundreds of bodies laying there you get shot by one of the dogs)")
                  print("you died")
                  death_message()
                if answer4m == "right":
                  print("(you sneak into the room to your right)")
                  print("(you lock the door just in time before they notice and try to barge in)")
                  right_room()

                if answer4m == "left":
                  print("(you sneak into the room to your left)")
                  print("(you lock the door just in time before they notice and try to barge in)")
                  left_room()

  if answer4f == "no":
    print("(you don't push her)")
    print("(you keep walking until you hear the soud of cars)")
    print("Should we follow the sound?")
    print("Cat: no, the dogs are dominating the roads here, we can't trust them..")
    print("ok.. i guess we'll just continue on the path then")
    print("Cat: yes, just follow me")
    print("(you walk for quite some time, then you see a big factory)")
    print("Cat: this is it, we have to walk through the door on the side of the building, my friends should have taken care of the guards)")
    print("wait what?? what are you talking about??")
    print("Cat: just follow me")
    print("(you say nothing, but do as you're told)")
    print("(you go inside, it's dark and quiet, to your left is three doors)")
    print("Cat: they're in the security room")
    security_room()



def right_room():
  global rose, stick, tulip, stone, files_documents, gun, cat_live
  print("(the room is filled with files and documents)")
  answer5a = input("(read the files and documents?)")
  if answer5a == "no":
    print("(you don't read the files and documents)")
  if answer5a == "yes":
    print("(you read the files and documents)")
    print("-World domination. Dogs will be the only kind. Eliminate all other species.-")
    print("what the hell..?")
  if gun < 1:
    print("(the dogs kick down the door and shoot you)")
    print("(you died)")
    death_message()
  else:
    answer5b = input("(Take the files and documents?)")
    if answer5b == "no":
      print("(you don't take them)")
    if answer5b == "yes":
      print("(you take them with you)")
    answer5c = input("(leave the room?)")
    if answer5c == "no":
      right_room()
    if answer5c == "yes":
      answer5d = input("('left' room or the 'hallway'?)")
      if answer5d == "left":
        left_room()
      if answer5d == "hallway":
        hallway()


    
def left_room():
  global rose, stick, tulip, stone, files_documents, gun, cat_live
  print("(the room is filled with guns)")
  answer6a = input("(take a gun?)")
  if answer6a == "no":
    print("(you don't take a gun)")
    print("(the dogs kick down the door and shoot you)")
    print("(you died)")
    death_message()
  if answer6a == "yes":
    print("(you take a gun)")
    gun += 1
    print("(It's already filled with bullets)")
    print("(the dogs are trying to get through the door)")
    answer6b = input("(shoot them when they get through?)")
    if answer6b == "no":
      print("(the dogs get through the door and shoot you)")
      print("(you died)")
      death_message()
    if answer6b == "yes":
      print("(the dogs kick down and you shoot them both successfully)")
      answer6c = input("(go to the 'right' room or the 'hallway'?)")
      if answer6c == "right":
        right_room()
      if answer6b == "hallway":
        hallway()


  
def hallway():
  global rose, stick, tulip, stone, files_documents, gun, hallway_lights, camera, dead_bodies_pic, cat_live
  if hallway_lights <= 0:
    print("(the lights are off..)")
  else:
    print("(the lights are on)")
  print("(you walk down the hallway and end up by three doors)")
  three_doors()
 
def three_doors():
  answer7a = input("(which door do you walk through?) ('1', '2', '3'")
  if answer7a == "3":
     print("(you walk through the third door)")
     dead_bodies_room()
  if answer7a == "1":
    print("(you walk to the first door)")
    security_room()
  if answer7a == "2":
    print("(you walk through the second door)")
    lounge_room()


def dead_bodies_room():
  global rose, stick, tulip, stone, files_documents, gun, hallway_lights, camera, dead_bodies_pic, cat_live
  print("(inside lies hundred of dead bodies)")
  print("(you feel sick to your stomach)")
  print("(there's a camera standing in the corner, it's off)")
  answer7b = input("(take the camera?)")
  if answer7b == "no":
     print("(you leave the camera)")
  if answer7b == "yes":
    print("(you take the camera)")
    camera += 1
    answer7c = input("(take pictures of the bodies?)")
    if answer7c == "yes":
      print("(you took pictures of the bodies)")
      dead_bodies_pic += 1
    if answer7c == "no":
      print("you don't take pictures of the bodies)")
    answer7d = input("(leave the room?)")
    if answer7d == "no":
      print("(there's nothing to do here anymore)")
      print("(you leave the room)")
    if answer7d == "yes":
      print("(you leave the room)")
      three_doors()

def security_room():
  global rose, stick, tulip, stone, files_documents, gun, hallway_lights, camera, dead_bodies_pic, enter_security_room, cat_live, name
  enter_security_room += 1
  if enter_security_room > 1:
    print()
  else:
    if cat_live == 0:
     print("(you hear someone inside)")
     print("(you load your gun and get ready to open the door)")
     print("(you quickly open it and point your gun infront of you)")
     print("(inside is three cats)")
     print("you shoot one of them, but is then shot by the second cat)")
     print("(you died)")
     death_message()
    else:
      print("(you walk inside, there are three cats)")
      print("cat1: Cat!")
      print("Cat2: finally you're here!")
      print("cat3: ok ok, we have work to do")
      print("(none of them even looked at you)")
      print("(behind them lie two dead dogs)")
      print("Cat2: we killed the guards in the lounge room too")
      print("Cat: good, we will check it out")
      print("(you walk into the lounge room)")
      lounge_room()




def lounge_room():
  global rose, stick, tulip, stone, files_documents, gun, hallway_lights, camera, dead_bodies_pic, enter_security_room, cat_live
  if cat_live == 0:
    print("(there's dead guards filling the couches)")
    print("what the hell happened here?")
    print("(you hear something behind you, you turn around to see two cats each pointing a gun at you)")
    print("(they shoot you before you even get a chance to say something)")
    print("(you died)")
    death_message()
  else:
    print("(there's dead bodies filling the couches)")
    print("Cat: we have to get all their names")
    print("Cat: get all their keycards")
    print("(you collect all the cards while Cat watches you)")
    print("(you go back to the other cats and show them the cards)")
    print("cat3: great, now we can get out of here")
    cat_police_station()

def cat_police_station():
  print("(The cats show the officer all the keycards, without even saying anything the officer seemed to understand)")
  print("...")






def death_message():
  import random
  mylist = ["really?", "that was obvious!", "wow.. you're really dumb"]
  print (random.choice(mylist))
  answer8 = input("(try again?)")
  if answer8 == "no":
    exit()
  if answer8 == "yes":
    start_point()


    




start_point()