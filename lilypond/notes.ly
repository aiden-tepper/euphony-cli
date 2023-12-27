global = {
  \key bes \major
  \time 4/4
  \version "2.22.1"
}

\parallelMusic voiceA,voiceB,voiceC,voiceD {
f''4 f'' g'' g'' f'' ees'' f'' |
d''4 c'' d'' ees'' c'' c'' d'' |
bes'4 a' bes' bes' a' a' a' |
bes4 f' g' ees' f' f' bes |
}

\score {
          \new PianoStaff <<
             \new Staff {
               \global
               <<
                 \fixed c \voiceA
                 \\
                 \fixed c,  \voiceB
               >>
             }
             \new Staff {
               \global \clef bass
               <<
                 \fixed c, \voiceC
                 \\
                 \fixed c, \voiceD
               >>
             }
          >>
        }
        