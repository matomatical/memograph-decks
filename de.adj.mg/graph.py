from mg.graph import SpokenNode

def graph():
    for line in LINKS.splitlines()[1:]:
        line = line.split("#", maxsplit=1)[0]
        if "--" not in line:
            continue
        de, en = line.split("--")
        de = de.strip()
        en = en.strip()
        yield (
                SpokenNode(en, voice="en"),
                SpokenNode(de, voice="de"),
                "de.adj"
            )

LINKS = """de -- en                                     # notes (ignored)
ganz (1)      -- whole (1)
ganz (2)      -- all of the
groß          -- great/big
gut           -- good
neu           -- new
erste         -- first                                  # always decline
lang          -- long
deutsch       -- German
klein         -- small/little
alt           -- old
hoch (1)      -- high
hoch (2)      -- tall
einfach       -- easy (1)
letzte        -- last                                   # always decline
gleich (1)    -- like/same/equal
gleich (2)    -- right away                             # as an adverb?
möglich       -- possible                               # lit. 'likely'?
eigen         -- own/characteristic
schön         -- beautiful/pleasant
spät          -- late
wichtig       -- important
weitere       -- additional (1)                         # always decline
genau         -- exact
jung          -- young
kurz          -- short
stark         -- strong
richtig       -- right/correct
verschieden   -- various/different/diverse (1)
bestimmt      -- special/particular (1)
besser        -- better                                 # comparative of gut?
schnell       -- fast
sicher (1)    -- sure/certain
sicher (2)    -- safe/secure
nächste       -- next                                   # always decline
politisch     -- political
klar          -- clear (1)
schwer (1)    -- difficult
schwer (2)    -- heavy
einzeln       -- individual
bekannt       -- well-known
leicht (1)    -- light (not heavy)                      # cf. hell
leicht (2)    -- easy (2)
rund          -- round
frei          -- free (as in freedom)                   # cf. gratis/kostenlos
früh          -- early
unterschiedlich -- variable/different/diverse (2)
schlecht      -- bad
deutlich      -- clear (2)
allgemein     -- general
einzig        -- only/sole
gemeinsam     -- common/mutual
nah           -- near/close                             # also nahe?
voll          -- full
direkt        -- direct
international -- international
sozial        -- social
beste         -- best                                   # always decline
                                                        # superlative of gut?
rot           -- red
offen         -- open
meiste        -- most
besondere     -- special/particular (2)
gewiss        -- known/certain
öffentlich    -- public
halb          -- half
wahrscheinlich -- probable                              # lit.'trueseeming'?
europäisch    -- European
wesentlich    -- essential/fundamental
ähnlich       -- similar
häufig        -- frequent
schwarz       -- black
völlig        -- complete
gering (1)    -- low
gering (2)    -- small
schwierig     -- difficult (2)
praktisch     -- practical
persönlich    -- personal
-jährig       -- -years old
modern        -- modern
tief          -- deep
tatsächlich   -- actual/real
zusätzlich    -- additional (2)
amerikanisch  -- American
wirtschaftlich -- economic/financial
interessant   -- interesting
relativ       -- relative
gleichzeitig  -- simultaneous
grün          -- green
weiß          -- white
gesamt        -- whole/entire (2)
speziell      -- special/particular (3)
entscheidend  -- decisive
eng           -- narrow/close
technisch     -- technical
langsam       -- slow
ständing      -- constant
notwendig     -- necessary
rein          -- pure/pristine
englisch      -- English
wissenschaftlich -- scientific/scholarly
falsch        -- false
fremd         -- foreign/strange
fransösisch   -- French
selten        -- rare
normal        -- normal
wahr          -- true
privat        -- private
tot           -- dead
"""
