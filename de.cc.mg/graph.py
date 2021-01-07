from mg.graph import Node
from mg.data import parse

def graph():
    for topic, de, en in parse(LINKS):
        yield (
                Node(en, speak_str=en, speak_voice="en"),
                Node(de, speak_str=de, speak_voice="de"),
                "de." + topic,
            )

LINKS = """topic -- de -- en            # notes (ignored)
art.der --
    -- der              -- the              # definite article
    -- dieser           -- this/these       # demonstrative article close
    -- jener            -- that/those       # demonstrative article far
    -- einiger          -- some/few a       # are these also indefinite?
    -- mancher          -- some/many a
    -- irgendwelcher    -- some or other
    -- jeder            -- every/each
    -- solcher          -- such a
    -- welcher          -- which
    -- sämtliche        -- every/entire     # not used in singular
    -- alle             -- all              # not used in singular
    -- beider           -- both             # see usage notes
art.ein --
    -- ein              -- an               # indefinite article
    -- kein             -- no               # negative article
    -- mein             -- my               # possessive articles...
    -- dein             -- your (singular)
    -- sein             -- his/its (m)
    -- sein             -- its (n)
    -- ihr              -- her/its (f)
    -- unser            -- our
    -- euer             -- your (plural)
    -- ihr              -- their
    -- Ihr              -- your (formal)
    -- irgendein        -- someone's        # note it's irgend + ein!!

# pronouns
# TODO

# coordinating conjunctions
conj.coo --
    -- und              -- and
    -- oder             -- or
    -- aber             -- but/however
    -- denn             -- because/since
    -- sondern          -- but (on the contrary)    # negative main clause
    -- sowohl - als             -- both - and
    -- weder* - noch*           -- neither - nor
    -- entweder* - oder         -- either - or
    -- nich nur* - sondern auch -- not only - but also
conj.sub --
    -- dass             -- that
    -- als              -- when/as
    -- wenn             -- when/if
    -- weil             -- because
    -- ob               -- if
    -- obwohl           -- although
    -- falls            -- in case/if
    -- da               -- since/as
    -- damit            -- so that
    -- seit             -- since
    -- nachdem          -- after
    -- bevor            -- before
    -- indem            -- while
    -- um (zu)          -- in order (to)
    -- ohne (zu)        -- without (to)
    -- zumal            -- especially since
    -- ehe              -- before/until
    -- sowie            -- as well as/as soon as
    -- sodass           -- so that
    -- solange          -- so long as
    -- sobald           -- as soon as
    -- sofern           -- provided that
    -- umso             -- all the
    -- während          -- while/during
    # TODO: classify DESTO and BEZEIHUNGSWEISE

prep.akk --
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
prep.dat --
    -- zu               -- to
    -- von              -- from
    -- mit              -- with
    -- bei              -- by/near
    -- nach             -- after/to
    -- aus              -- out of/from
    -- seit             -- since
    -- gegenüber        -- opposite
    -- ab               -- from on
    -- außer            -- aside from/except
    -- gemäß            -- in accordance with
    -- entsprechend     -- corresponding with
    -- zufolge          -- according to
    -- samt             -- together with
prep.wex --
    -- in               -- into; in
    -- auf              -- onto; on
    -- an               -- to; at
    -- über             -- over/above
    -- vor              -- before/afront
    -- unter            -- under/below
    -- zwischen         -- between
    -- neben            -- next to/beside
    -- hinter           -- behind
prep.gen --
    -- während          -- during
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
