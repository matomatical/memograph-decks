from mg.graph import Node
from mg.data import parse

def graph():
    for de, en in parse(LINKS):
        yield (
                Node(en, speak_str=en, speak_voice="en"),
                Node(de, speak_str=de, speak_voice="de"),
                "de.verb"
            )

LINKS = """de   -- en                       # notes (ignored)
sein            -- to be                    # aux
haben           -- to have                  # aux
werden          -- to become                # aux?
werden          -- to will                  # modal?
können          -- to can                   # modal
müssen          -- to must                  # modal
sollen          -- to should/ought          # modal
wollen          -- to want                  # modal
dürfen          -- to may                   # modal
mögen           -- to like                  # modal
sagen           -- to say
machen          -- to make/do
geben           -- to give
kommen          -- to come
gehen           -- to go
wissen          -- to know    
sehen           -- to see
lassen          -- to let/allow
lassen          -- to have done
stehen          -- to stand
finden          -- to find
bleiben         -- to stay (at)
liegen          -- to lie (down)
heißen          -- to hail/be called
denken          -- to think
nehmen          -- to take    
tun             -- to do/perform
glauben         -- to believe
halten          -- to halt/stop
halten          -- to hold
nennen          -- to name
zeigen          -- to show
führen          -- to lead
sprechen        -- to speak
bringen         -- to bring
bringen         -- to take    
leben           -- to live (alive)
fahren          -- to go/ride/drive/etc.
meinen          -- to think/opine
fragen          -- to ask
kennen          -- to know    
gelten          -- to be valid (not expired)
stellen         -- to place/set
spielen         -- to play
arbeiten        -- to work
brauchen        -- to require/need
folgen          -- to follow
lernen          -- to learn
bestehen        -- to exist
bestehen        -- to insist
bestehen        -- to pass (an exam)        # be + stehen
verstehen       -- to understand            # ver + stehen
setzen          -- to set/place
bekommen        -- to get                   # be + kommen
beginnen        -- to begin    
erzählen        -- to tell                  # er + zählen (?)
versuchen       -- to try/attempt           # ver + suchen
schreiben       -- to write
laufen          -- to walk
erklären        -- to explain               # er + klären
entsprechen     -- to correspond            # ent + sprechen
sitzen          -- to sit
ziehen          -- to pull/move
scheinen        -- to shine
scheinen        -- to seem/appear    
fallen          -- to fall
gehören         -- to belong                # ge + hören?
entstehen       -- to originate/develop
entstehen       -- to arise                 # ent + stehen
erhalten        -- to receive               # er + halten
treffen         -- to meet
treffen         -- to hit
suchen          -- to search
legen           -- to lay (sth. down)
vorstellen      -- to introduce             # like, to 'set out'?
vorstellen      -- to imagine               # vor + stellen
handeln         -- to deal/trade
erreichen       -- to achieve/reach         # er + reichen
tragen          -- to carry
tragen          -- to wear
schaffen        -- to manage
schaffen        -- to create
lesen           -- to read
verlieren       -- to lose                  # ver + lieren?
darstellen      -- to portray/depict        # dar + stellen
erkennen        -- to admit/recognise
entwickeln      -- to develop               # ent + wickeln
reden           -- to talk
aussehen        -- to look/appear
erscheinen      -- to seem/appear           # er + scheinen
bilden          -- to form
bilden          -- to educate
anfangen        -- to begin                 # an + fangen
erwarten        -- to expect                # er + warten
wohnen          -- to live (reside)
betreffen       -- to concern/affect        # be + treffen
warten          -- to wait
vergehen        -- to pass (time)           # ver + gehen
helfen          -- to help
gewinnen        -- to win/gain              # not from winnen?
schließen       -- to close
fühlen          -- to feel
bieten          -- to offer    
interessieren   -- to interest
erinnern        -- to remind
ergeben         -- to result in
anbieten        -- to offer
studieren       -- to study
verbinden       -- to connect/link          # ver + binden
ansehen         -- to look at/watch         # an + sehen
fehlen          -- to lack
bedeuten        -- to mean/represent
vergleichen     -- to compare
möchten         -- to would like            # modal, actually K2P of mögen

steigen         -- to climb/increase
nutzen          -- to use
schauen         -- to look (at)
verlassen       -- to leave
einsetzen       -- to insert
ändern          -- to change
wachsen         -- to wax/grow
ausgehen        -- to go out
ausgehen        -- to assume
geschehen       -- to happen
beschreiben     -- to describe
annehmen        -- to take on/accept
kriegen         -- to receive               # see differences on stack exch.
planen          -- to plan
wirken          -- to work/take effect
bezeichnen      -- to call/name
befinden sich   -- to be/find oneself       # 'i find myself ...?' modal?
passieren       -- to pass/transpire
rufen           -- to call
aufnehmen       -- to take on/challenge
aufnehmen       -- to take up               # pick up, absorb, record, etc.
aufnehmen       -- to take in               # admit, receive, include, etc.
zunehmen        -- to gain/increase
bestimmen       -- to decide/determine/define
fordern         -- to demand
gefallen        -- to please/appeal to
öffnen          -- to open
schlagen        -- to hit/strike
treten          -- to step
übernehmen      -- to take over
übernehmen      -- to take on/accept
übernehmen sich -- to overdo/take on too much
verändern       -- to change
lachen          -- to laugh
verwenden       -- to use                   # there are some other senses
wählen          -- to choose/select/vote
erfolgen        -- to occur
enthalten       -- to hold in/contain
betrachten      -- to look at/watch
betrachten      -- to look at/consider
entscheiden     -- to decide
gelingen        -- to succeed
kaufen          -- to buy
erfahren        -- to find out/hear
erfahren        -- to experience
vergessen       -- to forget
stattfinden     -- to occur
bewegen         -- to move
feststellen     -- to establish/determine
verschwinden    -- to disappear
dienen          -- to serve (sb/with sth)
trinken         -- to drink
auftreten       -- to tread
auftreten       -- to step up/appear
stimmen         -- to be correct/all right  # also to vote, to tune (guitar)
verhalten sich  -- to behave                # to hold out? too hold oneself?
berichten       -- to report
rechnen         -- to calculate             # source of 'to reckon'?
beobachten      -- to observe
erleben         -- to experience
holen           -- to fetch/get
essen           -- to eat
reichen         -- to reach                 # to extend / to be enough
sterben         -- to die
unterscheiden   -- to distinguish
leisten         -- to achieve
verlangen       -- to demand
werfen          -- to throw
vorliegen       -- to be present (with)
zählen          -- to count
wünschen        -- to wish
bauen           -- to build
hängen          -- to hang
hoffen          -- to hope
freuen          -- to be happy
teilen          -- to divide/share          # teil = part
bezahlen        -- to pay
dauern          -- to dure/last/take (time) # 'duration'
stecken         -- to stash/put/pin
besuchen        -- to visit
bitten          -- to request/beg
sorgen sich     -- to worry
sorgen          -- to look after
ankommen        -- to arrive
beziehen        -- to cover                 # there are more senses
spüren          -- to sense/notice
spüren          -- to track
erhöhen         -- to raise/increase
melden          -- to register              # in rummy, we 'meld' to begin
melden          -- to report
vorkommen       -- to come forth
vorkommen       -- to occur
besitzen        -- to own/possess
betonen         -- to stress/emphasise
erfüllen        -- to fulfil/grant
beteiligen sich -- to partake in
beteiligen sich -- to share in
merken          -- to mark/notice           # 'mark my words'
merken sich     -- to remember
passen          -- to fit/suit
passen          -- to match
eignen sich     -- to suit as
richten         -- to aim/direct at
richten         -- to address (sb)
umfassen        -- to comprise
umfassen        -- to enclose
schlafen        -- to sleep
unterstützen    -- to support
lächeln         -- to smile
beschäftigen    -- to occupy/employ
lösen           -- to solve
lösen           -- to loosen
antworten       -- to answer
trennen         -- to separate/sever
einstellen      -- to put away
einstellen      -- to set up/prepare
einstellen      -- to stop/cease
lieben          -- to love
durchführen     -- to carry through
genügen         -- to suffice/be enough

aufbauen        -- to build up/erect
bestätigen      -- to confirm/endorse
untersuchen     -- to examine
verkaufen       -- to sell
blicken         -- to look/glance
drücken         -- to press/push
eingehen        -- to go into (history/heaven/matrimony/etc.)
erlauben        -- to allow
ausreichen      -- to suffice
schweigen       -- to remain silent
behandeln       -- to treat/handle
treiben         -- to drive (nail/animals/ball/etc.)
treiben         -- to pursue (craft/study/hobby/etc.)
überzeugen      -- to convince
benutzen        -- to use
drohen          -- to threaten
versprechen     -- to promise
entdecken       -- to discover
klingen         -- to klang/sound
reagieren       -- to react
kosten          -- to cost
verdienen       -- to earn
drehen          -- to turn/shift/spin
überraschen     -- to surprise
betreiben       -- to proceed with
fliegen         -- to fly
heben           -- to lift
stoßen          -- to thrust/push/punch
vertreten       -- to represent
vertreten       -- to advocate
ermöglichen     -- to enable
herstellen      -- to make/produce
leiden          -- to suffer
schicken        -- to send
wechseln        -- to swap/exchange
liefern         -- to deliver
zahlen          -- to pay
benötigen       -- to require/need
stammen         -- to stem/come (from sth)
verhindern      -- to prevent
abschließen     -- to lock
abschließen     -- to conclude/end
reisen          -- to travel
singen          -- to sing
überlegen       -- to hold over (hold sth over sb)
überlegen       -- to lay over/consider
überlegen sich  -- to lean over
erwähnen        -- to mention
greifen         -- to grab
verzichten      -- to do without
aufgeben        -- to give up               # also has some other meanings
betragen        -- to come/amount to        # lit. to carry to?
betragen sich   -- to behave                # lit. to carry oneself?
kochen          -- to cook
angeben         -- to declare               # lit. to give on?
angeben         -- to brag
angeben         -- to serve (ball)
begründen       -- to substantiate/justify
einrichten      -- to furnish               # has also some more meanings
festhalten      -- to hold
festhalten      -- to detain
geraten         -- to come into
geraten         -- to turn out
verfügen        -- to decree
schützen        -- to protect
vorbereiten     -- to prepare
wiederholen     -- to repeat                # wieder + holen?
stören          -- to disturb
feiern          -- to celebrate
vermitteln      -- to mediate
berücksichtigen -- to consider
ausschließen    -- to exclude/rule out
diskutieren     -- to discuss
funktionieren   -- to function/work
gründen         -- to found/establish
herrschen       -- to reign/prevail         # used also for environments
schieben        -- to push
schieben        -- to slide
behaupten       -- to assert/maintain
erheben         -- to raise
verfolgen       -- to pursue
zurückkommen    -- to return
zwingen         -- to force
ablehnen        -- to decline
anwenden        -- to employ/apply
auftauchen      -- to turn up/emerge/surface
beeinflussen    -- to influence
einfallen       -- to occur/remind          # lit. 'to fall on' like an apple?
einfallen       -- to come in/invade
existieren      -- to exist
fördern         -- to promote/support
ansprechen      -- to address               # also some more meanings
beachten        -- to heed/pay attention to
empfinden       -- to feel
entfernen       -- to remove
entfernen sich  -- to leave
schneiden       -- to cut
sichern         -- to secure
wenden          -- to turn
fassen          -- to grasp                 # also has some other meanings
informieren     -- to inform
kümmern         -- to concern
nicken          -- to nod
organisieren    -- to organize
prägen          -- to emboss/mint/shape
prägen          -- to coin (a word)
sinken          -- to sink
sinken          -- to fall/decrease
vermeiden       -- to avoid
ankündigen      -- to announce/herald
aufstehen       -- to stand up
verstärken      -- to strengthen/reinforce
vorsehen        -- to forsee/plan
beschränken     -- to restrict/limit
verletzen       -- to injure

# verbs gathered randomly e.g. from class, but i remember them anyway
servieren       -- to serve out
atmen           -- to breathe
hören           -- to hear
hassen          -- to hate
fressen         -- to feed
rennen          -- to run/race
rennen          -- to scramble
einkaufen       -- to shop                  # ein + kaufen
stehlen         -- to steal
backen          -- to bake
schneien        -- to snow
regnen          -- to rain
üben            -- to practice
analysieren     -- to analyse
buchstabieren   -- to spell
streichen       -- to paint/smear
streichen       -- to eliminate
streichen       -- to decorate
unterstreichen  -- to underline             # unter + streichen
notieren        -- to note (down)
markieren       -- to highlight
ergänzen        -- to complete/enter/fill in    # er + gänzen?
ergänzen        -- to complete/complement
ordnen          -- to order/arrange
zuordnen        -- to collate               # zu + ordnen
zeichnen        -- to draw
messen          -- to measure
fangen          -- to catch
leihen          -- to loan/borrow
brechen         -- to break
unterbrechen    -- to interrupt             # unter + brechen
befehlen        -- to command               # emp + fehlen?
empfehlen       -- to recommend             # emp + fehlen?
füllen          -- to fill
fassen          -- to grasp
"""
