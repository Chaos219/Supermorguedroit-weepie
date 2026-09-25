# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Dorothy")
define a = Character("Adelaide")
define l = Character("LeeRoy")
define o = Character("Ōe")
define b = Character("Mr. Hollis")
define c = Character("Chet")
define t1 = Character("Teenager1")
define t2 = Character("Teenager2")


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
label mainroute2:
    menu:
        "Handle things your way":
            show mc_main:
                xpos 0.65
                yalign 1.0
                zoom 0.455
            "I drop into the chair at the Royal and hammer out three pages of notes before I budge."
            "Problems, root causes, fixes, all lined up by cost."
            "When I yank the last sheet from the carriage, I've got a battle plan."
            "Now to hit them with the facts and hope they take even a scrap of it seriously."
        "Ask what they are struggling with":
            show mc_main:
                xpos 0.65
                yalign 1.0
                zoom 0.455
            "I grab my steno pad and a pencil."
            "It'll be a whole lot easier to patch this sinking ship if I know where they think the leak is."
            "I've got my own ideas, but I don't have the full picture."
        # [LISTEN +1]

"I slip my shoes back on, one after the other."
hide mc_main
show mc_annoyed:
    xpos 0.7
    yalign 1.0
    zoom 0.35
"Deep breath. Out the door and down the stairs."
# Scene 5: The Supermurgidroid Weepie - Day
"I take the narrow, creaking stairs down to the ground floor and push through the swinging door."
"The diner is completely dead."
"The buzzing neon sign outside bleeds a harsh red light across the black-and-white checkered linoleum."
"I slide into the nearest booth and let my steno pad land on the Formica with a sigh that rattles the sugar packets."
"I barely have time to reach for my pen before LeeRoy materialises at my elbow, clutching a tall, frosted glass in both hands like he’s guarding a sacred relic."
show leeroy_shrug:
    xpos 0.05
    yalign 1.0
    zoom 0.49
l "On the house."
m "I didn’t order yet."
l "It’s an apology. For the racket."
"I eye the milkshake. If I were a real journalist, I’d probably turn it down."
m "You can’t bribe me with food, LeeRoy."
hide leeroy_shrug
show leeroy_sigh:
    xpos 0.05
    yalign 1.0
    zoom 0.49
"He sets it down anyway."
l "I know. I'm just apologising with it."
"I drag the straw closer and take a sip."
hide mc_annoyed
show mc_main:
    xpos 0.65
    yalign 1.0
    zoom 0.455
"My eyebrows go up, just a little. For me, that’s practically applause."
m "Seems like you took my tips seriously."
l "Sure did. I put the glasses in the freezer."
m "And used less syrup."
l "Four to one ratio."
m "…This is a genuinely good milkshake, LeeRoy. Thank you."
hide leeroy_sigh
show leeroy_main:
    xpos -0.1
    yalign 1.0
    zoom 0.5
"He slides into the booth across from me, uninvited, grinning so wide I’m surprised his face doesn’t crack."
"I look past him at the back wall."
"It’s covered in framed paintings - cars, mostly."
"Rows and rows of cars, painted with the kind of grim devotion you’d expect from a monk."
m "I meant to ask, who did the-"
hide leeroy_main
show leeroy_shrug:
    xpos 0.05
    yalign 1.0
    zoom 0.49
"And then LeeRoy’s face falls, all at once, the way a child’s does when a balloon pops."
l "We had no customers today."
m "…Mm."
l "Eleven days our doors have been open, and I’ve had a fella ask to use the payphone, and an old lady who thought we were the First Methodist Church."
"I look at him over the rim of my glass. Then at the eight empty booths lined up behind him."
"For a second, I think about going easy. I don’t."
hide mc_main
show mc_annoyed:
    xpos 0.7
    yalign 1.0
    zoom 0.35
m "Well. It’s the name."
"(Blankly)"
l "What about it?"
m "LeeRoy."
l "It’s a great name!"
m "It is absolutely not a great name."
l "Supermorgiedroit! Like-super. Super cool."
l "The Supermurgitroid Weepie. The coolest dinner around."
"I put my glass down on the table."
m "Say it slowly."
l "Super. Murgit. Droit."
m "Could you read it off the sign outside?"
l "It’s reversed, let me- Super. Morgue-"
"I watch the realisation land."
l "…Morgue."
m "Morgue."
l "Super. Morgue."
m "Super Morgue. There is a spelling mistake."
l "But-"
hide leeroy_shrug
show leeroy_sigh:
    xpos 0.05
    yalign 1.0
    zoom 0.5
"LeeRoy stares past me at his own sign, glowing red through the window."
l "…so that’s why the Methodist lady gave me an odd look."
"The brass bell over the front door chimes."
"Four teenagers spill inside. Heavy wool letterman jackets, saddle shoes, chewing gum."
"One girl is holding a Kodak Brownie camera."
"All of them are already laughing before the door swings shut behind them."
t1 "-no, look at it, I told you, it literally says morgue"
t2 "Take one of me under the sign. Take one of me playing dead under the sign."
"They cram into a corner booth, buzzing with the kind of excitement that spells trouble."
hide mc_annoyed
hide leeroy_sigh
show leeroy_main:
    xpos 0.55
    yalign 1.0
    zoom 0.5
"LeeRoy is on his feet."
l "Customers."
"(Calling out)"
l "Adelaide! Adelaide, customers!"
show adelaide_main:
    xpos -0.05
    yalign 1.0
    zoom 0.55
"Adelaide comes out of the kitchen with the exact look of someone who’d rather be anywhere else."
"She ties on a stained canvas apron anyway. She glares at LeeRoy."
a "I was doing the books."
l "Ōe! Ōe, could you come here for a moment!"
hide adelaide_main
show oe_main:
    xpos -0.08
    yalign 1.0
    zoom 0.5
"Ōe appears in the doorway so fast it’s like they stepped out of thin air."
o "I swept the floor earlier."
hide leeroy_main
show leeroy_sigh:
    xpos 0.7
    yalign 1.0
    zoom 0.5
l "The name! You were in charge of making the sign."
o "Yes."
l "It says morgue."
"(After a long moment of calm consideration)"
o "You said it out loud, and I worked with what I heard."
o "I do not always know which letters your language is going to demand."
l "My- your language-"
"(Already turning back toward the kitchen)"
o "I have work to do. Goodbye."
hide oe_main
hide leeroy_sigh
show mc_main:
    xpos 0.65
    yalign 1.0
    zoom 0.455
"I reach into my coat pocket, pull out the crumpled newspaper clipping, and slide it across the table toward LeeRoy."
m "That’s the name used in the paper, too."
l "What?"
m "It ran in yesterday’s edition. Front page of the local section, with a photograph of the sign included."
m "Even if you changed the sign, people will probably stick with the 'first' version."
"I tip my glass toward the booth where the teenagers are busy arranging themselves on the floor to look like corpses for the camera."
m "And frankly? It seems to resonate with the youth."
show adelaide_main:
    xpos -0.05
    yalign 1.0
    zoom 0.55
"Adelaide walks briskly past us on her way back from taking their order, sliding the handwritten ticket onto the kitchen pass without breaking her stride."
a "It isn’t the worst name he’s had."
hide mc_main
show leeroy_sigh:
    xpos 0.7
    yalign 1.0
    zoom 0.49
"(Instantly)"
l "We’re not talking about that."
a "I didn’t say which one."
l "We’re not talking about it."
hide leeroy_sigh
hide adelaide_main
show mc_main:
    xpos 0.65
    yalign 1.0
    zoom 0.455
"They scatter back to work. I watch them serve customers and feel a flicker of satisfaction. There’s potential here."
menu:
    "Ask Adelaide what the other name was.":
        show adelaide_main:
            xpos -0.05
            yalign 1.0
            zoom 0.55
        "I decide to push my luck and ask her."
        "She claims she swore a solemn oath never to say it out loud."
        hide adelaide_main
        show leeroy_blush:
            xpos 0.05
            yalign 1.0
            zoom 0.5
        "LeeRoy turns a shade of red I didn’t know the human body was capable of and suddenly finds something incredibly urgent to scrub at the far end of the counter."
        hide leeroy_blush
    "Ask LeeRoy what the diner is struggling with.":
        show leeroy_sigh:
            xpos 0.05
            yalign 1.0
            zoom 0.5
        "He rattles off a list-some things I’d already scribbled in my notepad, others I hadn’t even thought of."
        "Turns out running a diner is a messier business than I figured."
        hide leeroy_sigh
        show leeroy_main:
            xpos -0.1
            yalign 1.0
            zoom 0.5
        "I jot down a few ideas to help and slide the note across to LeeRoy. He gives me a grateful look."
        hide leeroy_main
        # [LISTEN +1]

show leeroy_main:
    xpos -0.1
    yalign 1.0
    zoom 0.5
"The teenagers finally clear out, leaving sticky coin trays and a tip big enough for LeeRoy to gawk at like it belongs in a museum."
hide leeroy_main
"One of the boys grabs a napkin with the diner’s logo and stuffs it into his letterman jacket, like a badge of honour."
"The girl with the camera hangs back outside, standing on the cracked parking lot."
"She holds the Kodak Brownie up to her eye, squinting through the viewfinder, and photographs the buzzing red neon sign over and over from different angles until the novelty finally wears off and she jogs to catch up with her friends."
"I watch them go from my spot in the vinyl booth, chin in my hand."
show oe_main:
    xpos -0.08
    yalign 1.0
    zoom 0.5
"A few feet away, Ōe stands at the far end of the counter, where the neon can’t quite reach."
"They’re still as a statue, watching them too."
o "More will come now."
"They keep staring out the window."
m "That's the idea, isn't it?"
"The silence between us feels heavy."
o "Yes. That is the idea."
"They turn back to the dark corner and start sweeping again, every movement slow and careful."
hide oe_main
"I look down at my open spiral steno pad."
"I tap the tip of my pencil against the paper for a second before I start writing."
"Among the scribbled drafts and interview notes, I write the word “morgue” and underline it twice, hard and deep into the page."
"I’ve got an idea."
# Scene 1: Dorothy's Apartment - Night
"I drop onto the sagging edge of the mattress, night robe still wrapped around my chin, trapping in the October chill."
"The fabric reeks of dust and cigarettes."
"No matter how many times I wash my hair, that smell clings to me like a bad habit."
"Downstairs, someone’s pushing a broom."
"Slow, steady, like they’re getting paid by the hour."
"That scuff-drag, scuff-drag of stiff bristles on linoleum has been going since I hauled myself up the stairs ten minutes ago."
"It’s the kind of sound that could drive a person mad."
"Whoever is down there sweeps like he’s never seen a broom before."
hide mc_main
show mc_annoyed:
    xpos 0.7
    yalign 1.0
    zoom 0.35
m "Who the hell writes notes on their hand?"
"Silence. Just the groan of the floorboards settling and that relentless scrape."
m "…like some schoolkid trying to cheat on a spelling test. Tsk."
"I finally peel off the gown and let it fall in a wrinkled heap on the floor."
"I’ll curse the creases tomorrow, but tonight, it’s the least of my worries."
"I cross the cramped room to the orange crates stacked in the corner-my so-called record cabinet."
"I flip through the sleeves, pretending I’m picking at random. I’m not."
"My fingers land on a battered label, edges frayed and soft."
"Cleveland, 1957. Muddy Waters."
"Four of us jammed into Jimmy’s old Buick, windows down, music spilling into the sticky night while we promised ourselves we’d change the world."
"I slide the record out, slap it onto the hi-fi, and drop the needle."
"It pops and hisses, then the bass rolls in."
"I twist the volume up past the point where any neighbour with sense would start banging on the pipes."
"Not that it matters. There’s nobody left to bother."
"Just the diner downstairs, and they already ruined my day."
"It’s not like they’ve got customers. The place is a ghost town."
m "Twenty-nine days. Twenty-nine days, and then I’m on a Greyhound out of here, and I am never looking back."
"I start pacing the threadbare strip of rug between the bed and the desk."
"Three steps, turn, three steps back."
"The typewriter waits in the shadows, a new blank page loaded, just daring me to try something."
m "I just don’t get it. Why open a restaurant if you don’t know how to run one?"
m "Why hire counter staff who can’t even mix a basic fountain drink?"
"I freeze, one foot hovering above the rug."
m "Why am I letting this get under my skin? It’s not my racket."
"I start pacing again, faster now, grinding a deeper groove into the rug."
"The slow blues on the hi-fi do nothing to ease my unrest."
m "I have less than a month to break the biggest story in this county."
m "I have the chief breathing down my neck, ready to banish me to the society pages… and here I am, stewing over the proper syrup-to-soda ratio."
"My hand’s already on the cold window frame before I realise I’ve stopped."
"I’m staring down at the neon sign buzzing against the brick outside."
"Red. Off. Red. Off."
"The letters bleed through the thin curtains and crawl across my ceiling."
"I yank the curtain shut, hard. The brass rings screech against the rod."
"I flop back onto the bed, sinking into the lumpy springs, staring up at the ceiling."
"The red light still sneaks through the gap in the curtain, painting long, bloody shadows across the room."
m "I am absolutely not getting involved."
"Downstairs, the sweeping cuts out."
"A heavy pause settles in, thick enough to choke on."
"Then the scrape starts up again. Scuff-drag. Scuff-drag."
hide mc_annoyed
# Scene 2: Vesper Falls Courier - Newsroom - Day
show mc_main:
    xpos 0.65
    yalign 1.0
    zoom 0.455
"Tuesday, Special of the Day: Cheeseburger"
"Click. Clack. My low heels echo on the scuffed linoleum as I cross the main room."
"Just a handful of desks jammed together, radiator hissing slow and steady."
"The Underwood in the corner clacks out a lazy rhythm, and the air is thick and yellow with old cigarette smoke."
"I shoulder through the frosted glass door into the editor’s office, coat slipping down my arms."
"Three pitches rattle in my head, each one practised on the walk over."
"Chet’s already there, sprawled in the corner chair, wingtips kicked up on a side desk."
"Cigarette hanging from his lip, ash dropping onto his wrinkled tie."
m "Mr Hollis, I’ve got a-"
b "Kessler. Good. Sit down."
"I drop into the stiff wooden chair across from him."
"He doesn’t bother looking up from the galley proofs."
"Just slides a ragged square of newsprint across the green desk blotter, eyes still down."
b "I want it by Friday."
"I pick it up and skim the ink."
"Tear-sheet from last night’s edition. A girl in a poodle skirt, roller skates, tray balanced outside a diner. Adelaide."
m "Mr Hollis, we already ran a photo spread on this joint yesterday. What exactly am I supposed to write about…"
b "It’s local colour. Human interest."
b "Get a quote from whoever runs the place, write something cute about the milkshakes, ask if they’re hiring. Keep it breezy."
c "Focus on the roller skates, Anne. The readers eat that stuff up."
"That’s not my name?"
hide mc_main
show mc_annoyed:
    xpos 0.7
    yalign 1.0
    zoom 0.35
"I whip around to face Chet, every muscle wound tight as a spring."
"I open my mouth, ready to wipe that smug look off his face."
b "Two hundred words."
hide mc_annoyed
show mc_main:
    xpos 0.65
    yalign 1.0
    zoom 0.455
"My jaw snaps shut. The fight drains out of me, puddling on the floor."
m "…Yes, Chief."
b "Good."
"He keeps talking, something about the point spread for the pennant race, but it all turns to static."
"I nod, stand up, and slip back to my cramped desk in the bullpen."
"I trade a few empty words with the switchboard girl, shrug my coat back on."
"Before anyone can toss me another fluff piece, I slip out the glass doors, quiet as a ghost."
# Scene 3: Courier - Stairwell - Continuous
hide mc_main
show mc_annoyed:
    xpos 0.7
    yalign 1.0
    zoom 0.35
"I barely make it to the landing before my feet lock up."
"My fist is so tight, my nails carve little half-moons into my palm."
"I glance down and pry my fingers open."
"The newspaper clipping is mashed into a damp wad, stuck to my sweaty hand."
m "Absolute garbage."
"I press the crumpled paper against the hallway wall, right where the plaster flakes off in chalky curls."
"I scrub at the cheap newsprint with my thumb, trying to smooth out the mess I made."
"The girl in the poodle skirt grins at me through the smeared ink, all teeth and empty eyes, like some cheerleader who got her brains scooped out and replaced with whipped cream."
"I stare her down for a beat."
"Then I fold the clipping in half, neat as I can, tuck it deep in my coat pocket, and head back toward the diner."
# Scene 4: Dorothy's Apartment - Day
"The old shortbread tin sits open on the kitchen table, jammed up against the heavy black Singer just to make enough room to work."
"Inside, a roll of crumpled bills sits pinched by a tired rubber band, barely thicker than a deck of cards."
"Next to it, the Greyhound timetable, creased and worn soft from being folded to the same page over and over. CLEVELAND - NEW YORK CITY."
"I count the money out on the Formica tabletop."
"Then I count it again, slower this time, smoothing down the dog-eared corners as if giving the bills a little more care might miraculously make them multiply."
m "Forty-one dollars."
"I glance at the fare printed on the timetable. The math runs through my head."
m "Eleven weeks. That's if I don't buy a single record, skip lunch on Tuesdays, and pray to God nothing in this room breaks."
"I shove the tin aside. The rent book waits underneath."
"I flip the cover back."
"The monthly rate is written in that same old-fashioned, looping cursive as the specials board downstairs. The number is low. The kind of low that reads charity."
m "…well, at least the rent’s cheap."
"It sounds even sadder when I say it out loud."
"I push my chair back and head to the window."
"The neon sign buzzes below, throwing a harsh red glare. Beyond that, the parking lot, all cracked asphalt."
"Empty. Not a single headlight out there. No surprise."
"Maybe it's the name that goes on forever, maybe it's the lousy service, but whatever it is, it keeps folks away from this place like it's contagious."
m "Nobody's eating there."
"I fold my arms tight against the cold seeping through the glass."
hide mc_annoyed
show mc_melancholy:
    xpos 0.7
    yalign 1.0
    zoom 0.35
m "But if this keeps up-"
"I glance back at the sad little tin on the table."
m "-then the diner goes under. And the building goes into foreclosure with it. And I lose the room."
"I drop onto the narrow windowsill, right beside my typewriter. The keys press cold against my arm."
m "And then the saving stops. And then there's no Greyhound to New York."
m "And then I'm stuck writing the women's page until I'm sixty, just like Hollis said... and mother asks me every single Christmas when I'm finally going to settle down."
"I fish the crumpled newspaper clipping from my coat pocket and smooth it out beside the typewriter."
m "…there are only so many excuses I can use."
"Somewhere below my feet, a heavy plate crashes to the floor."
"A second later, two voices drift up through the floorboards, laughing like it's nothing."
m "I have to keep the milkshake people in business."
hide mc_melancholy
# Scene 6: Dorothy's Apartment - Wednesday Evening
show mc_main:
    xpos 0.65
    yalign 1.0
    zoom 0.455
"Wednesday, Special of the Day: Cheesy Fries"
"Almost a whole day passed."
"I’m still in my good wool dress."
"I put it on this morning to chase a lead at the municipal records office, which turned out to be a whole lot of nothing."
"If I unzip it now, that’s me surrendering to the day."
"I’m sprawled sideways in the lumpy armchair, paperback balanced on my knee."
"In the corner, a jazz record spins, low and steady."
"Suddenly, the brass section warps."
"The pitch slurs down in a long, sick groan, and then the turntable gives up."
"The reading lamp flickers out."
"Outside the window, the harsh red glare blinks out."
"Now the room is swallowed by real, honest darkness."
hide mc_main
show mc_annoyed:
    xpos 0.7
    yalign 1.0
    zoom 0.35
m "Oh, come on."
"I sit in the dark for a second, waiting for the grid to come back. It doesn’t."
"Then there’s a knock at my door. Three taps. Precise, sharp, spaced out just so."
"I blindly feel my way across the room, bump my hip against the edge of the desk, and pull the door open."
show oe_main:
    xpos -0.08
    yalign 1.0
    zoom 0.5
"Ōe stand in the drafty hallway, holding a thick wax candle."
"It isn’t lit."
"They look at me. They just keep looking at me."
"The silence stretches out."
"It passes comfortably, sails right past awkward, and settles somewhere on the far side into a stillness that Ōe appears to find perfectly pleasant."
o "Your dress is nice, Miss."
"I stare at the unlit wick in their hand, then up at their unblinking face, lit by the thin light from the hall window."
m "…Is this all you came up here for?"
o "I thought you liked engaging in small talk."
m "…"
o "The power is out."
m "Yes. I noticed. It’s your building, isn’t it?"
m "You should just go downstairs and flip the breaker switches back on."
o "I do not know how."
"I close my eyes and let out a slow breath."
"My father was always too busy for housework, and my mother wouldn’t touch anything with a wire for fear it might hurt."
"So, the job of handyman landed on me. I know a thing or two about power outages."
"I open my eyes."
"Ōe is still standing there in the dark, looking at me with the calm patience of a house cat waiting for a door to open."
m "Lead the way."
# Scene 7: Basement - Continuous
"I have to really lean into it to get the basement fuse box open."
"The metal door groans, rust flaking off under my hands."
"I strike a match against the wall-Oe just stands there, holding the candle."
"I get the wick lit, drip some wax onto a shelf, and jam the candle in place."
"My sleeves go up past my elbows. No sense getting them dirtier than they already are."
"Ōe’s eyes are glued to my hands. I can feel it, pressing down on my skin."
"If I looked up and met their stare, I’d probably lose my nerve, so I keep my eyes locked on the fuses and pretend I don’t notice."
m "It’s the back circuit. Look at this wiring. The casing is practically scorched."
o "The freezer."
m "You put the freezer on its own dedicated line?"
o "It has to stay very cold."
m "Well, yeah. That’s the general idea of a freezer."
"The silence stretches."
o "Yes."
"I grab the heavy metal lever and throw the main."
"Somewhere deep in the back of the kitchen, a massive compressor violently coughs awake, and the overhead bulbs in the hall flicker to life, buzzing with a yellowish glow."
"Ōe blinks at the glare, but it’s a second too late-like he forgot how. It makes my skin crawl."
m "There. But you need to call an electrician to rewire this panel before this whole building goes up in smoke."
"I wipe my hands on a rag, grime smearing across the fabric."
"I peek through the doorway. The diner’s empty. Are they even open?"
m "Where is everybody, anyway? It’s Wednesday night."
o "LeeRoy is out. He drives at night."
m "Drives where?"
o "Around."
m "And Adelaide?"
o "Out on business."
m "I don’t follow."
o "Please do not concern yourself with it, Miss."
menu:
    "Push it.":
        m "Shouldn’t concern myself with what?"
        "Ōe don’t answer."
        hide oe_main
        show oe_smile:
            xpos -0.13
            yalign 1.0
            zoom 0.52
        "They just keep smiling at me-a thin, polite, utterly dead smile."
        "I wait for them to elaborate, but they don’t blink, don’t shift their weight."
        "Are they even breathing?"
        "After a full, agonising minute of that stare, my nerves finally fray. I give up."
        hide oe_smile
    "Let it go.":
        "I snap my mouth shut and let the silence hang, deciding to match his rigid energy."
        "We stand there in the buzzing hallway, locked in an excruciating standoff."
        "Finally, Ōe tilts his head a fraction of an inch."
        o "Thank you for fixing the lights, Miss."
        "I give a curt nod."
        # [LISTEN +1]

show oe_main:
    xpos -0.08
    yalign 1.0
    zoom 0.5
"I turn for the stairs, hand landing on the bannister, but I stop short."
o "We will let LeeRoy know about the electrical issue. Would a free meal tomorrow be sufficient payment for your labour?"
m "That would be lovely. Does that include coffee?"
o "Yes."
m "…Right. Good. Good night."
"I tug my dress close and head up the stairs."
hide oe_main
hide mc_annoyed
# Scene 8: The Supermurgidroid Weepie - Thursday
show mc_main:
    xpos 0.65
    yalign 1.0
    zoom 0.455
"Thursday, Special of the Day: Onion rings"
"I slide into my usual booth."
"True to Ōe’s word, a heavy porcelain plate with a cheeseburger and a thick mug of black coffee is already waiting on the Formica tabletop."
"I stare at the plate. Something about it is just wrong. Deeply, fundamentally wrong."
"The bun is cold. Texture feels a little clammy when I poke it."
"The patty is a sickly, uniform grey."
"Not browned, not seared, just wet and pale, like it was boiled by mistake."
"There’s a single limp leaf of iceberg lettuce sitting right in the middle. A tragic little hat."
show leeroy_shrug:
    xpos 0.05
    yalign 1.0
    zoom 0.5
"LeeRoy is on the other side of the counter, hands behind his back, rocking on his heels."
"He looks like he might vibrate right out of his shoes."
l "Well? What do you think? On the house, just like promised."
"I pick up the burger. The bottom bun is damp. I take a bite. Chew."
hide mc_main
show mc_annoyed:
    xpos 0.7
    yalign 1.0
    zoom 0.35
"It’s like biting into a wet kitchen sponge."
"My face twists through a whole routine before landing on a scowl. I spit it out on the plate. Are they trying to poison me?!"
m "LeeRoy. Who made this?"
hide leeroy_shrug
show leeroy_main:
    xpos -0.1
    yalign 1.0
    zoom 0.5
"(Beaming proudly)"
l "I did!"
m "What in God's name have you done to it?"
hide leeroy_main
show leeroy_sigh:
    xpos 0.05
    yalign 1.0
    zoom 0.5
"(His smile faltering slightly)"
l "Just the usual. I cooked the meat until it was done."
m "And how exactly do you know when ground beef is done, LeeRoy?"
"A long, terrible pause stretches across the empty diner. He just blinks at me."
l "…Well. I. Uh. When it stops being red?"
"I drop the rest of the burger onto the plate. It lands with a wet, sad thud."
"I slide out of the booth and stand, smoothing my skirt."
m "Right. That's it. This is a culinary felony."
l "Where are you going?"
m "Behind the counter."
l "Wait, Miss Kessler, you can't go behind the-"
"I shove through the swinging wooden gate before he can finish, march right past him, and head for the kitchen."
hide leeroy_sigh
hide mc_annoyed
# Scene 9: Diner Kitchen - Continuous
show mc_main:
    xpos 0.65
    yalign 1.0
    zoom 0.455
"I know my way around a kitchen."
"I move through the cramped kitchen fast."
"I yank open the under-counter icebox, pop the lids off stainless steel prep pans, and make noises of genuine, unfiltered disgust."
show leeroy_sigh:
    xpos 0.05
    yalign 1.0
    zoom 0.5
"LeeRoy trails closely behind me, hovering over my shoulder like an anxious duckling."
hide leeroy_sigh
show adelaide_main:
    xpos -0.05
    yalign 1.0
    zoom 0.55
"Adelaide appears in the doorway, leaning against the frame with her arms folded, watching the show with detached interest."
m "The griddle is ice cold."
hide adelaide_main
"I slam the drawer shut and snatch up the red plastic squeeze bottle."
m "Why is the ketchup warm? Why is it sitting next to the radiator? And what-"
"I grab the glass percolator off the back burner and give it a cautious sniff."
"Instantly, I regret it. It smells like burnt tyres."
m "-is this Monday's coffee?"
show leeroy_sigh:
    xpos 0.05
    yalign 1.0
    zoom 0.5
l "We keep it on a low simmer. Just in case somebody comes in."
m "If they did, you’d put them in the hospital."
"I wheel on him, pointing a grease-stained spatula directly at his chest."
m "Have any of you ever actually worked in a kitchen? Any of you?"
"Silence drops over the room."
hide leeroy_sigh
show adelaide_main:
    xpos -0.05
    yalign 1.0
    zoom 0.55
"Adelaide suddenly finds a water stain on the ceiling absolutely fascinating."
hide adelaide_main
show leeroy_sigh:
    xpos 0.05
    yalign 1.0
    zoom 0.5
"LeeRoy studies the scuff marks on his saddle shoes."
m "Right. Grab an apron. Watch me."
hide leeroy_sigh
# MONTAGE
"I dump Monday's coffee sludge down the drain. It hits the stainless steel sink thick as motor oil."
"I march out to the dining room with a stick of white chalk."
"Ōe’s beautiful, antique cursive gets wiped away, replaced by my own ugly scrawl."
"At least you can read it from the street."
show oe_main:
    xpos -0.08
    yalign 1.0
    zoom 0.5
"Ōe stands by the jukebox, staring at the board with a look I can't decipher."
"Back in the kitchen, I crank the griddle up to three-hundred-and-fifty degrees."
hide oe_main
show leeroy_main:
    xpos -0.1
    yalign 1.0
    zoom 0.5
"I teach LeeRoy how to season a patty."
"He tries his earnest best to follow my lead, but he's shaping the raw ground beef far too gently."
m "LeeRoy, it's not the Queen of England. Smash it flat."
hide mc_main
show adelaide_main:
    xpos 0.6
    yalign 1.0
    zoom 0.55
hide leeroy_main
"Adelaide drifts in, grabs the Morton salt, and heads for the boiling potatoes."
"I snap my fingers-last week's salt disaster still fresh in my mind."
"She freezes, rolls her eyes, sets the salt down with a sharp click, and waits, arms crossed, for my demonstration."
hide adelaide_main
"For the next three hours, I put them through the basics."
"How to blend a malt. How to sear a burger so it doesn't look like a wet sock. How to fry onions without burning them."
"Soon, the whole diner smells like caramelised onions and beef fat, not floor wax."
"For once, it actually smells like a place someone might want to eat."
"But something feels off."
"All afternoon, LeeRoy doesn't taste a thing."
"Not a fry, not a sip of milkshake, not even a crumb of beef."
"He watches me taste, asks a million questions about flavour and texture, scribbles everything down in a brand-new notepad."
"But every time I shove a tasting spoon at him, he dodges."
"He ate a huge lunch before I came down. Sensitive stomach, he says. He trusts my palate."
"Or maybe he's on some new health kick his friend's friend swears by."
"He says it all so earnestly, I can't even argue. I just shake my head and keep cooking."
# Scene 10: The Supermurgidroid Weepie - Evening
"The specials board finally makes sense through the window, bold chalk letters lit up by the streetlights."
"The counter shines."
"Under the heat lamp, there’s a cheeseburger, fresh off the griddle."
"The bun is golden."
"The American cheese has melted just right, dripping over the patty’s edge."
"For once, it looks like food. Better yet, it smells like food too."
"I step back from the pass and wipe grease from my forehead with my wrist."
"I’m out of breath, cheeks burning from the griddle’s heat, and I can’t help grinning."
"I cross my arms tight, trying not to let it show."
show mc_annoyed:
    xpos 0.7
    yalign 1.0
    zoom 0.35
show leeroy_main:
    xpos -0.1
    yalign 1.0
    zoom 0.5
"LeeRoy leans over the counter, staring at the burger like it’s the Crown Jewels."
l "It looks... it looks exactly like the magazine advertisements."
m "That's because that is what a hamburger is actually supposed to look like, LeeRoy."
"He pulls his eyes away from the plate and turns to me."
l "Where did you learn to cook like that?"
"The question hits me right under the ribs. I stare hard at the chrome napkin dispensers."
m "Reading. I, uh... I used to read a lot of Betty Crocker cookbooks growing up."
"A flimsy half-truth."
"I spin on my heel, yank off the stained apron, and toss it onto a stool."
m "Look, I have to write some hundred words about this diner by Friday."
m "I’d rather not have to write a piece about a tragic municipal foreclosure. That's all."
hide leeroy_main
show adelaide_main:
    xpos -0.05
    yalign 1.0
    zoom 0.55
"Adelaide sits in the corner booth, eyes glued to her ledger."
"She doesn’t even look up, just turns a page."
a "Mm."
"I don’t stick around to defend myself."
hide adelaide_main
"I shove through the swinging gate and head up the narrow stairs to my room."

return
