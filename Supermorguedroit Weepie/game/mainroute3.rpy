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

label mainroute3:
scene bg diner 
camera:
    subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 

"Friday, Special of the Day: Vanilla Milkshake"

camera:
    subpixel True ypos 68 zoom 1.3 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    xpos 1 
    xpos 1
    linear 0.5 xpos 300
    linear 0.5 xpos 568
show M annoyed:
    subpixel True xpos 0.16 zoom 0.35 yalign 1.0
    parallel:
        ypos 1.0
        linear 0.15 ypos 0.9
        linear 0.15 ypos 1.0
        linear 0.15 ypos 0.9
        linear 0.15 ypos 1.0
        linear 0.15 ypos 0.9 
        linear 0.15 ypos 1.0
        linear 0.15 ypos 0.9
        linear 0.15 ypos 1.0
    parallel:
        easein 0.6 xpos 0.20
        easeout 0.6 xpos 0.3
show A evil:
    xpos 0.65 yalign 1.0 zoom 0.4

"I take the stairs two at a time, a manilla envelope tucked securely under my arm."

camera:
    pos (568, 68) 

show M annoyed:
    subpixel True 
    parallel:
        xpos 0.3 xzoom 1.0 yzoom 1.0 
        linear 0.08 xpos 0.38 xzoom 0.46 yzoom 1.04 
        linear 0.08 xpos 0.3 xzoom 1.0 yzoom 1.0 
    parallel:
        ypos 1.0 
        linear 0.16 ypos 1.0 
with Pause(0.26)
show M annoyed:
    pos (0.3, 1.0) xzoom 1.0 yzoom 1.0 

"I am racing the clock to beat the Friday morning layout, moving so fast I nearly plough straight into Adelaide the second I step out the back door."
"She is standing rigidly in the narrow, shrinking strip of shade along the brick wall, desperate to keep out of the morning sun."
"She is clutching a heavy wooden crate overflowing with soiled aprons and grease-stained dish rags."
"She does not look pleased. In fact, she looks ready to commit a felony."

show M annoyed:
    subpixel True xpos 0.3 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    pos (0.3, 1.0) 

m "Whoa sorry, sorry"
"(Not moving a single inch out of the shadows)"

show A evil:
    subpixel True 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    ypos 1.0 

a "It is fine. I am just seeing to the linens."
"(Stopping, shifting the envelope under my arm)"

show M annoyed:
    subpixel True xpos 0.3 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    pos (0.3, 1.0) 

m "You’re in charge of quite a lot of things around here, aren’t you? Waitress, accountant, charwoman…"

show A evil:
    subpixel True 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    ypos 1.0 

a "It appears so. LeeRoy’s orders."

show M annoyed:
    subpixel True xpos 0.3 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    pos (0.3, 1.0) 


show M annoyed:
    subpixel True xpos 0.3 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    pos (0.3, 1.0) 

m "Well, yes. I get it. He’s the boss."

show M annoyed:
    subpixel True xpos 0.3 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    pos (0.3, 1.0) 


m "Believe me, Adelaide, I know exactly what it’s like to have some overbearing man barking orders at you while you do all the actual heavy lifting"

show A evil:
    subpixel True 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    ypos 1.0 

a "He is not my boss."
"A beat. The rhythmic hum of the street traffic seems to drop away for a second."

show M annoyed:
    subpixel True xpos 0.3 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    pos (0.3, 1.0) 

m "…He’s not?"

show A evil:
    subpixel True 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    ypos 1.0 

a "I bought this building."
"She says it with a quiet, venomous dignity."

show A evil:
    subpixel True 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    ypos 1.0 

a "I own the griddle. I own the vinyl booths."

show A evil:
    subpixel True 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    ypos 1.0 

a "I own the jukebox, that hideous neon sign, the napkins, all of it."

show A evil:
    subpixel True 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    ypos 1.0 

a "Every single dollar in that room came directly out of my private account."

show A evil:
    subpixel True 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    ypos 1.0 

a "And yet, here I am, Mon Dieu, hiding in an alleyway, hauling filthy rags like a common scullery maid because I did not want to argue with him about the division of labor."
"I just stare at her."
"Somewhere deep behind my ribs, the hard-nosed reporter wakes all the way up."
"The bloodhound catches a scent."
"The entire power dynamic of the diner suddenly flips upside down in my head."

show M annoyed:
    subpixel True xpos 0.3 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    pos (0.3, 1.0) 

m "Wait. You’re the money?"

show A evil:
    subpixel True 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    ypos 1.0 

a "I am the money."

show M annoyed:
    subpixel True xpos 0.3 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    pos (0.3, 1.0) 

m "And he doesn’t"

show A evil:
    subpixel True 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    ypos 1.0 
with dissolve 

a "He knows. He is simply very…"

show A shy:
    ypos 1.0 xpos 0.65 zoom 0.4
with dissolve 

"She stops. She looks down at the crate of dirty laundry, searching for a word that isn’t outright cruel."
"For all her aristocratic venom, she can’t quite bring herself to completely bury him."

show A shy:
    subpixel True 
    ypos 1.0 xpos 0.65 zoom 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A shy:
    ypos 1.0 
with dissolve 

a "forgetful. He gets caught up in the performance of it all."

show M annoyed:
    subpixel True xpos 0.3 
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.40 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.50)
show M annoyed:
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

"I turn on my heel. The manila envelope can wait ten minutes."
"I reach out and grab the heavy brass handle of the diner’s back door."

show A evil:
    subpixel True 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    ypos 1.0 

a "Miss Kessler"

show A evil:
    subpixel True 
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.50 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.60)
show A evil:
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

"(Looking over my shoulder, tossing my coat onto a nearby crate and aggressively rolling up my sleeves)"

show M annoyed:
    subpixel True xpos 0.3 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    pos (0.3, 1.0) 

m "Oh, ho ho. Sit tight, Adelaide. Let me handle him."

show A evil:
    subpixel True 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show A evil:
    ypos 1.0 

a "I didn’t ask you to"

with hpunch
camera:
    subpixel True 
    xpos 568 
    linear 0.45 xpos 0 
show M annoyed:
    subpixel True 
    xpos 0.3 
    linear 0.45 xpos 0.0 
with Pause(0.55)
camera:
    xpos 0 
show M annoyed:
    xpos 0.0 

"The heavy door is already swinging shut behind me."

hide A evil

#Scene 12: Diner Kitchen - Continuous
camera:
    subpixel True 
    xpos 568 
    linear 0.45 xpos 0 
show M annoyed:
    subpixel True 
    xpos 0.6
    linear 0.45 xpos 0.4
show L main:
    xpos -0.05 yalign 1.0 zoom 0.45
with Pause(0.3)
camera:
    xpos 0 
show M annoyed:
    xpos 0.4


"I cross the checkered linoleum like a summer thunderstorm."
"Now that I know Adelaide holds the deed to the building and by extension, the lease to my room upstairs LeeRoy holds absolutely zero authority over me."
"I am entirely untouchable, and I am SO ready to crack heads."

show M annoyed:
    subpixel True xpos 0.4
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    pos (0.4, 1.0) 

m "LeeRoy. Have a minute?"

show L main:
    subpixel True 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L main:
    ypos 1.0 

l "Miss Kessler! Do you want to see the sear on these"

show M annoyed:
    subpixel True xpos 0.4
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    pos (0.4, 1.0) 
 

m "Is it true that Adelaide owns this building?"

show L main:
    subpixel True 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L main:
    ypos 1.0 

l "Well… yes."

show M annoyed:
    subpixel True xpos 0.4
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    pos (0.4, 1.0) 

m "Then why in the name of God did you send the SOLE financial backer of this establishment out into the alley to do the LAUNDRY?"

show L confused:
    xpos 0.08 yalign 1.0 zoom 0.45
with dissolve 

"Silence settles over the kitchen. I watch the gears in his head slowly grind into motion."

show L confused:
    subpixel True 
    ypos 1.0 xpos 0.08 zoom 0.45
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L confused:
    ypos 1.0 xpos 0.08 zoom 0.45

l "…Oh. Well. I..."
"His face drops. Genuine, profound guilt washes over him."

show L shrug:
    subpixel True 
    ypos 1.0 xpos 0.08 zoom 0.45
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L shrug:
    ypos 1.0 xpos 0.08 zoom 0.45
hide M annoyed 

l "You’re.. Miss Kessler, you're completely right. I shouldn't have even asked her! ADELAIDE! Addie, could you come back inside, please?"

show L shrug:
    subpixel True 
    xpos 0.08 
    linear 0.50 xpos 0.04 
show A main:
    subpixel True zoom 0.5 
    xpos 1.0 
    linear 0.50 xpos 0.22 
with Pause(0.60)
show L shrug:
    xpos 0.04 
show A main:
    xpos 0.22 yalign 1.0

"Adelaide steps through the back doorway, her voice flat and exhausted."

show A main:
    subpixel True zoom 0.5 yalign 1.0
    parallel:
        xpos 0.22 
        linear 0.10 xpos 0.22 
    parallel:
        ypos 1.0 
        linear 0.05 ypos 0.98 
        linear 0.05 ypos 1.0 
with Pause(0.20)
show A main:
    pos (0.22, 1.0) 

a "I am already here."

show L shrug:
    subpixel True 
    ypos 1.0 xpos 0.08 zoom 0.45
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L shrug:
    ypos 1.0 xpos 0.08 zoom 0.45

l "I am so sorry. I am so, so sorry, I made you put those down. Put that crate right down on the floor. ŌE!"

camera:
    subpixel True 
    ypos 68 zoom 1.3 
    linear 0.20 ypos 0 zoom 1.0 
show O solemn:
    subpixel True xpos 0.48 yalign 1.0 zoom 0.5
with Pause(0.30)
camera:
    ypos 0 zoom 1.0 

"Ōe materializes at the end of the counter."
"You could've sworn the space they're standing at was entirely empty a second ago."

show L shrug:
    subpixel True 
    ypos 1.0 xpos 0.08 zoom 0.45
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L shrug:
    ypos 1.0 xpos 0.08 zoom 0.45

l "Ōe, could you handle the dirty linens, please?"

show O main:
    xpos 0.5 yalign 1.0 zoom 0.48
with dissolve 

o "Yes."
"They take the heavy wooden crate from Adelaide without a single change in expression and vanish toward the basement."

hide O main
show M main:
    xpos 0.5 yalign 1.0 zoom 0.45
    subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

"I turn back to face Adelaide with a smile. I spread my hands wide, in a very 'told you so' manner."

show L main:
    subpixel True 
    ypos 1.0 xpos -0.05 zoom 0.47
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L main:
    ypos 1.0 xpos -0.05
with dissolve

l "There. Fixed."
"And he spins right back around to his sizzling griddle, armed with completely untroubled belief that he has just solved the systemic power imbalance of the entire restaurant."

hide L main 

"Adelaide and I stand beside him in the kitchen. We look at him. Then we look at each other."
"Adelaide raises a hand to rub her temples."

show A shy:
    subpixel True zoom 0.4 yalign 1.0
    parallel:
        xpos 0.3
        linear 0.10 xpos 0.3
    parallel:
        ypos 1.0 
        linear 0.05 ypos 0.98 
        linear 0.05 ypos 1.0 
with Pause(0.20)
show A shy:
    pos (0.3, 1.0) 

a "That is the tragedy of it. He isn't malicious... He just… he does not think things through."

show A main:
    xpos 0.22 yalign 1.0 zoom 0.5

"She adjusts her posture, lets out a long, long-suffering sigh, and drifts back out to the dining room to tend to her ledger books."

hide A main

menu:
    "Push LeeRoy harder.":
        "I am not letting him off the hook that easily."

        show L shrug:
            yalign 1.0 xpos 0.08 zoom 0.45

        "I march over and corner him by the kitchen pass, ready to give him a piece of my mind about the principles of delegated labor."
        "But before I can even wind up, he starts apologizing again."
        "He apologizes to me, he apologizes to Adelaide despite her not being present, he apologizes to the spatula."
        "He is so relentless with his apologies that I run out of righteous anger before he runs out of breath."

        hide L shrug 

    "Ask Adelaide why she doesn't just say no.":
        "I walk out to the dining room and lean over her booth."

        show A main:
            xpos 0.22 yalign 1.0 zoom 0.5

        show M main:
            subpixel True xpos 0.5
            ypos 1.0 zoom 0.45
            linear 0.05 ypos 0.98 
            linear 0.05 ypos 1.0 
        with Pause(0.20)
        show M main:
            pos (0.5, 1.0) 

        m "So, if you're the owner…"
        "I whisper."

        show M main:
            subpixel True xpos 0.5
            ypos 1.0 zoom 0.45
            linear 0.05 ypos 0.98 
            linear 0.05 ypos 1.0 
        with Pause(0.20)
        show M main:
            pos (0.5, 1.0) 

        m "Why don't you just refuse him?"

        "She doesn't look up, her fountain pen scratching smoothly across the paper."

        show A main:
            subpixel True zoom 0.5 yalign 1.0
            ypos 1.0 
            linear 0.05 ypos 0.98 
            linear 0.05 ypos 1.0 
        with Pause(0.20)
        show A main:
            pos (0.22, 1.0) 

        a "I cannot find the will to refuse him,"
        "she murmurs."
        "I look back across the diner toward the kitchen."
        "LeeRoy is beaming over the deep fryer, lifting the wire basket with a look of pure joy over a perfect batch of golden onion rings."
        "His happiness is so bright that I suddenly understand exactly why telling him 'no' didn't even cross her mind."

        hide A main
        hide M main
        # [LISTEN +1]

#Scene 13: The Supermurgidroid Weepie - Friday Evening
scene bg bedroom
camera:
    subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.1)*HueMatrix(0.0) 

show M main:
    xpos 0.12 yalign 1.0 zoom 0.45

"I close the door behind me. Chief actually approved the piece."

scene bg diner

show M main:
    xpos 0.12 yalign 1.0 zoom 0.45

"Even if it was at the cost of having my opening paragraph butchered, it went to print for the morning edition."
"And miraculously, it actually worked."
"The diner isn't exactly standing-room-only, but there are actual customers in the booths."
"Six, maybe eight scattered around the room."
"The Wurlitzer jukebox is finally plugged in, spinning a scratchy 45 that fills the air with a steady bassline."
"Out on the front sidewalk, visible through the plate glass, two teenage girls are strapping on the diner's roller skates and trying to balance on them with absolutely zero talent, clinging to the brick wall and shrieking with laughter."
"It is a vast improvement over the silence."
"I am slumped over the counter with a mug of black coffee, running on pure fumes after spending the entire night hunched over the keys of my Royal typewriter."
"My shoulders ache, my fingers are stiff, but I would do it all over again in a heartbeat."

show L main:
    xpos 0.45 yalign 1.0 zoom 0.5

"LeeRoy suddenly materializes on the other side of the counter."
"He slides a small, wooden-framed chalkboard down the table toward me."
"There are four items listed on it in slightly uneven chalk lettering."

show L main:
    subpixel True 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L main:
    ypos 1.0 

l "Miss Kessler. Pick one. On the house."
"I stare at him over the rim of my mug, my eyes narrowed."

show M main:
    subpixel True xpos 0.12 zoom 0.45
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    pos (0.12, 1.0) 

m "Are you actively trying to put me in the municipal hospital, LeeRoy?"
"He remains completely undeterred."

show L main:
    subpixel True 
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L main:
    ypos 1.0 

l "I would consider it a personal favour if you would be the very first to sample our new dessert menu."
"I let out a long, exhausted breath. I set my coffee down and lean forward to actually read the board."
#[CHOICE ROUTES GO HERE]
#[Whatever happens, happens]
#"[Name] gives me a lingering look, excuses [herself/himself/themselves], and slips back behind the counter to get back on the clock."
hide L main
hide M main
window hide
call screen dessert

screen dessert:

    imagebutton:
        idle Transform(dessert_adelaide, zoom=0.5, matrixcolor=BrightnessMatrix(-0.1))
        hover Transform(dessert_adelaide, zoom=0.5, matrixcolor=BrightnessMatrix(+0.1))
        align (0.3, 0.5)
        action Confirm("Choose the Pear pie?",Jump("next"))

    imagebutton:
        idle Transform(dessert_oe, zoom=0.5, matrixcolor=BrightnessMatrix(-0.1))
        hover Transform(dessert_oe, zoom=0.5, matrixcolor=BrightnessMatrix(+0.1))
        align (0.7, 0.5)
        action Confirm("Choose the Dark Chocolate Cherry cake?", Jump("oe"))

label oe:
    "LeeRoy takes the menu back with a smile." 
    
    LEEROY: "I'll bring it in a moment."

    "He then makes a beeline straight for the kitchen. I find myself staring at the drawings across the room, oblivious to my surroundings. Ōe slides a heavy white saucer across the counter. Resting on it is a single, perfect persimmon—a fruit entirely out of season and nowhere near native to this county. They have cut it into exactly eight identical wedges. The skin is peeled back. It is an arrangement that requires a level of obsessive attention wildly out of proportion for the establishment I am in."

    Dorothy: "Where… did you even get this?"

    ŌE: "Persistance."

    "I pick up one of the wedges and take a bite. The flavor is incredibly sweet. I stop chewing, my journalistic brain catching up with the sentence."

    Dorothy: "Persistence? This diner's only been open a month. Where would you even—"

    "Oe does not explain themselves, instead they hint toward the plate."

    ŌE: "Is it good?"

    Dorothy: "…I— yes. It's actually very good."

    "I finish the slice. Ōe sits perfectly still on the other side of the counter, watching me eat. Their expression is hard to read, it isn't hunger, not exactly. More of an.. interest?"

    ŌE: "You changed the menu."

    "My spine instantly goes rigid. I set the fruit down on the saucer, the defensive armor snapping right back into place."

    Dorothy: "Look, no offence but… it was difficult to read. The penmanship was beautiful, sure, but it was completely illegible. In the restaurant racket, that’s—"

    ŌE: "I am not complaining."

    "That stops me. I look at them. They both sound and look entirely sincere-"

    "They tilt their head, just a fraction of an inch, studying me."

    ŌE: "I have been thinking about it since Thursday."

    "I don't know what to do with that information. It is unnerving to be perceived this closely."

    Dorothy: "…it's just a board, Ōe."

    ŌE: "Yes."

    "I glance past their shoulder, looking out toward the dining room. My eyes drift up to the back wall. Dozens of framed oil paintings of cars hang there, each one rendered with what I can only call various degrees of obsessive precision."

    ◆ CHOICE(s)

    "Ask them about the paintings." → "Were the wall paintings your idea?" I ask, keeping my voice low. Ōe does not answer. They just looks at me, the silence stretching out until the Wurlitzer clicks in the corner. [LISTEN +1]

    "Change the subject." → 
    "I clear my throat, actively ignoring the sudden tightness in my chest, and point to the rest of the fruit."
    "Are you going to eat any of this, or did you just slice it up for your own entertainment?"
    "Ōe simply pushes the saucer an inch closer to me. "
    "It is for you, Miss Kessler."
    "I eat the rest in silence."
    jump next

label next:
hide L main 
camera:
    subpixel True 
    zoom 1.0 
    linear 0.50 zoom 1.25 
show M melancholy:
    subpixel True 
    parallel:
        xpos 0.16 xzoom 1.0 yzoom 1.0 
        linear 0.09 xpos 0.16 xzoom 0.81 yzoom 1.16 
        linear 0.41 xpos 0.08 xzoom 1.0 yzoom 1.0 
    parallel:
        zoom 0.35 
        linear 0.50 zoom 0.4 
with Pause(0.60)
camera:
    zoom 1.25 
show M melancholy:
    xpos 0.08 xzoom 1.0 yzoom 1.0 zoom 0.4 

"I watch them go, feeling a strange pull in my chest. Is it… no. Can't be."

"I'm a strong independent woman and I do NOT have such impure feelings. Over anyone."

camera:
    subpixel True zoom 1.25 
show M annoyed:
    subpixel True xpos 0.08 zoom 0.4  
with dissolve 

"I force my attention down to the table and push my plate away, the last smear of dessert drying on the porcelain."
"Over by the wall, the Wurlitzer clicks and whirs, dropping a new 45 onto the turntable with a crackle."
"I dig into my coat pocket, pull out my spiral steno pad, and flip it open to the section where I keep my better leads."
"I pull the cap off my fountain pen."

show M melancholy 
with dissolve 

"I stare at the paper for a long time before I finally write down the only real angle I can come up with on such a short notice:"
"The diner with the creepy name might just have a pulse after all."
"It is not exactly front-page news. Another candidate for being featured on the women's page alongside the rest of local fluff. It screams 'local colour'."
m "I still have time."
"Behind me, out in the dark asphalt lot, a pair of headlights sweeps across the windows."
"A heavy sedan downshifts, the tires crunching over the gravel as it slows off Route Nine and pulls into a parking space."
"I click the cap back onto my pen and slide the pad into my pocket."
"Whether I get my front-page scoop or not, one thing is dead certain: this joint is about to get a whole lot busier."
#Scene 14: The Supermurgidroid Weepie - Friday Night
camera:
    subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.2)*HueMatrix(0.0) 
    subpixel True zoom 1.0 

show M annoyed:
    subpixel True 
    xpos 0.16 xzoom 1.0 yzoom 1.0 
    linear 0.08 xpos 0.23 xzoom 0.55 yzoom 1.21 
    linear 0.08 xpos 0.16 xzoom 1.0 yzoom 1.0 
with Pause(0.26)
show M annoyed:
    xpos 0.16 xzoom 1.0 yzoom 1.0 

"I take another sip. It's quarter to one in the morning."
"The diner is thankfully empty and the jukebox had been plugged off for the night. Good riddance."
"I am perched at the far end of the counter nursing the last bitter dregs of the coffee pot, locked in an amiable argument with LeeRoy."
"It's quite the dilemma, trying to decide whether Friday's onion burger special has too much onion on it or too little."
"My position is that it does not."
"His position is that his eyes water whenever he walks past the prep station a complaint I point out he probably shouldn't be volunteering a potential customer."
"The brass bell over the front door chimes."
"A man steps inside. He looks to be in his late forties, wearing a faded coat against the autumn chill."
"He has a heavy olive-drab duffel bag slung over one shoulder and chalky road dust coating his trousers right up to the knee."

hide M annoyed 

e "You folks still open?"

show L main:
    yalign 1.0 xpos 0.4 zoom 0.5

"Leeroy bolts out of his seat, practically radiating with excitement."

show L main:
    subpixel True 
    ypos 1.0 xpos 0.4 zoom 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L main:
    ypos 1.0 xpos 0.4 zoom 0.5

l "We're open. Come on in."
"The man drops his bag heavily onto the linoleum and takes a seat two stools down from me."
"He squints up at the blackboard I wrote out on Tuesday."

hide L main 

e "What's the cheapest thing on there?"

show L main:
    subpixel True 
    yalign 1.0 xpos 0.4 zoom 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L main:
    ypos 1.0 xpos 0.4 zoom 0.5

l "Coffee's free after midnight."

hide L main 

e "Since when?"

show L main:
    subpixel True 
    yalign 1.0 xpos 0.4 zoom 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L main:
    ypos 1.0 xpos 0.4 zoom 0.5

l "…Since right now, I guess."
"Earl laughs. He sounds equally part tired and amused."
"He ends up ordering a cheeseburger anyway, along with a vanilla milkshake."
"Apparently he saw it listed on the menu and wanted to splurge. Mixing dairy and grease? What a madman."
"When it arrives, he takes a long draw of the milkshake. He immediately pulls the glass away and looks at LeeRoy."

hide L main 

e "It's.. quite good. Could use a bit of malt powder."
"I don't look up from my mug as I reply."

show M annoyed:
    subpixel True
    xpos 0.16 yalign 1.0 zoom 0.35
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 xpos 0.16 zoom 0.35

m "Tell him that. Please. He absolutely will not hear it from me."
"The man grins, wiping his mouth with the back of his hand."

hide M annoyed

e "Naw. I ain't getting in the middle of domestic troubles."
"For a few minutes, we just sit there, listening to the hum of the refrigerators."

show M main:
    subpixel True
    xpos 0.12 yalign 1.0 zoom 0.45
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    ypos 1.0 xpos 0.12 zoom 0.45

m "Where are you headed, anyway?"

hide M main

e "Toledo. My brother's got a gig lined up for me on a freight dock, starts Thursday morning."
e "I caught a ride as far as the county line, but it dried up."
e "Had nothing but asphalt and headlights for some… four hours."
"He nods toward the window, where the red glare bleeds onto the sidewalk."
e "Saw that sign from the road. Figured a joint called the 'Super Morgue' had to be worth a look."

show M main:
    subpixel True
    xpos 0.12 yalign 1.0 zoom 0.45
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    ypos 1.0 xpos 0.12 zoom 0.45

m "It is, actually."
"Earl excuses himself to use the washroom in the back, leaving his heavy canvas duffel resting against the chrome stool."
"I finish the last sip of my coffee, drop a dime on the counter for a tip and slide off my seat to gather my coat."

show L main:
    yalign 1.0 xpos 0.4 zoom 0.5 
show M main:
    subpixel True
    xpos 0.12 yalign 1.0 zoom 0.45
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    ypos 1.0 xpos 0.12 zoom 0.45 

m "Night, LeeRoy."

show L main:
    subpixel True 
    yalign 1.0 xpos 0.4 zoom 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L main:
    ypos 1.0 xpos 0.4 zoom 0.5

l "Goodnight, Miss Kessler."

hide L main
scene black
with fade
#[adelaide goes brrrrrr kills everyone here]

#testing stuff here
jump oe
