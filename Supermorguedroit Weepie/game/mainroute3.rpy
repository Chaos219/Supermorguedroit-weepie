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

"Friday, Special of the Day: Vanilla Milkshake"
"I take the stairs two at a time, a manilla envelope tucked securely under my arm."
"I am racing the clock to beat the Friday morning layout, moving so fast I nearly plough straight into Adelaide the second I step out the back door."
"She is standing rigidly in the narrow, shrinking strip of shade along the brick wall, desperate to keep out of the morning sun."
"She is clutching a heavy wooden crate overflowing with soiled aprons and grease-stained dish rags."
"She does not look pleased. In fact, she looks ready to commit a felony."
m "Whoa sorry, sorry"
"(Not moving a single inch out of the shadows)"
a "It is fine. I am just seeing to the linens."
"(Stopping, shifting the envelope under my arm)"
m "You’re in charge of quite a lot of things around here, aren’t you? Waitress, accountant, charwoman…"
a "It appears so. LeeRoy’s orders."
m "Well, yes. I get it. He’s the boss."
m "Believe me, Adelaide, I know exactly what it’s like to have some overbearing man barking orders at you while you do all the actual heavy lifting"
a "He is not my boss."
"A beat. The rhythmic hum of the street traffic seems to drop away for a second."
m "…He’s not?"
a "I bought this building."
"She says it with a quiet, venomous dignity."
a "I own the griddle. I own the vinyl booths."
a "I own the jukebox, that hideous neon sign, the napkins, all of it."
a "Every single dollar in that room came directly out of my private account."
a "And yet, here I am, Mon Dieu, hiding in an alleyway, hauling filthy rags like a common scullery maid because I did not want to argue with him about the division of labor."
"I just stare at her."
"Somewhere deep behind my ribs, the hard-nosed reporter wakes all the way up."
"The bloodhound catches a scent."
"The entire power dynamic of the diner suddenly flips upside down in my head."
m "Wait. You’re the money?"
a "I am the money."
m "And he doesn’t"
a "He knows. He is simply very…"
"She stops. She looks down at the crate of dirty laundry, searching for a word that isn’t outright cruel."
"For all her aristocratic venom, she can’t quite bring herself to completely bury him."
a "forgetful. He gets caught up in the performance of it all."
"I turn on my heel. The manila envelope can wait ten minutes."
"I reach out and grab the heavy brass handle of the diner’s back door."
a "Miss Kessler"
"(Looking over my shoulder, tossing my coat onto a nearby crate and aggressively rolling up my sleeves)"
m "Oh, ho ho. Sit tight, Adelaide. Let me handle him."
a "I didn’t ask you to"
"The heavy door is already swinging shut behind me."
#Scene 12: Diner Kitchen - Continuous
"I cross the checkered linoleum like a summer thunderstorm."
"Now that I know Adelaide holds the deed to the building and by extension, the lease to my room upstairs LeeRoy holds absolutely zero authority over me."
"I am entirely untouchable, and I am SO ready to crack heads."
m "LeeRoy. Have a minute?"
l "Miss Kessler! Do you want to see the sear on these"
m "Is it true that Adelaide owns this building?"
l "Well… yes."
m "Then why in the name of God did you send the SOLE financial backer of this establishment out into the alley to do the LAUNDRY?"
"Silence settles over the kitchen. I watch the gears in his head slowly grind into motion."
l "…Oh. Well. I..."
"His face drops. Genuine, profound guilt washes over him."
l "You’re..m Miss Kessler, you're completely right. I shouldn't have even asked her! ADELAIDE! Addie, could you come back inside, please?"
"Adelaide steps through the back doorway, her voice flat and exhausted."
a "I am already here."
l "I am so sorry. I am so, so sorry, I made you put those down. Put that crate right down on the floor. ŌE!"
"Ōe materializes at the end of the counter."
"You could've sworn the space they're standing at was entirely empty a second ago."
l "Ōe, could you handle the dirty linens, please?"
o "Yes."
"They take the heavy wooden crate from Adelaide without a single change in expression and vanish toward the basement."
"I turn back to face Adelaide with a smile. I spread my hands wide, in a very 'told you so' manner."
l "There. Fixed."
"And he spins right back around to his sizzling griddle, armed with completely untroubled belief that he has just solved the systemic power imbalance of the entire restaurant."
"Adelaide and I stand beside him in the kitchen. We look at him. Then we look at each other."
"Adelaide raises a hand to rub her temples."
a "That is the tragedy of it. He isn't malicious... He just… he does not think things through."
"She adjusts her posture, lets out a long, long-suffering sigh, and drifts back out to the dining room to tend to her ledger books."
menu:
    "Push LeeRoy harder.":
        "I am not letting him off the hook that easily."
        "I march over and corner him by the kitchen pass, ready to give him a piece of my mind about the principles of delegated labor."
        "But before I can even wind up, he starts apologizing again."
        "He apologizes to me, he apologizes to Adelaide despite her not being present, he apologizes to the spatula."
        "He is so relentless with his apologies that I run out of righteous anger before he runs out of breath."
    "Ask Adelaide why she doesn't just say no.":
        "I walk out to the dining room and lean over her booth."
        m "So, if you're the owner…"
        "I whisper."
        m "Why don't you just refuse him?"
        "She doesn't look up, her fountain pen scratching smoothly across the paper."
        a "I cannot find the will to refuse him,"
        "she murmurs."
        "I look back across the diner toward the kitchen."
        "LeeRoy is beaming over the deep fryer, lifting the wire basket with a look of pure joy over a perfect batch of golden onion rings."
        "His happiness is so bright that I suddenly understand exactly why telling him 'no' didn't even cross her mind."
        # [LISTEN +1]

#Scene 13: The Supermurgidroid Weepie - Friday Evening
"I close the door behind me. Chief actually approved the piece."
"Even if it was at the cost of having my opening paragraph butchered, it went to print for the morning edition."
"And miraculously, it actually worked."
"The diner isn't exactly standing-room-only, but there are actual customers in the booths."
"Six, maybe eight scattered around the room."
"The Wurlitzer jukebox is finally plugged in, spinning a scratchy 45 that fills the air with a steady bassline."
"Out on the front sidewalk, visible through the plate glass, two teenage girls are strapping on the diner's roller skates and trying to balance on them with absolutely zero talent, clinging to the brick wall and shrieking with laughter."
"It is a vast improvement over the silence."
"I am slumped over the counter with a mug of black coffee, running on pure fumes after spending the entire night hunched over the keys of my Royal typewriter."
"My shoulders ache, my fingers are stiff, but I would do it all over again in a heartbeat."
"LeeRoy suddenly materializes on the other side of the counter."
"He slides a small, wooden-framed chalkboard down the table toward me."
"There are four items listed on it in slightly uneven chalk lettering."
l "Miss Kessler. Pick one. On the house."
"I stare at him over the rim of my mug, my eyes narrowed."
m "Are you actively trying to put me in the municipal hospital, LeeRoy?"
"He remains completely undeterred."
l "I would consider it a personal favour if you would be the very first to sample our new dessert menu."
"I let out a long, exhausted breath. I set my coffee down and lean forward to actually read the board."
#[CHOICE ROUTES GO HERE]
#[Whatever happens, happens]
#"[Name] gives me a lingering look, excuses [herself/himself/themselves], and slips back behind the counter to get back on the clock."
"I watch them go, feeling a strange pull in my chest. Is it… no. Can't be."
"I'm a strong independent woman and I do NOT have such impure feelings. Over anyone."
"I force my attention down to the table and push my plate away, the last smear of dessert drying on the porcelain."
"Over by the wall, the Wurlitzer clicks and whirs, dropping a new 45 onto the turntable with a crackle."
"I dig into my coat pocket, pull out my spiral steno pad, and flip it open to the section where I keep my better leads."
"I pull the cap off my fountain pen."
"I stare at the paper for a long time before I finally write down the only real angle I can come up with on such a short notice:"
"The diner with the creepy name might just have a pulse after all."
"It is not exactly front-page news. Another candidate for being featured on the women's page alongside the rest of local fluff. It screams 'local colour'."
m "I still have time."
"Behind me, out in the dark asphalt lot, a pair of headlights sweeps across the windows."
"A heavy sedan downshifts, the tires crunching over the gravel as it slows off Route Nine and pulls into a parking space."
"I click the cap back onto my pen and slide the pad into my pocket."
"Whether I get my front-page scoop or not, one thing is dead certain: this joint is about to get a whole lot busier."
#Scene 14: The Supermurgidroid Weepie - Friday Night
"I take another sip. It's quarter to one in the morning."
"The diner is thankfully empty and the jukebox had been plugged off for the night. Good riddance."
"I am perched at the far end of the counter nursing the last bitter dregs of the coffee pot, locked in an amiable argument with LeeRoy."
"It's quite the dilemma, trying to decide whether Friday's onion burger special has too much onion on it or too little."
"My position is that it does not."
"His position is that his eyes water whenever he walks past the prep station a complaint I point out he probably shouldn't be volunteering a potential customer."
"The brass bell over the front door chimes."
"A man steps inside. He looks to be in his late forties, wearing a faded coat against the autumn chill."
"He has a heavy olive-drab duffel bag slung over one shoulder and chalky road dust coating his trousers right up to the knee."
e "You folks still open?"
"Leeroy bolts out of his seat, practically radiating with excitement."
l "We're open. Come on in."
"The man drops his bag heavily onto the linoleum and takes a seat two stools down from me."
"He squints up at the blackboard I wrote out on Tuesday."
e "What's the cheapest thing on there?"
l "Coffee's free after midnight."
e "Since when?"
l "…Since right now, I guess."
"Earl laughs. He sounds equally part tired and amused."
"He ends up ordering a cheeseburger anyway, along with a vanilla milkshake."
"Apparently he saw it listed on the menu and wanted to splurge. Mixing dairy and grease? What a madman."
"When it arrives, he takes a long draw of the milkshake. He immediately pulls the glass away and looks at LeeRoy."
e "It's.. quite good. Could use a bit of malt powder."
"I don't look up from my mug as I reply."
m "Tell him that. Please. He absolutely will not hear it from me."
"The man grins, wiping his mouth with the back of his hand."
e "Naw. I ain't getting in the middle of domestic troubles."
"For a few minutes, we just sit there, listening to the hum of the refrigerators."
m "Where are you headed, anyway?"
e "Toledo. My brother's got a gig lined up for me on a freight dock, starts Thursday morning."
e "I caught a ride as far as the county line, but it dried up."
e "Had nothing but asphalt and headlights for some… four hours."
"He nods toward the window, where the red glare bleeds onto the sidewalk."
e "Saw that sign from the road. Figured a joint called the 'Super Morgue' had to be worth a look."
m "It is, actually."
"Earl excuses himself to use the washroom in the back, leaving his heavy canvas duffel resting against the chrome stool."
"I finish the last sip of my coffee, drop a dime on the counter for a tip and slide off my seat to gather my coat."
m "Night, LeeRoy."
l "Goodnight, Miss Kessler."
#[adelaide goes brrrrrr kills everyone here]