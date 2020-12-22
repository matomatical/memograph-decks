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
so              -- this
dann            -- then
da              -- there
noch            -- still/yet                # has further meanings
also            -- so/therefore
nur             -- only
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
erst            -- first/only               # not clear...?
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
schließlich     -- after all/finally
eher            -- earlier
eher            -- rather/more
"""
"""
je              -- 
früher          -- 
zunächst        -- 
irgendwie       -- 
bisher          -- 
manchmal        -- 
her             -- 
ebenso          -- 
ziemlich        -- 
außerdem        -- 
inzwishen       -- 
sofort          -- 
plötzlich       -- 
bald            -- 
genug           -- 
endlich         -- 
insbesondere    -- 
hin             -- 
ebenfalls       -- 
gestern         -- 
bitte           -- 
zusammen        -- 
jedenfalls      -- 
wobei           -- 
bloß            -- 
jeweils         -- 
unten           -- 
insgesamt       -- 
vorher          -- 
beispielsweise  -- 
meist           -- 
trozdem         -- 
zudem           -- 
leider          -- 
mindestens      -- 
zumindest       -- 
irgendwo        -- 
zuerst          -- 
unbedingt       -- 
hinaus          -- 
zuletzt         -- 
dennoch         -- 
lieber          -- 
zugleich        -- 
nochmal         -- 
danke           -- 
derzeit         -- 
zuvor           -- 
teilweise       -- 
"""
