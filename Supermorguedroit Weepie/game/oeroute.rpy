



label oe:
scene bg office
with fade
camera:
    subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 

# MC is fuming/annoyed
# If Marcia isn't a character drawing or sketch then a silhouette is fine

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.16
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "And then…! And then…! He said if I didn't get a real story soon, I'd be in the women's section!"

hide M annoyed 

mar "Gee, I mean, there's nothing wrong with the women's section, Dorothy…"

"Marcia wrote the household tips column and answered letters from housewives about etiquette and recipes."

"She had been sweet to me ever since I was hired - she was always sweet to everyone."

"It drove me nuts that she didn't see how limiting it was compared to being a real reporter."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.16
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "You're so friendly, I can't even yell at you about it."

hide M annoyed

"Marcia laughed. Her face took on a concerned look."

mar "Okay, but you're all right? When you left work I thought you were going to blow your top."

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.16
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "Yes, I'm all right."

hide M annoyed

mar "Your face was so red…"

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.16
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "Yes, I'm fine now…"

hide M annoyed

mar "You were muttering something under your breath…"

show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.16
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "I'm…"

hide M annoyed

mar "It was something about his eyeballs…"

# M flustered and shouting
show M annoyed:
    subpixel True 
    yalign 1.0 zoom 0.35 xpos 0.16
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    ypos 1.0 

m "Marcia! I'm fine!"

"Marcia's face slipped into a sly smile and she started giggling. She had successfully wound me up."

show M main:
    subpixel True 
    yalign 1.0 zoom 0.45 xpos 0.12
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    ypos 1.0 

"I started laughing too."

"Marcia touched my arm in a sisterly way."

hide M main

mar "I'm sorry you're having such a tough time…"

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

# MC is smiling

m "Thanks, Marcia."

hide M main

mar """Oh! You know what? One of my favorite bands is coming to town. You should come with me!

It's The Rip-Chords, you've heard of them, right?"""

"I was befuddled. Not because Marcia was asking me to go to a concert with her, but because she didn't strike me as the type to like a rock band like The Rip-Chords."

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "The Rip-Chords are coming here?"

hide M main

mar "I know, isn't it ginchy! This little town never has anything happen and my favorite band is going to have a concert."

show M melancholy:
    xpos 0.16 zoom 0.35 yalign 1.0

"I hadn't thought of Marcia as being a fan of rock music. She seemed more like the light jazz type."

"Something involving a white guy with an accordion."

# MC curious or thoughtful.

show M melancholy:
    subpixel True 
    xpos 0.16 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    yalign 1.0

m "Do you listen to a lot of rock records?"

hide M melancholy 

mar "All that I can get my hands on. The Mucky Mucks, Salt River Navy Band, The Herdsmen, Hub Kapp and the Wheels, …"

"I teased her."

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

# MC playful or happy

m "Marcia, I thought you were a square! Just look at that sweater you're wearing…"

hide M main

mar "I am, I wouldn't dare go to a concert by myself…but I'll go with a friend! Please say you'll come…"

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

# MC agreeable or happy

m "Sure, okay. How can I say no?"

"Marcia was the most normal friend I'd made since moving here."

"And I truly couldn't wait to see the Rip-chords!"

scene black
with fade

# black screen or background transition of some kind here

"The days flew by until the day of the concert."

# Scene OE.02  - Marcia can't come!
scene bg office 
with fade
# fx - newsroom ambience or theme

"I was handing in my story about the road widening project to the boss."

# boss - impassive, bored, neutral
# MC - thoughtful

b "Great. I guess we need the filler on page four. You know this won't…"

show M melancholy:
    subpixel True 
    xpos 0.16 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    yalign 1.0

m "I know, I know. I'm working on something. Say, is Marcia around?"

# Not sure if we named the boss or not, just say "the boss" if we didn't

"I knew Mr.Hollis always kept an eye out for Marcia just because of her legs."

"She actually worked hard on her little part of the paper but all he cared about was how tight her skirts were."

hide M melancholy

b "She called in sick today. Some kind of flu."

"He sounded less concerned than disappointed that he didn't get to leer at her."

b "Say, could you do her household hints column? Something about keeping the china closet dusted or whatever?"

# exit boss

show M smile:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M smile:
    yalign 1.0

"I was already on my way out of his office, so I was able to pretend I didn't hear him."

"Back at my desk I thought for a second, then grabbed the phone."

# MC is determined or concerned
# image of rotary phone

"Maybe she was actually sick, or maybe…"

hide M smile

mar "H…hello?"

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "Marcia…it's Dorothy.  I heard you were sick…"

"Or was she just playing hooky from work.."

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "There's nobody at my desk to hear…are you sick?"

hide M main

mar """Oh…gosh yes Dorothy...I'm fit to be tied… Or…

I guess I would be fit to be tied if I was feeling fit for anything."""

show M annoyed:
    subpixel True 
    xpos 0.16 xzoom 1.0 yzoom 1.0 zoom 0.35 yalign 1.0
    linear 0.10 xpos 0.17 xzoom 0.93 yzoom 1.11 
    linear 0.10 xpos 0.16 xzoom 1.0 yzoom 1.0 
with Pause(0.30)
show M annoyed:
    xpos 0.16 xzoom 1.0 yzoom 1.0 

# MC looks concerned/sad

mar """I have the flu and it's just awful!

On the day the Rip-Chords are here…"""

show M smile:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M smile:
    yalign 1.0

m "It's okay, you just rest up. Do you have everything you need? Do you need me to bring some soup over or…"

hide M smile

"She answered much too quickly."

mar "No no! Don't bring me any food. I've got plenty of groceries.."

# Not sure if we have a  "thought balloon" font like italics or something? Rewrite the next line if we don't use that into more of a narration joke.

"Apparently even free food isn't welcome if it's from the Weepie…"

mar "it just burns me up that I won't get to go to the concert…"

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "We'll go another time…"

hide M main

mar "What?! No, you have to go. Don't let my flu stop you…"

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "Marcia…"

hide M main

mar "The tickets are in my desk drawer, grab them and go have a good time."

# MC is uncertain, questioning

show M melancholy:
    subpixel True 
    xpos 0.16 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    yalign 1.0

m "I don't know…"

hide M melancholy 

mar "I insist. Don't make me argue with you, I…ohh…I have to go…right now!…sorry!"

# fade phone

"She hung up."

"I thought about it for a moment, then went and got the tickets from her desk."

# picture of the tickets

# Cut to black or other transition


"Maybe I would ask LeeRoy. It seemed like his kind of concert."
scene black
with fade

scene bg diner
with fade
# Scene OE.03 - Marcia meets Oe and asks them instead

camera:
    subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.2)*HueMatrix(0.0) 

# bg diner - dimly lit or shady perhaps?
# MC enters, enthused

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "LeeRoy, hey!"

# MC looks shocked.
# Oe is there, neutral

show O solemn:
    subpixel True 
    yalign 1.0 zoom 0.55 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    yalign 1.0

o "He isn't here."

"I was used to the diner being empty of customers but somehow when Oe was the only one there, it seemed even emptier somehow."

"At least LeeRoy and Adelaide would bicker and fight."

"Oe was just sitting behind the counter looking out the front door blankly."

"They were smoking that weird old-fashioned pipe."

show M smile:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M smile:
    yalign 1.0

m "I…uh…do you know where he is?"

show O solemn:
    subpixel True 
    yalign 1.0 zoom 0.55 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    yalign 1.0

o "No."

"Their voice was so flat, so neutral…"

"Then they turned their eyes on me - still empty, still expressionless."

show O main:
    subpixel True 
    yalign 1.0 zoom 0.5 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    yalign 1.0

o "What do you have there?"

"I had forgotten I had entered waving the tickets."

"Oe looked at them like an owl looking at a dead mouse."

"Animalistically interested, yet slightly disgusted."

show M smile:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M smile:
    yalign 1.0

m "Er, tickets…"

show O main:
    subpixel True 
    yalign 1.0 zoom 0.5 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    yalign 1.0

o "To what?"

show M annoyed:
    subpixel True 
    xpos 0.16 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0

m "To…to a rock and roll show…the Rip-Chords…"

"They stared at me blankly. I suddenly kept babbling."

show M annoyed:
    subpixel True 
    xpos 0.16 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0

m "I was going to, ah, go with a friend, but she got sick, and then I thought LeeRoy might…"

show O solemn:
    subpixel True 
    yalign 1.0 zoom 0.55 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    yalign 1.0

o "You thought LeeRoy might what?"

show M annoyed:
    subpixel True 
    xpos 0.16 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0

m "I thought he might want to go with me…"

show O solemn:
    subpixel True 
    yalign 1.0 zoom 0.55 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    yalign 1.0

o "You will not find LeeRoy tonight."

"They intoned this with the flat certainty of a math teacher correcting a student."

show M annoyed:
    subpixel True 
    xpos 0.16 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0

m "Oh…Oh I see…"

show O main
with dissolve 

camera:
    subpixel True 
    zoom 1.0 
    linear 0.30 zoom 1.15 
show M smile:
    subpixel True 
    xpos 0.12 zoom 0.45
    linear 0.30 xpos 0.08
show O main:
    subpixel True 
    xpos 0.5 zoom 0.5
    linear 0.30 xpos 0.35 
with Pause(0.40)
camera:
    zoom 1.15 
show M smile:
    xpos 0.08
show O main:
    xpos 0.35 zoom 0.5

# Not sure if we can do a zoom in on Oe here? Something where they're like "standing closer"?

"It was like they were suddenly in my personal space."

"Completely unnerving. They didn't breathe at all, but also weren't holding their breath."

"Of all my downstairs neighbors, Oe seemed most like a living corpse."

"No - not just any corpse. Undertakers could make corpses look peaceful."

"Oe looked completely lifeless, standing this close."

"It was an intense feeling."

"Suddenly I felt myself blurt it out."

# You can use italics instead of caps for emphasis here if you want; or rewrite for a different way of emphasizing

show M smile:
    subpixel True 
    xpos 0.08 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M smile:
    yalign 1.0

m "Do…do YOU want to go?"

"I immediately regretted it. Their answer came back as quick as a mousetrap snapping, and just as final."

show O solemn:
    subpixel True 
    yalign 1.0 zoom 0.55 xpos 0.35
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    yalign 1.0

o "I will accompany you."

show M smile:
    subpixel True 
    xpos 0.08 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M smile:
    yalign 1.0

m "O…okay. That's…that's…"

# back to normal for Oe. still flat expression

show O main:
    subpixel True 
    yalign 1.0 zoom 0.5 xpos 0.35
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    yalign 1.0

o "That's 'cool'?"

"I couldn't tell if they were being sarcastic or not. Their voice hadn't changed at all."

show M smile:
    subpixel True 
    xpos 0.08 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M smile:
    yalign 1.0

m "Y..yeah…that's cool."

"An awkward pause followed. Oe hadn't blinked once since I came into the room."

show M smile:
    subpixel True 
    xpos 0.08 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M smile:
    yalign 1.0

m "I'll meet you down here….in half an hour?"

show O solemn:
    subpixel True xpos 0.35 zoom 0.55
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) yzoom 1.0 
    linear 0.10 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(-10.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) yzoom 0.95 
    linear 0.10 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) yzoom 1.0 
with Pause(0.30)
show O solemn:
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) yzoom 1.0 

"They just nodded and put their pipe back in their mouth impassively."

"I scurried up the stairs like a little mouse running away from an alley cat."

"What had I gotten myself into?"

"They were just going to stand there like a lump."

"God help anyone who bumped into them!"

# Transitional background or black

# Don't know if we have a "going out" outfit for the MC, if so we can put in a line here about changing clothes.  If not, maybe something about freshening up

# Scene OE.04 - The Concert
hide black
hide black onlayer overlay
scene black 
with fade
scene bg office
with fade

camera:
    subpixel True zoom 1.0 
    matrixcolor BrightnessMatrix(-0.1) * SaturationMatrix(0.75) * TintMatrix("#ff000069")
# background - outside of a theater or other building

"They didn't change their clothes; I don't think I'd ever seen them in anything else."

# Do we establish if the MC has a car? If so, we can adjust the next line

"When they got off the bus, I noticed nobody else was sitting on it."

"As if the moment they got on, everyone else knew to get off."

show O main:
    subpixel True 
    yalign 1.0 zoom 0.5 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    yalign 1.0

o "The Rip-Chords?"

show M annoyed:
    subpixel True 
    xpos 0.16 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0

m "It's a pun on 'ripcord'. The thing you pull to open a parachute."

show O main:
    subpixel True 
    parallel:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) yzoom 1.0 
        linear 0.10 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(15.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) yzoom 1.04 
        linear 0.10 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) yzoom 1.0 
    parallel:
        xzoom 1.0 
        linear 0.10 xzoom 1.0 
with Pause(0.30)
show O main:
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) xzoom 1.0 yzoom 1.0 

"Oe looked up."

show M annoyed:
    subpixel True 
    xpos 0.16 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0

m "No, no, they don't parachute in…"

"They looked back across at me expressionlessly."

show M main:
    xpos 0.12 zoom 0.45 yalign 1.0

"Suddenly I realized…"

"They were joking!"

# MC nervous / awkward smile

show M smile:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M smile:
    yalign 1.0

m "Oh! Oh, hehe…yea…you got me."

"Oe didn't smile an inch. But when we walked in we were walking closer together."

# bg interior of the theater

"Seats were scattered around the outside of the room."

"A few tables were set up near a bar."

"But most of the audience was milling around the dance floor."

"Oe didn't make their way to a seat or onto the floor, they just stood stock still."

"The crowds went around us like water."

"I felt awkward again, like I'd brought my mom to the concert."

show M smile:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M smile:
    yalign 1.0

m "Er… It's gonna be loud…"

show O solemn:
    subpixel True 
    yalign 1.0 zoom 0.55 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    yalign 1.0

o "I believe rock and roll music is meant to be performed loudly?"

"A strange question - I didn't know how to answer so I just shrugged helplessly."

"Thankfully after a moment, a young man came out to the microphone, grabbing it by the stand."

hide O solemn
hide M annoyed

# A silhouette for him maybe

guy "Ladies and gentlemen, straight from Pascagoula, Florida, live tonight here in the Sunrise Musical Theater, please welcome… the Rip-Chords!"

# remove the silhouette
# fx: rowdy clapping
# MC enthusiastic, cheering

"The crowd went crazy. I joined in, clapping and screaming."

show O main:
    subpixel True 
    yalign 1.0 zoom 0.5 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    yalign 1.0

"Oe watched me carefully as if I was a bug. They were studying through a magnifying glass."

"The lead singer - Johnny 'Rips' Goldman - came to the mike."

hide O main

# generic silhouette again maybe?

rip "Thank you…we're gonna start with a song we just wrote…it's called 'Rompin' At Sunset Beach'..."

# fx: rowdy clapping

"With four sharp pops of the snare drum the song started."

# music: 1960s rock

"The crowd rushed for the dance floor, the music was so lively and exciting."

camera:
    subpixel True ypos 0 
    parallel:
        xpos 0 
        linear 0.10 xpos -198 
        linear 0.10 xpos -162 
        linear 0.10 xpos -243 
    parallel:
        xzoom 1.0 
        linear 0.10 xzoom 1.12 
        linear 0.10 xzoom 1.0 
    parallel:
        yzoom 1.0 
        linear 0.10 yzoom 1.0 
    parallel:
        zoom 1.0 
        linear 0.30 zoom 1.25 
show M main:
    subpixel True zoom 0.45 yalign 1.0
    pos (0.12, 1.0) 
    linear 0.30 pos (0.16, 0.95) 
with Pause(0.40)
camera:
    pos (-243, 0) xzoom 1.0 yzoom 1.0 zoom 1.25 
show M main:
    pos (0.16, 0.95) 

"I was carried along, even though Oe was not."

"Before I knew it I was dancing away in a huge crowd of people."

"After the first song, then the second, I looked around to see where Oe was."

# MC shocked/surprised

show M smile:
    xpos 0.16 zoom 0.45 
with dissolve 

"To my horror they were now out on the dance floor with everyone else."

"They were twisting their knee and waist back and forth in opposite directions."

# Thinking here

show M melancholy:
    xpos 0.2 zoom 0.35
with dissolve 

"Wait…are they doing the Charleston?"

hide M melancholy 

# Back to narration

show O smile:
    subpixel True xpos 0.45 zoom 0.5 yalign 1.0
with dissolve 

"They were, and I could see the crowd starting to giggle behind their hands at them."

"At first glance they were offputting, awkward…"

"But when they were actually trying to fit in, Oe was almost laughable."

"I was getting ready to come back and say something when I noticed…"

show O smile:
    subpixel True xpos 0.45 zoom 0.5 yalign 1.0
    parallel:
        ypos 1.0 zoom 0.5 
        linear 0.30 xpos 0.35 ypos 1.28 zoom 0.7 
    parallel:
        xzoom 1.0 yzoom 1.0 
        linear 0.10 xzoom 0.76 yzoom 1.21 
        linear 0.20 xzoom 1.0 yzoom 1.0 
with Pause(0.40)
show O smile:
    pos (0.35, 1.28) xzoom 1.0 yzoom 1.0 zoom 0.7 

# Maybe another Oe zoom in here?

"Their eyes got a glint in them. A sharp, perceptive glint."

"Their blank face took on a determined cast."

"They started imitating the moves of a young woman to their right."

"Haltingly at first, but very quickly picking them up."

"No longer a laughable sight, the crowd lost interest in them."

"And then as I faced them I saw…their expression start to change."

"It was the first time I'd ever seen it change."

# Happy Oe here

show O excited:
    xpos 0.35 zoom 0.53 yalign 1.0
with dissolve 

"When the Rip-Chords blasted into their big hit song and the crowd whooped and surged, Oe too whooped and surged."

"The happiness of the dancing had overtaken them."

"As if they had imitated a person having the time of their life until that emotion entered them as well."

"Soon Oe was in the middle of the crowd with me, dancing away."

# MC enthused/happy here

show M main:
    xpos 0.16 zoom 0.45 yalign 1.0

"Every new dance the crowd did, they picked it up almost instantly: the frug, the shimmy, the watusi, the twist…"

"Oe clearly had never seen them before, but they learned it instantly, and in a matter of minutes they were throwing themselves into it instead of simply imitating."

"They danced harder than I did."

# This would be a great place for a CG if we're looking for one for this route.

"Before we knew it…"

hide M main 
hide O excited

rip "You're a lovely crowd, we're going to take a little intermission and be back in ten minutes."

# fx: rowdy clapping

"The crowd rushed for the bar, for the restrooms…"

show M annoyed:
    xpos 0.2 zoom 0.35 yalign 1.0

"I was exhausted, sweaty, wobbling on my feet."

show O main:
    xpos 0.45 zoom 0.5 yalign 1.0
with dissolve 

# MC tired/exhausted
# Oe back to neutral

"Of course Oe was cool as a cucumber…even cold to the touch when their fingers held my elbow."

"For the first time, Oe was leading me instead of me leading them."

"Their cold hand had me by the elbow and we went out into a dingy alleyway."

#fx: city ambience

"A few scattered knots of concertgoers were smoking. Oe produced their pipe and lit it."

show O solemn:
    xpos 0.45 zoom 0.53 yalign 1.0
with dissolve 

# Oe pipe

"Their expression was back to being neutral."

"I couldn't help myself, I was enthused."

# MC excited/happy

show M main:
    subpixel True 
    yalign 1.0 zoom 0.45 xpos 0.12
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "Oe, you're an amazing dancer! You picked it up perfectly!"

show O solemn:
    subpixel True xpos 0.45 zoom 0.53 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    pos (0.45, 1.0) 

o "Gratifying of you to say so. The pleasure is mine, to find so many new steps."

show M main:
    subpixel True 
    yalign 1.0 zoom 0.45 xpos 0.12
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "You don't…you don't seem like the kind of person who keeps up with new things…"

"They regarded me through the smoke with their blank gaze, then they began to speak."

"Their cool voice cut through the humid, smoky air."

# In this monologue, we might change MC's attitude to thoughtful, maybe even sad. same for Oe, though They can also still appear static. This might be a good place for some warm or spooky music too. Also might be a good idea to have a few images vaguely referring to Oe's comments here. 

show O solemn:
    subpixel True xpos 0.45 zoom 0.53 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    pos (0.45, 1.0)

show M melancholy:
    xpos 0.16 zoom 0.35 yalign 1.0
with dissolve 

o "Most things - new or old - pass. You buy a blouse, it lasts a decade, perhaps two at most."

show O solemn:
    subpixel True xpos 0.45 zoom 0.53 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    pos (0.45, 1.0)

"A pipe can last a hundred years if you care for it properly."

show O solemn:
    subpixel True xpos 0.45 zoom 0.53 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    pos (0.45, 1.0)

"A well made sword, maintained by an expert, can keep its edge perhaps two hundred. "

show O main:
    subpixel True xpos 0.47 zoom 0.5 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    pos (0.47, 1.0)

"But eventually almost everything that is material fades."

show O main:
    subpixel True xpos 0.47 zoom 0.5 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    pos (0.47, 1.0)

"If you look at things from the perspective of forever, of infinity, there's very little that can ever last."

show O solemn:
    subpixel True xpos 0.45 zoom 0.53 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    pos (0.45, 1.0)

"None of LeeRoy's cars will be running in twenty years."

show O solemn:
    subpixel True xpos 0.45 zoom 0.53 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    pos (0.45, 1.0)

"The diner won't be around in ten years; the building itself will be knocked down in thirty or forty."

show O main:
    subpixel True xpos 0.47 zoom 0.5 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    pos (0.47, 1.0)

"There'll be another building there before a hundred years are out."

show O main:
    subpixel True xpos 0.47 zoom 0.5 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    pos (0.47, 1.0)

"Everyone who ever set foot in that building will be dead - except for me, and my friends."

show O main:
    subpixel True xpos 0.47 zoom 0.5 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    pos (0.47, 1.0)

"Why love anything? It will die. The traces of it will rot and soon even those traces will disappear forever."

show O solemn:
    subpixel True xpos 0.45 zoom 0.53 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    pos (0.45, 1.0)

"Leaving you as the only one to mourn."

show O main:
    subpixel True xpos 0.47 zoom 0.5 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    pos (0.47, 1.0)

"Eventually all you have inside your heart is grief."

show O solemn:
    subpixel True xpos 0.45 zoom 0.53 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    pos (0.45, 1.0)

"No other emotion can get inside without knocking over grief's teacups, elbowing grief's belongings off the mantelpiece, bumping against grief's portraits on the wall…"

show O main:
    subpixel True xpos 0.47 zoom 0.5 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    pos (0.47, 1.0)

"I can't grieve or I would go mad. Quite mad."

show O main:
    subpixel True xpos 0.47 zoom 0.5 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    pos (0.47, 1.0)

"So…what can we love, then?"

show O main:
    subpixel True xpos 0.47 zoom 0.5 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    pos (0.47, 1.0)

"Something as immortal as we are."

show O solemn:
    subpixel True xpos 0.45 zoom 0.53 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    pos (0.45, 1.0)

"Art.  Music. Theater."

show O solemn:
    subpixel True xpos 0.45 zoom 0.53 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    pos (0.45, 1.0)

"The emotion that flows out of it is real."

show O main:
    subpixel True xpos 0.47 zoom 0.5 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    pos (0.47, 1.0)

"You take it in… it stays with you…"

show O main:
    subpixel True xpos 0.47 zoom 0.5 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    pos (0.47, 1.0)

"Even something amateurish or awkward…it stays with you as long as you choose to keep yourself open to it."

show O main:
    subpixel True xpos 0.47 zoom 0.5 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    pos (0.47, 1.0)

"You let it go when you wish, and not before."

show O solemn:
    subpixel True xpos 0.45 zoom 0.53 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    pos (0.45, 1.0)

"And never in grief, but in satisfaction and pleasure."

show O smile:
    subpixel True xpos 0.45 zoom 0.53 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O smile:
    pos (0.45, 1.0)

"That's why I love hearing new music…and dancing in new ways…"

show O main:
    subpixel True xpos 0.47 zoom 0.5 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    pos (0.47, 1.0)

"…why I love going to the library when they receive new books…"

show O main:
    subpixel True xpos 0.47 zoom 0.5 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    pos (0.47, 1.0)

"…why I love to see a gallery opening with a painter or sculptor I've never seen before…"

show O main:
    subpixel True xpos 0.47 zoom 0.5 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    pos (0.47, 1.0)

"…even your little news stories give me pleasure."

show O main:
    subpixel True xpos 0.47 zoom 0.5 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    pos (0.47, 1.0)

"They don't need to be a work of titanic genius…they just need to be real.  Real today, right now."

show O solemn:
    subpixel True xpos 0.45 zoom 0.53 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    pos (0.45, 1.0)

"Tomorrow will be the same as today in so many ways. And if you've seen as many tomorrows as I have, you don't really care about any particular one."

show O solemn:
    subpixel True xpos 0.45 zoom 0.53 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    pos (0.45, 1.0)

"But there is always something new in the creation of art…"

show O main:
    subpixel True xpos 0.47 zoom 0.5 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    pos (0.47, 1.0)

"This is the first rock and roll concert I've been to, you're right."

show O smile:
    subpixel True xpos 0.45 zoom 0.53 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O smile:
    pos (0.45, 1.0)

"But I certainly hope it won't be my last."

show O smile:
    subpixel True xpos 0.45 zoom 0.53 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O smile:
    pos (0.45, 1.0)

"There is so much to experience here."

# if we've changed music, background, images, as described above, here they should go back to normal

show O solemn:
    subpixel True xpos 0.45 zoom 0.53 yalign 1.0
with dissolve 

"Oe trailed off, the smoke from their pipe finally ending. They tapped the bowl of the pipe on the brick wall, letting the ash fall into the alleyway."

"From inside we heard the crowd begin to cheer again. The band was back."

# happy oe

show O excited:
    subpixel True xpos 0.4 zoom 0.55 yalign 1.0
    ypos 1.0 
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O excited:
    pos (0.4, 1.0)

"Oe's face lit up again."

o "Time for more? You aren't too tired…"

show M main:
    subpixel True 
    yalign 1.0 zoom 0.45 xpos 0.12
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

# MC happy/determined

m "N…no! I'm ready for more!"

"The two of us went back in just as the first jangling chords tore across the crowd."

scene black
with fade 

# transition or black screen

"We rode the bus home together - nobody else on board."

"I somehow understood why they were as awkward as they were."

"An infinite life…you couldn't compare it to a finite one like mine."

"I felt closer to them; they had opened up to me about their philosophy…"

"New emotional experiences through their own immortal self experiencing art…not through items or places or people…"

"We arrived home."
camera:
    reset
scene bg diner
with fade

# Bg diner

"We stopped outside the diner. Through the window we could see LeeRoy and Adelaide bickering over something."

# oe is blank faced

show O main:
    subpixel True 
    yalign 1.0 zoom 0.5 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    yalign 1.0

o "Thank you for inviting me. I hope you will think of me again if you have the opportunity."

# mc is happy

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "I…I will. You're welcome. I had a great time."

hide O main

"Without another word, they turned and went into the diner. I saw the other two immediately begin to try to draw them into the argument."

"I went up the side stairs instead."

scene black
with fade 

# transition/black bg

# Scene OE.05 The library
scene bg diner 
with fade 

camera:
    subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 

# Note that the MC needs to have been given the work ultimatum at this point; a big story or else.

"I was out of groceries the next night, so I was stuck eating downstairs."

"LeeRoy was not his usual ebullient self, though. He seemed distracted."

show L shrug:
    subpixel True xpos 0.55 zoom 0.45
    yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L shrug:
    pos (0.55, 1.0) 

l "Hey, have you seen the old one?"

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "Oe? No, not in a day or two. Why?"

show L shrug:
    subpixel True xpos 0.55 zoom 0.45
    yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L shrug:
    pos (0.55, 1.0) 

l "Well…they didn't come home this morning. It's probably nothing, but they usually are here sleeping in the meat locker when the sun goes down."

with hpunch
# MC befuddled/shocked

# thought balloon/italics

"The meat locker?!"

"I shook it off. At least it explained why their skin was always cold." 

# MC normal

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "When was the last time you saw them?"

show L shrug:
    subpixel True xpos 0.55 zoom 0.45
    yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L shrug:
    pos (0.55, 1.0)  

l "Yesterday evening. they went out right after sundown."

"I suddenly remembered one of Marcia's community calendar entries."

# thought balloon/italics, or perhaps a newspaper? Not sure of the best format here

"The library will be putting out their new books this week!"

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "I think they were headed to the library. I'll go check it out."

show L shrug:
    subpixel True xpos 0.55 zoom 0.45
    yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show L shrug:
    pos (0.55, 1.0) 
l "Thanks. Books make me fall asleep just thinking about them. Honk shoo!"

"I rolled my eyes at him and headed out."

hide L shrug

scene black 
with fade

scene bg library
with fade 

# bg exterior library at night. kinda "any building at night" works here

"The library wasn't open for very long after dark."

"I didn't doubt Oe could stay after closing if they wanted to…"

"But it did worry me that they didn't show up at all back at the diner."

"Of all the vampires there, I thought of them as the most introverted."

"I had only seen them open up at the Rip-Chords concert."

"When thinking back, they barely said anything at all compared to the other two…"

"But they were always there."

"I approached one of the librarians at the desk."

# Librarian can probably be a silhouette

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "Er, excuse me…"

hide M main

lib "Yes? We're closing in half an hour…."

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "Yes, well, I'm looking for a friend. They're about this tall, sort of…"

# MC awkward/nervous

show M smile:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M smile:
    yalign 1.0

m "...grey…"

hide M smile

lib "OH!  Oh.  You're with..with them…"

"It was clear that Oe had made an impression."

lib "Can you let them know…I know we sort of…let them stay after closing last night…"

lib "But they can't be in the building after we lock it up…tonight…"

"She said all of this as if she didn't quite know why she had gone along with the idea."

"Oe had clearly used some kind of vampire mesmerism on her."

# MC neutral/charming

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "I'll let them know. Thank you. They're… eccentric. I'll try to get them to leave before you close."

hide M main

lib "Thanks. They're downstairs in the basement stacks."

# bg a bunch of shelves, dimly lit?

# Oe neutral

# MC concerned/curious

show O solemn:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.5
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

"Oe was sitting alone at a table in the middle of the room."

"The lights seemed dimmer closer to them."

"They were just staring forward, lost in thought…"

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "Oe?"

"No answer."

"I didn't know what to do.  I was about to touch their shoulder when I realized how dangerous that might be."

show M main:
    subpixel True 
    parallel:
        xpos 0.12 
        linear 0.30 xpos 0.34 
    parallel:
        ypos 1.0 
        linear 0.05 ypos 0.98 
        linear 0.05 ypos 1.0 
        linear 0.05 ypos 0.98 
        linear 0.05 ypos 1.0 
        linear 0.05 ypos 0.98 
        linear 0.05 ypos 1.0 
with Pause(0.40)
show M main:
    pos (0.34, 1.0) 

# Not sure if we can use the movement of the characters on screen to get across this movement, but it's a good spot to put some in if we can

"Instead I moved to the other side of the table and sat down opposite them."

"They couldn't avoid seeing me, but we didn't have to talk until they wanted to."

"In the middle of the table I noticed a community event leaflet from the circulation desk."

# Not sure if we want to do a leaflet font, box, or other delineation here.

"leaf The Art of the American Expedition!"

"An exhibition at the Sullivan Gallery"

"A hundred years ago, American ships visited Japan for the first time."

"What many don't know is that they returned with many priceless works of ancient Japanese art."

"From bronze mirrors to woodblock prints…"

"…from silk hanging scrolls to religious statues…"

"These treasures are now on display for the first time in this traveling exhibition."

"There was a picture of the First Lady, wearing her classic pillbox hat, shaking hands with an old man at the bottom of the flyer."

"Oe was staring at the flyer blankly."

show O main:
    subpixel True yalign 1.0 zoom 0.5 xpos 0.5
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.20 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 360.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.30)
show O main:
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 360.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

"I looked up at them and they finally spoke."

show O main:
    subpixel True 
    yalign 1.0 zoom 0.5 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    yalign 1.0

o "I shouldn't grieve…I shouldn't grieve…or else what else will I spend my centuries doing but grieving?"

# MC concerned

show M melancholy:
    subpixel True 
    xpos 0.36 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    yalign 1.0

m "Oe…"

"They tapped them finger on a picture of a scroll right in the center of the flyer."

"The painting showed a brown horizon of mountains and a field of flowers scattered with broken swords. The inscription underneath said:"

"Handscroll depicting aftermath of the siege of Shirakawa-den, July 1156. Artist unknown."

show O main:
    subpixel True 
    yalign 1.0 zoom 0.5 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    yalign 1.0

o "I knew the artist… I…"

show O solemn:
    subpixel True xpos 0.5 zoom 0.53 yalign 1.0
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.20 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.30)
show O solemn:
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

"Their voice gave out."

show O solemn:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    yalign 1.0

o "He was my father. He gave it to me."
# MC is shocked

show M melancholy:
    subpixel True 
    xpos 0.36 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    yalign 1.0

m "Your father!"

show O solemn:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    yalign 1.0

o "When he came home from the siege I bothered him to paint me the battle."

show O main:
    subpixel True 
    yalign 1.0 zoom 0.5 xpos 0.52
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    yalign 1.0

o "I was just a little child, I couldn't have known what he'd seen."

show O smile:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O smile:
    yalign 1.0

o "Finally he gave in, and just painted this empty field."

show O main:
    subpixel True 
    yalign 1.0 zoom 0.5 xpos 0.52
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    yalign 1.0

o "At the time I hated it, but ever since then I've remembered this field of flowers…"

show O solemn:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    yalign 1.0

o "After I was turned, I never saw anyone in my family again."

show O smile:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O smile:
    yalign 1.0

o "But I saw this field of peaceful flowers in my mind so many times…"

show O main:
    subpixel True 
    yalign 1.0 zoom 0.5 xpos 0.52
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    yalign 1.0

o "Now to find out that someone just gave it to the Americans as a bribe…or it was taken as theft…"

# M is shocked
# Oe is bitter/sad

show M melancholy:
    subpixel True 
    xpos 0.36 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    yalign 1.0

m "Oe…"

# Oe angry/upset

show O solemn:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    yalign 1.0

o "I hate grieving. I hate it! But I see this and I grieve my father, my home in the hills! I grieve the sun on the flowers! The sun anywhere!"

show M melancholy:
    subpixel True 
    xpos 0.36 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    yalign 1.0

m "Oh Oe…"

# Oe holding a dark handkerchief?

"Tears of blood formed at the corner of their eyes and they blotted them with a dark handkerchief that would hide the stains."

show O solemn:
    subpixel True 
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    linear 0.20 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.30)
show O solemn:
    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 

"I took their cold hand and held it in both of mine."

# Oe back to normal


"They didn't pull away. They still hadn't really moved at all since I came into the basement."

show O main:
    subpixel True 
    yalign 1.0 zoom 0.5 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    yalign 1.0

o "It belongs to me, it's mine. But I can't have it, I can't have it! It has lasted this long, eight hundred years, as long as I have, but how much longer?"

show O main:
    subpixel True 
    yalign 1.0 zoom 0.5 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    yalign 1.0

o "Look how frayed it is, look how it's almost pulling apart."

show O main:
    subpixel True 
    yalign 1.0 zoom 0.5 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    yalign 1.0

o "And I'm still the same as the night I left it behind me!"

show M melancholy:
    subpixel True 
    xpos 0.36 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    yalign 1.0

m "Oe…it's not wrong to want something that belongs to you…something that means something to you."

show M melancholy:
    subpixel True 
    xpos 0.36 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    yalign 1.0

m "You can't just sit down here in the basement of the library staring at it, hoping your feelings about it will change."

show M melancholy:
    subpixel True 
    xpos 0.36 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    yalign 1.0

m "Even if they hurt, they're your feelings."

"Oe finally looked back up at me."

show M melancholy:
    subpixel True 
    xpos 0.36 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M melancholy:
    yalign 1.0

m "The exhibition is tomorrow night, do you want to… go see it?"

show O main:
    subpixel True 
    parallel:
        xpos 0.5 xzoom 1.0 yzoom 1.0 
        linear 0.05 xpos 0.53 xzoom 0.84 yzoom 1.09 
        linear 0.15 xpos 0.5 xzoom 1.0 yzoom 1.0 
    parallel:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.20 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, -5.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
with Pause(0.30)
show O main:
    xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, -5.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) xzoom 1.0 yzoom 1.0 

"They suddenly lurched forward."

# Oe angry

show O main:
    subpixel True 
    yalign 1.0 zoom 0.5 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    yalign 1.0


o "No! I don't want to see it, I want to have it! I want to see it when I lay down to sleep at dawn! I want to see it when I wake up every dusk!"

o "I want to have it, I was ungrateful when my father gave it to me but he's dust and my home is dust and everyone I knew was dust but it's here and I want it!"

show M main:
    xpos 0.34 yalign 1.0 zoom 0.45
with dissolve 

"I felt for Oe in that moment…everything taken from them so long ago and now, just out of their reach, something that they wanted more than anything else."

show M main:
    subpixel True 
    xpos 0.34 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "Let's walk home, Oe.  I think we may be able to help each other…"

show O main:
    subpixel True 
    xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) xzoom 1.0 yzoom 1.0 
    linear 0.05 xpos 0.53 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, -5.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) xzoom 0.84 yzoom 1.09 
    linear 0.15 xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) xzoom 1.0 yzoom 1.0 
with Pause(0.30)
show O main:
    xpos 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) xzoom 1.0 yzoom 1.0 

# Oe hopeful/warm

show O smile:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O smile:
    yalign 1.0

# black/transition here

scene black
with fade 

# Scene OE.06 The Prep
scene bg office 
with fade 

"The next day I went to the Sullivan Gallery. It was connected somehow to the city or to the university, through ties of big-money donors, probably."

"I was surrounded by bright sunlight."

"Workers had opened all the windows and doors to give the place a good airing out before the exhibition tonight."

"The smell of cleaning supplies, the roar of vacuum cleaners, the sweeping sound of brooms and the squeak of polishing cloths were all around."

"I was met at the door by Matheson Burwell, the gallery assistant director."

# Matheson can be a silhouette I think

# MC is normal/upbeat

mat "I don't see why your paper needs another set of pictures. They sent a man out yesterday."

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "That's what I said when they sent me out! Something about some of the layout pictures not coming out."

hide M main

mat "Is that an instant camera?"

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "It's just for tracing."

"This excuse didn't really make sense but he didn't have time to think about it, there were too many things happening."

hide M main

mat "Well, don't touch any of the cases."

"The artifacts had not yet been put in place, but I was happy to see that the plaques and signs for each of the pieces were being attached to the walls and plinths."

"That made it easy."

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "I won't be a minute."

"I strolled carefully around the space, taking pictures of the glass doors to the courtyard outside…"

"...the doors to the restrooms…"

"...the skylight…"

"...a few of the cases…"

"It was actually a beautiful space. With all the elbow grease going into it, the gallery was going to look amazing tonight."

"Too bad."

"Finally I located the case that would contain Oe's scroll."

"I read the inscription:"

# inscription text maybe

"The siege of Shirakawa-den took place in July 1156 during the Heian Rebellion. The exact date of the painting is unknown, but fits the style of the time. The artist is also unknown, but thought to be a member of a provincial household."

# back to normal

"I hadn't thought of Oe as someone who might have actual knowledge that nobody else had, but they could have told the historians exactly who and when it was made…"

"It made me feel that they were, themselves, just as precious as any of the artifacts that would be displayed here."

scene black
with fade 

# black/transition

"And I wanted them to have what rightly belonged to them."


# Scene OE.07 The heist
scene bg office 
with fade 
camera:
    subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0) 

# bg is the exhibition hall at night time. you can add some lights or just make it seem a bit darker

# mc is there, if she has a "glamour" outfit she can be wearing it. expression happy

"I was trying to keep my nerves at bay and remember the plan."

# Thinking/flashback here maybe? I leave to you how to show this. We could even fully flash back to the diner or MC's apartment in a new scene here

scene bg diner
with fade 
camera:
    subpixel True matrixcolor BrightnessMatrix(-0.1)*SaturationMatrix(0.0) 

show O main:
    subpixel True 
    yalign 1.0 zoom 0.5 xpos 0.35
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    yalign 1.0

o "You haven't seen the full power of the blood."

show O solemn:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.35
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    yalign 1.0

o "Few living have.  LeeRoy and Adelaide barely have a fraction of the knowledge that I do."

show O solemn:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.35
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    yalign 1.0

o "They're like children running around a field waving paper swords."

show O main:
    subpixel True 
    yalign 1.0 zoom 0.5 xpos 0.35
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O main:
    yalign 1.0

o "It can be very difficult for a human to look at it directly.  It affects the mind."

show O solemn:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.35
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O solemn:
    yalign 1.0

o "You have to be focused and practiced. So let's go over it again."

scene bg office 
with fade 
camera:
    reset
camera:
    subpixel True matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-0.15)*HueMatrix(0.0)    

# Back to the gallery, the MC

"I had a glass of wine but hadn't dared to even take a sip."

"I waved it around rather drunkenly as I flirted with the security guard."

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "Don't you think all these old rich people are phonies?"

hide M main

guard "Couldn't say, ma'am."

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "See, I respect a working man, someone with an actual job that their mother didn't buy for them."

hide M main

guard "Is that so, ma'am."

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "Someone like you…"

"On the one hand I was annoyed that I was striking out so badly.  On the other hand, I had a good excuse."

"I was so nervous I could barely keep my voice from cracking. I kept glancing at the keys on his belt."

"I had exactly two things to do and those keys were one of them."

# a pic of the keys might be cool here

"The skylight was open to the sky - just a crack given its size, but a solid eight inches according to my pictures."

"More than enough for Oe."

"The lights began to flicker, to dim."

hide M main

guy "What's that sound?"

lady "It sounds like…I don't know what it sounds like…"

show M main:
    xpos 0.12 zoom 0.45 yalign 1.0

"I was looking up so I saw it immediately. A bat came in through the skylight, then another…"

"And another and another, faster and faster, screeching, their wings flapping with ugly, leathery sounds."

"Hundreds of them, maybe thousands, and accompanied by an evil black fog that seemed to absorb the warm incandescent lights of the chandeliers and spotlights."

"The guard I was standing next to was agog as the swarm of bats began to descend on the guests, but he did step forward to help."

"Nothing doing."

# MC exaggeratedly upset

show M annoyed:
    subpixel True 
    xpos 0.16 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0

m "Oh my god! Save me! I hate bats! Please!"

with hpunch
hide M annoyed

"I threw myself in his arms and spilled my wine everywhere."

"He didn't really have any choice but to hold me up."

"A dozen guests or so were stampeding for the bathroom when a scream came out from there too."

"Rats, hundreds, boiling out of the toilets in a teeth gnashing frenzy."

"Total pandemonium as everyone ran for the exits."

"I grabbed for the keys…"

"...got them!"

# MC happy

guard "Are you okay miss?" 

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "You're so brave!!"

"He didn't look brave, the fog was descending from the ceiling at a sinister, relentless pace, the lights snuffed out one by one from the top down."

"I scrambled across the floor. The rats went around me. I hope nobody notices…"

"A hand emerged from the fog. Oe's grey, cold hand."

"Quick as a flash, I passed them the keys, then ran for the courtyard door."

"Burwell was there, standing right in front of the door."

"That's what we didn't want. Witnesses to see them when they were in their normal form."

show M annoyed:
    subpixel True 
    xpos 0.16 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0

m "Mr. Burwell! Don't be a hero, run!"

"I grabbed him by the lapels and shoved him backwards through the courtyard door."

show M annoyed:
    subpixel True 
    xpos 0.16 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0

m "Run, save yourself!"

show M annoyed:
    subpixel True 
    xpos 0.16 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0

m "Ahhhhhhhh!!!!!"

with hpunch

"Within the swirling fog and bats and rats I heard the clunk of the case opening."

"I didn't dare look, I just continued screaming bloody muirder."

show M annoyed:
    subpixel True 
    xpos 0.16 zoom 0.35 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M annoyed:
    yalign 1.0

m "It's horrible, horrible!!"

"That was it. Burwell took to his heels."

"The courtyard had twelve foot walls, but Oe had said it was their best escape route."

"They emerged from the fog holding a scroll case, clutching it tight in their grey hands."

"Just a quick nod to me and then, in a split second, they raced into the moonlit night."

"Faster than a car; faster than a speeding bullet."

"They leapt over the courtyard wall with a balletic grace that made it look easy."

"They landed so light on their feet that I didn't even hear it."

"Oe had escaped. The plan had worked."

"I let myself flow back into the rush of panicked attendees."

"I started listening to what people were saying…what the mayor's wife said…"

"...what the gallery owner said…"

"...what the chief of police said…"

"Sneaking out just far enough to quickly write down the quotes."

"About the time people started to notice, I ran for a pay phone."

# MC is excited

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "Stop the presses! I got a big story!"

# black or transition

camera:
    reset
scene black
with fade 

scene bg bedroom 
with fade 

# bg MC's apartment

# MC enters, happy

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "We did it! I got the front page!"

# Oe, sad

show O main:
    yalign 1.0 zoom 0.5 xpos 0.5

"Oe was sitting at my little kitchen table, looking at the scroll with sad, longing eyes."

"Not their normal blank expression."

show M main:
    subpixel True 
    xpos 0.12 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "Is it…is it what you wanted?"

# Oe happy

show O excited:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O excited:
    yalign 1.0

o "Yes…yes, it's wonderful. It hurts so badly to look at it.  But it is wonderful to see it."

show M main:
    subpixel True 
    xpos 0.12 
    linear 0.20 xpos 0.43 
with Pause(0.30)
show M main:
    xpos 0.43 
with easeinleft 

"I impulsively hugged them` from behind."

"They did not resist or flinch."

show M main:
    subpixel True 
    xpos 0.43 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "You know…even if you hadn't become a vampire…you would have outlived your father probably."

show M main:
    subpixel True 
    xpos 0.43 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "He must have hoped that you would look at it after he was gone."

show O excited:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O excited:
    yalign 1.0

o "Yes. It made him immortal, just a little bit."

"They turned to face me. Although they were cold to the touch, their expression at last was warm."

show O excited:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O excited:
    yalign 1.0

o "Congratulations on the front page story. I look forward to reading it tomorrow."

show M main:
    subpixel True 
    xpos 0.43 zoom 0.45 yalign 1.0
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show M main:
    yalign 1.0

m "I couldn't have done it without you."

show O smile:
    subpixel True 
    yalign 1.0 zoom 0.53 xpos 0.5
    linear 0.05 ypos 0.98 
    linear 0.05 ypos 1.0 
with Pause(0.20)
show O smile:
    yalign 1.0

o "The kindness was all yours."

"Their fingers gently wrapped the scroll and slid it back into the case." 

