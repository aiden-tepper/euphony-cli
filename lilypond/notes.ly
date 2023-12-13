global = {
  \key fis \minor
  \time 4/4
}

\parallelMusic voiceA,voiceB,voiceC,voiceD {
d4 ees bes b aes f bes ees |
d4 bes bes ges aes f g g |
f4 ees d b b a bes bes |
aes4 ges f ees ees c ees ees |
}

\score {
          \new PianoStaff <<
             \new Staff {
               \global
               <<
                 \relative c'' \voiceA
                 \\
                 \relative c'  \voiceB
               >>
             }
             \new Staff {
               \global \clef bass
               <<
                 \relative c \voiceC
                 \\
                 \relative c \voiceD
               >>
             }
          >>
        }
        