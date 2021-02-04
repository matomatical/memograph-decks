from mg.node import Node


def graph():
    for topic, *args in parse(LINKS):
        # treat nouns specially
        if topic.startswith("de.noun"):
            der, de, en = args
            der_de = f"{der} {de}"
            the_en = f"the {en}"
            # one for the translation (without articles)
            yield (
                Node(en, print_str=the_en,speak_str=the_en,speak_voice="en"),
                Node(de, print_str=der_de,speak_str=der_de,speak_voice="de"),
                topic + ".en",
            )
            # one for the gender itself (note: duplicates removed by mg)
            yield (
                Node(de,  speak_str=de,     speak_voice="de"),
                Node(der, speak_str=der_de, speak_voice="de"),
                topic + ".gender",
            )
        elif topic.startswith("de.abbr"):
            # abbreviations map spelling to german
            # also, make sure the speaker spells out the abbreviation!
            abbr, full = args
            dotted_abbr = ".".join(abbr.replace(".", ""))
            yield (
                Node(abbr, speak_str=dotted_abbr, speak_voice="de"),
                Node(full, speak_str=full, speak_voice="de"),
                topic,
            )
        # all others have standard format (so far)
        else:
            de, en = args
            yield (
                Node(en, speak_str=en, speak_voice="en"),
                Node(de, speak_str=de, speak_voice="de"),
                topic,
            )



def parse(links_text, sep="--", skip_header=True):
    """
    utility functions for parsing lists of links
    """
    for line in links_text.splitlines()[skip_header:]:
        # remove comments, whitespace
        line = line.split("#", maxsplit=1)[0].strip()
        if sep not in line:
            continue
        # split and process remaining line
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

de.conj.coo --
 -- und             -- and
 -- oder            -- or
 -- aber            -- but/however
 -- denn            -- because/since
 -- sondern         -- but (on the contrary)    # negative main clause
 -- beziehungsweise -- respectively
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
 -- umso            -- all the                  # e.g. 'all the better to ...'
 -- während         -- while/during
 -- je - desto      -- the - the                # e.g. 'the more the merrier'


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
 -- servieren       -- to serve out
 -- mitteln         -- to average
 -- bereiten        -- to prepare
 -- wähnen          -- to think/imagine         # but mistakenly?


# # #
# Numbers
#

de.num.card --
 -- null            -- zero
 -- eins            -- one
 -- zwei            -- two
 -- drei            -- three
 -- vier            -- four
 -- fünf            -- five
 -- sechs           -- six
 -- sieben          -- seven
 -- acht            -- eight
 -- neun            -- nine
 -- zehn            -- ten
 -- elf             -- eleven
 -- zwölf           -- twelve
 -- dreizehn        -- thirteen
 -- vierzehn        -- fourteen
 -- fünfzehn        -- fifteen
 -- sechzehn        -- sixteen
 -- siebzehn        -- seventeen
 -- achtzehn        -- eighteen
 -- neunzehn        -- nineteen
 -- zwanzig         -- twenty
 -- dreißig         -- thirty
 -- vierzig         -- forty
 -- fünfzig         -- fifty
 -- sechzig         -- sixty
 -- siebzig         -- seventy
 -- achtzig         -- eighty
 -- neunzig         -- ninety
 -- hundert         -- hundred
 -- tausend         -- thousand
 -- hunderttausend  -- hundredthousand

de.num.ord --
 -- erste           -- first
 -- zweite          -- second
 -- dritte          -- third
 -- vierte          -- fourth
 -- fünfte          -- fifth
 -- sechste         -- sixth
 -- siebte          -- seventh                  # also 'siebente'; poetic
 -- achte           -- eighth
 -- neunte          -- ninth
 -- zehnte          -- tenth
 -- elfte           -- eleventh
 -- zwölfte         -- twelfth
 -- dreizehnte      -- thirteenth
 -- vierzehnte      -- fourteenth
 -- fünfzehnte      -- fifteenth
 -- sechzehnte      -- sixteenth
 -- siebzehnte      -- seventeenth
 -- achtzehnte      -- eighteenth
 -- neunzehnte      -- nineteenth
 -- zwanzigste      -- twentieth
 -- dreißigste      -- thirtieth
 -- vierzigste      -- fortieth
 -- fünfzigste      -- fiftieth
 -- sechzigste      -- sixtieth
 -- siebzigste      -- seventieth
 -- achtzigste      -- eightieth
 -- neunzigste      -- ninetieth
 -- hundertste      -- hundredth
 -- tausendste      -- thousandth
 -- hunderttausendste   -- hundredthousandth
 -- millionste      -- millionth
 -- milliardste     -- billionth


# # #
# NOUNS (and their genders)
# 

de.noun --
 -- das -- Jahr         -- year
 -- das -- Mal          -- time/occurrence
 -- das -- Beispiel     -- example
 -- die -- Zeit         -- time
 -- die -- Frau         -- woman/wife           # also title 'Mrs.'
 -- der -- Mensch       -- man/human
 -- das -- Kind         -- child
 -- der -- Tag          -- day
 -- der -- Mann         -- man/husband
 -- das -- Land         -- land/country
 -- die -- Frage        -- question
 -- das -- Haus         -- house/home
 -- der -- Fall         -- fall                 # also means 'case'
 -- plu -- Leute        -- people               # plural only
 -- die -- Arbeit       -- work
 -- das -- Prozent      -- percent
 -- die -- Hand         -- hand
 -- die -- Stadt        -- town
 -- der -- Herr         -- gentleman            # also title 'Mr.'
 -- der -- Teil         -- part/section         # also das?
 -- das -- Problem      -- problem
 -- die -- Welt         -- world
 -- das -- Recht        -- right/law
 -- das -- Ende         -- end
 -- die -- Million      -- million
 -- die -- Schule       -- school
 -- die -- Woche        -- week
 -- der -- Vater        -- father
 -- die -- Seite        -- side
 -- die -- Seite        -- page
 -- das -- Leben        -- life
 -- die -- Mutter       -- mother
 -- der -- Grund        -- grounding/basis/reason
 -- das -- Auge         -- eye
 -- das -- Wort         -- word
 -- das -- Geld         -- money
 -- die -- Sache        -- thing
 -- die -- Art          -- type/kind
 -- der -- Bereich      -- area/region
 -- der -- Weg          -- way/path
 -- die -- Stunde       -- hour
 -- der -- Name         -- name
 -- die -- Geschichte   -- history
 -- die -- Gesellschaft -- society/company
 -- der -- Kopf         -- head
 -- das -- Paar         -- pair/couple
 -- die -- Möglichkeit  -- likelihood/possibility
 -- das -- Unternehmen  -- enterprise/company
 -- das -- Bild         -- picture
 -- das -- Buch         -- book
 -- das -- Wasser       -- water
 -- die -- Stelle       -- place                # stellen = to place
 -- die -- Stelle       -- position/role        # like for a job
 -- die -- Form         -- form/shape
 -- die -- Mark         -- mark (currency)
 -- die -- Entwicklung  -- development
 -- der -- Monat        -- month
 -- die -- Familie      -- family
 -- der -- Morgen       -- morning              # also 'tomorrow'?
 -- der -- Abend        -- evening
 -- die -- Aufgabe      -- task/asg./job
 -- die -- Universität  -- university           # abbr.: 'die Uni'
 -- der -- Sinn         -- sense/meaning
 -- der -- Staat        -- state
 -- das -- Ziel         -- goal
 -- das -- Ziel         -- destination
 -- der -- Freund       -- friend (m)
 -- die -- Freundin     -- friend (f)
 -- das -- Thema        -- topic/theme
 -- die -- Person       -- person
 -- der -- Euro         -- euro (currency)
 -- die -- Nacht        -- night
 -- das -- Ding         -- thing
 -- der -- Raum         -- room/space
 -- der -- Blick        -- look/glance/view
 -- der -- Platz        -- place
 -- der -- Platz        -- public square
 -- die -- Zahl         -- number
 -- das -- System       -- system
 -- die -- Uhr          -- clock/watch
 -- die -- Uhr          -- o'clock
 -- plu -- Eltern       -- parents              # plural only
 -- die -- Straße       -- street
 -- die -- Minute       -- minute
 -- die -- Gruppe       -- group
 -- der -- Wert         -- value/worth
 -- das -- Gesicht      -- face
 -- die -- Sprache      -- language
 -- der -- Anfang       -- beginning
 -- der -- Ort          -- place/location
 -- der -- Ort          -- town
 -- der -- Moment       -- moment
 -- die -- Folge        -- result/consequence
 -- das -- Interesse    -- interest
 -- die -- Milliarde    -- billion
 -- die -- Rolle        -- role
 -- die -- Rolle        -- roll
 -- die -- Tür          -- door
 -- der -- Schüler      -- pupil/student (m)
 -- die -- Schülerin    -- pupil/student (f)
 -- die -- Bedeutung    -- meaning
 -- die -- Bedeutung    -- significance
 -- der -- Text         -- text
 -- das -- Ergebnis     -- result
 -- der -- Krieg        -- war
 -- die -- Weise        -- way/manner
 -- die -- Regierung    -- rule/government
 -- das -- Stück        -- piece/bit/part
 -- die -- Wohnung      -- apartment
 -- das -- Gespräch     -- conversation

 -- der -- Meter        -- metre
 -- der -- Punkt        -- dot/point/period
 -- die -- Situation    -- situation
 -- der -- Lehrer       -- teacher (m)
 -- die -- Lehrerin     -- teacher (f)
 -- der -- Preis        -- price
 -- der -- Preis        -- prize
 -- der -- Preis        -- praise
 -- die -- Abbildung    -- illustration         # Abbreviated 'Abb.'
 -- der -- Begriff      -- concept/idea
 -- die -- Funktion     -- function
 -- der -- Boden        -- bottom/ground
 -- das -- Jahrhundert  -- century
 -- der -- Sohn         -- son
 -- das -- Werk         -- work
 -- die -- Stimme       -- voice
 -- die -- Stimme       -- vote
 -- der -- Rahmen       -- frame
 -- der -- Rahmen       -- framework
 -- die -- Richtung     -- direction
 -- das -- Programm     -- programme
 -- die -- Angst        -- fear/anxiety
 -- die -- Information  -- information
 -- die -- Kunst        -- art
 -- die -- Musik        -- music
 -- die -- Politik      -- politics
 -- der -- Beruf        -- occupation/profession
 -- die -- Regel        -- rule
 -- die -- Regel        -- period/menstruation
 -- der -- Schritt      -- (foot) step
 -- der -- Absatz       -- turn (of heel, a line break/paragraph)
 -- der -- Gott         -- god
 -- das -- Auto         -- automobile/car
 -- die -- Beziehung    -- relationship
 -- die -- Erfahrung    -- experience
 -- der -- Tisch        -- table
 -- die -- Zukunft      -- future
 -- das -- Spiel        -- game
 -- das -- Gefühl       -- feeling
 -- das -- Licht        -- light
 -- der -- Präsident    -- president (m)
 -- die -- Präsidentin  -- president (f)
 -- der -- Markt        -- market
 -- die -- Bank         -- bank
 -- die -- Partei       -- (political) party
 -- die -- Tochter      -- daughter
 -- das -- Verhältnis   -- relationship
 -- die -- Kirche       -- church
 -- der -- Film         -- film
 -- der -- Gedanke      -- thought
 -- der -- Doktor       -- doctor               # abbr. 'Dr.'
 -- das -- Mädchen      -- girl                 # 'little maid'
 -- die -- Entscheidung -- decision
 -- der -- Prozess      -- (court) trial
 -- der -- Prozess      -- process
 -- der -- Betrieb      -- operation/business
 -- der -- Zusammenhang -- connection/context
 -- das -- Gesetz       -- law/statute
 -- der -- Arm          -- arm
 -- die -- Firma        -- firm/company
 -- die -- Kraft        -- strength/power
 -- der -- September    -- September
 -- der -- Student      -- student
 -- das -- Zuhause      -- home
 -- die -- Chance       -- chance
 -- die -- Zeitung      -- newspaper
 -- der -- Erfolg       -- success
 -- die -- Grenze       -- border/frontier/limit
 -- der -- Satz         -- sentence
 -- das -- Angebot      -- offer
 -- das -- Internet     -- internet
 -- die -- Kultur       -- culture
 -- die -- Lage         -- position (situation, location)
 -- die -- Leistung     -- achievement/performance
 -- das -- Mitglied     -- member
 -- das -- Projekt      -- project
 -- das -- Zimmer       -- room
 -- der -- Chef         -- chief/boss (m)
 -- die -- Chefin       -- chief/boss (f)
 -- der -- Zug          -- train
 -- der -- Arzt         -- doctor (m)
 -- der -- Ärztin       -- doctor (f)
 -- der -- Fuß          -- foot
 -- der -- Körper       -- body
 -- die -- Klasse       -- class (school, social)
 -- die -- Lösung       -- solution
 -- die -- Höhe         -- height (altitude, limit)
 -- der -- Junge        -- boy
 -- das -- Fenster      -- window
 -- die -- Luft         -- air
 -- die -- Meinung      -- opinion
 -- die -- Idee         -- idea
 -- das -- Produkt      -- product
 -- das -- Studium      -- study (of)
 -- der -- Vergleich    -- comparison
 -- der -- Vergleich    -- simile
 -- das -- Mittel       -- means
 -- das -- Modell       -- model
 -- die -- Natur        -- nature
 -- das -- Bett         -- bed
 -- der -- Kunde        -- customer (m)
 -- die -- Kundin       -- customer (f)
 -- die -- Kunde        -- science
 -- plu -- Kunde        -- tidings              # plural only
 -- der -- Mitarbeiter      -- collaborator (m)
 -- die -- Mitarbeiterin    -- collaborator (f)
 -- der -- Tod          -- death
 -- das -- Geschäft     -- business             # all of the english senses
 -- der -- Spaß         -- fun
 -- die -- Wirtschaft   -- economy/commerce
 -- das -- Tier         -- animal
 -- die -- Bewegung     -- motion
 -- der -- Gast         -- guest
 -- die -- Sicherheit   -- security/safety
 -- der -- Einsatz      -- inset/compartment
 -- der -- Einsatz      -- stake                # other related senses

 -- das -- Gebiet       -- area/region
 -- der -- Dank         -- gratefulness
 -- das -- Dorf         -- village
 -- der -- Kollege      -- colleague (m)
 -- die -- Kollegin     -- colleague (f)
 -- die -- Angabe       -- statement
 -- der -- Bruder       -- brother
 -- die -- Verfügung    -- decree
 -- das -- Fach         -- compartment
 -- das -- Fach         -- field/subject        # is it related to faculty?
 -- das -- Herz         -- heart
 -- der -- Kontakt      -- contact
 -- die -- Menge        -- set (math)
 -- die -- Menge        -- amount/quantity
 -- der -- Sommer       -- Summer
 -- der -- Unterschied  -- difference
 -- der -- Anspruch     -- claim
 -- die -- Antwort      -- answer
 -- die -- Verbindung   -- connection/link
 -- die -- Vorstellung  -- idea
 -- die -- Vorstellung  -- imagination
 -- die -- Vorstellung  -- introduction
 -- die -- Anwendung    -- application (of)
 -- das -- Alter        -- age
 -- die -- Kost         -- cost/expense
 -- der -- Patient      -- patient (m)
 -- die -- Patientin    -- patient (f)
 -- die -- Polizei      -- police
 -- das -- Theater      -- theatre
 -- die -- Ausbildung   -- training
 -- die -- Gefahr       -- danger
 -- das -- Gerät        -- piece of equipment
 -- der -- Kilometer    -- kilometre
 -- die -- Hilfe        -- help
 -- der -- Computer     -- computer
 -- der -- Dollar       -- dollar
 -- das -- Verfahren    -- process
 -- der -- Vertrag      -- contract
 -- die -- Maßnahme     -- measure (for/against sth)
 -- die -- Mitte        -- middle
 -- der -- Oktober      -- October
 -- die -- Ordnung      -- order (tidiness, structure)
 -- der -- Stoff        -- substance
 -- der -- Beginn       -- beginning
 -- das -- Glück        -- luck/fortune
 -- das -- Wochenende   -- weekend
 -- der -- Professor    -- professor (m)
 -- der -- Professorin  -- professor (f)
 -- die -- Reihe        -- row
 -- die -- Reihe        -- series (math)
 -- der -- Westen       -- west                 # also just 'West' will do
 -- die -- Bevölkerung  -- population/people
 -- das -- Institut     -- institute
 -- der -- Osten        -- east                 # also just 'Ost' will do
 -- die -- Schwester    -- sister
 -- die -- Erde         -- earth/ground
 -- die -- Erde         -- Earth
 -- die -- Ebene        -- plane
 -- die -- Ebene        -- plain
 -- die -- Reise        -- trip/journey
 -- die -- Einheit      -- unity
 -- das -- Haar         -- hair
 -- der -- Montag       -- Monday
 -- die -- Nähe         -- neighbourhood/vicinity
 -- das -- Prinzip      -- principle
 -- der -- Vorteil      -- advantage
 -- die -- Struktur     -- structure
 -- der -- Autor        -- author
 -- die -- Bedingung    -- condition
 -- das -- Risiko       -- risk
 -- die -- Wahl         -- choice
 -- die -- Wahl         -- election
 -- die -- Wirkung      -- effect
 -- der -- Brief        -- letter
 -- die -- Größe        -- size/height
 -- plu -- Medien       -- media
 -- der -- Sonntag      -- Sunday
 -- die -- Macht        -- might/strength
 -- die -- Untersuchung -- investigation/examination
 -- die -- Veränderung  -- change
 -- das -- Datum        -- data                 # used in plural (die Daten)
 -- der -- Einfluss     -- influence
 -- die -- Methode      -- method
 -- die -- Organisation -- organization
 -- die -- Liebe        -- love
 -- die -- Rede         -- speech (talk, rhetoric)
 -- die -- Rede         -- talk/dialogue
 -- der -- Sport        -- sport
 -- der -- Augenblick   -- moment               # wow! lit. 'glance of eyes'?
 -- die -- Diskussion   -- discussion
 -- die -- Forderung    -- demand
 -- der -- Kreis        -- circle (of sth)
 -- der -- Kreis        -- circuit
 -- die -- Technik      -- technique
 -- die -- Technik      -- technology
 -- der -- Versuch      -- attempt              # also experiment/test
 -- die -- Krankheit        -- illness
 -- die -- Schwierigkeit    -- difficulty
 -- die -- Tätigkeit        -- activity
 -- die -- Voraussetzung    -- prerequisite
 -- der -- Kampf        -- fight/struggle
 -- der -- Künstler     -- artist (m)
 -- die -- Künstlerin   -- artist (f)
 -- die -- Region       -- region
 -- der -- Eindruck     -- impression
 -- die -- Reaktion     -- reaction
 -- der -- Beitrag      -- contribution
 -- das -- Konzept      -- concept/draft
 -- die -- Linie        -- line
 -- der -- Mund         -- mouth
 -- der -- Wunsch       -- wish
 -- der -- Artikel      -- article
 -- der -- Gegensatz    -- opposite
 -- das -- Kapitel      -- chapter              # false friend? watch out!
 -- die -- Literatur    -- literature


# # #
# ABBREVIATIONS
#

de.abbr -- 
 -- bzw.            -- beziehungsweise          # correspondingly (resp.)
 -- z.B.            -- zum Beispiel             # for example (e.g.)
 -- usw.            -- und so weiter            # and so forth (etc.)
 -- d.h.            -- das heißt                # that is (i.e.)
 -- u.a.            -- unter anderem            # among others (etc.)
 -- vgl.            -- vergleiche               # compare with (cf.?)
 -- ca.             -- zirka                    # circa (around)
 -- v.C.            -- vor Christus             # before Christ (BC)
 -- n.C.            -- nach Christus            # after Christ (AC)


# # #
# SPECIAL TOPICS 
#
# NOTE: Contains some duplicates with above, but these are
# meant to be ignored by the script.
# TODO: Just watch out for forks!

# Calendar words

de.noun --
 -- die -- Zeit         -- time
 -- der -- Morgen       -- morning
 -- das -- Morgen       -- future
 -- das -- Morgen       -- tomorrow (vague)
 -- der -- Vormittag    -- beforemidday
 -- der -- Mittag       -- midday
 -- der -- Nachmittag   -- afternoon
 -- der -- Abend        -- evening
 -- die -- Nacht        -- night
 -- die -- Mitternacht  -- midnight
 -- der -- Tag          -- day
 -- der -- Sonntag      -- Sunday
 -- der -- Montag       -- Monday
 -- der -- Dienstag     -- Tuesday
 -- der -- Mittwoch     -- Wednesday
 -- der -- Donnerstag   -- Thursday
 -- der -- Freitag      -- Friday
 -- der -- Samstag      -- Saturday
 -- das -- Wochenende   -- Weekend
 -- die -- Woche        -- Week
 -- der -- Wochentag    -- Weekday
 -- der -- Monat        -- Month
 -- der -- Januar       -- January
 -- der -- Februar      -- February
 -- der -- März         -- March
 -- der -- April        -- April
 -- der -- Mai          -- May
 -- der -- Juni         -- June
 -- der -- Juli         -- July
 -- der -- August       -- August
 -- der -- September    -- September
 -- der -- Oktober      -- October
 -- der -- November     -- November
 -- der -- Dezember     -- December
 -- die -- Jahreszeit   -- Season
 -- der -- Sommer       -- Summer
 -- der -- Herbst       -- Autumn
 -- der -- Winter       -- Winter
 -- der -- Frühling     -- Spring
 -- das -- Semester     -- semester
 -- das -- Wintersemester   -- Winter semester  # WS, Okt--Mär, germany
 -- das -- Sommersemester   -- Summer semester  # SS, Apr--Sep, germany
 -- das -- Herbstsemester   -- Autumn semester  # HS, Sep--Dez, switzerland
 -- das -- Frühlingsemester -- Spring semester  # FS, Feb--Jun, switzerland
 -- das -- Jahr         -- year
 -- das -- Datum        -- date

de.adv --
 -- heute           -- today
 -- gestern         -- yesterday
 -- morgen          -- tomorrow

# TODO: Add the many holidays

# Colours and related words

de.adj --
 -- rot             -- red
 -- rosa            -- pink                     # no declension
 -- lila            -- lilac                    # no declension
 -- violett         -- violet
 -- gelb            -- yellow
 -- gold            -- gold
 -- grün            -- green
 -- blau            -- blue
 -- türkis          -- turquoise
 -- braun           -- brown
 -- beige           -- beige
 -- ocker           -- ochre
 -- grau            -- gray
 -- silber          -- silver
 -- weiß            -- white
 -- schwarz         -- black

de.noun -- das -- Morgenrot     -- morning red sky
de.noun -- das -- Abendrot      -- evening red sky
de.verb -- rot werden           -- to become red/blush
de.verb -- rotsehen             -- to see red
de.adj  -- blau                 -- drunk
de.adj  -- blauäugig            -- blue-eyed/naive
de.verb -- blaumachen           -- to 'make blue' (skip work)
de.verb -- bräunen              -- to brown/tan
de.noun -- die -- Grauzone          -- grey area
de.noun -- der -- Schwarzfahrer     -- 'black rider' (fare evader) (m)
de.noun -- die -- Schwarzfahrerin   -- 'black rider' (fare evader) (f)
de.noun -- der -- Schwarzseher      -- 'black seer' (pessimist) (m)
de.noun -- die -- Schwarzseherin    -- 'black seer' (pessimist) (f)
de.verb -- schwarzmalen             -- to 'paint black' (be pessimistic)
de.verb -- schwarzärgern sich       -- to turn black (with anger)
"""
