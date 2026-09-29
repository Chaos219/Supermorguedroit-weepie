# The script of the game goes in this file.

init python:
    def boopy_voice(event, boopfile="bleep007.ogg", **kwargs):

        if event == "show_done":
            renpy.sound.play(boopfile, loop=True)
        elif event == "slow_done":
            renpy.sound.stop()    
# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Characters
define m = Character("Dorothy", callback=boopy_voice)
define a = Character("Adelaide", callback=boopy_voice, cb_boopfile="bleep023.ogg")
define l = Character("LeeRoy", callback=boopy_voice, cb_boopfile="bleep011.ogg")
define o = Character("Ōe", callback=boopy_voice, cb_boopfile="bleep008.ogg")
define b = Character("Mr. Hollis", callback=boopy_voice, cb_boopfile="bleep017.ogg")
define c = Character("Chet", callback=boopy_voice, cb_boopfile="bleep014.ogg")
define t1 = Character("Teenager1", callback=boopy_voice, cb_boopfile="bleep005.ogg")
define t2 = Character("Teenager2", callback=boopy_voice, cb_boopfile="bleep026.ogg")
define e = Character("Earl", callback=boopy_voice, cb_boopfile="bleep030.ogg")
define mar = Character("Marcia")
define rip = Character("'Rips' Goldman")
define guard = Character("Guard")
define guy = Character("Guy")
define lady = Character("Lady")
define mat = Character("Matheson")
define lib = Character("Librarian")

# Backgrounds
image bg bedroom = im.Scale("images/bedroom_bg.png",1920,1080)
image bg diner = im.Scale("images/diner_bg.png",1920,1080)
image bg office = im.Scale("images/office_bg.png",1920,1080)
image bg library = im.Scale("images/library_bg.png",1920,1080)

# Sprites
image M main="mc_main.png"
image M annoyed="mc_annoyed.png"
image M angry="mc_angry.png"
image M melancholy="mc_melancholy.png"
image M disgusted="mc_disgusted.png"
image M smile="mc_smile.png"
image A main="adelaide_main.png"
image A happy="adelaide_happy.png"
image A shy="adelaide_shy.png"
image A evil="adelaide_evil.png"
image L main="leeroy_main.png"
image L sigh="leeroy_sigh.png"
image L shrug="leeroy_shrug.png"
image L blush="leeroy_blush.png"
image L confused="leeroy_confused.png"
image O main="oe_main.png"
image O smile="oe_smile.png"
image O solemn="oe_solemn.png"
image O excited="oe_excited.png"

# The game starts here.

label start:
    camera:
        perspective True

window hide
$ quick_menu = False

play music "intro.ogg"
image woman = Movie(size=(1920, 1080), channel="movie_dp", play="images/woman.webm")
image house = Movie(size=(1920, 1080), channel="movie_dp", play="images/house.webm")
image street = Movie(size=(1920, 1080), channel="movie_dp", play="images/street.webm")
image horse = Movie(size=(1920, 1080), channel="movie_dp", play="images/horse.webm")

window hide
$ quick_menu = False
show house
show fairyfaybug with easeinright
pause 1.0
show game with easeinright
pause 1.0
show spooktober with easeinright
pause 2.0
hide game with easeoutright
hide spooktober with easeoutleft
hide fairyfaybug with easeoutleft
hide house
show woman
pause 1.0
show writers with easeinleft
pause 1.0
show jason with easeinleft
show arvantus with easeinleft
show endy with easeinleft
pause 2.0
hide jason with easeoutleft
hide arvantus with easeoutleft
hide endy with easeoutleft
hide writers
hide woman
show street
pause 1.0
show artists with easeintop
show art_names with easeinbottom
pause 2.0
hide art_names with easeoutbottom
hide artists with easeouttop
hide street
show horse
pause 1.0
show programmers with easeinleft
show music with easeinright
show pro_names with easeinleft
show dael with easeinright
pause 1.0
hide programmers
hide music
hide pro_names
hide dael
hide horse
window show
$ quick_menu = True
"VESPER FALLS, OHIO - SEPTEMBER 1962"
stop music
play sound "phone.ogg"
"A telephone rings. The shrill sound tears through the silence."
play music "retro.ogg"
scene bg bedroom
show M annoyed:
    xpos 0.0
    yalign 1.0
    zoom 0.35
"I bolt upright."
"The room smells of stale coffee and aerosol hairspray, and as far as my eye can see, it's in a state of chaotic disarray."
"Outside my window, dead in the daylight, the diner downstairs is already bleeding its aggressive neon sign through the curtains:"
"THE SUPERMORGUEDROID WEEPIE."
    
camera:
    subpixel True zoom 1.32 
show bg bedroom:
    subpixel True xzoom 1.0 
    pos (0.5, 1.06) zoom 1.47 
    linear 0.54 pos (0.5, 1.0) zoom 1.0 
show M annoyed:
    subpixel True 
    parallel:
        xpos 0.06 
        linear 0.54 xpos 0.08 
    parallel:
        ypos 1.06 xzoom 1.0 zoom 0.45 
        linear 0.17 ypos 1.11 xzoom 1.0 zoom 0.49 
        linear 0.37 ypos 0.94 xzoom 1.0 zoom 0.38 
    parallel:
        zrotate 0.0 orientation (0.0, 0.0, 0.0) 
        linear 0.17 zrotate 0.0 orientation (0.0, 0.0, 0.0) 
    parallel:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.17 matrixtransform ScaleMatrix(1.04, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.37 matrixtransform ScaleMatrix(0.92, 1.03, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.08 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.72)
show bg bedroom:
    pos (0.5, 1.0) zoom 1.0 
show M annoyed:
    pos (0.08, 0.94) zrotate 0.0 orientation (0.0, 0.0, 0.0) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) xzoom 1.0 zoom 0.38 


"I swing my legs out of bed and immediately trip."



show M annoyed:
    subpixel True xzoom 1.0 yzoom 1.0 zoom 0.38 alpha 1.0 blur 0.0 
    pos (0.08, 0.94) 
    linear 0.42 pos (0.2, 1.07) 
with Pause(0.52)
show M annoyed:
    pos (0.2, 1.07) 




camera:
    subpixel True 
    zoom 1.32 
    linear 0.18 zoom 1.0 
show M annoyed:
    subpixel True 
    pos (0.08, 0.94) 
    linear 0.18 pos (0.16, 1.0) 
with Pause(0.28)    
camera:
    zoom 1.0 
show M annoyed:
    pos (0.16, 1.0) 
"My foot catches on a pile of thrifted clothes I tossed onto the scorch mark on the carpet."

show M annoyed:
    pos (0.16, 1.0) 

show M annoyed:
    subpixel True 
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.58 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.68)
show M annoyed:
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

show M annoyed:
    subpixel True 
    xpos 0.16 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.44 xpos 0.32 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.54)
show M annoyed:
    xpos 0.32 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 


with hpunch
"I stumble forward, barely catching my balance."
"I weave through the room, passing a hissing radiator and orange crates stacked high with my prized rock-and-roll vinyls."
play sound "phone.ogg"
"I pass the kitchen table, the current domain of my sewing machine."

show M annoyed:
    subpixel True
    parallel:
        xpos 0.16 
        linear 0.50 xpos 0.51 
    parallel:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.23 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.60)
show M annoyed:
    xpos 0.51 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 



"There's a half-finished hem pinned down that I've been telling myself to stitch since last week."
"On the windowsill, my secondhand Royal Quiet De Luxe typewriter sits poised with a blank page."
show M melancholy:
    subpixel True pos (0.46, 1600) zoom 0.65 
show M melancholy:
    subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with dissolve

"Waiting for me to finish up my next grandiose story that will finally hit the mark. Surely."
"A stray sock lies abandoned on the floorboards."
play sound "phone.ogg"

show M melancholy:
    subpixel True 
    pos (0.46, 1600) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) zoom 0.65 
    linear 0.51 pos (0.12, 1200) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) zoom 0.46 
with Pause(0.61)
show M melancholy:
    pos (0.12, 1200) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) zoom 0.46 

"I snatch it up without breaking stride, tossing it aside as I lunge for the heavy rotary phone."

show M main:
    xpos -0.05
    yalign 1.0
    zoom 0.455

show M main:
    subpixel True pos (0.01, 1.42) zoom 0.72 
with dissolve
stop sound
play sound "pickup.ogg"
m "Courier, Kessler - ah, I mean. Hello, Dorothy speaking."
b "Dorothy."
"His voice is unhurried. Almost too calm. My jaw clenches tight."
with hpunch
camera:
    subpixel True 
    pos (0, 0) yzoom 1.0 zoom 1.0 
    linear 0.55 pos (163, 81) yzoom 1.0 zoom 1.25 
show M annoyed:
    subpixel True pos (0.12, 1.2) zoom 0.5
with Pause(0.65)
camera:
    pos (163, 81) yzoom 1.0 zoom 1.25 


m "M-Mr. Hollis."
b "I'm giving Chet the Glenn piece."
show M melancholy
m "T-The… I pitched that. Multiple times. A-And I already have the Mercury press packet, a source at Lewis-"
b "Dorothy."
camera:
    subpixel True 
    pos (163, 81) zoom 1.25 
    linear 0.25 pos (0, 0) zoom 1.0 
with Pause(0.35)
camera:
    pos (0, 0) zoom 1.0 
"There's a pause."
b "Dolly. I've already made up my mind."
camera:
    subpixel True pos (0, 0) zoom 1.0 
    xzoom 1.0 
    linear 0.08 xzoom 1.0 
show M annoyed:
    subpixel True 
    xzoom 1.0 yzoom 1.0 
    linear 0.08 xzoom 0.92 yzoom 1.12 
    linear 0.10 xzoom 1.0 yzoom 1.0 
with Pause(0.5)
camera:
    xzoom 1.0 
show M annoyed:
    xzoom 1.0 yzoom 1.0 
"I flinch at the pet name."
show M disgusted:
    zoom 0.45
with dissolve 
m "With all due respect, Chet spells orbit with two t's."
b "Your hatred toward that man is getting old."
m "I refuse to write any more columns for the women's page."
"The man on the other line lets out an exhausted sigh."
b "You want to play a journalist? Be my guest. I'm giving you a month."
b "Bring me something worthy of being put on the front page. A story that can sell."
b "And then we can talk about moving you off the women's page."
show M melancholy with dissolve
m "And if I fail?"
b "You'll write about every wedding, yard sale, and Garden Club, and you'll stop being a nuisance about it."
show M annoyed:
    subpixel True 
    xpos 0.16 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.24 xpos 0.33 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.34)
"Click. The line goes dead."
show M annoyed:
    subpixel True 
    pos (0.33, 1.5) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) zoom 0.63 
    linear 0.66 pos (0.16, 1.0) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) zoom 0.38 
with Pause(0.76)
show M annoyed:
    pos (0.16, 1.0) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) zoom 0.38 
"I stand there, my hand clutching the receiver. The dial tone hums against my ear."
show M angry:
    subpixel True xpos 0.16 ypos 1.0
    parallel:
        xzoom 1.0 yzoom 1.0 
        linear 0.10 xzoom 0.8 yzoom 1.2 
        linear 0.10 xzoom 1.0 yzoom 1.0 
    parallel:
        zoom 0.35 
        linear 0.10 zoom 0.35
with Pause(0.30)
show M angry:
    xzoom 1.0 yzoom 1.0 zoom 0.35 

with hpunch 
m "The nerve of that man! I have filed at least A HUNDRED pieces, and only one of them had to have a correction."
m "So what if it happened to be the most important one?!"
m "For the love of god, Chet put a DEAD woman's name on a wedding announcement in June, and nobody said as much as boo-"
with hpunch
"I slam the receiver back onto the cradle. All the fight drains out of me, exchanged for existential dread."
show M main:
    xpos 0.12
    yalign 1.0
    zoom 0.455
with dissolve
"I force my face into the tight smile aimed at precisely no one. I've been using it far too often lately."
m "You want a story? Fine. I'll give you one."
menu:
    "Call my Friend":
        "I pick up the receiver. My fingers dial the all-too-familiar number."
        
        camera:
            subpixel True 
            zoom 1.0 
            linear 0.24 zoom 1.15 
        with Pause(0.34)
        camera:
            zoom 1.15 

        "It rings and rings. She doesn't pick up."

        camera:
            subpixel True 
            zoom 1.15 
            linear 0.28 zoom 1.0 
        with Pause(0.38)
        camera:
            zoom 1.0 

        "I put the phone back down."
        show M annoyed:
            xpos 0.12
            yalign 1.0
            zoom 0.35
        with dissolve
        m "Must be at the shop already."
        
        show M main:
            subpixel True zoom 0.45
            xpos 0.12 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
            easein 1.16 xpos 0.42 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
            easeout 1.08 xpos 0.42 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
            easein 1.23 xpos 0.12 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        with Pause(3.57)
        show M main:
            xpos 0.12 zoom 0.45 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

        "Unwilling to do any real writing, I decide to clean up my room — at least a little."
    "Get to Work":

        show M main:
            subpixel True 
            pos (0.12, 1.0) zoom 0.455 
            linear 0.61 pos (0.28, 1.2) zoom 0.63 
        with Pause(0.71)
        show M main:
            pos (0.28, 1.2) zoom 0.63 

        "I stretch, adjust the pencil in my hair, and sit down at my typewriter."
        "I commit to writing about the upcoming celebration that's to take place in the square."
        
        show M melancholy:
            subpixel True zoom 0.46 
        with dissolve


        "Why is this city so obsessed with corn?"

show M melancholy:
    subpixel True zoom 0.46
    pos (0.28, 1.2)
with dissolve

"I collapse backwards onto the mattress, the worn springs groaning in protest."
"In my hand is yesterday's edition of the Vesper Falls Courier."
"I read — no, I consume the text, chewing through the column the way other people chew their overcooked bacon."
"I snap the broadsheet open, the scent of black ink briefly cutting through the stale air of my apartment."
"Perhaps I should open the windows. Later."

show M annoyed:
    subpixel True zoom 0.46 
with dissolve

"And there it is. Glaring at me, sprawled a ridiculous four columns wide."
"NEW EATERY OPENS ON ROUTE NINE - THE SUPERMORGUEDROID WEEPIE!" 
"PROMISES ROLLER SERVICE, OPEN LATE HOURS!"
"I stare at the headline for a long, agonising moment."
"The bold typeface seems set on making my brain hurt."
m "… such riveting news."
"I flip the page. The crisp paper crinkles as I turn it back."
"I trace the letters with my nail, just to confirm I’m not hallucinating."
m "All it apparently takes is slapping skates on teenage girls, and you're ready for the front page of a newspaper. Ugh."
"I flip over to page four, glaring at a tiny column tucked next to a sprawling advertisement for a Hoover vacuum cleaner."
show M melancholy with dissolve
"It promises to clean all my worries!"
m "First American to orbit the Earth."
"I chew my lip."
show M annoyed with dissolve
m "Three times around and then made a safe landing. And they reduced his latest speech to a… footnote."
"A thought crosses my mind."
show M melancholy with dissolve
m "I wonder if it's because he chose Florida."
"I let my head fall back against the mattress, staring up at the water-stained ceiling —"
"— which is, practically speaking, a very good analogy to the current state of my life."
m "Overshadowed by a diner..."
"I lift the paper again."
show M annoyed
"My eyes keep snagging on that absurd, borderline-offensive string of letters."
"It makes my editorial senses itch."
m "The Supermurgitroid Weepie…"
"I try sounding it out."
m "The Super-morgue-droid. Weepie."
m "It's not even spelled correctly. How charming."
"I lower the newspaper, squinting at the red neon light currently invading my personal space with an eyestraining glow."
m "Who looked at that name and said yes?"
with hpunch
"Upset, I toss the Courier aside."
"It hits the edge of the blanket and slides off, hitting the floorboards with a sad, dull thwack."
"I leave it there for precisely two seconds before I rethink my actions."

show M annoyed:
    subpixel True 
    pos (0.34, 1.1) zoom 0.46
    linear 0.37 pos (0.16, 1.0) zoom 0.35 
with Pause(0.47)
show M annoyed:
    pos (0.16, 1.0) zoom 0.35 

"Then, I groan, lean precariously over the edge of the bed, and retrieve it."
"Because no matter how furious I am at the world, I simply cannot leave a newspaper on the floor."
#Scene 2 Dorothys Apartment - Afternoon
show M main:
    xpos 0.12
    yalign 1.0
    zoom 0.455
"The afternoon sun bakes the cramped room, casting long, mocking shadows across the floorboards."

show M annoyed:
    subpixel True 
    zoom 0.35
    xpos 0.16 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.42 xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.52)
show M annoyed:
    xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

"I pace. Three fast steps across the rug. Pivot. Three steps back."
"I gnaw on the edge of an already-ruined thumbnail, my eyes constantly darting back to the typewriter."
"The floor is currently a graveyard for six violently crumpled balls of paper."
"In the carriage of the secondhand Royal, the seventh page sits waiting. Sadly, it did not magically fill itself while I was pacing around."
"I start thinking out loud, my voice bouncing off the peeling wallpaper."

show M annoyed:
    subpixel True 
    xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.47 xpos 0.16 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.57)
show M annoyed:
    xpos 0.16 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

"Talking out loud helps me sort my thoughts faster."

show M melancholy:
    subpixel True 
    ypos 1.0 zoom 0.35 
    easein 0.38 ypos 1.2 zoom 0.5 
with Pause(0.48)
show M melancholy:
    ypos 1.2 zoom 0.5 

m "Okay. Dorothy, think. Think. What was the last rumour floating around?"
m "Right, the farmers' auction. Every town has dirty money. Somebody is definitely crooked..."
m "... but I don't know the first thing about livestock. They wouldn't trust a woman either."
"Three steps. Pivot. I keep pacing."

show M melancholy:
    subpixel True 
    parallel:
        xpos 0.16000000000000003 
        easeout 0.20 xpos 0.16000000000000003 
        easeout 0.50 xpos 0.5 
    parallel:
        ypos 1.2 zoom 0.5 
        linear 0.20 ypos 1.0 zoom 0.35 
    parallel:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.70 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.30 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(1.10)
show M melancholy:
    pos (0.5, 1.0) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) zoom 0.35 

m "A story on the mayor? No."
m "Everyone knows Mayor Lindqvist cries at parades like his life depends on it. That's not news."

show M annoyed:
    subpixel True 
    xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.51 xpos 0.16 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.61)
show M annoyed:
    xpos 0.16 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

"I pull the steno pencil from my hair, twirling it furiously through my fingers."
m "The machine plant. The line workers have been causing trouble at the tavern lately."
m "Maybe there’s a strike brewing. Dad works the floor; he'd definitely know something..."
"I let out a hollow, humourless laugh, gesturing wildly at the empty room with my pencil."
m "Except he’d rather take a bullet than snitch on a soul."

show M main:
    subpixel True xpos 0.12 zoom 0.46
with dissolve

"I force myself to stand perfectly still."
"The sheer desperation is starting to leak into my voice, and I absolutely hate the sound of it."

camera:
    subpixel True 
    zoom 1.0 
    linear 0.45 zoom 1.2 
with Pause(0.55)
camera:
    zoom 1.2 

m "I have one month. That's plenty of time! I don't have to figure it all out today."
with hpunch
"And then, right beneath my feet, the floorboards vibrate."
"An argument is breaking out downstairs in the diner."
"It’s muffled by the wood and plaster, but the furious cadence is unmistakable."
"Two distinct voices, rapidly escalating in volume."
show M annoyed:
    xpos 0.16
    yalign 1.0
    zoom 0.35
"I glare down at the floor."

camera:
    subpixel True 
    zoom 1.2 
    linear 0.20 zoom 1.0 
with Pause(0.30)
camera:
    zoom 1.0 

"Instantly, the tight, suffocating knot of anxiety in my chest hardens into a sharp spike of righteous fury."
m "I cannot WORK in this ruckus."
"Downstairs, the shouting spikes."
with hpunch
"A second later, a massive CLANG echoes through the floor as something large and metallic violently crashes over."
"By the time the noise stops, I am already reaching for my shoes."
# Scene 3. The Supermurgidroid Weepie - Evening
scene black with fade
scene bg diner with fade 
show M angry:
    xpos 0.16
    yalign 1.0
    zoom 0.35
show cg
camera:
    subpixel True pos (1440, 351) zoom 1.88 
with hpunch
play sound "door_slamming.ogg"
"I push through the heavy doors at a brisk pace, my winter coat thrown hastily over my nightgown."

camera:
    subpixel True 
    parallel:
        pos (1440, 351) 
        linear 0.69 pos (1278, 297) 
    parallel:
        zoom 1.88 
        linear 0.68 zoom 1.74 
with Pause(0.79)
camera:
    pos (1278, 297) zoom 1.74 

"I still have a steno pencil tucked in my hair."

camera:
    subpixel True 
    pos (1278, 297) zoom 1.74 
    linear 0.50 pos (1170, 279) zoom 1.67 
with Pause(0.60)
camera:
    pos (1170, 279) zoom 1.67 



"I am entirely, resolutely prepared to interrupt somebody's evening."
camera:
    subpixel True 
    pos (1170, 279) zoom 1.67 
    linear 0.57 pos (675, 243) zoom 1.56 
with Pause(0.67)
camera:
    pos (675, 243) zoom 1.56 
"There are two milkshakes on the counter."

camera:
    subpixel True 
    pos (675, 243) zoom 1.56 
    linear 0.41 pos (0, 0) zoom 1.0 
with Pause(0.51)
camera:
    pos (0, 0) zoom 1.0 


"Sitting next to them is the duo responsible."
hide M angry

#show A main:
    #subpixel True xpos 0.22 zoom 0.55
#show L sigh:
    #subpixel True xpos 0.6 ypos 0.1 zoom 0.5

"LEEROY looks to be in his early twenties."

camera:
    subpixel True 
    xpos 0 zoom 1.0 
    linear 0.37 xpos 0 zoom 1.21 
with Pause(0.47)
camera:
    xpos 0 zoom 1.21 
    
"He wears his locs in a ponytail and a bright shirt with flowers on it."
"Before I have the chance to assess his appearance further, he gestures animatedly with a long metal spoon."
"Beside him is ADELAIDE."

camera:
    subpixel True 
    xpos 0 
    linear 0.37 xpos 207 
with Pause(0.47)
camera:
    xpos 207 


"She looks late twenties, immaculate, and is wearing expensive, sharp-heeled shoes."
"She was supposedly the waitress, but there wasn't an apron in sight."
"Her lips are curled in a tight pout."

#show L sigh:
    #subpixel True xpos 0.6 
    #ypos 0.1 
    #linear 0.07 ypos 0.05 
    #linear 0.07 ypos 0.1 
#with Pause(0.24)
#show L sigh:
    #pos (0.6, 0.1) 

l "- it's about balance, Adelaide. You can't just put cold things in a cup and call it a beverage-"

#show A main:
    #subpixel True xpos 0.22 
    #ypos 0.0 
    #linear 0.06 ypos -0.05 
    #linear 0.05 ypos 0.0 
#with Pause(0.21)
#show A main:
    #pos (0.22, 0.0) 

a "I followed the card."

#show L sigh:
    #subpixel True xpos 0.6 
    #ypos 0.1 
    #linear 0.07 ypos 0.05 
    #linear 0.07 ypos 0.1 
#with Pause(0.24)
#show L sigh:
    #pos (0.6, 0.1) 

l "Like a hostage."


hide L sigh
hide A main

"I march right up to the chrome counter."
hide cg
with hpunch
show M angry:
    xpos 0.16
    yalign 1.0
    zoom 0.35
m "It is twenty past nine. I am trying to sleep and I can hear E V E R Y  S I N G L E-"

hide M angry
show A main:
    xpos 0.22
    ypos 0.0
    zoom 0.55
show L main:
    xpos 0.45
    ypos 0.1
    zoom 0.5

show A main:
    subpixel True 
    xpos 0.22 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.19 xpos 0.12 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
show L main:
    subpixel True 
    xpos 0.45 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.19 xpos 0.45 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.29)
show A main:
    xpos 0.12 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
show L main:
    xpos 0.45 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

"I stop. Both of them have turned to look at me."

"They do not look guilty. Nor do they look annoyed that I barged into their conversation."
"The man looks at me with sheer, unadulterated delight."

show L main:
    subpixel True xpos 0.45
    ypos 0.1 
    linear 0.07 ypos 0.05 
    linear 0.07 ypos 0.1 
with Pause(0.24)
show L main:
    pos (0.45, 0.1) 

l "A customer!"

show A main:
    subpixel True xpos 0.12
    ypos 0.1 
    linear 0.07 ypos 0.0
    linear 0.07 ypos -0.05
with Pause(0.24)
show A main:
    pos (0.12, 0.0) 

a "She's not a customer, Leeroy. She's the upstairs."

show L main:
    subpixel True xpos 0.45
    ypos 0.1 
    linear 0.07 ypos 0.05 
    linear 0.07 ypos 0.1 
with Pause(0.24)
show L main:
    pos (0.45, 0.1) 

l "But she can be the judge!"

hide A main
hide L main
show M annoyed:
    subpixel True xpos 0.12 zoom 0.35
    ypos 0.2
    linear 0.07 ypos 0.1
    linear 0.07 ypos 0.2
with Pause(0.24)
show M annoyed:
    pos (0.12, 0.2) 

m "I beg your-"

show L main:
    subpixel True zoom 0.5
    xpos 0.45 ypos 81
    linear 0.28 xpos 0.25 
with Pause(0.38)
show L main:
    subpixel True ypos 81 zoom 0.5 

"He's already sliding both glasses towards me."

show L main:
    subpixel True xpos 0.25
    ypos 0.1 
    linear 0.07 ypos 0.05 
    linear 0.07 ypos 0.1 
with Pause(0.24)
show L main:
    pos (0.25, 0.1) 

l "Help us determine which milkshake is better."

hide M annoyed
show A main:
    subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)
show A main:
    subpixel True xpos 0.5 zoom 0.55
    ypos 0.1 
    linear 0.07 ypos 0.0
    linear 0.07 ypos -0.05
with Pause(0.24)
show A main:
    pos (0.5, 0.0) 

a "Leeroy, why are you dragging her into-."

hide L main
hide A main
show M annoyed:
    xpos 0.12
    yalign 1.0
    zoom 0.35

"I look at the milkshakes. I look at the door I just came through. I look back at the milkshakes."
"I strongly dislike milkshakes."
"I think of them as dessert pretending to be a drink, and I consider anyone who orders them to be, well, children."
"But I am exhausted, and I just want the bickering to stop."

show M annoyed:
    subpixel True xpos 0.12 zoom 0.35
    ypos 1.0
    linear 0.07 ypos 1.05
    linear 0.07 ypos 1.0
with Pause(0.24)
show M annoyed:
    pos (0.12, 1.0) 
    
m "Fine. Fine! Just because I want to sleep this century,"

show M annoyed:
    subpixel True 
    pos (0.12, 1.0) zoom 0.35 
    linear 0.19 pos (0.35, 1.0) zoom 0.35 
with Pause(0.32)
show M annoyed:
    pos (0.35, 1.0) zoom 0.35 

camera:
    subpixel True 
    pos (0, 0) zoom 1.0 
    easein 0.20 pos (475, 51) zoom 1.25 
with Pause(0.30)
camera:
    pos (475, 51) zoom 1.25 

"I say, sitting on a stool."
"I take LeeRoy's glass. I take a reluctant sip."
show M melancholy
"It is genuinely not bad. Not great either, but it's not like I'm an expert on the things I dislike."

show M annoyed:
    subpixel True xpos 0.35 zoom 0.35
    ypos 1.0
    linear 0.07 ypos 1.05
    linear 0.07 ypos 1.0
with Pause(0.24)
show M annoyed:
    pos (0.35, 1.0) 

m "Hm."

show L main:
    subpixel True xpos 0.45 zoom 0.5
    ypos 0.07
    linear 0.07 ypos 0.02
    linear 0.07 ypos 0.07
with Pause(0.24)
show L main:
    pos (0.45, 0.07) 

l "You see? That's the ratio right there. Four parts to one."

show L main:
    subpixel True xpos 0.45 zoom 0.5
    ypos 0.07
    linear 0.07 ypos 0.02
    linear 0.07 ypos 0.07
with Pause(0.24)
show L main:
    pos (0.45, 0.07) 

l "You get the cold hitting you up front, and then it comes back around on you, sweet at the back, like a-"
"He delivers this entire speech with total, sweeping conviction."

show M melancholy:
    xpos 0.35 zoom 0.35

"But it sounds off. Has he been rehearsing it?"
"It sounds far too polished, like words you'd find in a novel rather than spoken."

show M annoyed:
    xpos 0.35 zoom 0.35

show M annoyed:
    subpixel True xpos 0.35 zoom 0.35
    ypos 1.0
    linear 0.07 ypos 1.05
    linear 0.07 ypos 1.0
with Pause(0.24)
show M annoyed:
    pos (0.35, 1.0) 

m "It's fine. An… average milkshake."

hide L main
show A main:
    xpos 0.5
    zoom 0.55

"I reach for Adelaide's glass. I take a sip."
with hpunch
"I freeze as my taste buds are deeply shocked — my entire face scrunches up."
"My soul takes a brief vacation."
"I pull the glass away from my mouth and set it back on the counter very, very slowly as I struggle to keep a neutral face."

show M disgusted:
    subpixel True xpos 0.35 zoom 0.45
    yalign 1.0
    linear 0.07 ypos 1.05
    linear 0.07 ypos 1.0
with Pause(0.24)
show M disgusted:
    pos (0.35, 1.0) 

m "What is in that?"

show A main:
    subpixel True xpos 0.5 zoom 0.55
    ypos 0.0
    linear 0.07 ypos -0.05
    linear 0.07 ypos 0.0
with Pause(0.24)
show A main:
    pos (0.5, 0.0) 

a "Strawberries. Milk. Ice."

show M disgusted:
    subpixel True xpos 0.35 zoom 0.45
    ypos 1.0
    linear 0.07 ypos 1.05
    linear 0.07 ypos 1.0
with Pause(0.24)
show M disgusted:
    pos (0.35, 1.0) 

m "There's something else."

show A evil:
    subpixel True pos (0.62, 0.05) zoom 0.39 
with dissolve

a "Salt."

show M disgusted:
    subpixel True xpos 0.35 zoom 0.45
    ypos 1.0
    linear 0.07 ypos 1.05
    linear 0.07 ypos 1.0
with Pause(0.24)
show M disgusted:
    pos (0.35, 1.0) 

m "How… much salt?"

show A main:
    subpixel True xpos 0.5 zoom 0.55
    ypos 0.0
    linear 0.07 ypos -0.05
    linear 0.07 ypos 0.0
with Pause(0.24)
show A main:
    pos (0.5, 0.0) 

a "The card said a pinch."

show M annoyed:
    subpixel True xpos 0.35 zoom 0.35
    ypos 1.0
    linear 0.07 ypos 1.05
    linear 0.07 ypos 1.0
with Pause(0.24)
show M annoyed:
    pos (0.35, 1.0) 

m "And… how much did you use?"

show A main:
    subpixel True xpos 0.5 zoom 0.55
    yalign 1.0
    linear 0.07 ypos 0.98
    linear 0.07 ypos 1.0
with Pause(0.24)
show A main:
    pos (0.5, 1.0) 

a "A pinch. I don't know how much a pinch is. I used what I could pick up."

show O main:
    xpos 0.03 ypos 81 zoom 0.5
with easeinleft

"A long pause. I stare at her perfectly manicured hands."

show M annoyed:
    subpixel True xpos 0.35 zoom 0.35
    ypos 1.0
    linear 0.07 ypos 1.05
    linear 0.07 ypos 1.0
with Pause(0.24)
show M annoyed:
    pos (0.35, 1.0) 

m "Have you tasted it?"

show A main:
    subpixel True xpos 0.5 zoom 0.55
    ypos 0.0
    linear 0.07 ypos -0.05
    linear 0.07 ypos 0.0
with Pause(0.24)
show A main:
    pos (0.5, 0.0) 

a "I'm not feeling like drinking dairy."

hide M annoyed
hide A main
hide O main

"And then, from directly behind them, a voice speaks from the shadows at the end of the counter."


o "She is right about the salt."
with hpunch

show M annoyed:
    subpixel True ypos 0.18 xzoom 1.0 yzoom 1.0 zoom 0.35
    parallel:
        xpos 0.35 
        linear 0.59 xpos 0.5 
    parallel:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.21 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.38 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.69)
show M annoyed:
    pos (0.5, 0.18) matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

"I flinch and spin around."

show O main:
    xpos 0.03
    ypos 81
    zoom 0.5

"Another person has been standing there the entire scene. In the dark. Perfectly, impossibly still."
"They are holding a broom in one hand, but they hold it gracefully like a butler rather than a cleaner."
"They do not blink. They do not shift their weight as they address me."
"They haven't moved a single muscle since before I walked in, and I am only now, startlingly, aware that they were there at all."

show M annoyed:
    subpixel True xpos 0.5 zoom 0.35
    ypos 0.18
    linear 0.07 ypos 0.13
    linear 0.07 ypos 0.18
with Pause(0.24)
show M annoyed:
    pos (0.5, 0.18) 

m "How long have you been sta-"

show O main:
    subpixel True 
    xpos 0.03 
    linear 0.16 xpos 0.08 
with Pause(0.26)
show O main:
    xpos 0.08 

o "Yes."

show M annoyed:
    subpixel True xpos 0.5 zoom 0.35
    ypos 0.18
    linear 0.07 ypos 0.13
    linear 0.07 ypos 0.18
with Pause(0.24)
show M annoyed:
    pos (0.5, 0.18) 

m "That's not... that isn't an answer to that question."
show O solemn with dissolve
"Ōe considers this. Seriously."
"As though regular social interaction is a puzzle they haven't quite solved yet."
"They do not produce a second answer."
hide O main
menu:
    "Give them the whole lecture.":
        "I cross my arms and deliver my unexpected food criticism."
        "It's pointed, it's witty, and I humble them both to the core."
        "How dare they disturb my peace and then serve such an unfortunate milkshake to me!"
        "I pay good money for this room, and as landlords they're certainly not delivering."
    "Ask what they were actually arguing about.":

        show M annoyed:
            subpixel True 
            parallel:
                xpos 0.5 
                linear 0.22 xpos 0.35 
            parallel:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
                linear 0.09 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
                linear 0.13 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        with Pause(0.32)
        show M annoyed:
            xpos 0.35 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

        "The frustration seeps out of me."

        show L sigh:
            xpos 0.6 ypos 81
            zoom 0.5

        "I ask, and LeeRoy admits, deflated, that nobody has come in since they opened."
        l "Well, they did the first time, but for some reason customers are not returning."

        hide M annoyed
        show A main:
            subpixel True xpos 0.2 zoom 0.55
            ypos -0.02
            linear 0.07 ypos -0.05
            linear 0.07 ypos -0.02
        with Pause(0.24)
        show A main:
            pos (0.2, -0.02)

        "Adelaide looks away and says, quietly,"
        a "He wanted tonight to go well."
        # [LISTEN +1]
hide A main

"Either way, I end up giving LeeRoy some practical advice—less syrup."
"Chill the glasses first."
"Under no circumstances let Adelaide near the salt shaker."
"Perhaps she should be banned from using salt altogether."


show L main:
    xpos 0.45
    ypos 0.07
    zoom 0.5

show M annoyed:
    subpixel True yalign 1.0 zoom 0.35
    xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.50 xpos 0.35 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.60)
show M annoyed:
    xpos 0.35 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 


"LeeRoy writes it all down."
"He has no pen and thus resorts to scribbling ink on his hand."
"I consider giving him one of my papers, but then again — he should have enough money to afford his own writing supplies."

show M annoyed:
    subpixel True xpos 0.35 zoom 0.35
    yalign 1.0
    linear 0.07 ypos 0.98
    linear 0.07 ypos 1.0
with Pause(0.24)
show M annoyed:
    pos (0.35, 1.0) 

m "Right. Wonderful. Delighted to help. Now if you'd be so kind, I'm intending to return to sleep."
hide L main

show M annoyed:
    subpixel True 
    xpos 0.5 yalign 1.0
    linear 0.19 xpos 0.2
with Pause(0.48)
show M annoyed:
    xpos 0.2

camera:
    subpixel True 
    pos (475, 51) zoom 1.25 
    linear 0.38 pos (1, 1) zoom 1.0 
with Pause(0.48)
camera:
    pos (1, 1) zoom 1.0 

"I stand up, pulling my coat tighter around my nightgown."
"I am halfway out the door when the voice stops me."

show O main:
    xpos 0.47
    yalign 1.0
    zoom 0.5

o "Miss Kessler."
"I freeze. I slowly turn around."
"I don't recall introducing myself to them."
"Then again, if they're affiliated with the landlord, it makes sense they would know of me."
o "Sleep well."
"A quiet silence spreads between us."

show M annoyed:
    subpixel True xpos 0.2 yalign 1.0 zoom 0.35
    yalign 1.0
    linear 0.07 ypos 0.98
    linear 0.07 ypos 1.0
with Pause(0.24)
show M annoyed:
    pos (0.2, 1.0) 

m "...thank you."
hide O main
"I push the door open and leave."
"It swings shut behind me, drowning out the rest of their conversation."
hide M annoyed

    # This ends the game.

jump mainroute2
