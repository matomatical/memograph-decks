from mg.graph import Node
from mg.data import parse

def graph():
    for de, en in parse(LINKS):
        yield (
                Node(en, speak_str=en, speak_voice="en"),
                Node(de, speak_str=de, speak_voice="de"),
                "de.adv"
            )

# NOTE: These seem pretty tough to translate due to differences in adverb
# usage between German and English, especially compared to adjectives.
# But below are some rough glosses that should be enough to get started.
# NOTE: Some of these are also kinda adjectives...! Though not the most
# frequently used ones.
LINKS = """de   -- en                       # notes (ignored)
auch            -- also
so              -- so/thus/this way
dann            -- then
da              -- there
noch            -- still/yet                # has further meanings
also            -- so/therefore
nur             -- just/only
schon           -- already
mehr            -- more                     # ahhh 'be more red', 'run more'
jetzt           -- now
immer           -- always
sehr            -- so/very
hier            -- here
doch            -- but/indeed               # tough to translate, see usages
wieder          -- again
eigentlich      -- actually
oben            -- above/up                 # not clear...?
nun             -- now
heute           -- today
weit            -- widely                   # also adj 'wide'?
eben            -- just/exactly             # tough to translate, see usages
erst            -- first
natürlich       -- naturally
vielleicht      -- perhaps/maybe
dort            -- there
einmal          -- once
gar             -- at all
bereits         -- already
etwa            -- about/approx
gerade          -- just/exactly             # also adj 'direct'/'straight'?
zwar            -- admittedly
zwar            -- to be precise
wirklich        -- really/actually
jedoch          -- however
nie             -- never
oft             -- often
allerdings      -- though
allerdings      -- certainly
fast            -- almost/nearly
wohl            -- well
überhaupt       -- generally
gern(e)         -- fondly/with pleasure
besonders       -- particularly
warum           -- why
allein          -- alone
kaum            -- hardly/barely
deshalb         -- therefore
sogar           -- even/indeed
sonst           -- otherwise
weiter          -- further
anders          -- differently
schließlich     -- in closing/conclusion
eher            -- earlier
eher            -- rather/more
je              -- ever/forever             # also a preposition for 'each'
früher          -- formerly                 # also adjective 'former'
zunächst        -- firstly
zunächst        -- for now
irgendwie       -- somehow
bisher          -- until now/hitherto
manchmal        -- sometimes
her             -- from sth/swh             # also broader, see usage
ebenso          -- just as (sth as sth)
ziemlich        -- quite/fairly
außerdem        -- besides/as well
inzwischen      -- meanwhile
sofort          -- immediately
plötzlich       -- suddenly
bald            -- soon
genug           -- enough
endlich         -- finally
insbesondere    -- in particular
hin             -- to sth/swh
ebenfalls       -- likewise
gestern         -- yesterday
bitte           -- please
zusammen        -- together
jedenfalls      -- in any case
wobei           -- whereby (by/near what)   # interrogative *adverb* (?)
bloß            -- just/only
jeweils         -- any/each time
unten           -- down/below/under/at the bottom
insgesamt       -- in all/in total
vorher          -- before                   # cf. früher?
beispielsweise  -- for example
meist           -- mostly
trotzdem        -- nevertheless
zudem           -- moreover
leider          -- unfortunately
mindestens      -- at least
zumindest       -- at least
irgendwo        -- somewhere
zuerst          -- first
unbedingt       -- absolutely               # also adjective 'absolute'
hinaus          -- out/beyond
zuletzt         -- lastly
dennoch         -- nevertheless
lieber          -- gladly (?)               # 'rather' in the freq dict? ??
zugleich        -- simultaneously
nochmal         -- again                    # also 'noch mal' (just noch+mal?)
danke           -- thank you                # also 'no, thank you' to decline
derzeit         -- at the moment
zuvor           -- before
teilweise       -- partly
"""
