# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Dorothy")
define a = Character("Adelaide")
define l = Character("LeeRoy")
define o = Character("Ōe")
define b = Character("Mr. Hollis")


# The game starts here.

label start:

"Monday, Special of the Day: Strawberry Milkshake"
"The tape starts to play. A drum fill. Then brass."
"TITLE CARD slashes across the screen in hot pink, cutting perfectly to the rhythm of the music."
"Black-and-white stock footage flashes by: A lonely two-lane highway. A rusted water tower."
"A stifling church social with kids in incredibly tacky frilly dresses."
"A row of identical front porches with perfectly cut lawns."
"A woman in a pressed apron, waving mindlessly at nothing."
"The footage is beautiful, but lacks substance. A soul. It's just so… ordinary. Mundane."
"The music cuts out mid-phase. A postcard is shown on the screen."
"VESPER FALLS, OHIO - SEPTEMBER 1962"
"A telephone rings. The shrill sound tears through the silence."
"I bolt upright."
"The room smells of stale coffee and aerosol hairspray, and as far as my eye can see, it’s in a state of chaotic disarray."
"Outside my window, dead in the daylight, the diner downstairs is already bleeding its aggressive neon sign through the curtains:"
"THE SUPERMURGIDROID WEEPIE."
show mc_annoyed:
    xalign 1.0
    yalign 1.0
    zoom 0.4
"I swing my legs out of bed and immediately trip."
"My foot catches on a pile of thrifted clothes I tossed onto the scorch mark on the carpet."
"I stumble forward, barely catching my balance."
"I weave through the room, passing a hissing radiator and orange crates stacked high with my prized rock-and-roll vinyls."
"I pass the kitchen table, the current domain of my sewing machine."
"There's a half-finished hem pinned down that I've been telling myself to stitch since last week."
"On the windowsill, my secondhand Royal Quiet De Luxe typewriter sits poised with a blank page."
"Waiting for me to finish up my next grandiose story that will finally hit the mark. Surely."
"A stray sock lies abandoned on the floorboards."
"I snatch it up without breaking stride, tossing it aside as I lunge for the heavy rotary phone."
hide mc_annoyed
show mc_main:
    xalign 1.1
    yalign 1.0
    zoom 0.52
m "Courier, Kessler - ah, I mean. Hello, Dorothy speaking."
b "Dorothy."
"His voice is unhurried. Almost too calm. My jaw clenches tight."
hide mc_main
show mc_annoyed:
    xalign 1.0
    yalign 1.0
    zoom 0.4
m "M-Mr. Hollis."
b "I'm giving Chet the Glenn piece."
m "T-The… I pitched that. Multiple times. A-And I already have the Mercury press packet, a source at Lewis-"
b "Dorothy."
"There's a pause."
b "Dolly. I've already made up my mind."
"I flinch at the pet name."
m "With all due respect, Chet spells orbit with two t's."
b "Your hatred toward that man is getting old."
m "I refuse to write any more columns for the women's page."
"The man on the other line lets out an exhausted sigh."
b "You want to play a journalist? Be my guest. I'm giving you a month."
b "Bring me something worthy of being put on the front page. A story that can sell."
b "And then we can talk about moving you off the women's page."
m "And if I fail?"
b "You'll write about every wedding, yard sale, and Garden Club, and you'll stop being a nuisance about it."
"Click. The line goes dead."
"I stand there, my hand clutching the receiver. The dial tone hums against my ear."
hide mc_annoyed
show mc_angry:
    xalign 1.0
    yalign 1.0
    zoom 0.4
m "The nerve of that man! I have filed at least a hundred pieces, and only one of them had to have a correction."
m "So what if it happened to be the most important one?!"
m "For the love of god, Chet put a dead woman's name on a wedding announcement in June, and nobody said as much as boo-"
"I slam the receiver back onto the cradle. All the fight drains out of me, exchanged for existential dread."
hide mc_angry
show mc_main:
    xalign 1.1
    yalign 1.0
    zoom 0.52
"I force my face into the tight smile aimed at precisely no one. I've been using it far too often lately."
m "You want a story? Fine. I'll give you one."
menu:
    "Call my Friend":
        "I pick up the receiver. My fingers dial the all-too-familiar number."
        "It rings and rings. She doesn't pick up."
        "I put the phone back down."
        hide mc_main
        show mc_annoyed:
            xalign 1.0
            yalign 1.0
            zoom 0.4
        m "Must be at the shop already."
        hide mc_annoyed
        show mc_main:
            xalign 1.1
            yalign 1.0
            zoom 0.52
        "Unwilling to do any real writing, I decide to clean up my room—at least a little."
    "Get to Work":
        "I stretch, adjust the pencil in my hair, and sit down at my typewriter."
        "I commit to writing about the upcoming celebration that's to take place in the square."
        "Why is this city so obsessed with corn?"

"I collapse backwards onto the mattress, the worn springs groaning in protest."
"In my hand is yesterday's edition of the Vesper Falls Courier."
"I read—no, I consume the text, chewing through the column the way other people chew their overcooked bacon."
"I snap the broadsheet open, the scent of black ink briefly cutting through the stale air of my apartment."
"Perhaps I should open the windows. Later."
hide mc_main
show mc_annoyed:
    xalign 1.0
    yalign 1.0
    zoom 0.4
"And there it is. Glaring at me, sprawled a ridiculous four columns wide."
"NEW EATERY OPENS ON ROUTE NINE - THE SUPERMURGIDROID WEEPIE" 
"PROMISES ROLLER SERVICE, OPEN LATE HOURS"
"I stare at the headline for a long, agonising moment."
"The bold typeface seems set on making my brain hurt."
m "… such riveting news."
"I flip the page. The crisp paper crinkles as I turn it back."
"I trace the letters with my nail, just to confirm I’m not hallucinating."
m "All it apparently takes is slapping skates on teenage girls, and you're ready for the front page of a newspaper. Ugh."
"I flip over to page four, glaring at a tiny column tucked next to a sprawling advertisement for a Hoover vacuum cleaner."
"It promises to clean all my worries!"
m "First American to orbit the Earth."
"I chew my lip."
m "Three times around and then made a safe landing. And they reduced his latest speech to a… footnote."
"A thought crosses my mind."
m "I wonder if it's because he chose Florida."
"I let my head fall back against the mattress, staring up at the water-stained ceiling—"
"—which is, practically speaking, a very good analogy to the current state of my life."
m "Overshadowed by a diner,"
"I mumble."
"I lift the paper again."
"My eyes keep snagging on that absurd, borderline-offensive string of letters."
"It makes my editorial senses itch."
m "The Supermurgidroid Weepie…"
"I try sounding it out."
m "The Super-murgi-droid. Weepie."
"I lower the newspaper, squinting at the red neon light currently invading my personal space with a red glow."
m "Who looked at that name and said yes?"
"Upset, I toss the Courier aside."
"It hits the edge of the blanket and slides off, hitting the floorboards with a sad, dull thwack."
"I leave it there for precisely two seconds before I rethink my actions."
"Then, I groan, lean precariously over the edge of the bed, and retrieve it."
"Because no matter how furious I am at the world, I simply cannot leave a newspaper on the floor."
#Scene 2 Dorothys Apartment - Afternoon
hide mc_annoyed
show mc_main:
    xalign 1.1
    yalign 1.0
    zoom 0.52
"The afternoon sun bakes the cramped room, casting long, mocking shadows across the floorboards."
hide mc_main
show mc_annoyed:
    xalign 1.0
    yalign 1.0
    zoom 0.4
"I pace. Three fast steps across the rug. Pivot. Three steps back."
"I gnaw on the edge of an already-ruined thumbnail, my eyes constantly darting back to the typewriter."
"The floor is currently a graveyard for six violently crumpled balls of paper."
"In the carriage of the secondhand Royal, the seventh page sits waiting. It is blank."
"I start thinking out loud, my voice bouncing off the peeling wallpaper."
"Talking out loud helps me sort my thoughts faster."
m "Okay. Dorothy, think. Think. What was the last rumour floating around?"
m "Right, the farmers' auction. Every town has dirty money. Somebody is definitely crooked..."
m "... but I don't know the first thing about livestock. They wouldn't trust a woman either."
"Three steps. Pivot. I keep pacing."
m "A story on the mayor? No."
m "Everyone knows Mayor Lindqvist cries at parades like his life depends on it. That's not news."
"I pull the steno pencil from my hair, twirling it furiously through my fingers."
m "The machine plant. The line workers have been causing trouble at the tavern lately."
m "Maybe there’s a strike brewing. Dad works the floor; he'd definitely know something..."
"I let out a hollow, humourless laugh, gesturing wildly at the empty room with my pencil."
m "Except he’d rather take a bullet than snitch on a soul."
hide mc_annoyed
show mc_main:
    xalign 1.1
    yalign 1.0
    zoom 0.52
"I force myself to stand perfectly still."
"The sheer desperation is starting to leak into my voice, and I absolutely hate the sound of it."
m "I have one month. That's plenty of time! I don't have to figure it all out today."
"And then, right beneath my feet, the floorboards vibrate."
"An argument is breaking out downstairs in the diner."
"It’s muffled by the wood and plaster, but the furious cadence is unmistakable."
"Two distinct voices, rapidly escalating in volume."
hide mc_main
show mc_annoyed:
    xalign 1.0
    yalign 1.0
    zoom 0.4
"I glare down at the floor."
"Instantly, the tight, suffocating knot of anxiety in my chest hardens into a sharp spike of righteous fury."
m "I cannot WORK in this ruckus."
"Downstairs, the shouting spikes."
"A second later, a massive CLANG echoes through the floor as something large and metallic violently crashes over."
"By the time the noise stops, I am already reaching for my shoes."
# Scene 3. The Supermurgidroid Weepie - Evening
hide mc_annoyed
show mc_angry:
    xalign 1.0
    yalign 1.0
    zoom 0.4
"I push through the heavy doors at a brisk pace, my winter coat thrown hastily over my nightgown."
"I still have a steno pencil tucked in my hair."
"I am entirely, resolutely prepared to interrupt somebody's evening."
"The diner is a pristine, bright shrine to chrome and checkerboard linoleum."
"There are images hung on the back wall, paintings; someone also hung a katana there."
"It's an assortment of varied art, featuring a surprising amount of cars."
"'Cars are cool', reads one of the posters. How... interesting."
"Eight booths line the walls in bright red vinyl. All of them empty."
"In the corner sits a jukebox that nobody has bothered to plug in yet."
"Behind the counter, the specials board proudly reads MONDAY: STRAWBERRY MILKSHAKE in an elegant, sweeping cursive that looks like it belongs on a 19th-century treaty, not a diner menu."
"Two milkshakes sit on the counter like evidence at a high-stakes trial."
"Standing over them is the duo responsible."
hide mc_angry
show adelaide_main:
    xalign 0.0
    yalign 1.0
    zoom 0.55
show leeroy_sigh:
    xalign 1.0
    yalign 1.0
    zoom 0.55
"LEEROY looks to be in his early twenties."
"He is African-American, wears a paper hat with dreads tucked underneath in a ponytail."
"Before I have the chance to assess his appearance further, he gestures animatedly with a long metal spoon."
"Beside him is ADELAIDE."
"She looks late twenties, immaculate, and is wearing expensive, sharp-heeled shoes."
"She also wears a diner apron, though her expression strongly suggests the apron was not her idea."
"Her arms are tightly folded."
l "- it's about balance, Adelaide. You can't just put cold things in a cup and call it a beverage-"
a "I followed the card."
l "Like a hostage."
hide leeroy_sigh
hide adelaide_main
show mc_annoyed:
    xalign 1.0
    yalign 1.0
    zoom 0.4
"I march right up to the chrome counter."
m "It is twenty past nine. I am trying to sleep and yet, and I can hear every single-"
hide mc_annoyed
show adelaide_main:
    xalign 0.0
    yalign 1.0
    zoom 0.55
show leeroy_main:
    xalign 1.0
    yalign 1.0
    zoom 0.55
"I stop. Both of them have turned to look at me."
"They do not look guilty. Nor do they look annoyed that I barged into their conversation."
"The man looks at me with sheer, unadulterated delight."
l "A customer!"
show adelaide_main:
    xalign 0.0
    yalign 1.0
    zoom 0.55
a "She's not a customer, Leeroy. She's the upstairs."
l "But she can be the judge!"
hide adelaide_main
hide leeroy_main
show mc_annoyed:
    xalign 1.0
    yalign 1.0
    zoom 0.4
m "I beg your-"
hide mc_annoyed
show mc_annoyed:
    xalign 0.0
    yalign 1.0
    zoom 0.4
show leeroy_main:
    xalign 1.0
    yalign 1.0
    zoom 0.55
"(already sliding both frosted glasses down the counter toward me)"
l "Help us determine which milkshake is better."
hide mc_annoyed
show adelaide_main:
    xalign 0.0
    yalign 1.0
    zoom 0.55
a "Leeroy, why are you dragging her into-."
hide leeroy_main
show mc_annoyed:
    xalign 1.0
    yalign 1.0
    zoom 0.4
"I look at the milkshakes. I look at the door I just came through. I look back at the milkshakes."
"I strongly dislike milkshakes."
"I think of them as dessert pretending to be a drink, and I consider anyone who orders them to be, well, children."
"But I am exhausted, and I just want the bickering to stop."
m "Fine. Fine! Just because I want to sleep this century,"
"I say, sitting on a stool."
"I take LeeRoy's glass. I take a reluctant sip."
hide adelaide_main
"It is genuinely not bad. Not great either, but it's not like I'm an expert on the things I dislike."
m "Hm."
hide mc_annoyed
show mc_annoyed:
    xalign 0.0
    yalign 1.0
    zoom 0.4
show leeroy_main:
    xalign 1.0
    yalign 1.0
    zoom 0.55
l "You see? That's the ratio right there. Four parts to one."
l "You get the cold hitting you up front, and then it comes back around on you, sweet at the back, like a-"
"He delivers this entire speech with total, sweeping conviction."
"But it sounds off. Has he been rehearsing it?"
"It sounds far too polished, like words you'd find in a novel rather than spoken."
m "It's fine. An… average milkshake."
hide leeroy_main
hide mc_annoyed
show mc_annoyed:
    xalign 1.0
    yalign 1.0
    zoom 0.4
show adelaide_main:
    xalign 0.05
    yalign 1.0
    zoom 0.55
"I reach for Adelaide's glass. I take a sip."
"I freeze as my taste buds are deeply shocked—my entire face changes, scrunches."
"My soul takes a brief vacation."
"I pull the glass away from my mouth and set it back on the counter very, very slowly as I struggle to keep a neutral face."
m "What is in that?"
a "Strawberries. Milk. Ice."
m "There's something else."
a "Salt."
m "How… much salt?"
a "The card said a pinch."
m "And… how much did you use?"
a "A pinch. I don't know how much a pinch is. I used what I could pick up."
"A long pause. I stare at her perfectly manicured hands."
m "Have you tasted it?"
a "I'm not feeling like drinking dairy."
hide mc_annoyed
hide adelaide_main
"And then, from directly behind them, a voice speaks from the shadows at the end of the counter."
o "She is right about the salt."
"I flinch and spin around."
show oe_main:
    xalign 1.0
    yalign 1.0
    zoom 0.5
"Another person has been standing there the entire scene. In the dark. Perfectly, impossibly still."
"They are holding a broom in one hand, but they hold it gracefully like a butler rather than a cleaner."
"They do not blink. They do not shift their weight as they address me."
"They haven't moved a single muscle since before I walked in, and I am only now, startlingly, aware that they were there at all."
hide oe_main
show mc_annoyed:
    xalign 0.9
    yalign 1.0
    zoom 0.4
show oe_main:
    xalign 0.05
    yalign 1.0
    zoom 0.5
m "How long have you been sta-"
o "Yes."
m "That's not... that isn't an answer to that question."
"Ōe considers this. Seriously."
"As though regular social interaction is a puzzle they haven't quite solved yet."
"They do not produce a second answer."
hide oe_main
menu:
    "Give them the whole lecture.":
        "I cross my arms and deliver my unexpected food criticism."
        "It's pointed, it's witty, and I humble them both to the core."
        "How dare they disturb my peace and then serve such an unfortunate milkshake to me!"
        "I pay good money for this room, and as landlords they're certainly not delivering."
    "Ask what they were actually arguing about.":
        "The frustration seeps out of me."
        show leeroy_sigh:
            xalign 0.0
            yalign 1.0
            zoom 0.55
        "I ask, and LeeRoy admits, deflated, that nobody has come in since they opened."
        l "Well, they did the first time, but for some reason customers are not returning."
        hide mc_annoyed
        show adelaide_main:
            xalign 1.0
            yalign 1.0
            zoom 0.55
        "Adelaide looks away and says, quietly,"
        a "He wanted tonight to go well."
        # [LISTEN +1]
hide adelaide_main
show mc_annoyed:
    xalign 1.0
    yalign 1.0
    zoom 0.4
"Either way, I end up giving LeeRoy some practical advice—less syrup."
"Chill the glasses first."
"Under no circumstances let Adelaide near the salt shaker."
"Perhaps she should be banned from using salt altogether."
hide leeroy_sigh
show leeroy_main:
    xalign 0.0
    yalign 1.0
    zoom 0.55
"LeeRoy writes it all down."
"He has no pen and thus resorts to scribbling ink on his hand."
"I consider giving him one of my papers, but then—he should have enough money to afford his own writing supplies."
m "Right. Wonderful. Delighted to help. Now if you'd be so kind, I'm intending to return to sleep."
hide leeroy_main
"I stand up, pulling my coat tighter around my nightgown."
"I am halfway out the door when the voice stops me."
show oe_main:
    xalign 0.0
    yalign 1.0
    zoom 0.5
o "Miss Kessler."
"I freeze. I slowly turn around."
"I don't recall introducing myself to them."
"Then again, if they're affiliated with the landlord, it makes sense they would know of me."
o "Sleep well."
"A quiet silence spreads between us."
m "...thank you."
hide oe_main
"I push the door open and leave."
"It swings shut behind me, drowning out the rest of their conversation."
hide mc_annoyed

    # This ends the game.

jump mainroute2
