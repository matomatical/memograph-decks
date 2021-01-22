from mg.graph import Node
from mg.data import parse

def graph():
    for topic, de, en in parse(LINKS):
        yield (
                Node(en, speak_str=en, speak_voice="en"),
                Node(de, speak_str=de, speak_voice="de"),
                "de.prep." + topic,
            )

LINKS = """topic -- de  -- en               # notes (ignored)
akk --
    -- für              -- for
    -- um               -- around
    -- um               -- at (time)
    -- durch            -- through
    -- bis              -- until/to
    -- gegen            -- against
    -- ohne             -- without
    -- per              -- per/by
    -- wider            -- contrary to/against
    -- pro              -- per                  # also dat
    -- entlang          -- along                # also dat
dat --
    -- zu               -- to
    -- von              -- from
    -- mit              -- with
    -- bei              -- by/near
    -- nach             -- after/to
    -- aus              -- out of/from
    -- seit             -- since (time)
    -- gegenüber        -- opposite
    -- ab               -- from on
    -- außer            -- aside from/except
    -- gemäß            -- in accordance with
    -- entsprechend     -- corresponding with
    -- zufolge          -- according to
    -- samt             -- together with
wex --
    -- in               -- into; in
    -- auf              -- onto; on
    -- an               -- to; at
    -- über             -- over/above
    -- vor              -- before/afront
    -- unter            -- under/below
    -- zwischen         -- between
    -- neben            -- next to/beside
    -- hinter           -- behind
gen --
    -- während          -- while/during
    -- wegen            -- because (of)         # also dat
    -- innerhalb        -- inside (of)
    -- aufgrund         -- on grounds (of)
    -- trotz*           -- in spite (of)        # also dat
    -- statt*           -- instead (of)         # also dat
    -- laut*            -- in accordance (of)   # also dat
    -- außerhalb        -- outside (of)
    -- angesichts       -- in the face (of)
    -- mithilfe         -- with the help (of)
    -- anhand           -- on the basis (of)
    -- mittels          -- by means (of)
    -- hinsichtlich     -- in view (of)
    -- bezüglich        -- concerning
    -- einschließlich   -- inclusive (of)
    -- jenseits         -- on the other side (of)
    -- zugunsten        -- in favour (of)
    -- infolge          -- as a consequence (of)
    -- anstelle         -- in place (of)
    -- seitens          -- on the part (of)     # as in 'for their part'
    -- beiderseits      -- on both sides (of)
    -- diesseits        -- on this side (of)
    -- (...) halber     -- on behalf (of)
    -- um (...) willen  -- for (...'s) sake
"""