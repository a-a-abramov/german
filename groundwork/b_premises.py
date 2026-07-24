# PREMISES[(topic, scene_number)] = (title, premise_sentence, comedic_angle)
# scene_number is 1-based, in the order emitted by gen_doc.TOPIC_SCENES.
PREMISES = {}

TOPIC_META = {
    'Grammatik & Verbindungswörter': "Prepositions, conjunctions, question words, pronouns, modal/hilfsverbs, degree adverbs and other glue words — the connective tissue of every scene (see strategy note below).",
    'In der Wohnung & Zuhause': "Rooms, furniture, household objects, chores, moving house.",
    'Körper & Gesundheit': "Body parts, illness, doctor, pharmacy, hospital, symptoms.",
    'Tiere': "Animals and farm life (a small, genuinely thin category in the B1 list).",
    'Essen, Kochen & Restaurant': "Food, drink, cooking, groceries, restaurant & café life.",
    'Familie & Beziehungen': "Family members, life stages, relationships, weddings, parenting.",
    'Arbeit & Beruf': "Jobs, workplace, careers, hiring/firing, professions.",
    'Unterwegs & Verkehr': "Transport, traffic, directions, cars, trains, planes.",
    'Einkaufen & Geld': "Shopping, prices, banking, paying, contracts, budgets.",
    'Natur, Wetter & Umwelt': "Weather, landscape, environment, climate, countryside.",
    'Gefühle & Charakter': "Emotions and personality traits.",
    'Schule & Bildung': "School, university, courses, exams, learning.",
    'Freizeit, Medien & Technik': "Hobbies, sport, TV/film/music, art, gadgets, the internet.",
    'Reisen & Urlaub': "Travel, hotels, vacation, tourism.",
    'Zeit & Kalender': "Time expressions, calendar, daily routine, punctuality.",
    'Kommunikation & Post': "Talking, phoning, writing letters/emails, the postal system, news media.",
    'Stadt, Ämter & Recht': "City life, government offices, bureaucracy, police, law, crime.",
    'Kleidung & Aussehen': "Clothing, accessories, hairstyling, appearance.",
    'Menge, Maß & Eigenschaften': "Size, quantity, quality judgments and general descriptive adjectives.",
    'Handlungen: Alltagsverben': "The general-purpose verb toolkit — give/take, fix, organize, react — that powers everyday scenes.",
    'Denken, Wissen & Meinen': "Mental verbs: think, know, decide, remember, doubt, agree.",
    'Gesellschaft, Politik & Wirtschaft': "Society, politics, economy — the smallest topic; most B1 words in this space are abstract enough to also fit Stadt/Ämter or Denken.",
}

T = 'Grammatik & Verbindungswörter'
PREMISES[(T,1)] = ("Der Wegbeschreibungs-Kauderwelsch", "A tourist asks a local for directions and gets an answer built entirely out of prepositions, no content words.", "The local is so proud of using every preposition correctly that the tourist ends up more lost than before.")
PREMISES[(T,2)] = ("Der zweite Streckenabschnitt", "The same over-eager local keeps going, piling on more prepositions for a second, even longer route.", "By the end he's pointing in six directions at once and contradicting himself.")
PREMISES[(T,3)] = ("Der Ausredenkatalog", "Someone late for work rehearses an excuse in front of a mirror, stringing together every connector to sound more sophisticated.", "The sentence gets so long and hedged that by the time it ends, the meeting is over.")
PREMISES[(T,4)] = ("Der endlose Nebensatz", "The same rehearsal continues, the excuse spiraling into ever more nested clauses.", "He finally just says 'weil... äh...' and gives up, defeated by his own grammar.")
PREMISES[(T,5)] = ("Der Verhörraum", "A detective interrogates a suspect using nothing but question words, rapid-fire.", "The suspect answers every question with another question, and the interrogation turns into a ping-pong match.")
PREMISES[(T,6)] = ("Die Nachbarschaftsdrohne", "A neighbor's drone hovers around, and everyone shouts spatial directions trying to get it to land.", "The drone operator is deaf and just nods at everything, sending it further astray each time.")
PREMISES[(T,7)] = ("Verstecken im Möbelhaus", "Kids play hide-and-seek in a furniture store, calling out where they're hiding.", "One kid hides literally inside a wardrobe display and nobody can find him for an hour.")
PREMISES[(T,8)] = ("Die Parkplatzsuche", "A driver circles a full car park giving turn-by-turn directions to a passenger holding a phone.", "They pass the same spot three times before realizing 'geradeaus' was actually a dead end.")
PREMISES[(T,9)] = ("Der GPS-Ausfall", "The GPS breaks mid-hike and the group has to navigate by shouting direction words at each other across a ravine.", "They end up walking in a perfect circle back to the car.")
PREMISES[(T,10)] = ("Der Wecker-Kampf", "Someone hits snooze on their alarm clock over and over, narrating each delay with a time adverb.", "By 'irgendwann' it's already afternoon and they missed the whole day.")
PREMISES[(T,11)] = ("Die Warteschlange beim Amt", "People in a slow-moving government-office queue mutter time words about how long they've been waiting.", "The person at counter one has apparently been 'gleich dran' for three years.")
PREMISES[(T,12)] = ("Der Countdown zur Prüfung", "A student obsessively tracks the time before an exam, narrating every stage of dread.", "'Zurzeit' revises nothing and just refreshes the clock app instead.")
PREMISES[(T,13)] = ("Der Wiederholungstäter", "A repeat-offender packrat keeps promising 'irgendwann' to clean the garage, one excuse per weekend.", "Years pass; the garage now qualifies as an archaeological site.")
PREMISES[(T,14)] = ("Die Mengenlehre am Buffet", "Guests at a buffet negotiate portion sizes using nothing but degree and quantity words.", "One guest says 'ein bisschen mehr' seven times until his plate collapses under the weight.")
PREMISES[(T,15)] = ("Die Waage im Fitnessstudio", "Two friends compare gym progress, hedging every claim with degree adverbs to avoid admitting who's stronger.", "They both end up so vague that neither can tell who actually won the bet.")
PREMISES[(T,16)] = ("Der übervorsichtige Wettermelder", "A radio presenter reads the weather forecast while hedging every single sentence with a degree word.", "By the end the forecast is technically true for every possible weather condition at once.")
PREMISES[(T,17)] = ("Die Beichte im Café", "A friend confesses something embarrassing, softening the blow with modal particles and hedges.", "By the time she finally says the actual secret, everyone has already guessed three wrong, funnier things.")
PREMISES[(T,18)] = ("Der Familienstreit ums Sofa", "A family argues about who broke what, everyone using vague pronouns to avoid blame.", "'Jemand' turns out to be the dog, who is smugly unbothered on the ruined sofa.")
PREMISES[(T,19)] = ("Die Bühnenmagierin", "A magician on stage makes items vanish, narrating with pronouns and indefinite articles to build suspense.", "Her 'niemand' trick fails because the volunteer is clearly visible the whole time, hiding behind a too-small curtain.")
PREMISES[(T,20)] = ("Der Ratespiel-Moderator", "A game-show host quizzes contestants with vague-pronoun riddles.", "One contestant answers every riddle with 'zufällig' as if that were the actual word being guessed.")
PREMISES[(T,21)] = ("Die überforderten Eltern", "Parents negotiate bedtime with a toddler using every modal verb they know to sound firm and flexible at once.", "The toddler out-negotiates them and ends up staying up an hour later.")
PREMISES[(T,22)] = ("Der Small-Talk-Marathon beim Amt", "Strangers waiting at a government office make painfully polite small talk to pass the time.", "One insists on complimenting everything in the room, down to the fluorescent lighting.")
PREMISES[(T,23)] = ("Die WG-Küchenkonferenz", "Roommates hold a mock-formal meeting about kitchen chaos, using stiff small-talk phrases for comic effect.", "The 'meeting' is really just about who keeps leaving dishes, but they minute it like a UN summit.")
PREMISES[(T,24)] = ("Der zu ehrliche Nachbar", "A blunt neighbor comments on everything happening on the street, unfiltered.", "His running commentary turns a boring afternoon into unwanted reality TV for the whole block.")
PREMISES[(T,25)] = ("Die Reklamation im Elektroladen", "A customer tries to return a broken gadget, using every polite hedge to avoid sounding rude.", "The clerk is even more indirect, and the return process takes forty-five minutes of mutual politeness.")
PREMISES[(T,26)] = ("Der Möbelaufbau-Streit", "A couple assembles flatpack furniture, bickering with clipped filler words instead of full sentences.", "The finished shelf ends up upside down, but structurally sound.")
PREMISES[(T,27)] = ("Der Heimweh-Anruf", "Someone calls home describing a chaotic new apartment using small, connective words to soften every complaint.", "Their parent keeps interrupting with 'wirklich?' until the call is 90% interjections.")
PREMISES[(T,28)] = ("Der Privatdetektiv im Café", "An amateur detective narrates his stakeout under his breath, treating mundane details as huge clues.", "His biggest breakthrough of the day is realizing the barista is 'privat' just tired, not suspicious.")
PREMISES[(T,29)] = ("Die Menükarte ohne Fotos", "A waiter describes dishes using only abstract words because the printer broke and the menu has no images.", "A tourist orders 'das Stück' and receives a mysteriously unlabeled item.")
PREMISES[(T,30)] = ("Das Vertrauensspiel", "Team-building exercise: colleagues must fall backward and trust a catcher, narrating the whole ordeal.", "The one colleague who insists everything is 'einverstanden' is the one who forgets to catch.")
PREMISES[(T,31)] = ("Die Bastelrunde", "A craft circle fills in a half-finished puzzle, discussing what still needs completing.", "It turns out to be a jigsaw of their own faces, and nobody wants to admit whose nose is missing.")
PREMISES[(T,32)] = ("Die Wortspielabende", "Friends play a word game where you must use obscure connector words in a sentence to score points.", "The game dissolves into an argument about whether 'gesamt-' is even allowed as a standalone word.")

T = 'Unterwegs & Verkehr'
PREMISES[(T,1)] = ("Die Fahrschulprüfung", "A nervous learner driver takes their test, narrating every action to the instructor out loud.", "They announce the seatbelt three times before actually buckling it, stalling the car twice in a one-way street.")
PREMISES[(T,2)] = ("Der verpasste Flug", "A family sprints through an airport trying to catch a departing flight after misreading the schedule.", "Dad insists the pilot will 'definitely wait for us' while dragging a suitcase that keeps popping open.")
PREMISES[(T,3)] = ("Die Bahnhofsverwirrung", "A tourist tries to find the right platform among S-Bahn, U-Bahn and long-distance trains, asking everyone for help.", "Three different strangers give three contradictory directions, and he ends up on all three trains in one hour.")
PREMISES[(T,4)] = ("Der Fahrradkurier im Stress", "A bike courier weaves through pedestrian zones and speed limits while narrating a running commentary of near-misses.", "He nearly flattens a jogger, apologizes over his shoulder, and speeds off unbothered.")
PREMISES[(T,5)] = ("Der Anfängerlotse", "A backseat driver gives contradictory turn-by-turn directions during a road trip, causing chaos at every curve.", "They end up doing a full loop and passing the same lift-bridge twice.")
PREMISES[(T,6)] = ("Die Motorradpanne", "A motorcycle breaks down mid-trip, and the rider has to hitch a ride while pushing it through a parking lot.", "A stranger's car ends up towing it with a rope that snaps hilariously at the worst possible moment.")
PREMISES[(T,7)] = ("Die Fahrradtour zur Altstadt", "A group cycles into the historic city center, arguing over the map and getting stuck in a tight lane.", "One cyclist's backpack knocks over an entire café's outdoor seating on the way past.")
PREMISES[(T,8)] = ("Die Tankstellenpanne", "A driver's car sputters into a gas station on fumes right as a huge traffic jam forms on the highway overpass.", "He accidentally puts the wrong fuel in and has to call for help, blocking the pump for everyone else.")
PREMISES[(T,9)] = ("Die Umleitung ins Nirgendwo", "A detour sign sends drivers on a bizarre loop through a town, ending up back where the traffic jam started.", "By the fifth roundabout, the driver starts recognizing the same dog on the same corner.")

T = 'Schule & Bildung'
PREMISES[(T,1)] = ("Der verschlafene Prüfungstag", "A student who overslept sprints to school, illustrations of the missed material scattered across the exam sheet.", "He mixes up the diagram labels so badly the teacher isn't sure if it's biology or abstract art.")
PREMISES[(T,2)] = ("Die Bibliotheksdurchsuchung", "A student desperately searches the library for one specific book right before a deadline.", "The book turns out to be checked out by the teacher who assigned the essay in the first place.")
PREMISES[(T,3)] = ("Der Forschungsclub", "An overambitious school club announces a grand research project with a fancy progress report.", "Their big 'breakthrough' turns out to be reheated homework from last semester.")
PREMISES[(T,4)] = ("Die Gedichtstunde", "A patience-testing poetry class drags on while a bored student doodles instead of writing.", "His 'poem' turns out to be one sentence repeated with different punctuation, and the teacher grades it anyway.")
PREMISES[(T,5)] = ("Der Berufsschulmarathon", "An apprentice bounces between shifts at the trade school and a part-time job, narrating an exhausting schedule.", "He falls asleep mid-sentence during roll call and answers 'here' to someone else's name.")
PREMISES[(T,6)] = ("Die Referatspanne", "A student's presentation slides crash right as they start presenting to the whole class.", "They improvise the entire university-level topic using only hand gestures and a marker on the whiteboard.")
PREMISES[(T,7)] = ("Der Übersetzungsnotfall", "A student mistranslates a foreign pen pal's letter so badly that the reply makes no sense at all.", "The pen pal writes back thinking they've been challenged to a duel.")

T = 'Freizeit, Medien & Technik'
PREMISES[(T,1)] = ("Der Filmabend-Chaos", "Friends try to film a home movie for a subscription channel, but nobody can operate the camera properly.", "The 'star' of the film keeps accidentally walking out of frame to check her phone.")
PREMISES[(T,2)] = ("Die Kunstausstellung", "An amateur artist's gallery opening features one badly hung painting and a memorial plaque nobody understands.", "A visitor mistakes the coat rack for an exhibit and starts seriously analyzing it.")
PREMISES[(T,3)] = ("Der Streaming-Absturz", "A group tries to binge-watch a show but the file keeps corrupting mid-scene.", "They end up acting out the missing dialogue themselves, badly, in increasingly dramatic voices.")
PREMISES[(T,4)] = ("Die improvisierte Geburtstagsfeier", "The TV remote breaks right before a birthday party, so guests must operate everything manually.", "Someone has to physically stand by the TV changing channels like a human remote control all night.")
PREMISES[(T,5)] = ("Das Fotoshooting-Desaster", "An amateur photographer tries to shoot a festival, but the equipment keeps malfunctioning at the worst moments.", "Every 'perfect shot' turns out to have someone's thumb over the lens.")
PREMISES[(T,6)] = ("Der Hobbykeller", "A dad shows off his overstuffed hobby room full of half-finished projects and forgotten instruments.", "He proudly demonstrates the guitar despite knowing exactly one chord.")
PREMISES[(T,7)] = ("Der Technik-Support-Notruf", "A grandparent calls for tech help installing an app, describing the problem in wildly wrong terms.", "The 'broken phone' turns out to just be upside down the whole time.")
PREMISES[(T,8)] = ("Das Heimkino-Upgrade", "A couple assembles a home theater system, arguing over the instructions and mixing up all the cables.", "The speakers end up playing the neighbor's WiFi-connected doorbell instead of the movie.")
PREMISES[(T,9)] = ("Die Museumsführung", "A overenthusiastic museum guide gives a tour that's more performance art than history lesson.", "He recites a made-up backstory for a painting that's actually just a fire extinguisher on the wall.")
PREMISES[(T,10)] = ("Das Konzert im Wohnzimmer", "An amateur band records a music video in someone's cramped living room with all borrowed instruments.", "The drummer keeps hitting the ceiling lamp on every beat.")
PREMISES[(T,11)] = ("Die Quizshow-Aufnahme", "Friends film their own homemade game show using a hand-drawn wheel and props from around the house.", "The prize turns out to be a coupon for one free hug, and everyone still wants to win.")
PREMISES[(T,12)] = ("Das Vereinsfest", "A local sports club throws a chaotic celebration after an unlikely victory.", "Their trophy is a repurposed pasta jar, and everyone toasts to it as if it were gold.")
PREMISES[(T,13)] = ("Der Vereinssporttag", "A workplace organizes an awkward team-sports day where nobody remembers the actual rules.", "The 'referee' makes up new rules on the spot to settle every dispute in the funniest way possible.")
PREMISES[(T,14)] = ("Der Theaterprobenabend", "An amateur theater group rehearses a scene that keeps falling apart because of forgotten lines.", "The lead actor starts improvising in rhyme just to keep going, and the director loves it too much to stop him.")
PREMISES[(T,15)] = ("Die Stadtführung für Touristen", "A tour guide leads visitors past famous landmarks, embellishing every fact more than the last.", "By the final stop, the 'historic fountain' is apparently haunted by seventeen different ghosts.")
PREMISES[(T,16)] = ("Das Fußballtraining", "An amateur football coach tries to train a hopeless team using increasingly dramatic sports metaphors.", "The team's biggest achievement of the day is not falling over during warm-up stretches.")
PREMISES[(T,17)] = ("Der Zirkusbesuch", "A family visits a slightly run-down circus with an over-the-top ringmaster.", "The lion tamer's lion is clearly a very large, very unbothered house cat.")

T = 'Handlungen: Alltagsverben'
PREMISES[(T,1)] = ("Die Bürobesprechung", "An overly formal office meeting drags on with everyone stalling on trivial administrative details.", "Someone spends ten minutes debating the correct procedure for booking a meeting room they're already sitting in.")
PREMISES[(T,2)] = ("Der Kundendienstanruf", "A customer service call goes in circles as the agent keeps transferring the caller between departments.", "By the fourth transfer, the caller is talking to the same person who first picked up.")
PREMISES[(T,3)] = ("Die Steuererklärung", "Two roommates try to sort out a joint declaration, arguing over who's responsible for which forms.", "They accidentally submit each other's tax numbers and spend the rest of the evening panicking.")
PREMISES[(T,4)] = ("Der Umzugstag", "Friends help someone move apartments, constantly grabbing, carrying, and handing off boxes in a chaotic chain.", "The heaviest box, labeled 'books', turns out to be full of bricks someone was keeping for no reason.")
PREMISES[(T,5)] = ("Die Rückgabe im Baumarkt", "Someone tries to return a broken tool, carrying it awkwardly through the whole store looking for the right counter.", "The 'broken' tool works perfectly the second the clerk touches it.")
PREMISES[(T,6)] = ("Der Frühjahrsputz", "A family does a chaotic spring cleaning, connecting hoses, printing labels, and losing patience with each other.", "The dad insists on fixing the printer himself and ends up with more ink on his shirt than the page.")
PREMISES[(T,7)] = ("Der WG-Streit ums Sofa", "Roommates fight over a broken sofa, laughing, joking, and living around the mess instead of fixing it.", "They eventually agree the sofa 'has character' and just cover the hole with a blanket forever.")
PREMISES[(T,8)] = ("Der Gartentag", "A family plants a garden while battling a garden hose that seems to have a mind of its own.", "The hose sprays everyone except the actual plants, no matter how they aim it.")
PREMISES[(T,9)] = ("Der Sporttag im Park", "Friends organize an improvised race and jumping contest in the park, keeping score badly.", "The self-declared 'winner' clearly fell down halfway through but insists it counts as style points.")
PREMISES[(T,10)] = ("Die Bootsfahrt-Panne", "A group tries to escape, dive, and swim their way out of a mishap on a leaky rented rowboat.", "The 'life jacket' turns out to be a inflatable pool flamingo someone grabbed by mistake.")
PREMISES[(T,11)] = ("Der Vergleichs-Streit unter Nachbarn", "Two neighbors compare, argue, and pack up their yard sale items, trying to out-haggle each other.", "They end up trading items back and forth so many times neither remembers who owns what anymore.")
PREMISES[(T,12)] = ("Die Autowäsche", "Friends wash a car in the driveway, getting distracted, spraying each other, and forgetting the actual car.", "By the end the car is cleaner in one spot and filthier everywhere else than when they started.")
PREMISES[(T,13)] = ("Die Wanderung mit Hindernissen", "A hiking group stumbles, stops, and struggles up a hill that turns out to be much steeper than the map showed.", "The self-appointed 'guide' gets lost twice using his own compass.")
PREMISES[(T,14)] = ("Der Renovierungsversuch", "A couple tries fixing up an old apartment, changing plans mid-project and abandoning half-finished tasks.", "The 'accent wall' ends up three different colors because nobody could agree and nobody wanted to repaint it.")
PREMISES[(T,15)] = ("Die verspätete Rückkehr", "Someone tries to make it home in time for dinner, juggling errands that keep piling up.", "They arrive just as everyone else has finished eating and gone to bed.")
PREMISES[(T,16)] = ("Die Reparaturwerkstatt", "A DIY enthusiast tries fixing a broken appliance, changing his approach every five minutes.", "He ends up with more screws left over than the appliance originally had.")
PREMISES[(T,17)] = ("Die Rettungsaktion", "Neighbors help rescue a cat stuck in a tree, taking turns and calling for backup.", "The fire department arrives just as the cat casually climbs down on its own, unbothered.")
PREMISES[(T,18)] = ("Die Nachbarschaftsspende-Aktion", "A street organizes a donation drive, searching for, weighing, and cataloguing old items to give away.", "Someone accidentally donates their own house keys hidden inside an old coat pocket.")
PREMISES[(T,19)] = ("Das Dankesfest", "A community throws a small thank-you party for a helpful neighbor, offering food and gifts all evening.", "The neighbor is too polite to say he's allergic to literally everything on the table.")

T = 'Denken, Wissen & Meinen'
PREMISES[(T,1)] = ("Der Debattierclub", "An amateur debate club argues about a trivial topic as if the fate of the world depended on it.", "Nobody actually knows what the original topic was anymore by round three.")
PREMISES[(T,2)] = ("Die Gerichtsshow-Parodie", "Friends stage a mock trial over who ate the last slice of cake, complete with dramatic evidence.", "The 'evidence' is a single crumb, presented as if it were a smoking gun.")
PREMISES[(T,3)] = ("Der Wissenschaftskongress im Kleinformat", "A neighborhood science fair features wildly overconfident presentations of very small discoveries.", "One 'researcher' presents his conclusion that his cat prefers Tuesdays, with full slideshow.")
PREMISES[(T,4)] = ("Die Familienabstimmung", "A family votes on where to go for vacation, and the decision keeps flip-flopping every five minutes.", "The dog's random bark is treated as the deciding vote.")
PREMISES[(T,5)] = ("Der Strategie-Brettspielabend", "Friends plan an elaborate board game strategy, listing every possible outcome out loud.", "Their meticulous plan collapses the instant someone rolls the wrong number.")
PREMISES[(T,6)] = ("Das Klassentreffen der Erinnerungen", "Old classmates reunite and try to remember shared stories, each recalling a wildly different version.", "Nobody can agree who actually won the legendary sack race from twenty years ago.")
PREMISES[(T,7)] = ("Die Schatzsuche im Dachboden", "Someone rummages through the attic, discovering strange objects and inventing backstories for each.", "A mysterious key turns out to open nothing more exciting than an old bike lock.")
PREMISES[(T,8)] = ("Die Verschwörungstheorie am Stammtisch", "Friends at a regular pub table build an increasingly elaborate, silly conspiracy theory about a local shop closing early.", "The 'evidence' keeps growing more absurd until someone points out the shop is just closed for holiday.")
PREMISES[(T,9)] = ("Die Konferenzraum-Verwirrung", "A negotiation between two small business owners spirals into confused compromise proposals.", "They end up agreeing to something neither of them actually wanted, just to end the meeting.")
PREMISES[(T,10)] = ("Der Lügendetektor-Abend", "Friends play a party game trying to spot each other's lies, getting suspicious over everything.", "Someone's true statement gets voted 'obviously a lie' just because it sounded too weird to be real.")
PREMISES[(T,11)] = ("Das Risikospiel", "A group debates whether to try a slightly risky activity, weighing pros and cons dramatically.", "The most cautious person of the group ends up being the first to jump in.")
PREMISES[(T,12)] = ("Die Wettervorhersage-Zweifel", "Friends argue about whether to trust the forecast for a planned outdoor event.", "They end up bringing every possible weather item and using none of them because it's perfectly sunny.")

T = 'Einkaufen & Geld'
PREMISES[(T,1)] = ("Der Ausverkaufstag", "Shoppers scramble through a chaotic sale, grabbing discounted items faster than they can decide if they want them.", "Two strangers end up in a polite but intense tug-of-war over the same discounted lamp.")
PREMISES[(T,2)] = ("Die Wochenendeinkäufe", "A family does the weekly grocery run on a tight budget, calculating every item's cost out loud.", "Dad's strict budgeting collapses the second he sees the bakery section.")
PREMISES[(T,3)] = ("Der erste Gehaltscheck", "A new employee obsessively checks their bank account after receiving their first paycheck.", "They immediately spend it all on something wildly impractical out of sheer excitement.")
PREMISES[(T,4)] = ("Die verwirrende Bankfiliale", "Someone tries to open an account and gets lost in an endless maze of forms and machines.", "The ATM eats the card, the counter sends them back to the ATM, and the loop never ends.")
PREMISES[(T,5)] = ("Der Flohmarktverkäufer", "An overenthusiastic flea-market seller haggles wildly with every browsing customer.", "He gives a heartfelt sales pitch for an obviously broken toaster as if it were a family heirloom.")
PREMISES[(T,6)] = ("Der Kreditkartenschock", "Someone opens their credit card statement and is horrified by a mysterious huge purchase.", "It turns out to be their own forgotten online order from three months ago.")
PREMISES[(T,7)] = ("Der Möbelmarkt-Vergleich", "A couple compares prices between two furniture stores, debating every euro of difference.", "They spend more time and money on coffee while deciding than they save on the actual furniture.")
PREMISES[(T,8)] = ("Die Onlinebestellung geht schief", "A customer tracks a delayed package obsessively, refreshing the tracking page every five minutes.", "The package arrives completely crushed, containing a single, oddly undamaged rubber duck.")
PREMISES[(T,9)] = ("Die Steuerprüfung im Supermarkt", "Someone tallies receipts at the supermarket checkout, trying to stay under a strict weekly budget.", "The final total is one cent over, and they have to put back a single item under everyone's judging eyes.")
PREMISES[(T,10)] = ("Der Mietvertrag-Papierkram", "A tenant signs a new lease, drowning in insurance, deposit, and payment paperwork.", "They accidentally sign up for a service they never wanted just from clicking through forms too fast.")

T = 'Menge, Maß & Eigenschaften'
PREMISES[(T,1)] = ("Der Möbelmess-Fehler", "Someone measures a new wardrobe against the doorway, insisting it will 'definitely' fit.", "It gets stuck at a comically awkward angle, blocking the hallway for the whole afternoon.")
PREMISES[(T,2)] = ("Der Wettbewerb um die größte Kürbis", "Neighbors compete in an amateur giant-vegetable growing contest, obsessing over every centimeter.", "The 'winning' pumpkin turns out to be mostly held together with tape after a fall.")
PREMISES[(T,3)] = ("Die Inventur im Lagerhaus", "Warehouse workers do a chaotic stock count, constantly losing track of the total.", "They recount the same box four times because someone kept moving it while counting.")
PREMISES[(T,4)] = ("Die Bewertungsshow", "Friends host a mock talent show, giving overly dramatic, contradictory reviews of each act.", "The 'perfect score' judge and the 'harshest critic' turn out to be scoring completely different performances by accident.")
PREMISES[(T,5)] = ("Der Wertschätzungsstreit im Antiquitätenladen", "A shop owner and a customer argue over whether an old vase is priceless or worthless.", "It turns out to be a cheap souvenir, but both refuse to back down out of pure stubbornness.")
PREMISES[(T,6)] = ("Der Fitnesstest", "Friends attempt an informal strength and endurance test in the park, judging each other's fairness.", "The self-proclaimed fittest one is out of breath after the warm-up alone.")
PREMISES[(T,7)] = ("Die Umfrage in der Fußgängerzone", "A market researcher surveys passersby, comparing answers that all somehow contradict each other.", "The 'average' answer ends up being something nobody actually said.")
PREMISES[(T,8)] = ("Die statistische Wette", "Friends bet on percentages and averages during a football match, arguing over vague estimates.", "Their 'exact calculations' turn out to be completely made up on the spot.")
PREMISES[(T,9)] = ("Der Übertreibungswettbewerb", "Friends compete over who can tell the most exaggerated story about their weekend.", "The most unbelievable story turns out to be completely true, to everyone's shock.")
PREMISES[(T,10)] = ("Der Materialtest im Baumarkt", "A DIYer tests different materials' toughness by hitting, bending, and dropping samples in the aisle.", "He accidentally proves the display shelf itself is the weakest material in the store.")
PREMISES[(T,11)] = ("Der Geschwindigkeitswettstreit", "Friends race shopping carts through an empty parking lot, timing each other dramatically.", "The 'fastest' one crashes spectacularly into a row of stacked crates at the finish line.")
PREMISES[(T,12)] = ("Der Charaktertest beim Speeddating", "At a speed-dating event, participants describe themselves using only vague personality adjectives.", "Two people describe themselves identically and realize they're actually siblings.")
PREMISES[(T,13)] = ("Die Gewohnheitsdebatte am Frühstückstisch", "A couple argues gently over morning routines and small habits neither wants to change.", "They discover after years together neither actually likes the habit they were defending.")

T = 'In der Wohnung & Zuhause'
PREMISES[(T,1)] = ("Der Einzugstag", "Someone moves into a new, mostly empty apartment, cheerfully naming every room out loud like a tour guide.", "The 'apartment tour' for a single friend takes twenty minutes because they insist on describing the closet too.")
PREMISES[(T,2)] = ("Die improvisierte Küche", "A cramped student apartment's kitchen doubles as living room, with furniture crammed wherever it fits.", "The couch and the fridge are pushed so close together that opening either requires teamwork.")
PREMISES[(T,3)] = ("Der Balkon-Pooltag", "Neighbors improvise a tiny inflatable pool on a cramped balcony during a heatwave.", "The garden hose fills it just as someone below opens their window directly underneath.")
PREMISES[(T,4)] = ("Die Heizungsreparatur", "A landlord tries to fix a broken heater himself instead of calling a professional.", "He ends up needing the actual repairman anyway, plus a new toolbox after breaking most of the old one.")
PREMISES[(T,5)] = ("Der Dachbodenfund", "Someone clears out a cluttered attic and stumbles on a chair so old it might be an antique.", "It collapses the moment anyone actually sits on it.")
PREMISES[(T,6)] = ("Der Frühjahrsputz-Marathon", "A roommate deep-cleans the whole apartment in one obsessive afternoon.", "They find three missing spoons, one shoe, and no explanation for either.")
PREMISES[(T,7)] = ("Das Möbelaufbau-Chaos", "Two friends try assembling flatpack furniture without reading the instructions.", "The finished 'bookshelf' looks suspiciously like a wobbly ladder.")
PREMISES[(T,8)] = ("Der Frühlingsputz im Wohnzimmer", "A family reorganizes the living room, disagreeing about furniture placement the whole afternoon.", "By evening the room is back in almost the exact same layout it started in.")
PREMISES[(T,9)] = ("Der Schlüsselverlust", "Someone locks themselves out and has to improvise entry through increasingly ridiculous methods.", "The spare key turns out to have been in their pocket the entire time.")
PREMISES[(T,10)] = ("Der gemütliche Fernsehabend", "Friends gather in a living room stuffed with mismatched furniture for movie night.", "Someone insists the ancient, creaky armchair is 'the good one' and fights anyone who sits in it.")
PREMISES[(T,11)] = ("Der Umzugswagen", "A family loads a moving truck, arguing over how to fit oversized furniture through narrow doors.", "The wardrobe barely fits by being tilted at an almost comedic forty-five-degree angle.")
PREMISES[(T,12)] = ("Das neue Zuhause", "After a long move, someone finally relaxes in their new, freshly organized living room.", "They immediately can't find a single box labeled correctly among the fifty they packed.")

T = 'Natur, Wetter & Umwelt'
PREMISES[(T,1)] = ("Der Gewitter-Campingausflug", "Campers set up a tent just as dark clouds roll in over a riverside meadow.", "The tent collapses the second the first raindrop hits, in front of a very unimpressed audience of ducks.")
PREMISES[(T,2)] = ("Der Bauernhofbesuch", "City kids visit a farm and are baffled by basic country facts everyone else takes for granted.", "One insists the potatoes 'grow on trees' until the farmer patiently digs one up to prove otherwise.")
PREMISES[(T,3)] = ("Die Bergwanderung mit Aussicht", "Hikers finally reach a mountain viewpoint after a long climb, awestruck by the view.", "The view is immediately ruined by a cloud rolling in the second everyone gets their camera out.")
PREMISES[(T,4)] = ("Die Autopanne auf dem Land", "A car breaks down on a rural road near a harbor town, and the driver has to improvise repairs.", "The 'repair' involves duct tape, a farmer's advice, and a suspicious amount of luck.")
PREMISES[(T,5)] = ("Die Seefahrt bei Nebel", "A small boat trip gets eerily foggy, and the crew navigates mostly by guesswork and superstition.", "They 'discover' a mysterious island that turns out to be the same dock they left from.")
PREMISES[(T,6)] = ("Der Strandtag mit Überraschungen", "A beach day turns chaotic as the tide comes in faster than anyone expected.", "Someone's sandcastle empire is swallowed by the sea mid-victory-speech.")
PREMISES[(T,7)] = ("Die Sternennacht im Tal", "Friends camp in a valley and try (badly) to identify constellations.", "Every single 'star' they point at turns out to be a distant airplane.")
PREMISES[(T,8)] = ("Der plötzliche Wetterumschwung", "A picnic gets abruptly interrupted by wind and clouds rolling in from nowhere.", "The tablecloth becomes an impromptu kite, sailing off with half the sandwiches still on it.")

T = 'Familie & Beziehungen'
PREMISES[(T,1)] = ("Das Familientreffen im Altersheim", "Several generations gather to visit a grandparent, and everyone tells wildly different versions of family history.", "The grandmother insists she remembers everyone's age wrong, on purpose, just to see their reactions.")
PREMISES[(T,2)] = ("Die Hochzeitsvorbereitung", "A couple's engaged relatives argue over wedding invitations and seating charts for cousins nobody's met.", "The seating chart ends up requiring a whiteboard the size of a door.")
PREMISES[(T,3)] = ("Die Geburtstagsüberraschung", "Friends plan a surprise party but keep almost giving it away through terrible acting.", "The 'surprised' birthday person had actually known for a week and pretends convincingly anyway.")
PREMISES[(T,4)] = ("Die Jugendliebe-Geschichte", "An older relative tells an embellished story about their teenage romance at a family dinner.", "Every retelling adds a new dramatic detail that definitely wasn't there the first time.")
PREMISES[(T,5)] = ("Der erste Kindergartentag", "Parents nervously drop off their child at kindergarten for the first time.", "The child is completely fine; it's the parents who need consoling in the parking lot.")
PREMISES[(T,6)] = ("Die Großfamilien-Reise", "A sprawling extended family plans a group trip and can't agree on anything.", "The final itinerary satisfies literally nobody but somehow makes everyone equally happy about that.")
PREMISES[(T,7)] = ("Die Rentnerclub-Runde", "Retirees gather weekly, gently teasing each other about health, memory, and old family gossip.", "Nobody can actually remember what the running joke was originally about, but they laugh anyway.")
PREMISES[(T,8)] = ("Die Versöhnung nach dem Streit", "A couple works through a small disagreement, over-apologizing in increasingly formal language.", "The 'serious conflict' turns out to be about whose turn it was to walk the dog.")

T = 'Gefühle & Charakter'
PREMISES[(T,1)] = ("Die Achterbahnfahrt", "Friends line up for a rollercoaster, each reacting to the fear in a wildly different way.", "The one who claimed to be fearless screams the loudest the entire ride.")
PREMISES[(T,2)] = ("Der peinliche Vorstellungsgesprächs-Traum", "Someone recounts an embarrassing dream about a disastrous job interview at breakfast.", "Everyone at the table admits they've had the exact same anxiety dream, in painfully specific detail.")
PREMISES[(T,3)] = ("Die enttäuschte Kochshow", "An amateur cook's ambitious dinner party dish collapses spectacularly right before guests arrive.", "The backup plan, ordering pizza, turns out to be the guests' favorite part of the evening.")
PREMISES[(T,4)] = ("Der Trostpreis", "A friend loses a minor competition and everyone tries clumsily to cheer them up.", "The 'consolation gift' is so absurd it accidentally becomes the highlight of their week.")
PREMISES[(T,5)] = ("Die Dankesrede", "Someone gives an overly emotional thank-you speech at a small local award ceremony.", "They get so choked up over a minor certificate that people start crying along out of secondhand emotion.")
PREMISES[(T,6)] = ("Der Kritikerclub", "Friends review a terrible amateur film with theatrical, contradictory opinions.", "The harshest critic turns out to be an uncredited extra in the film.")
PREMISES[(T,7)] = ("Die Liebeserklärung im Regen", "Someone plans a big romantic gesture that gets rained out and ruined step by step.", "The soggy, disastrous version ends up being more memorable than the perfect plan ever would have been.")
PREMISES[(T,8)] = ("Der Streit im Fahrstuhl", "Two strangers get stuck in an elevator and slowly go from annoyed to oddly bonded.", "By the time they're rescued, they've become unlikely best friends and exchange numbers.")
PREMISES[(T,9)] = ("Die Wunschliste ans Universum", "Friends write silly wish lists for the new year, half-joking, half-serious.", "The most ridiculous wish on the list is the only one that actually comes true by year's end.")

T = 'Kommunikation & Post'
PREMISES[(T,1)] = ("Der falsch adressierte Brief", "Someone writes an angry letter to their landlord but sends it to the wrong address entirely.", "The actual recipient, a stranger, writes back a genuinely helpful reply anyway.")
PREMISES[(T,2)] = ("Die Anrufbeantworter-Odyssee", "Someone leaves an increasingly rambling voicemail after being cut off mid-sentence multiple times.", "The final voicemail is just them saying 'call me back' forty different ways.")
PREMISES[(T,3)] = ("Der Buchstabierwettbewerb am Telefon", "Someone tries to spell their complicated last name to a call center agent using the phonetic alphabet, badly.", "Their invented code words ('B wie Banane') confuse the agent more than actual letters would.")
PREMISES[(T,4)] = ("Die Entschuldigungskarte", "A student writes an elaborate excuse note explaining a missed deadline.", "The excuse is so overly detailed and dramatic that the teacher suspects it's fiction and grades it as a short story instead.")
PREMISES[(T,5)] = ("Die Glückwunschkarten-Fabrik", "A family mass-produces greeting cards for every relative's birthday in one chaotic afternoon.", "They run out of good wishes and start writing increasingly absurd compliments by card fifteen.")
PREMISES[(T,6)] = ("Der Radiomoderator im Praktikum", "A nervous intern hosts their first live radio segment, stumbling over every hint and cue card.", "Dead air strikes at the worst moment, filled only by his own audible panic breathing.")
PREMISES[(T,7)] = ("Die Reklamations-Hotline", "Someone calls customer support, getting passed between departments over a minor complaint.", "By the third transfer they're talking to someone in a completely unrelated company.")
PREMISES[(T,8)] = ("Die Dorfzeitung", "A tiny local newsletter reports breathlessly on utterly mundane village events.", "The 'breaking news' headline turns out to be about a cat stuck in a tree, again.")
PREMISES[(T,9)] = ("Der Poesiealbum-Eintrag", "Classmates write increasingly ridiculous entries in a friend's old-school memory book.", "One entry is just a single word repeated in seventeen different colors.")
PREMISES[(T,10)] = ("Der stille Streit", "A couple has an argument entirely through passive-aggressive sticky notes instead of talking.", "The notes escalate until one is just a single, silently furious exclamation mark.")
PREMISES[(T,11)] = ("Der Umfrage-Stand in der Fußgängerzone", "A market researcher tries to get busy pedestrians to answer a long survey.", "Most answers are just people trying to walk away faster while still technically responding.")
PREMISES[(T,12)] = ("Die Nachbarschaftsversammlung", "Neighbors debate a trivial building issue with wildly exaggerated formality.", "The vote on a broken doorbell somehow takes longer than actually fixing it would have.")
PREMISES[(T,13)] = ("Die Wörterbuch-Rätselrunde", "Friends play a game guessing definitions of obscure words from an old dictionary.", "Someone's completely made-up fake definition wins the round because it sounded more convincing than the real one.")
PREMISES[(T,14)] = ("Der Zeitschriften-Abo-Stapel", "Someone finally sits down to sort through months of unread magazines and newsletters.", "Every single one somehow already has next month's issue arriving at the same moment.")

T = 'Stadt, Ämter & Recht'
PREMISES[(T,1)] = ("Der Behördenmarathon", "Someone spends an entire day bouncing between government offices trying to register a new address.", "Each office sends them to a different building, and they end up back at the first one by closing time.")
PREMISES[(T,2)] = ("Der Einbruch, der keiner war", "Police investigate a reported break-in that turns out to be the homeowner's own forgotten spare key attempt.", "The 'burglar' description perfectly matches the homeowner's own reflection in the window.")
PREMISES[(T,3)] = ("Das Fundbüro-Chaos", "A lost-and-found office is overflowing with bizarre unclaimed items nobody can explain.", "Someone claims a lost umbrella that turns out to belong to someone else entirely, with an identical one.")
PREMISES[(T,4)] = ("Die Ratsversammlung ums Wahrzeichen", "A town council argues passionately over a minor local landmark's upkeep.", "The heated debate turns out to be about a statue nobody can actually agree what it's supposed to depict.")
PREMISES[(T,5)] = ("Die Straßensperrung wegen Königsbesuch", "A small town prepares chaotically for a supposed royal visit that turns out to be a misunderstanding.", "The 'king' is actually just a costumed actor for an unrelated event three streets over.")
PREMISES[(T,6)] = ("Die Pressekonferenz im Rathaus", "A mayor holds an overly formal press conference about a very minor town achievement.", "The big announcement turns out to be about a new public bench.")
PREMISES[(T,7)] = ("Der verlegte Reisepass", "Someone frantically searches for their passport the night before a trip, tearing the apartment apart.", "It was in their jacket pocket the entire time, worn the whole search.")
PREMISES[(T,8)] = ("Die Verkehrskontrolle", "A police officer stops a driver for a minor infraction, and the excuse offered gets more elaborate by the second.", "The excuse eventually involves a very convincing but entirely fictional medical emergency.")
PREMISES[(T,9)] = ("Der Gerichtssaal-Sketch", "Friends stage a mock trial for a silly neighborhood dispute over a fence.", "The 'jury' is a group of very serious-looking garden gnomes borrowed for the occasion.")
PREMISES[(T,10)] = ("Der Ladendiebstahl-Verdacht", "A shopkeeper suspiciously eyes a customer buying a huge, oddly specific pile of random items.", "It turns out to be ingredients for the world's most impractical sandwich, not a heist.")
PREMISES[(T,11)] = ("Die Unterschriftensammlung", "A neighbor collects signatures for a petition about a trivial local issue with dramatic urgency.", "Half the signatures turn out to be from the same person using slightly different handwriting.")
PREMISES[(T,12)] = ("Die Zertifikatsübergabe", "A small community club holds an overly formal ceremony for a minor achievement certificate.", "The certificate is presented with the pomp of a Nobel Prize, for finishing a crossword puzzle.")

T = 'Arbeit & Beruf'
PREMISES[(T,1)] = ("Das Vorstellungsgespräch-Desaster", "A job applicant tries to sound impressively experienced despite obvious nervousness in an interview.", "He accidentally lists his hobby as 'work' three separate times before catching himself.")
PREMISES[(T,2)] = ("Die Kündigungs-Überraschung", "An employee dramatically quits a job they actually love, over a minor misunderstanding.", "They immediately regret it and spend the rest of the day trying to un-quit as casually as possible.")
PREMISES[(T,3)] = ("Der Streik in der Fabrik", "Factory workers stage a good-natured strike over cafeteria food quality, complete with homemade signs.", "Management resolves it instantly by simply improving the coffee, ending the strike in ten minutes.")
PREMISES[(T,4)] = ("Der erste Arbeitstag", "A nervous new hire tries to look competent on their very first day at an unfamiliar office.", "They confidently sit at the CEO's desk, not realizing whose office it actually is.")
PREMISES[(T,5)] = ("Die Firmengründung im Wohnzimmer", "Two friends 'launch a company' from a cluttered living room with wildly ambitious plans.", "Their entire business plan is written on the back of a pizza box.")
PREMISES[(T,6)] = ("Die Beförderungsfeier", "A workplace throws an overly enthusiastic party for a colleague's minor promotion.", "The cake spells the wrong job title, and nobody has the heart to mention it.")
PREMISES[(T,7)] = ("Der Werkstattbesuch", "A mechanic explains an absurdly complicated car problem to a confused customer using props.", "The 'complex diagnosis' turns out to be a coin stuck in the cup holder rattling around.")
PREMISES[(T,8)] = ("Das Praktikum bei der Zeitung", "An eager intern at a newspaper is assigned only trivial tasks despite grand journalistic ambitions.", "Their first 'published' piece is just the weekly parking schedule notice.")
PREMISES[(T,9)] = ("Der Radiosport-Kommentator", "An overly dramatic amateur commentator narrates a minor local sports match like it's a world championship.", "He gets more excited about the halftime snack break than the actual game.")
PREMISES[(T,10)] = ("Die Bewerbungsmappe", "Someone assembles an overly polished job application for a very casual part-time position.", "The application is longer than the actual job description.")
PREMISES[(T,11)] = ("Die Werkzeugkiste-Katastrophe", "A handyman's disorganized toolbox causes chaos on a simple repair job.", "He spends longer looking for the right tool than the actual repair would have taken.")

T = 'Kleidung & Aussehen'
PREMISES[(T,1)] = ("Die Modenschau im Wohnzimmer", "Friends stage a silly homemade fashion show using thrift-store finds and bedsheets as capes.", "The 'showstopper outfit' is just someone wrapped entirely in a shower curtain, strutting confidently.")
PREMISES[(T,2)] = ("Der Frisörbesuch, der schiefging", "Someone asks for a small trim and ends up with a dramatically different haircut.", "They insist they 'meant to do that' to everyone who asks, unconvincingly.")
PREMISES[(T,3)] = ("Der Kleiderschrank-Notstand", "Someone digs through an overstuffed wardrobe trying to find one specific missing item before a party.", "They find seventeen single socks and not one matching pair.")
PREMISES[(T,4)] = ("Das missglückte Date-Outfit", "Someone spends hours picking the perfect outfit for a first date, changing their mind constantly.", "They end up going in the very first outfit they tried on, an hour later.")

T = 'Körper & Gesundheit'
PREMISES[(T,1)] = ("Der Hausarztbesuch", "Someone describes a minor ailment to the doctor with wildly exaggerated symptoms.", "The doctor's diagnosis is simply 'you need more sleep,' delivered with visible exhaustion of their own.")
PREMISES[(T,2)] = ("Der Marathon-Trainingsunfall", "An overambitious first-time runner overdoes their training and ends up hilariously sore.", "They can't climb stairs the next day and have to be helped by a very unimpressed roommate.")
PREMISES[(T,3)] = ("Die Erkältungswelle im Büro", "An entire office catches the same cold within days, each person insisting theirs is the worst case.", "The healthiest-looking person turns out to be the one who's been secretly suffering the most.")
PREMISES[(T,4)] = ("Der Selbstdiagnose-Notfall", "Someone convinces themselves they have a serious illness after reading symptoms online.", "The actual diagnosis is just needing to drink more water.")
PREMISES[(T,5)] = ("Der Krankenhausbesuch bei Oma", "Grandchildren visit a grandparent recovering from a minor procedure in the hospital.", "The grandparent is more worried about missing their favorite TV show than about their own recovery.")
PREMISES[(T,6)] = ("Der Notaufnahme-Fehlalarm", "A minor kitchen accident sends someone rushing dramatically to the emergency room.", "The injury turns out to need nothing more than a small bandage, applied in thirty seconds.")
PREMISES[(T,7)] = ("Die Zahnarztangst", "Someone works themselves into a panic before a routine dental checkup.", "The appointment is over before they've even finished nervously rambling in the waiting room.")
PREMISES[(T,8)] = ("Der Physiotherapietermin", "A patient exaggerates every small movement during a physical therapy session for sympathy.", "The therapist calmly points out they were sprinting fine in the parking lot minutes earlier.")
PREMISES[(T,9)] = ("Der Yoga-Kurs für Anfänger", "A stiff beginner struggles hilariously through a gentle yoga class meant for relaxation.", "Their idea of the 'child's pose' looks suspiciously like they've simply fallen asleep.")
PREMISES[(T,10)] = ("Die Familiengeschichte über Uroma", "Relatives tell exaggerated stories about a great-grandmother's supposedly dramatic health scares.", "Every retelling makes the illness sound more serious than the doctor's actual, mild diagnosis.")
PREMISES[(T,11)] = ("Der Apothekenbesuch mit Zettel", "Someone hands the pharmacist a long, messy shopping list mixing real medicine with random errands.", "The pharmacist patiently points out that 'milk' isn't something they sell.")

T = 'Reisen & Urlaub'
PREMISES[(T,1)] = ("Der Packstress vor der Abreise", "Someone tries to pack for a trip at the last minute, throwing random items into an overstuffed suitcase.", "They forget the actual passport but somehow remember three different chargers for devices they don't own.")
PREMISES[(T,2)] = ("Die Hotelverwechslung", "A family arrives at what they think is their booked hotel, only to find it's the wrong one entirely.", "The actual hotel turns out to be a tiny, forgotten guesthouse two streets away with a much better breakfast.")
PREMISES[(T,3)] = ("Der Rentnerausflug ans Meer", "A group of retirees goes on a seaside excursion, bickering affectionately about every stop on the itinerary.", "Their strict schedule gets completely derailed by an impromptu ice cream stop that everyone secretly wanted anyway.")
PREMISES[(T,4)] = ("Die Heimreise-Odyssee", "A trip home gets delayed by every possible transport mishap in a row.", "By the time they finally arrive, they've told the story so many times it's grown into an epic saga.")

T = 'Zeit & Kalender'
PREMISES[(T,1)] = ("Der Morgenmuffel", "Someone struggles through their entire morning routine half-asleep, narrating each stumbling step.", "They leave the house confidently before realizing they're still wearing slippers.")
PREMISES[(T,2)] = ("Die Terminüberschneidung", "Someone realizes they've double-booked two important events at the exact same time.", "They try sprinting between both venues and end up fully missing one and half-attending the other.")
PREMISES[(T,3)] = ("Die Silvesterfeier-Erinnerungen", "Friends recount a wild New Year's Eve party, each remembering the timeline completely differently.", "Nobody can agree what time the fireworks actually started, or who started them early by accident.")
PREMISES[(T,4)] = ("Der ewig gleiche Tagesablauf", "Someone complains about how monotonous their daily routine has become, describing it hour by hour.", "The 'boring routine' includes an oddly specific daily argument with a stubborn printer.")
PREMISES[(T,5)] = ("Die verpasste Deadline", "Someone realizes far too late that an important deadline was actually yesterday, not today.", "Their 'punctual' excuse email is sent exactly one minute before they finally notice the mistake.")
PREMISES[(T,6)] = ("Der Startschuss zum Sommerfest", "A neighborhood festival's opening ceremony is delayed repeatedly by small technical mishaps.", "By the time the 'official start' finally happens, half the guests have already eaten all the food.")
PREMISES[(T,7)] = ("Der Kalender voller Erinnerungen", "Someone reviews an old calendar full of forgotten appointments and reminders scribbled in the margins.", "One cryptic note just says 'don't forget!!' with no indication of what not to forget.")

T = 'Gesellschaft, Politik & Wirtschaft'
PREMISES[(T,1)] = ("Die Nachbarschaftsdebatte", "Neighbors from different backgrounds debate a minor community issue, each bringing in wildly broad arguments.", "The debate about a shared garden fence somehow ends up covering the entire history of humanity.")
PREMISES[(T,2)] = ("Der Wirtschaftsgipfel im Kleingarten", "Allotment gardeners hold a mock 'economic summit' over how to divide a shared harvest fairly.", "Their complex trade agreement collapses over who gets the last, biggest tomato.")

T = 'Essen, Kochen & Restaurant'
PREMISES[(T,1)] = ("Der Bäckerei-Notfall", "Someone bakes bread for the first time and it comes out looking nothing like the recipe photo.", "They serve it anyway, confidently calling the brick-like loaf 'rustic'.")
PREMISES[(T,2)] = ("Der Café-Vormittag", "Friends meet at a café for coffee and end up arguing playfully about the 'correct' way to eat an egg.", "The debate escalates until the whole café is quietly listening in, amused.")
PREMISES[(T,3)] = ("Das Grillfest der Nachbarn", "A neighborhood barbecue turns chaotic as everyone insists on grilling their own dish their own way.", "The grill catches a small, dramatic flare-up right as the 'grill master' is bragging about his technique.")
PREMISES[(T,4)] = ("Die Kochshow-Parodie", "Friends film a silly homemade cooking show, narrating dramatically over a very simple dish.", "The 'secret ingredient' reveal is just regular salt, treated like a plot twist.")
PREMISES[(T,5)] = ("Der Fast-Food-Notstand", "A group debates for way too long over a simple fast-food order, changing their minds constantly.", "By the time they finally order, the kitchen is already closing.")
PREMISES[(T,6)] = ("Die Familienrezept-Weitergabe", "A grandmother tries to teach her grandchild a traditional recipe with wildly imprecise, old-fashioned measurements.", "'A handful' and 'until it feels right' turn out to be the only actual instructions given.")
PREMISES[(T,7)] = ("Der Marmeladen-Wettbewerb", "Neighbors compete in an amateur jam-making contest with fiercely guarded secret recipes.", "The 'secret ingredient' in the winning jam turns out to be a happy accident nobody can replicate again.")
PREMISES[(T,8)] = ("Das internationale Buffet", "A potluck dinner features dishes from many countries, with each guest passionately defending their own.", "The most popular dish by far is the one nobody can identify or pronounce.")
PREMISES[(T,9)] = ("Die Restaurantkritik-Parodie", "An amateur food blogger dramatically reviews a very ordinary neighborhood restaurant.", "Their five-paragraph review is entirely about the bread basket.")
PREMISES[(T,10)] = ("Der zu scharfe Wettkampf", "Friends challenge each other to eat increasingly spicy food at a competitive dinner.", "The self-proclaimed 'spice champion' taps out first, dramatically reaching for the entire milk carton.")
PREMISES[(T,11)] = ("Der Kellner-Ausbildungstag", "A trainee waiter fumbles through their first shift, mixing up every order at the table.", "They somehow end up serving dessert before the appetizer, and the guests decide they actually prefer it that way.")
PREMISES[(T,12)] = ("Der Weinkeller-Ausflug", "Friends tour a small local winery, pretending to be much more sophisticated tasters than they actually are.", "Their elaborate tasting notes are all suspiciously similar to 'tastes like grapes.'")

T = 'Tiere'
PREMISES[(T,1)] = ("Der chaotische Bauernhofbesuch", "City visitors help feed animals on a farm and immediately get overwhelmed by an overeager goat.", "The goat steals someone's hat and proudly parades around the pen wearing it like a trophy.")
