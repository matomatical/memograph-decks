from mg.graph import Node
from mg.data import parse

def graph():
    for de, en in parse(LINKS):
        yield (
                Node(en, speak_str=en, speak_voice="en"),
                Node(de, speak_str=de, speak_voice="de"),
                "de.verb"
            )

LINKS = """de -- en                                     # notes (ignored)
sein          -- to be                                  # aux
haben         -- to have                                # aux
werden        -- to become                              # aux?
werden        -- to will                                # modal?
können        -- to can                                 # modal
müssen        -- to must                                # modal
sollen        -- to should/ought                        # modal
wollen        -- to want                                # modal
dürfen        -- to may                                 # modal
mögen         -- to like                                # modal
sagen         -- to say
machen        -- to make/do
geben         -- to give
kommen        -- to come
gehen         -- to go
wissen        -- to know    
sehen         -- to see
lassen        -- to let/allow
lassen        -- to have done
stehen        -- to stand
finden        -- to find
bleiben       -- to stay (at)
liegen        -- to lie (down)
heißen        -- to hail/be called
denken        -- to think
nehmen        -- to take    
tun           -- to do/perform
glauben       -- to believe
halten        -- to halt/stop
halten        -- to hold
nennen        -- to name
zeigen        -- to show
führen        -- to lead
sprechen      -- to speak
bringen       -- to bring
bringen       -- to take    
leben         -- to live (alive)
fahren        -- to go/ride/drive/etc.
meinen        -- to think/opine
fragen        -- to ask
kennen        -- to know    
gelten        -- to be valid (not expired)
stellen       -- to place/set
spielen       -- to play
arbeiten      -- to work
brauchen      -- to require/need
folgen        -- to follow
lernen        -- to learn
bestehen      -- to exist
bestehen      -- to insist
bestehen      -- to pass (an exam)                      # be + stehen
verstehen     -- to understand                          # ver + stehen
setzen        -- to set/place
bekommen      -- to get                                 # be + kommen
beginnen      -- to begin    
erzählen      -- to tell                                # er + zählen (?)
versuchen     -- to try/attempt                         # ver + suchen
schreiben     -- to write
laufen        -- to walk
erklären      -- to explain                             # er + klären
entsprechen   -- to correspond                          # ent + sprechen
sitzen        -- to sit
ziehen        -- to pull/move
scheinen      -- to shine
scheinen      -- to seem/appear    
fallen        -- to fall
gehören       -- to belong                              # ge + hören?
entstehen     -- to originate/develop
entstehen     -- to arise                               # ent + stehen
erhalten      -- to receive                             # er + halten
treffen       -- to meet
treffen       -- to hit
suchen        -- to search
legen         -- to lay (sth. down)
vorstellen     -- to introduce                          # like, to 'set out'?
vorstellen     -- to imagine                            # vor + stellen
handeln       -- to deal/trade
erreichen     -- to achieve/reach                       # er + reichen
tragen        -- to carry
tragen        -- to wear
schaffen      -- to manage
schaffen      -- to create
lesen         -- to read
verlieren     -- to lose                                # ver + lieren?
darstellen    -- to portray/depict                      # dar + stellen
erkennen      -- to admit/recognise
entwickeln    -- to develop                             # ent + wickeln
reden         -- to talk
aussehen      -- to look/appear
erscheinen    -- to seem/appear                         # er + scheinen
bilden        -- to form
bilden        -- to educate
anfangen      -- to begin                               # an + fangen
erwarten      -- to expect                              # er + warten
wohnen        -- to live (reside)
betreffen     -- to concern/affect                      # be + treffen
warten        -- to wait
vergehen      -- to pass (time)                         # ver + gehen
helfen        -- to help
gewinnen      -- to win/gain                            # not from winnen?
schließen     -- to close
fühlen        -- to feel
bieten        -- to offer    
interessieren -- to interest
erinnern      -- to remind
ergeben       -- to result in
anbieten      -- to offer    
studieren     -- to study
verbinden     -- to connect/link
ansehen       -- to watch/look at
fehlen        -- to lack
bedeuten      -- to mean/represent
vergleichen   -- to compare
möchten       -- to would like                          # modal, K2P of mögen

# verbs gathered randomly e.g. from class, but i remember them anyway
atmen         -- to breathe
sterben       -- to die
hören         -- to hear
lachen        -- to laugh
lieben        -- to love
hassen        -- to hate
essen         -- to eat
trinken       -- to drink
fressen       -- to feed
rennen        -- to run/race
rennen        -- to scramble
vergessen     -- to forget
kaufen        -- to buy
einkaufen     -- to shop                                # ein + kaufen
verkaufen     -- to sell                                # ver + kaufen
passen        -- to fit/suit
passen        -- to match
kosten        -- to cost
stehlen       -- to steal
zahlen        -- to pay                                 # difference?
bezahlen      -- to pay                                 # be + zahlen
bitten        -- to thank
gefallen      -- to please/appeal to
schlafen      -- to sleep
kochen        -- to cook
backen        -- to bake
besuchen      -- to visit                               # be + suchen?
schneien      -- to snow
regnen        -- to rain
üben          -- to practice
antworten     -- to answer
diskutieren   -- to discuss
analysieren   -- to analyse
buchstabieren -- to spell
streichen     -- to paint/smear
streichen     -- to eliminate
streichen     -- to decorate
unterstreichen -- to underline                          # unter + streichen
rechnen       -- to calculate
notieren      -- to note (down)
markieren     -- to highlight
ergänzen      -- to complete/enter/fill in              # er + gänzen?
ergänzen      -- to complete/complement
ordnen        -- to order/arrange
zuordnen      -- to collate                             # zu + ordnen
lösen         -- to solve
zeichnen      -- to draw
schneiden     -- to cut
öffnen        -- to open
messen        -- to measure
fangen        -- to catch
leihen        -- to loan/borrow
treten        -- to step
brechen       -- to break
unterbrechen  -- to interrupt                           # unter + brechen
befehlen      -- to command                             # emp + fehlen?
empfehlen     -- to recommend                           # emp + fehlen?
werfen        -- to throw
holen         -- to fetch/get
wiederholen   -- to repeat                              # wieder + holen?
passieren     -- to pass/transpire
"""
