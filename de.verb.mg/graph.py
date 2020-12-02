def graph():
    for line in LINKS.splitlines()[1:]:
        line = line.split("#", maxsplit=1)[0]
        if "--" not in line:
            continue
        de, en = line.split("--")
        de = de.strip()
        en = en.strip()
        yield ("de.verb", en, de)

LINKS = """de -- en                                     # notes (ignored)
sein          -- to be                                  # aux
haben         -- to have                                # aux
werden (1)    -- to become                              # aux?
werden (2)    -- to will                                # modal?
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
wissen        -- to know (1)
sehen         -- to see
lassen (1)    -- to let/allow
lassen (2)    -- to have done
stehen        -- to stand
finden        -- to find
bleiben       -- to stay (at)
liegen        -- to lie (down)
heißen        -- to hail/be called
denken        -- to think
nehmen        -- to take (1)
tun           -- to do/perform
glauben       -- to believe
halten (1)    -- to halt/stop
halten (2)    -- to hold
nennen        -- to name
zeigen        -- to show
führen        -- to lead
sprechen      -- to speak
bringen (1)   -- to bring
bringen (2)   -- to take (2)
leben         -- to live (alive)
fahren        -- to go/ride/drive/etc.
meinen        -- to think/opine
fragen        -- to ask
kennen        -- to know (2)
gelten        -- to be valid (not expired)
stellen       -- to place/set
spielen       -- to play
arbeiten      -- to work
brauchen      -- to require/need
folgen        -- to follow
lernen        -- to learn
bestehen (1)  -- to exist
bestehen (2)  -- to insist
bestehen (3)  -- to pass (an exam)                      # be + stehen
verstehen     -- to understand                          # ver + stehen
setzen        -- to set/place
bekommen      -- to get                                 # be + kommen
beginnen      -- to begin (1)
erzählen      -- to tell                                # er + zählen (?)
versuchen     -- to try/attempt                         # ver + suchen
schreiben     -- to write
laufen        -- to walk
erklären      -- to explain                             # er + klären
entsprechen   -- to correspond                          # ent + sprechen
sitzen        -- to sit
ziehen        -- to pull/move
scheinen (1)  -- to shine
scheinen (2)  -- to seem/appear (1)
fallen        -- to fall
gehören       -- to belong                              # ge + hören?
entstehen (1) -- to originate/develop
entstehen (2) -- to arise                               # ent + stehen
erhalten      -- to receive                             # er + halten
treffen (1)   -- to meet
treffen (2)   -- to hit
suchen        -- to search
legen         -- to lay (sth. down)
vorstellen (1) -- to introduce                          # like, to 'set out'?
vorstellen (2) -- to imagine                            # vor + stellen
handeln       -- to deal/trade
erreichen     -- to achieve/reach                       # er + reichen
tragen (1)    -- to carry
tragen (2)    -- to wear
schaffen (1)  -- to manage
schaffen (2)  -- to create
lesen         -- to read
verlieren     -- to lose                                # ver + lieren?
darstellen    -- to portray/depict                      # dar + stellen
erkennen      -- to admit/recognise
entwickeln    -- to develop                             # ent + wickeln
reden         -- to talk
aussehen      -- to look/appear
erscheinen    -- to seem/appear (2)                     # er + scheinen
bilden (1)    -- to form
bilden (2)    -- to educate
anfangen      -- to begin (2)                           # an + fangen
erwarten      -- to expect                              # er + warten
wohnen        -- to live (reside)
betreffen     -- to concern/affect                      # be + treffen
warten        -- to wait
vergehen      -- to pass (time)                         # ver + gehen
helfen        -- to help
gewinnen      -- to win/gain                            # not from winnen?
schließen     -- to close
fühlen        -- to feel
bieten        -- to offer (1)
interessieren -- to interest
erinnern      -- to remind
ergeben       -- to result in
anbieten      -- to offer (2)
studieren     -- to study
verbinden     -- to connect/link
ansehen       -- to watch/look at
fehlen        -- to lack
bedeuten      -- to mean/represent
vergleichen   -- to compare
möchten       -- to would like                          # modal, K2P of mögen

# verbs gathered randomly e.g. from class, but i remember them anyway
atmen         -- to breath
sterben       -- to die
hören         -- to hear
lachen        -- to laugh
lieben        -- to love
hassen        -- to hate
essen         -- to eat
trinken       -- to drink
fressen       -- to feed
rennen (1)    -- to run/race
rennen (2)    -- to scramble
vergessen     -- to forget
kaufen        -- to buy
einkaufen     -- to shop                                # ein + kaufen
verkaufen     -- to sell                                # ver + kaufen
passen (1)    -- to fit/suit
passen (2)    -- to match
kosten        -- to cost
stehlen       -- to steal
zahlen        -- to pay (1)                             # difference?
bezahlen      -- to pay (2)                             # be + zahlen
bitten        -- to thank
gefallen      -- to please/appeal to
schlaffen     -- to sleep
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
streichen (1) -- to paint/smear
streichen (2) -- to eliminate
streichen (3) -- to decorate
unterstreichen -- to underline                          # unter + streichen
rechnen       -- to calculate
notieren      -- to note (down)
markieren     -- to highlight
ergänzen (1)  -- to complete/enter/fill in              # er + gänzen?
ergänzen (2)  -- to complete/complement
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
"""
