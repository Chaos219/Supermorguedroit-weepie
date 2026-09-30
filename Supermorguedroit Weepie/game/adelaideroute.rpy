# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #how eileen happy

    # These display lines of dialogue.

    # e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    #return

label adelaide:

#int. Diner - Afternoon
camera:
    reset 
scene bg diner with fade 
camera:
    subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 

"Still rattled over my latest failure to turn up a single worthwhile headline after pounding the pavement all day, I decide to head back and ask my vamp-landlords for help. Why didn't I think of that before? There's a group of supposed immortals right below me, and here I am, trying to wrangle a story about a cow farm."
"It is well before opening time, and from the street, the diner looks pitch black with no sign of anyone inside. However, when I try the front door, the knob turns right in my hand. It is… unlocked. What the—! My blood immediately boils."
"They can't cook, fix drinks, and apparently, they can't lock their OWN establishment either! It figures this place is so affordable; they are practically inviting burglars up my stairs."

with hpunch

"I step inside the dark restaurant, ready to give someone a piece of my mind, when a loud clatter echoes from the back. The unmistakable sound of water spilling on the linoleum, as something metallic falls to the floor."
"Before I can even process what I am hearing, a string of furious, muffled cursing immediately follows. I follow the racket to the back room, only to find Adelaide stranded in the center of a massive, foamy pool of spilled mop water."

show A evil:
    subpixel True zoom 0.4 
    xpos 702 
    yalign 1.0 
    linear 0.05 ypos 0.95 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "That blockhead LeeRoy and his creepy little shadow! They completely trash the kitchen, then simply WALTZ out to ‘find inspiration’, leaving me to wrestle with this… UGH!"

show A evil:
    subpixel True zoom 0.4 
    xpos 702 
    yalign 1.0 
    linear 0.05 ypos 0.95 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "Mon Dieu, just look at this— when I get my hands on those two peasants, the things I’ll—"

hide A evil

"The company phone starts to ring."

show M annoyed:
    xpos 0.35 yalign 1.0 zoom 0.35 

m "(Who in the world is calling this place at this hour?)"

hide M annoyed 
show A evil:
    subpixel True zoom 0.4 
    xpos 702 
    yalign 1.0 
    linear 0.05 ypos 0.95 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "Let it ring. I am already drowning in servitude; I refuse to play the receptionist on top of it!"

show A evil:
    subpixel True zoom 0.4 
    xzoom 1.0 yzoom 1.0 
    linear 0.08 xzoom 0.59 yzoom 1.06 
    linear 0.08 xzoom 1.0 yzoom 1.0 
with Pause(0.26)
show A evil:
    xzoom 1.0 yzoom 1.0 

"I watch Adelaide furiously dunk the mop back into the, now, empty bucket. She clearly isn’t going to touch that receiver, and the ringing is starting to grate on my nerves."

hide A evil
show M annoyed:
    subpixel True xpos 0.35 yalign 1.0 zoom 0.35 
    parallel:
        ypos 1.0 
        linear 0.08 ypos 0.98 
        linear 0.08 ypos 1.0 
with Pause(0.26)
show M annoyed:
    yalign 1.0 xpos 0.35 zoom 0.35

m "I… suppose I should answer it. What if it’s an emergency?."

show M annoyed:
    subpixel True zoom 0.35 
    parallel:
        xpos 0.35
        linear 0.50 xpos 0.6
    parallel:
        ypos 1.0 
        linear 0.10 ypos 0.98 
        linear 0.10 ypos 1.0 
        linear 0.10 ypos 0.98 
        linear 0.10 ypos 1.0 
with Pause(0.60)
show M annoyed:
    pos (0.6, 1.0) 

"I walk over to the counter and pick up the heavy receiver.."
m "Hello, dinner?"

hide M annoyed 
with hpunch

b "Dolly!"

show M annoyed:
    subpixel True zoom 0.35 xpos 0.6 yalign 1.0
    xzoom 1.0 yzoom 1.0 
    linear 0.08 xzoom 0.56 yzoom 1.21 
    linear 0.08 xzoom 1.0 yzoom 1.0 
with Pause(0.26)
show M annoyed:
    xzoom 1.0 yzoom 1.0 

m "Ahh! B-boss? Why are you calling the dinner?"

show M annoyed:
    subpixel True zoom 0.35 
    yalign 1.0 xpos 0.6
    linear 0.08 ypos 0.98 
    linear 0.08 ypos 1.0 
with Pause(0.26)
show M annoyed:
    yalign 1.0 xpos 0.6

m "I mean, afternoon, Chief! What's uh, what's going on?"

hide M annoyed 

b " I rang your room upstairs, but there was no answer. Since you are living above the dinner, I figured I’d try the main line."

show M annoyed:
    subpixel True zoom 0.35 
    yalign 1.0 xpos 0.6
    linear 0.08 ypos 0.98 
    linear 0.08 ypos 1.0 
with Pause(0.26)
show M annoyed:
    yalign 1.0 xpos 0.6

m "Oh, uhhh, right. (How embarassing!)"

hide M annoyed 

b "Listen, kid, I’m calling to give you the skinny on the Sunday edition. The publisher just moved the goalpost."

show M annoyed:
    subpixel True zoom 0.35 xpos 0.6
    parallel:
        yalign 1.0 
        linear 0.08 ypos 0.98 
        linear 0.08 ypos 1.0 
    parallel:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.08 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 5.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.26)
show M annoyed:
    yalign 1.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 5.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

m "Oh?"

hide M annoyed 

b "I will have to slash your deadline. In half. Which is to say you now have half as much time to get a headline."

camera:
    subpixel True 
    zoom 1.0 
    linear 0.08 zoom 1.25 
show M annoyed:
    subpixel True 
    parallel:
        xpos 0.6 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) zoom 0.35 
        linear 0.08 xpos 0.4 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) zoom 0.4 
    parallel:
        yalign 1.0 
        linear 0.08 ypos 0.98 
        linear 0.08 ypos 1.0 
with Pause(0.26)
camera:
    zoom 1.25 
show M annoyed:
    pos (0.4, 1.0) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) zoom 0.4 
with hpunch 

m "WHAT? How?? Why??"

hide M annoyed 

b "Don’t bark at me, Dorothy. I don’t run the presses. Word on the street is the Chronicle is dropping a massive spread on the auction scandal. The publisher wants to beat them to the punch, which means the layout has to be finalized earlier."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0 xpos 0.4

m "But you can’t just cut my time in half! We had a deal! I don’t- I don’t even have a solid lead yet!"

hide M annoyed 

b "That sounds like a ‘you’ problem, Sweetheart. If you don’t have a knockout story by the new deadline, you will have to make-do and write for the woman's pages."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0 xpos 0.4

m "Chief! I…"

hide M annoyed 

b "Now, I realize working under a real time-crunch is a tough beat…,"

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0 xpos 0.4

m "Yeah."

hide M annoyed 

b "...and a bit of a raw deal…"

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0 xpos 0.4

m "Mmmm."

hide M annoyed 

b "...and perhaps even agonizingly stressful.."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0 xpos 0.4

m "(Can he just stop it already?!)"

hide M annoyed 

b "But this is the newspaper business, darling. If you want to be a top-flight reporter, you have to be able to handle the heat. Have it on my desk by the end of the month. Don’t let me down."

"Click."
"He hangs up."

camera:
    subpixel True 
    zoom 1.25 
    linear 0.30 zoom 1.0 
show M annoyed:
    subpixel True 
    xpos 0.4 zoom 0.4 yalign 1.0
    linear 0.30 xpos 0.6 zoom 0.35 
with Pause(0.40)
camera:
    zoom 1.0 
show M annoyed:
    xpos 0.6 zoom 0.35 yalign 1.0
    
m "……………………………………."
"I stand there dumbfounded. Half as much time??"

show M annoyed:
    subpixel True 
    yzoom 1.0 
    easeout 0.20 yzoom 1.1 
    easeout 0.20 yzoom 1.0 
    easeout 0.20 yzoom 1.1 
    easeout 0.20 yzoom 1.0 
with Pause(0.90)
show M annoyed:
    yzoom 1.0 

m "Okay, stay calm. I just need to take a deep breath, and focus. And… breathe in. Breathe out…"

show M annoyed:
    subpixel True 
    parallel:
        ypos 1.0 
        linear 0.10 ypos 0.9 
        linear 0.20 ypos 1.0 
    parallel:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.30 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.40)
show M annoyed:
    ypos 1.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

"I eye the back room door and hear the commotion on the other side escalating into a frenzy."

hide M annoyed
with hpunch

a "I DESPISE MOPS! I LOATHE GRIME! I. HATE. LEEROY. I HATE RUINING MY MANICURE! I HATE THAT FLARING BALL IN THE SKY! I HATE–"

with hpunch

stop music

play sound "door_slamming.ogg"

show M annoyed:
    subpixel True 
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    parallel:
        xpos 0.6 yalign 1.0 zoom 0.35
        linear 0.30 xpos 0.6 
        linear 0.50 xpos 0.08 
    parallel:
        ypos 1.0 zoom 0.35 xpos 0.6
        linear 0.40 ypos 0.9 
        linear 0.10 ypos 1.0 
        linear 0.10 ypos 0.9 
        linear 0.10 ypos 1.0 
with Pause(0.90)
show M annoyed:
    pos (0.08, 1.0) 
with easeinright

"Panic taking over, I march over to the door and shove it open with a bang. The sudden noise startles Adelaide out of her wits."

play music "retro.ogg"

camera:
    reset

show M annoyed:
    subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    xpos -0.2 
    linear 0.20 xpos 0.25 
show A evil:
    subpixel True 
    xpos 1260 yalign 1.0 zoom 0.4
    linear 0.30 xpos 1260 
with Pause(0.40)

show M annoyed:
    xpos 0.25 
show A evil:
    subpixel True xpos 1260 yalign 1.0 zoom 0.4
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.20 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.30)
show A evil:
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

"She whips around with a sharp hiss, her fangs bared in full force. For a split second, she looks ready to commit violence."

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "Oh. It is just… you. Again."

show M annoyed:
    subpixel True 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "I am terribly sorry about your poor cleaning experience, but I need your help and it truly, earnestly cannot wait!"

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4
    linear 0.05 ypos 0.98
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "As convincing as your obnoxious tone is, can you not see that I am currently occupied with something?"

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "I…what are you doing?"

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "Is it not obvious? Humiliating, grueling labor completely unfit for someone such as myself."

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "And yet, here I am. Slaving away."

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "Maybe this is revenge from the universe."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "Where is everyone? Are you the only one here?"

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "Seeing as you had to not only rudely barge into this room, but also the restaurant as a whole, I would assume that it was obvious that yes, I am indeed the only person around."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "It is quite a mess in here, are you sure you can clean up all of this by yourself?"

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "Thank you for noticing that this is indeed a mess too large for one to clean up. You may be wondering where those two other idiots are."

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "They're off into the sun where I can’t follow them. Those buffoons left me to clean up after their messes, as usual."

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "On the topic of messes, you look like one."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "Thank you, I haven’t noticed."

show A main:
    subpixel True 
    ypos 1.02 zoom 0.53 xpos 954
    linear 0.05 ypos 1.0
    linear 0.05 ypos 1.02
with Pause(0.20)
show A main:
    ypos 1.02 zoom 0.53 xpos 954

a "No need to get snappy. Let’s go."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "Let’s go where?"

show A main:
    subpixel True 
    yalign 1.0 zoom 0.53
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A main:
    yalign 1.02 zoom 0.53

a "Your room. The others will clean this up."

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 1260
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "I’ll make sure of that."

scene black with fade 
scene bg bedroom with fade 

"She drags me up to my room, where she pushes me on my bed and starts rummaging through my makeup."

with hpunch
show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.3
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "What are you doing?"

show A main:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A main:
    yalign 1.0 

a "The first step to feeling good is looking good."

show M melancholy
with dissolve 

"She starts reapplying some of my makeup. Her hands are surprisingly gentle as she holds my cheek to stabilize my face while applying my signature blue eyeliner."

show A shy:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.6
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A shy:
    yalign 1.0 

a "Why are you getting so worked up about this anyways? What’s so wrong about writing for the women’s pages? You’re a woman after all."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.3
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0  

m "You wouldn’t get it. It’s about honor! Dignity! A chance to finally leave this boring town behind!"

show A main:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A main:
    yalign 1.0 

a "Alright, if it’s about dignity, why are you acting like a wet rag in front of your boss?"

show A main:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A main:
    yalign 1.0 

a "It’s honestly pathetic to see you fold in front of him."

show M melancholy:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.3
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    ypos 1.0 

m "Well - you know -"

show M melancholy:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.3
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    ypos 1.0 

m "I’m scared of him. I guess."

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.6
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "Scared of him? Please. You come downstairs to yell at us every day but you’re scared of a lowly human?"

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.6
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "You do know LeeRoy could kill you without even trying."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.3
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "LeeRoy wouldn’t hurt a fly -"

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.6
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "But he could! And I could as well!"

show M melancholy:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.3
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    ypos 1.0 

m "You’re not gonna hurt me."

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.6
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "You don’t know that."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35
    linear 0.05 ypos 0.98
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "If you attack me I’ll just run out into the sun."

show A shy:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.6
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A shy:
    yalign 1.0 

a "You’re not being fair."
"She pokes me with the back of a makeup brush with a pout that’s almost cute."

show M melancholy:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.3
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    ypos 1.0 

m "Either way, my boss pays me and I need the money. I want to leave this city. And if I lose my job, well -"

show M melancholy:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.3
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    ypos 1.0 

m "I wouldn’t just lose that chance, I’d have to move back with my parents. And you understand why I wouldn’t wanna do that."
a "..."

show M melancholy:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.3
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    ypos 1.0 

m "You do understand it, right?"

show A shy:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.6
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A shy:
    yalign 1.0 

a "Honestly, I don’t even think I remember my parents."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "What?"

show M melancholy:
    xpos 0.3 yalign 1.0 zoom 0.35
with dissolve 

"I look at her. While my relationship with my parents wasn’t always sunshine and rainbows, they still mattered a lot to me. Forgetting them? Out of question."

show A shy:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.6
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A shy:
    yalign 1.0 

a "I mean, that’s part of being a vampire. And my parents didn’t really raise me to begin with."

show M melancholy:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.3
    linear 0.05 ypos 0.98
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    ypos 1.0 

m "I don’t know if that’s insensitive to ask, but - When did you get turned?"

show A shy:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.6
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A shy:
    yalign 1.0 
    
a "Hm? It’s fine, I guess."

show A main:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A main:
    yalign 1.0 

a "I let myself get turned during the french revolution. We were nobles and I didn’t exactly want to die."

show M melancholy:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.3
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    ypos 1.0 

m "So you ran away from taking accountability?"

show A main:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A main:
    yalign 1.0 

a "Oh come on, I wasn’t the sole perpetrator."

show A shy:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.6
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A shy:
    yalign 1.0 

a "But yeah, I guess."

show A shy:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.6
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A shy:
    yalign 1.0 

a "I’m not like you, you know."

show M melancholy:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.3
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    ypos 1.0 

m "What’s that supposed to mean?"

show A shy:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.6
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A shy:
    yalign 1.0 

a "Well, I don’t go yelling at people when they disturb my sleep, I wasn’t even able to tell LeeRoy when I was upset with him."

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.6
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "And when I’m in the wrong, I just smile and insult someone to feel better."

show M main:
    subpixel True 
    yalign 1.0 zoom 0.45 xpos 0.26
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    ypos 1.0 

m "Oh I do that too."

show A happy:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.6
with dissolve 

"Adelaide laughs and for once her smile seems genuine before it turns icy again."

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.6
    linear 0.05 ypos 0.98
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "You know, if you ever need that headline, I don’t mind killing someone for you."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.3
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "I- no thanks. I can do this without murder, thank you very much."

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.6
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "Your loss, but don’t forget the offer stands."

scene black with fade 
#New Day
scene bg bedroom with fade 
camera:
    subpixel True 
    pos (476, 168) zoom 1.25 
    linear 0.30 pos (0, 0) zoom 1.0 
with Pause(0.40)
camera:
    pos (0, 0) zoom 1.0 

"Today’s Special: Blood of your enemies."

with hpunch 

"I threw my newspaper collection on the floor."

show M angry:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.16
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M angry:
    ypos 1.0 

m "How dare he?! That stuck-up, smirking Asshole!"

show M angry:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.16
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M angry:
    ypos 1.0 

m "I’m gonna DO SOMETHING TO HIM!"

with hpunch
show M disgusted:
    xpos 0.16 zoom 0.45 yalign 1.0
with dissolve 

"I stick even more pins in Chet's picture on my pinboard, a habit whenever I feel angry at him."

show A main:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.48
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A main:
    yalign 1.0 

a "You alright?"
"I look up from angrily blacking out some of his articles when I saw Adelaide has invited herself in."

show M angry:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.16
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M angry:
    ypos 1.0 

m "Get lost."

show A main:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.48
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A main:
    yalign 1.0  

a "I heard you yell. What happened? Couldn’t find a headline?"

show M angry:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.16
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M angry:
    ypos 1.0 

m "Oh no, I DID find a headline!"

show M angry:
    subpixel True 
    xpos 0.16 
    linear 0.20 xpos 0.24 
with Pause(0.30)
show M angry:
    xpos 0.24 
with easeinright

"I stand up and come closer to her, fuming."

show M disgusted:
    subpixel True 
    yalign 1.0 zoom 0.45 xpos 0.24
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M disgusted:
    ypos 1.0  

m "My boss gave it to Chet. Again. Even though it was MY story. MY LEADS."

show A main:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.48
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A main:
    yalign 1.0  

a "Doesn’t seem like he was planning on giving you a chance to begin with."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.24
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "Doesn’t seem so."

show M melancholy 
with dissolve 

"I sigh, staring at the mess of newspapers. Somewhere there was my life’s work."
"This hemline will make you look ten years younger! Try this tea to calm your nerves if your husband comes home too late every night! Five recipes to lose even more weight!"
"Was this all I was? All I would ever be? At this point, I didn’t know anymore."

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.55
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "You should stand up to him."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.24
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "Hm?"

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.55
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "It’s getting dark anyways. I’ll come with you."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.24
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "And what am I supposed to tell him? That he’s a sexist bastard that can go put his slimy smirk up his own ass?"

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.55
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "That would be one option, yes."
"I can see a tiny glimmer of amusement in her eyes at my choice of words."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.24
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "Well, as much as I’d love to do that, I don’t want to lose the job."

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.55
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "You can work for the diner. You’ve been practically doing that anyways."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.24
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0

m "The diner that’s barely functioning? Are you sure it can afford another staff member?"

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.55
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0 

a "It couldn’t afford the first staff member."

show A happy:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.55
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A happy:
    yalign 1.0 

a "But I always can."
"She winks at me and takes my hand."

show A happy:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.55
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A happy:
    yalign 1.0 

a "You deserve better than this. So come on. Let’s go!"

#Office Outside
scene black with fade 
scene bg office with fade 

"We rushed to the Office to catch the Boss before he left the building."
b "Now, what are you doing here, Sweetheart? Ready to give up?"
"The old man let’s his gaze wander over Adelaide and grins, showing off his gold tooth."
b "My, and who is this doll? Did you bring me a hooker as an apology?"

show M angry:
    xpos 0.16 zoom 0.35 yalign 1.0
with hpunch

"I stare at him. I feel my blood boil. I was done with this. Humiliating me was one thing - but this crossed everything."

show M angry:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.16
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M angry:
    ypos 1.0

m "How Dare you? Who do you think you are to treat other humans like that?"

show M angry:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.16
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M angry:
    ypos 1.0

m "Do you think you can just say and do whatever you want with no consequences? Do you think you’ll get away with treating me like trash?"

hide M angry 

"The boss laughs and gets out a cigar, about to light it. I snatch it away from him and throw it on the ground."
b "Naw, the little girl is mad… You’ll have to pay for that one."

show M angry:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.16
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M angry:
    ypos 1.0

m "The only one paying will be you!"

with hpunch 

scene murder_cg:
    size (1920, 1080)

"I quickly saw surprise flash in his eyes as I lunged on him and we fell to the ground."

with hpunch

camera:
    subpixel True pos (0, 0) zoom 1.0 alpha 1.0 additive 0.0 
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    linear 0.10 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.1)*HueMatrix(0.0) 

"I threw punch after punch, ignoring the cracking noises his bones were making under my hands."

camera:
    subpixel True pos (0, 0) zoom 1.0 alpha 1.0 additive 0.0 
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    linear 0.10 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.2)*HueMatrix(0.0) 

"Adelaide stood at the side, a bit surprised, but even more so intrigued."

camera:
    linear 0.10 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.3)*HueMatrix(0.0) 
with Pause(0.40)
camera:
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.3)*HueMatrix(0.0) 

"After a few solid minutes I finally stood back up, out of breath."

scene bg office with fade

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.16
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0

m "You can take his blood if you want."

hide murder_cg

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.55
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.

a "Take his blood? Please, I don’t want to touch that with a five foot pole."
m "..."

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.55
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0
    
a "We should leave. People are gonna be here soon."
"She grabs my hand and practically pulls me back to the diner. I just stare at the floor as I follow her. My hands are full of his blood."

#Diner
scene black with fade 
scene bg diner with fade 
camera:
    subpixel True pos (0, 0) zoom 1.0 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 

show L confused:
    yalign 1.0 zoom 0.45 xpos 0.48

l "Yo, Where were you? What happened?"

show A main:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.2
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A main:
    yalign 1.0

a "No time to explain, we’re moving."

hide L confused 

show O solemn:
    subpixel True xpos 0.45 zoom 0.5 
    yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    pos (0.45, 1.0) 

o "Again? Where to this time?"

show A main:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.2
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A main:
    yalign 1.0

a "New York."

hide O solemn

"I finally looked up."

show A main:
    subpixel True 
    xpos 0.2 
    linear 0.20 xpos 0.3 
with Pause(0.30)
show A main:
    xpos 0.3 

show M melancholy:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.16
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    ypos 1.0

m "New York?"

show A happy:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A happy:
    yalign 1.0

a "Of course. And as promised, you’ll come with us. You wanted to go to the city, no?"

show M melancholy:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.16
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    ypos 1.0

m "W- well, yes. Not this way, but -"

show A shy:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A shy:
    yalign 1.0

a "Life doesn’t always turn out the way you want it to."
 
show L main:
    subpixel True xpos 0.5 zoom 0.5 
    yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L main:
    pos (0.5, 1.0) 

l "New York it is. But you better have a good reason for this."
"He already starts packing up stuff."

hide L main

show A evil:
    subpixel True 
    yalign 1.0 zoom 0.4 xpos 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    yalign 1.0

a "Oh trust me, we have a damn good reason."

return