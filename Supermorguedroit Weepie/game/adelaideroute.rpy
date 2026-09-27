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
scene bg diner 
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
    yalign 1.0 zoom 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0 

m "But you can’t just cut my time in half! We had a deal! I don’t- I don’t even have a solid lead yet!"

hide M annoyed 

b "That sounds like a ‘you’ problem, Sweetheart. If you don’t have a knockout story by the new deadline, you will have to make-do and write for the woman's pages."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0 

m "Chief! I…"

hide M annoyed 

b "Now, I realize working under a real time-crunch is a tough beat…,"

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0 

m "Yeah."

hide M annoyed 

b "...and a bit of a raw deal…"

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0 

m "Mmmm."

hide M annoyed 

b "...and perhaps even agonizingly stressful.."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.4
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0 

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
    xpos 0.4 zoom 0.4 
    linear 0.30 xpos 0.6 zoom 0.35 
with Pause(0.40)
camera:
    zoom 1.0 
show M annoyed:
    xpos 0.6 zoom 0.35 
    
m "……………………………………."
"I stand there dumbfounded. Half as much time??"
m "Okay, stay calm. I just need to take a deep breath, and focus. And… breathe in. Breathe out…"
"I eye the back room door and hear the commotion on the other side escalating into a frenzy."
a "I DESPISE MOPS! I LOATHE GRIME! I. HATE. LEEROY. I HATE RUINING MY MANICURE! I HATE THAT FLARING BALL IN THE SKY! I HATE–"
"Panic taking over, I march over to the door and shove it open with a bang. The sudden noise startles Adelaide out of her wits."
"She whips around with a sharp hiss, her fangs bared in full force. For a split second, she looks ready to commit violence."
"Oh. It is just… you. Again."
"I am terribly sorry about your poor cleaning experience, but I need your help and it truly, earnestly cannot wait!"
a "As convincing as your obnoxious tone is, can you not see that I am currently occupied with something?"
m "I…what are you doing?"
a "Is it not obvious? Humiliating, grueling labor completely unfit for someone such as myself."
a "And yet, here I am. Slaving away."
a "Maybe this is revenge from the universe."
m "Where is everyone? Are you the only one here?"
a "Seeing as you had to not only rudely barge into this room, but also the restaurant as a whole, I would assume that it was obvious that yes, I am indeed the only person around."
m "It is quite a mess in here, are you sure you can clean up all of this by yourself?"
a "Thank you for noticing that this is indeed a mess too large for one to clean up. You may be wondering where those two other idiots are."
a "They're off into the sun where I can’t follow them. Those buffoons left me to clean up after their messes, as usual."
a "On the topic of messes, you look like one."
m "Thank you, I haven’t noticed."
a "No need to get snappy. Let’s go."
m "Let’s go where?"
a "Your room. The others will clean this up."
a "I’ll make sure of that."
"She drags me up to my room, where she pushes me on my bed and starts rummaging through my makeup."
m "What are you doing?"
a "The first step to feeling good is looking good."
"She starts reapplying some of my makeup. Her hands are surprisingly gentle as she holds my cheek to stabilize my face while applying my signature blue eyeliner."
a "Why are you getting so worked up about this anyways? What’s so wrong about writing for the women’s pages? You’re a woman after all."
m "You wouldn’t get it. It’s about honor! Dignity! A chance to finally leave this boring town behind!"
a "Alright, if it’s about dignity, why are you acting like a wet rag in front of your boss?"
a "It’s honestly pathetic to see you fold in front of him."
m "Well - you know -"
m "I’m scared of him. I guess."
a "Scared of him? Please. You come downstairs to yell at us every day but you’re scared of a lowly human?"
a "You do know LeeRoy could kill you without even trying."
m "LeeRoy wouldn’t hurt a fly -"
a "But he could! And I could as well!"
m "You’re not gonna hurt me."
a "You don’t know that."
m "If you attack me I’ll just run out into the sun."
a "You’re not being fair."
"She pokes me with the back of a makeup brush with a pout that’s almost cute."
m "Either way, my boss pays me and I need the money. I want to leave this city. And if I lose my job, well -"
m "I wouldn’t just lose that chance, I’d have to move back with my parents. And you understand why I wouldn’t wanna do that."
a "..."
m "You do understand it, right?"
a "Honestly, I don’t even think I remember my parents."
m "What?"
"I look at her. While my relationship with my parents wasn’t always sunshine and rainbows, they still mattered a lot to me. Forgetting them? Out of question."
a "I mean, that’s part of being a vampire. And my parents didn’t really raise me to begin with."
m "I don’t know if that’s insensitive to ask, but - When did you get turned?"
a "Hm? It’s fine, I guess."
a "I let myself get turned during the french revolution. We were nobles and I didn’t exactly want to die."
m "So you ran away from taking accountability?"
a "Oh come on, I wasn’t the sole perpetrator."
a "But yeah, I guess."
a "I’m not like you, you know."
m "What’s that supposed to mean?"
a "Well, I don’t go yelling at people when they disturb my sleep, I wasn’t even able to tell LeeRoy when I was upset with him."
a "And when I’m in the wrong, I just smile and insult someone to feel better."
m "Oh I do that too."
"Adelaide laughs and for once her smile seems genuine before it turns icy again."
a "You know, if you ever need that headline, I don’t mind killing someone for you."
m "I- no thanks. I can do this without murder, thank you very much."
a "Your loss, but don’t forget the offer stands."

#New Day
"Today’s Special: Blood of your enemies."
"I threw my newspaper collection on the floor."
m "How dare he?! That stuck-up, smirking Asshole!"
m "I’m gonna DO SOMETHING TO HIM!"
"I stick even more pins in Chet's picture on my pinboard, a habit whenever I feel angry at him."
a "You alright?"
"I look up from angrily blacking out some of his articles when I saw Adelaide has invited herself in."
m "Get lost."
a "I heard you yell. What happened? Couldn’t find a headline?"
m "Oh no, I DID find a headline!"
"I stand up and come closer to her, fuming."
m "My boss gave it to Chet. Again. Even though it was MY story. MY LEADS."
a "Doesn’t seem like he was planning on giving you a chance to begin with."
m "Doesn’t seem so."
"I sigh, staring at the mess of newspapers. Somewhere there was my life’s work."
"This hemline will make you look ten years younger! Try this tea to calm your nerves if your husband comes home too late every night! Five recipes to lose even more weight!"
"Was this all I was? All I would ever be? At this point, I didn’t know anymore."
a "You should stand up to him."
m "Hm?"
a "It’s getting dark anyways. I’ll come with you."
m "And what am I supposed to tell him? That he’s a sexist bastard that can go put his slimy smirk up his own ass?"
a "That would be one option, yes."
"I can see a tiny glimmer of amusement in her eyes at my choice of words."
m "Well, as much as I’d love to do that, I don’t want to lose the job."
a "You can work for the diner. You’ve been practically doing that anyways."
m "The diner that’s barely functioning? Are you sure it can afford another staff member?"
a "It couldn’t afford the first staff member."
a "But I always can."
"She winks at me and takes my hand."
a "You deserve better than this. So come on. Let’s go!"
#Office Outside
"We rushed to the Office to catch the Boss before he left the building."
b "Now, what are you doing here, Sweetheart? Ready to give up?"
"The old man let’s his gaze wander over Adelaide and grins, showing off his gold tooth."
b "My, and who is this doll? Did you bring me a hooker as an apology?"
"I stare at him. I feel my blood boil. I was done with this. Humiliating me was one thing - but this crossed everything."
m "How Dare you? Who do you think you are to treat other humans like that?"
m "Do you think you can just say and do whatever you want with no consequences? Do you think you’ll get away with treating me like trash?"
"The boss laughs and gets out a cigar, about to light it. I snatch it away from him and throw it on the ground."
b "Naw, the little girl is mad… You’ll have to pay for that one."
m "The only one paying will be you!"
"I quickly saw surprise flash in his eyes as I lunged on him and we fell to the ground."
"I threw punch after punch, ignoring the cracking noises his bones were making under my hands."
"Adelaide stood at the side, a bit surprised, but even more so intrigued."
"After a few solid minutes I finally stood back up, out of breath."
m "You can take his blood if you want."
a "Take his blood? Please, I don’t want to touch that with a five foot pole."
m "..."
a "We should leave. People are gonna be here soon."
"She grabs my hand and practically pulls me back to the diner. I just stare at the floor as I follow her. My hands are full of his blood."
#Diner
l "Yo, Where were you? What happened?"
a "No time to explain, we’re moving."
o "Again? Where to this time?"
a "New York."
"I finally looked up."
m "New York?"
a "Of course. And as promised, you’ll come with us. You wanted to go to the city, no?"
m "W- well, yes. Not this way, but -"
a "Life doesn’t always turn out the way you want it to."
l "New York it is. But you better have a good reason for this."
"He already starts packing up stuff."
a "Oh trust me, we have a damn good reason."

return