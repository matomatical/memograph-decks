from mg.node import Node


def graph():
    # most words
    for topic, de, en in parse(LINKS):
        yield (
            Node(en, speak_str=en, speak_voice="en"),
            Node(de, speak_str=de, speak_voice="de"),
            topic,
        )

    # nouns (and their genders)
    words = set()
    for de, en in parse(NOUNS):
        art, noun = de[:3], de[4:]
        yield (
            Node(en,   speak_str=en, speak_voice="en"),
            Node(noun, print_str=de, speak_str=de, speak_voice="de"),
            "de.noun.en"
        )
        if de not in words:
            words.add(de)
            yield (
                Node(noun, speak_str=noun, speak_voice="de"),
                Node(art,  speak_str=de,   speak_voice="de"),
                "de.noun.gender"
            )


def parse(links_text, sep="--", skip_header=True):
    """
    utility functions for parsing lists of links
    """
    for line in links_text.splitlines()[skip_header:]:
        if sep not in line:
            continue
        # remove comments, whitespace
        line = line.split("#", maxsplit=1)[0].strip()
        fields = tuple(map(str.strip, line.split(sep)))
        if fields[0] == "":
            fields = prefix + fields[1:]
        if fields[-1] == "":
            prefix = fields[:-1]
        else:
            yield fields


LINKS = """topic -- de -- en                    # notes (ignored)

# # #
# ADJECTIVES
# 

de.adj --
 -- ganz            -- whole    
 -- ganz            -- entire
 -- ganz            -- all of the
 -- groß            -- great/big
 -- groß            -- tall    
 -- gut             -- good
 -- neu             -- new
 -- erste           -- first                    # always decline
 -- lang            -- long
 -- deutsch         -- German
 -- klein           -- small    
 -- alt             -- old
 -- hoch            -- high
 -- hoch            -- tall    
 -- einfach         -- easy    
 -- letzte          -- last                     # always decline
 -- gleich          -- like/same/equal
 -- gleich          -- right away               # as an adverb?
 -- möglich         -- possible                 # lit. 'likely'?
 -- eigen           -- own/characteristic
 -- schön           -- beautiful/pleasant
 -- spät            -- late
 -- wichtig         -- important
 -- weitere         -- additional               # always decline
 -- genau           -- exact
 -- jung            -- young
 -- kurz            -- short
 -- stark           -- strong
 -- richtig         -- right/correct
 -- verschieden     -- various/different/diverse
 -- bestimmt        -- special/particular    
 -- besser          -- better                   # comparative of gut?
 -- schnell         -- fast
 -- sicher          -- sure/certain
 -- sicher          -- safe/secure
 -- nächste         -- next                     # always decline
 -- politisch       -- political
 -- klar            -- clear    
 -- schwer          -- difficult    
 -- schwer          -- heavy
 -- einzeln         -- individual
 -- bekannt         -- well-known
 -- leicht          -- light (not heavy)        # cf. hell
 -- leicht          -- easy    
 -- rund            -- round
 -- frei            -- free (as in freedom)     # cf. gratis/kostenlos
 -- früh            -- early
 -- unterschiedlich -- variable/different/diverse
 -- schlecht        -- bad
 -- deutlich        -- clear    
 -- allgemein       -- general
 -- einzig          -- only/sole
 -- gemeinsam       -- common/mutual
 -- nah             -- near/close               # also nahe?
 -- voll            -- full
 -- direkt          -- direct
 -- international   -- international
 -- sozial          -- social
 -- beste           -- best                     # always decl, supve of gut?
 -- rot             -- red
 -- offen           -- open
 -- meiste          -- most
 -- besondere       -- special/particular    
 -- gewiss          -- known/certain
 -- öffentlich      -- public
 -- halb            -- half
 -- wahrscheinlich  -- probable                 # lit.'trueseeming'?
 -- europäisch      -- European
 -- wesentlich      -- essential/fundamental
 -- ähnlich         -- similar
 -- häufig          -- frequent
 -- schwarz         -- black
 -- völlig          -- complete
 -- gering          -- low
 -- gering          -- small    
 -- schwierig       -- difficult    
 -- praktisch       -- practical
 -- persönlich      -- personal
 -- jährig          -- years old
 -- modern          -- modern
 -- tief            -- deep
 -- tatsächlich     -- actual/real
 -- zusätzlich      -- additional    
 -- amerikanisch    -- American
 -- wirtschaftlich  -- economic/financial
 -- interessant     -- interesting
 -- relativ         -- relative
 -- gleichzeitig    -- simultaneous
 -- grün            -- green
 -- weiß            -- white
 -- gesamt          -- entire
 -- speziell        -- special/particular    
 -- entscheidend    -- decisive                 # entscheiden+'d', 'deciding'
 -- eng             -- narrow/close
 -- technisch       -- technical
 -- langsam         -- slow
 -- ständing        -- constant
 -- notwendig       -- necessary
 -- rein            -- pure/pristine
 -- englisch        -- English
 -- wissenschaftlich -- scientific/scholarly
 -- falsch          -- false
 -- fremd           -- foreign/strange/alien
 -- fransösisch     -- French
 -- selten          -- rare
 -- normal          -- normal
 -- wahr            -- true
 -- privat          -- private
 -- tot             -- dead

# # #
# ADVERBS
#
# These seem pretty tough to translate due to differences in adverb
# usage between German and English, especially compared to adjectives.
# But below are some rough glosses that should be enough to get started.
# 
# Some of these are also adjectives...! I should sort out the difference.

de.adv --
 -- auch            -- also
 -- so              -- so/thus/this way
 -- dann            -- then
 -- da              -- there
 -- noch            -- still/yet                # has further meanings
 -- also            -- so/therefore
 -- nur             -- just/only
 -- schon           -- already
 -- mehr            -- more                     # ahh 'be more red, run more'
 -- jetzt           -- now
 -- immer           -- always
 -- sehr            -- so/very
 -- hier            -- here
 -- doch            -- but/indeed               # tough translate, see usages
 -- wieder          -- again
 -- eigentlich      -- actually
 -- oben            -- above/up                 # not clear...?
 -- nun             -- now
 -- heute           -- today
 -- weit            -- widely                   # also adj 'wide'?
 -- eben            -- just/exactly             # tough translate, see usages
 -- erst            -- first
 -- natürlich       -- naturally
 -- vielleicht      -- perhaps/maybe
 -- dort            -- there
 -- einmal          -- once
 -- gar             -- at all
 -- bereits         -- already
 -- etwa            -- about/approx
 -- gerade          -- just/exactly             # also adj 'direct/straight'?
 -- zwar            -- admittedly
 -- zwar            -- to be precise
 -- wirklich        -- really/actually
 -- jedoch          -- however
 -- nie             -- never
 -- oft             -- often
 -- allerdings      -- though
 -- allerdings      -- certainly
 -- fast            -- almost/nearly
 -- wohl            -- well
 -- überhaupt       -- generally
 -- gern(e)         -- fondly/with pleasure
 -- besonders       -- particularly
 -- warum           -- why
 -- allein          -- alone
 -- kaum            -- hardly/barely
 -- deshalb         -- therefore
 -- sogar           -- even/indeed
 -- sonst           -- otherwise
 -- weiter          -- further
 -- anders          -- differently
 -- schließlich     -- in closing/conclusion
 -- eher            -- earlier
 -- eher            -- rather/more
 -- je              -- ever/forever             # also a prep for 'each'
 -- früher          -- formerly                 # also adj 'former'
 -- zunächst        -- firstly
 -- zunächst        -- for now
 -- irgendwie       -- somehow
 -- bisher          -- until now/hitherto
 -- manchmal        -- sometimes
 -- her             -- from sth/swh             # also broader, see usage
 -- ebenso          -- just as (sth as sth)
 -- ziemlich        -- quite/fairly
 -- außerdem        -- besides/as well
 -- inzwischen      -- meanwhile
 -- sofort          -- immediately
 -- plötzlich       -- suddenly
 -- bald            -- soon
 -- genug           -- enough
 -- endlich         -- finally
 -- insbesondere    -- in particular
 -- hin             -- to sth/swh
 -- ebenfalls       -- likewise
 -- gestern         -- yesterday
 -- bitte           -- please
 -- zusammen        -- together
 -- jedenfalls      -- in any case
 -- wobei           -- whereby (by/near what)   # interrogative *adverb* (?)
 -- bloß            -- just/only
 -- jeweils         -- any/each time
 -- unten           -- down/below/under/at the bottom
 -- insgesamt       -- in all/in total
 -- vorher          -- before                   # cf. früher?
 -- beispielsweise  -- for example
 -- meist           -- mostly
 -- trotzdem        -- nevertheless
 -- zudem           -- moreover
 -- leider          -- unfortunately
 -- mindestens      -- at least
 -- zumindest       -- at least
 -- irgendwo        -- somewhere
 -- zuerst          -- first
 -- unbedingt       -- absolutely               # also adjective 'absolute'
 -- hinaus          -- out/beyond
 -- zuletzt         -- lastly
 -- dennoch         -- nevertheless
 -- lieber          -- gladly (?)
 -- zugleich        -- simultaneously
 -- nochmal         -- again
 -- danke           -- thank you                # also 'no, thank you'
 -- derzeit         -- at the moment
 -- zuvor           -- before
 -- teilweise       -- partly

# # #
# ARTICLES
# 

de.art.der --
 -- der             -- the                      # definite article
 -- dieser          -- this/these               # demonstrative article close
 -- jener           -- that/those               # demonstrative article far
 -- einiger         -- some/few a               # are these also indefinite?
 -- mancher         -- some/many a
 -- irgendwelcher   -- some or other
 -- jeder           -- every/each
 -- solcher         -- such a
 -- welcher         -- which
 -- sämtliche       -- every/entire             # not used in singular
 -- alle            -- all                      # not used in singular
 -- beider          -- both                     # see usage notes

de.art.ein --
 -- ein             -- an                       # indefinite article
 -- kein            -- no                       # negative article
 -- mein            -- my                       # possessive articles...
 -- dein            -- your (singular)
 -- sein            -- his/its (m)
 -- sein            -- its (n)
 -- ihr             -- her/its (f)
 -- unser           -- our
 -- euer            -- your (plural)
 -- ihr             -- their
 -- Ihr             -- your (formal)
 -- irgendein       -- someone's                # note it's irgend + ein!!

# # #
# CONJUNCTIONS
# 
# TODO: classify 'je - desto' and 'bezeihungsweise' as COO or SUB conj?

de.conj.coo --
 -- und             -- and
 -- oder            -- or
 -- aber            -- but/however
 -- denn            -- because/since
 -- sondern         -- but (on the contrary)    # negative main clause
 -- sowohl - als    -- both - and
 -- weder* - noch*  -- neither - nor
 -- entweder* - oder          -- either - or
 -- nicht nur* - sondern auch -- not only - but also

de.conj.sub --
 -- dass            -- that
 -- als             -- as/when
 -- wenn            -- when/if
 -- weil            -- because
 -- ob              -- if
 -- obwohl          -- although
 -- falls           -- in case/if
 -- da              -- because/since
 -- damit           -- so that
 -- seit            -- since (time)
 -- nachdem         -- after
 -- bevor           -- before
 -- indem           -- while/during
 -- um (zu)         -- in order (to)
 -- ohne (zu)       -- without (to)
 -- zumal           -- especially since
 -- ehe             -- before/until
 -- sowie           -- as well as/as soon as
 -- sodass          -- so that
 -- solange         -- so long as
 -- sobald          -- as soon as
 -- sofern          -- provided that
 -- umso            -- all the
 -- während         -- while/during


# # #
# PREPOSITIONS
# 

de.prep.akk --
 -- für             -- for
 -- um              -- around
 -- um              -- at (time)
 -- durch           -- through
 -- bis             -- until/to
 -- gegen           -- against
 -- ohne            -- without
 -- per             -- per/by
 -- wider           -- contrary to/against
 -- pro             -- per                      # also dat
 -- entlang         -- along                    # also dat

de.prep.dat --
 -- zu              -- to
 -- von             -- from
 -- mit             -- with
 -- bei             -- by/near
 -- nach            -- after/to
 -- aus             -- out of/from
 -- seit            -- since (time)
 -- gegenüber       -- opposite
 -- ab              -- from on
 -- außer           -- aside from/except
 -- gemäß           -- in accordance with
 -- entsprechend    -- corresponding with
 -- zufolge         -- according to
 -- samt            -- together with

de.prep.wex --
 -- in              -- into; in
 -- auf             -- onto; on
 -- an              -- to; at
 -- über            -- over/above
 -- vor             -- before/afront
 -- unter           -- under/below
 -- zwischen        -- between
 -- neben           -- next to/beside
 -- hinter          -- behind

de.prep.gen --
 -- während         -- while/during
 -- wegen           -- because (of)             # also dat
 -- innerhalb       -- inside (of)
 -- aufgrund        -- on grounds (of)
 -- trotz*          -- in spite (of)            # also dat
 -- statt*          -- instead (of)             # also dat
 -- laut*           -- in accordance (of)       # also dat
 -- außerhalb       -- outside (of)
 -- angesichts      -- in the face (of)
 -- mithilfe        -- with the help (of)
 -- anhand          -- on the basis (of)
 -- mittels         -- by means (of)
 -- hinsichtlich    -- in view (of)
 -- bezüglich       -- concerning
 -- einschließlich  -- inclusive (of)
 -- jenseits        -- on the other side (of)
 -- zugunsten       -- in favour (of)
 -- infolge         -- as a consequence (of)
 -- anstelle        -- in place (of)
 -- seitens         -- on the part (of)         # as in 'for their part'
 -- beiderseits     -- on both sides (of)
 -- diesseits       -- on this side (of)
 -- (...) halber    -- on behalf (of)
 -- um (...) willen -- for (...'s) sake

# # #
# PRONOUNS
#

de.pron.personal.nom --
 -- ich             -- I
 -- du              -- you (singular)
 -- er              -- he/it (m)
 -- es              -- it (n)
 -- sie             -- she/it (f)
 -- man             -- man/one
 -- man             -- they (impersonal)
 -- wir             -- we
 -- ihr             -- you (plural)
 -- sie             -- they
 -- Sie             -- you (formal)

de.pron.personal.akk --
 -- mich            -- me
 -- dich            -- you (singular)
 -- ihn             -- him/it (m)
 -- es              -- it (n)
 -- sie             -- she/it (f)
 -- einen           -- one
 -- uns             -- us
 -- euch            -- you (plural)
 -- sie             -- them
 -- Sie             -- you (formal)

de.pron.personal.dat --
 -- mir             -- to me
 -- dir             -- to you (singular)
 -- ihm             -- to him/it (m)
 -- ihm             -- to it (n)
 -- ihr             -- to her/it (f)
 -- einem           -- to one
 -- uns             -- to us
 -- euch            -- to you (plural)
 -- ihnen           -- to them
 -- Ihnen           -- to you (formal)

de.pron.reflexive --
 -- mich            -- myself
 -- mir             -- to myself
 -- dich            -- yourself (singular)
 -- dir             -- to yourself (singular)
 -- sich            -- (to) himself/itself (m)
 -- sich            -- (to) itself (n)
 -- sich            -- (to) herself/itself (f)
 -- uns             -- (to) ourselves
 -- euch            -- (to) yourselves
 -- sich            -- (to) themselves
 -- sich            -- (to) yourself (formal)   # no capital!

de.pron.possessive --
 -- meiner          -- mine
 -- deiner          -- yours (singular)
 -- seiner          -- his/its (m)
 -- seiner          -- its (n)
 -- ihrer           -- hers/its (f)
 -- unserer         -- ours                     # pronounced 'unsrer'
 -- euerer          -- yours (plural)           # pronounced 'eurer'
 -- ihrer           -- theirs
 -- Ihrer           -- yours (formal)

de.pron.possessive.wegen --
 -- meinetwegen     -- on my account
 -- deinetwegen     -- on your (singular) account
 -- seinetwegen     -- on his/its (m) account
 -- seinetwegen     -- on its (n) account
 -- ihretwegen      -- on her/its (f) account
 -- unsertwegen     -- on our account
 -- euretwegen      -- on your (plural) account
 -- Ihretwegen      -- on your (formal) account

de.pron.interrogative --
 -- was             -- what
 -- wer             -- who                      # nom who   (of course,
 -- wen             -- whom                     # akk who    this is just
 -- wem             -- to whom                  # dat who    EXTRA-STRONG
 -- wessen          -- whose                    # gen who    DECLENSION)
 -- wo              -- where
 -- wann            -- when
 -- wie             -- how
 -- warum           -- why
 -- welcher         -- which
 -- was für einer   -- what for a/what kind of
 -- wofür           -- wherefor/for what/why
 -- wodurch         -- whereby/by what/how
 -- wobei           -- whereby/by what/near what
 -- womit           -- wherewith/with what
 -- worauf          -- whereon/on what

de.pron.relative --
 -- der(en)         -- that                     # EXTRA-STRONG DECLENSION
 -- wer             -- who                      # EXTRA-STRONG DECLENSION
 -- wen             -- whom
 -- wem             -- to whom
 -- wessen          -- whose
 -- was             -- what

de.pron.demonstrative --
 -- der(en)         -- the (spoken)             # EXTRA-STRONG DECLENSION
 -- dieser          -- this/these               # not in spoken german
 -- jener           -- that/those               # not in spoken german
 -- derselbe        -- the same one             # decline the 'der' bit
 -- derjenige       -- the one                  # decline the 'der' bit

de.pron.indefinite --
 -- etwas           -- something
 -- nichts          -- nothing
 -- irgendetwas     -- something or other
 -- alles           -- everything
 -- jemand          -- someone                  # case declension -/en/em/es
 -- irgendjemand    -- someone or other         # case declension -/en/em/es
 -- niemand         -- noone                    # case declension -/en/em/es
 -- einer           -- one                      # no plural; DER declension
 -- keiner          -- none                     # DER declension
 -- jeder (?)       -- anyone/everyone?         # what is the declension?
 -- einiger (?)     -- some/few                 # what is the declension?
 -- mancher (?)     -- many                     # what is the declension?
 -- solcher (?)     -- such                     # what is the declension?



# # #
# VERBS
# 

de.verb --
 -- sein            -- to be                    # aux
 -- haben           -- to have                  # aux
 -- werden          -- to become                # aux?
 -- werden          -- to will                  # modal?
 -- können          -- to can                   # modal
 -- müssen          -- to must                  # modal
 -- sollen          -- to should/ought          # modal
 -- wollen          -- to want                  # modal
 -- dürfen          -- to may                   # modal
 -- mögen           -- to like                  # modal
 -- sagen           -- to say
 -- machen          -- to make/do
 -- geben           -- to give
 -- kommen          -- to come
 -- gehen           -- to go
 -- wissen          -- to know    
 -- sehen           -- to see
 -- lassen          -- to let/allow
 -- lassen          -- to have done
 -- stehen          -- to stand
 -- finden          -- to find
 -- bleiben         -- to stay (at)
 -- liegen          -- to lie (down)
 -- heißen          -- to hail/be called
 -- denken          -- to think
 -- nehmen          -- to take    
 -- tun             -- to do/perform
 -- glauben         -- to believe
 -- halten          -- to halt/stop
 -- halten          -- to hold
 -- nennen          -- to name
 -- zeigen          -- to show
 -- führen          -- to lead
 -- sprechen        -- to speak
 -- bringen         -- to bring
 -- bringen         -- to take    
 -- leben           -- to live (alive)
 -- fahren          -- to go/ride/drive/etc.
 -- meinen          -- to think/opine
 -- fragen          -- to ask
 -- kennen          -- to know    
 -- gelten          -- to be valid (not expired)
 -- stellen         -- to place/set
 -- spielen         -- to play
 -- arbeiten        -- to work
 -- brauchen        -- to require/need
 -- folgen          -- to follow
 -- lernen          -- to learn
 -- bestehen        -- to exist
 -- bestehen        -- to insist
 -- bestehen        -- to pass (an exam)        # be + stehen
 -- verstehen       -- to understand            # ver + stehen
 -- setzen          -- to set/place
 -- bekommen        -- to get                   # be + kommen
 -- beginnen        -- to begin    
 -- erzählen        -- to tell                  # er + zählen (?)
 -- versuchen       -- to try/attempt           # ver + suchen
 -- schreiben       -- to write
 -- laufen          -- to walk
 -- erklären        -- to explain               # er + klären
 -- entsprechen     -- to correspond            # ent + sprechen
 -- sitzen          -- to sit
 -- ziehen          -- to pull/move
 -- scheinen        -- to shine
 -- scheinen        -- to seem/appear    
 -- fallen          -- to fall
 -- gehören         -- to belong                # ge + hören?
 -- entstehen       -- to originate/develop
 -- entstehen       -- to arise                 # ent + stehen
 -- erhalten        -- to receive               # er + halten
 -- treffen         -- to meet
 -- treffen         -- to hit
 -- suchen          -- to search
 -- legen           -- to lay (sth. down)
 -- vorstellen      -- to introduce             # like, to 'set out'?
 -- vorstellen      -- to imagine               # vor + stellen
 -- handeln         -- to deal/trade
 -- erreichen       -- to achieve/reach         # er + reichen
 -- tragen          -- to carry
 -- tragen          -- to wear
 -- schaffen        -- to manage
 -- schaffen        -- to create
 -- lesen           -- to read
 -- verlieren       -- to lose                  # ver + lieren?
 -- darstellen      -- to portray/depict        # dar + stellen
 -- erkennen        -- to admit/recognise
 -- entwickeln      -- to develop               # ent + wickeln
 -- reden           -- to talk
 -- aussehen        -- to look/appear
 -- erscheinen      -- to seem/appear           # er + scheinen
 -- bilden          -- to form
 -- bilden          -- to educate
 -- anfangen        -- to begin                 # an + fangen
 -- erwarten        -- to expect                # er + warten
 -- wohnen          -- to live (reside)
 -- betreffen       -- to concern/affect        # be + treffen
 -- warten          -- to wait
 -- vergehen        -- to pass (time)           # ver + gehen
 -- helfen          -- to help
 -- gewinnen        -- to win/gain              # not from winnen?
 -- schließen       -- to close
 -- fühlen          -- to feel
 -- bieten          -- to offer    
 -- interessieren   -- to interest
 -- erinnern        -- to remind
 -- ergeben         -- to result in
 -- anbieten        -- to offer
 -- studieren       -- to study
 -- verbinden       -- to connect/link          # ver + binden
 -- ansehen         -- to look at/watch         # an + sehen
 -- fehlen          -- to lack
 -- bedeuten        -- to mean/represent
 -- vergleichen     -- to compare
 -- möchten         -- to would like            # modal, actually K2P mögen

 -- steigen         -- to climb/increase
 -- nutzen          -- to use
 -- schauen         -- to look (at)
 -- verlassen       -- to leave
 -- einsetzen       -- to insert
 -- ändern          -- to change
 -- wachsen         -- to wax/grow
 -- ausgehen        -- to go out
 -- ausgehen        -- to assume
 -- geschehen       -- to happen
 -- beschreiben     -- to describe
 -- annehmen        -- to take on/accept
 -- kriegen         -- to receive               # see differences on stackex
 -- planen          -- to plan
 -- wirken          -- to work/take effect
 -- bezeichnen      -- to call/name
 -- befinden sich   -- to be/find oneself       # 'i find myself ...?' modal?
 -- passieren       -- to pass/transpire
 -- rufen           -- to call
 -- aufnehmen       -- to take on/challenge
 -- aufnehmen       -- to take up               # pick up, absorb, record, ...
 -- aufnehmen       -- to take in               # admit, receive, include, ...
 -- zunehmen        -- to gain/increase
 -- bestimmen       -- to decide/determine/define
 -- fordern         -- to demand
 -- gefallen        -- to please/appeal to
 -- öffnen          -- to open
 -- schlagen        -- to hit/strike
 -- treten          -- to step
 -- übernehmen      -- to take over
 -- übernehmen      -- to take on/accept
 -- übernehmen sich -- to overdo/take on too much
 -- verändern       -- to change
 -- lachen          -- to laugh
 -- verwenden       -- to use                   # there are some other senses
 -- wählen          -- to choose/select/vote
 -- erfolgen        -- to occur
 -- enthalten       -- to hold in/contain
 -- betrachten      -- to look at/watch
 -- betrachten      -- to look at/consider
 -- entscheiden     -- to decide
 -- gelingen        -- to succeed
 -- kaufen          -- to buy
 -- erfahren        -- to find out/hear
 -- erfahren        -- to experience
 -- vergessen       -- to forget
 -- stattfinden     -- to occur
 -- bewegen         -- to move
 -- feststellen     -- to establish/determine
 -- verschwinden    -- to disappear
 -- dienen          -- to serve (sb/with sth)
 -- trinken         -- to drink
 -- auftreten       -- to tread
 -- auftreten       -- to step up/appear
 -- stimmen         -- to be correct/all right  # also to vote, tune (guitar)
 -- verhalten sich  -- to behave                # to hold out/hold oneself?
 -- berichten       -- to report
 -- rechnen         -- to calculate             # source of 'to reckon'?
 -- beobachten      -- to observe
 -- erleben         -- to experience
 -- holen           -- to fetch/get
 -- essen           -- to eat
 -- reichen         -- to reach                 # to extend / to be enough
 -- sterben         -- to die
 -- unterscheiden   -- to distinguish
 -- leisten         -- to achieve
 -- verlangen       -- to demand
 -- werfen          -- to throw
 -- vorliegen       -- to be present (with)
 -- zählen          -- to count
 -- wünschen        -- to wish
 -- bauen           -- to build
 -- hängen          -- to hang
 -- hoffen          -- to hope
 -- freuen          -- to be happy
 -- teilen          -- to divide/share          # teil = part
 -- bezahlen        -- to pay
 -- dauern          -- to dure/last/take (time) # 'duration'
 -- stecken         -- to stash/put/pin
 -- besuchen        -- to visit
 -- bitten          -- to request/beg
 -- sorgen sich     -- to worry
 -- sorgen          -- to look after
 -- ankommen        -- to arrive
 -- beziehen        -- to cover                 # there are more senses
 -- spüren          -- to sense/notice
 -- spüren          -- to track
 -- erhöhen         -- to raise/increase
 -- melden          -- to register              # in rummy, we 'meld' to begin
 -- melden          -- to report
 -- vorkommen       -- to come forth
 -- vorkommen       -- to occur
 -- besitzen        -- to own/possess
 -- betonen         -- to stress/emphasise
 -- erfüllen        -- to fulfil/grant
 -- beteiligen sich -- to partake in
 -- beteiligen sich -- to share in
 -- merken          -- to mark/notice           # 'mark my words'
 -- merken sich     -- to remember
 -- passen          -- to fit/suit
 -- passen          -- to match
 -- eignen sich     -- to suit as
 -- richten         -- to aim/direct at
 -- richten         -- to address (sb)
 -- umfassen        -- to comprise
 -- umfassen        -- to enclose
 -- schlafen        -- to sleep
 -- unterstützen    -- to support
 -- lächeln         -- to smile
 -- beschäftigen    -- to occupy/employ
 -- lösen           -- to solve
 -- lösen           -- to loosen
 -- antworten       -- to answer
 -- trennen         -- to separate/sever
 -- einstellen      -- to put away
 -- einstellen      -- to set up/prepare
 -- einstellen      -- to stop/cease
 -- lieben          -- to love
 -- durchführen     -- to carry through
 -- genügen         -- to suffice/be enough
 
 -- aufbauen        -- to build up/erect
 -- bestätigen      -- to confirm/endorse
 -- untersuchen     -- to examine
 -- verkaufen       -- to sell
 -- blicken         -- to look/glance
 -- drücken         -- to press/push
 -- eingehen        -- to go into (history/heaven/matrimony/etc.)
 -- erlauben        -- to allow
 -- ausreichen      -- to suffice
 -- schweigen       -- to remain silent
 -- behandeln       -- to treat/handle
 -- treiben         -- to drive (nail/animals/ball/etc.)
 -- treiben         -- to pursue (craft/study/hobby/etc.)
 -- überzeugen      -- to convince
 -- benutzen        -- to use
 -- drohen          -- to threaten
 -- versprechen     -- to promise
 -- entdecken       -- to discover
 -- klingen         -- to klang/sound
 -- reagieren       -- to react
 -- kosten          -- to cost
 -- verdienen       -- to earn
 -- drehen          -- to turn/shift/spin
 -- überraschen     -- to surprise
 -- betreiben       -- to proceed with
 -- fliegen         -- to fly
 -- heben           -- to lift
 -- stoßen          -- to thrust/push/punch
 -- vertreten       -- to represent
 -- vertreten       -- to advocate
 -- ermöglichen     -- to enable
 -- herstellen      -- to make/produce
 -- leiden          -- to suffer
 -- schicken        -- to send
 -- wechseln        -- to swap/exchange
 -- liefern         -- to deliver
 -- zahlen          -- to pay
 -- benötigen       -- to require/need
 -- stammen         -- to stem/come (from sth)
 -- verhindern      -- to prevent
 -- abschließen     -- to lock
 -- abschließen     -- to conclude/end
 -- reisen          -- to travel
 -- singen          -- to sing
 -- überlegen       -- to hold over (hold sth over sb)
 -- überlegen       -- to lay over/consider
 -- überlegen sich  -- to lean over
 -- erwähnen        -- to mention
 -- greifen         -- to grab
 -- verzichten      -- to do without
 -- aufgeben        -- to give up               # also has some other meanings
 -- betragen        -- to come/amount to        # lit. to carry to?
 -- betragen sich   -- to behave                # lit. to carry oneself?
 -- kochen          -- to cook
 -- angeben         -- to declare               # lit. to give on?
 -- angeben         -- to brag
 -- angeben         -- to serve (ball)
 -- begründen       -- to substantiate/justify
 -- einrichten      -- to furnish               # has also some more meanings
 -- festhalten      -- to hold
 -- festhalten      -- to detain
 -- geraten         -- to come into
 -- geraten         -- to turn out
 -- verfügen        -- to decree
 -- schützen        -- to protect
 -- vorbereiten     -- to prepare
 -- wiederholen     -- to repeat                # wieder + holen?
 -- stören          -- to disturb
 -- feiern          -- to celebrate
 -- vermitteln      -- to mediate
 -- berücksichtigen -- to consider
 -- ausschließen    -- to exclude/rule out
 -- diskutieren     -- to discuss
 -- funktionieren   -- to function/work
 -- gründen         -- to found/establish
 -- herrschen       -- to reign/prevail         # used also for environments
 -- schieben        -- to push
 -- schieben        -- to slide
 -- behaupten       -- to assert/maintain
 -- erheben         -- to raise
 -- verfolgen       -- to pursue
 -- zurückkommen    -- to return
 -- zwingen         -- to force
 -- ablehnen        -- to decline
 -- anwenden        -- to employ/apply
 -- auftauchen      -- to turn up/emerge/surface
 -- beeinflussen    -- to influence
 -- einfallen       -- to occur/remind          # lit. 'to fall on' (apple?)
 -- einfallen       -- to come in/invade
 -- existieren      -- to exist
 -- fördern         -- to promote/support
 -- ansprechen      -- to address               # also some more meanings
 -- beachten        -- to heed/pay attention to
 -- empfinden       -- to feel
 -- entfernen       -- to remove
 -- entfernen sich  -- to leave
 -- schneiden       -- to cut
 -- sichern         -- to secure
 -- wenden          -- to turn
 -- fassen          -- to grasp                 # also has some other meanings
 -- informieren     -- to inform
 -- kümmern         -- to concern
 -- nicken          -- to nod
 -- organisieren    -- to organize
 -- prägen          -- to emboss/mint/shape
 -- prägen          -- to coin (a word)
 -- sinken          -- to sink
 -- sinken          -- to fall/decrease
 -- vermeiden       -- to avoid
 -- ankündigen      -- to announce/herald
 -- aufstehen       -- to stand up
 -- verstärken      -- to strengthen/reinforce
 -- vorsehen        -- to forsee/plan
 -- beschränken     -- to restrict/limit
 -- verletzen       -- to injure

# (some verbs gathered randomly e.g. from class, but i remember them anyway)
 -- servieren       -- to serve out
 -- atmen           -- to breathe
 -- hören           -- to hear
 -- hassen          -- to hate
 -- fressen         -- to feed
 -- rennen          -- to run/race
 -- rennen          -- to scramble
 -- einkaufen       -- to shop                  # ein + kaufen
 -- stehlen         -- to steal
 -- backen          -- to bake
 -- schneien        -- to snow
 -- regnen          -- to rain
 -- üben            -- to practice
 -- analysieren     -- to analyse
 -- buchstabieren   -- to spell
 -- streichen       -- to paint/smear
 -- streichen       -- to eliminate
 -- streichen       -- to decorate
 -- unterstreichen  -- to underline             # unter + streichen
 -- notieren        -- to note (down)
 -- markieren       -- to highlight
 -- ergänzen        -- to complete/enter/fill in    # er + ganz + ¨-en
 -- ergänzen        -- to complete/complement
 -- ordnen          -- to order/arrange
 -- zuordnen        -- to collate               # zu + ordnen
 -- zeichnen        -- to draw
 -- messen          -- to measure
 -- fangen          -- to catch
 -- leihen          -- to loan/borrow
 -- brechen         -- to break
 -- unterbrechen    -- to interrupt             # unter + brechen
 -- befehlen        -- to command               # emp + fehlen?
 -- empfehlen       -- to recommend             # emp + fehlen?
 -- füllen          -- to fill
 -- fassen          -- to grasp
"""

"""
# TODO: Could add nouns with genders as topic, like so:
de.noun.das -- Jahr -- year
de.noun.das -- Mal  -- time/occurrence
# but then how to quick noun-to-topic?
"""

NOUNS = """art de -- the en                 # notes (ignored)
das Jahr        -- the year
das Mal         -- the time/occurrence
das Beispiel    -- the example
die Zeit        -- the time
die Frau        -- the woman/wife           # also title 'Mrs.'
der Mensch      -- the man/human
das Kind        -- the child
der Tag         -- the day
der Mann        -- the man/husband
das Land        -- the land/country
die Frage       -- the question
das Haus        -- the house/home
der Fall        -- the fall                 # also means 'case'
plu Leute       -- the people               # plural only
die Arbeit      -- the work
das Prozent     -- the percent
die Hand        -- the hand
die Stadt       -- the town
der Herr        -- the gentleman            # also title 'Mr.'
der Teil        -- the part/section
das Problem     -- the problem
die Welt        -- the world
das Recht       -- the right/law
das Ende        -- the end
die Million     -- the million
die Schule      -- the school
die Woche       -- the week
der Vater       -- the father
die Seite       -- the side
die Seite       -- the page
das Leben       -- the life
die Mutter      -- the mother
der Grund       -- the grounding/basis/reason
das Auge        -- the eye
das Wort        -- the word
das Geld        -- the money
die Sache       -- the thing
die Art         -- the type/kind
der Bereich     -- the area/region
der Weg         -- the way/path
die Stunde      -- the hour
der Name        -- the name
die Geschichte  -- the history
die Gesellschaft -- the society/company
der Kopf        -- the head
das Paar        -- the pair/couple
die Möglichkeit -- the likelihood/possibility
das Unternehmen -- the enterprise/company
das Bild        -- the picture
das Buch        -- the book
das Wasser      -- the water
die Stelle      -- the place                # stellen = to place
die Stelle      -- the position/role        # like for a job
die Form        -- the form/shape
die Mark        -- the mark (currency)
die Entwicklung -- the development
der Monat       -- the month
die Familie     -- the family
der Morgen      -- the morning              # also 'tomorrow'?
der Abend       -- the evening
die Aufgabe     -- the task/asg./job
die Universität -- the university           # abbr.: 'die Uni'
der Sinn        -- the sense/meaning
der Staat       -- the state
das Ziel        -- the goal
das Ziel        -- the destination
der Freund      -- the friend (m)
die Freundin    -- the friend (f)
das Thema       -- the topic/theme
die Person      -- the person
der Euro        -- the euro (currency)
die Nacht       -- the night
das Ding        -- the thing
der Raum        -- the room/space
der Blick       -- the look/glance/view
der Platz       -- the place
der Platz       -- the public square
die Zahl        -- the number
das System      -- the system
die Uhr         -- the clock/watch
die Uhr         -- the o'clock
plu Eltern      -- the parents              # plural only
die Straße      -- the street
die Minute      -- the minute
die Gruppe      -- the group
der Wert        -- the value/worth
das Gesicht     -- the face
die Sprache     -- the language
der Anfang      -- the beginning
der Ort         -- the place/location
der Ort         -- the town
der Moment      -- the moment
die Folge       -- the result/consequence
das Interesse   -- the interest
die Milliarde   -- the billion
die Rolle       -- the role
die Rolle       -- the roll
die Tür         -- the door
der Schüler     -- the pupil/student (m)
die Schülerin   -- the pupil/student (f)
die Bedeutung   -- the meaning
die Bedeutung   -- the significance
der Text        -- the text
das Ergebnis    -- the result
der Krieg       -- the war
die Weise       -- the way/manner
die Regierung   -- the rule/government
das Stück       -- the piece/bit/part
die Wohnung     -- the apartment
das Gespräch    -- the conversation
"""
