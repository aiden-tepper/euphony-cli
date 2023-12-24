global = {
  \key c \major
  \time 4/4
}

\parallelMusic voiceA,voiceB,voiceC,voiceD {
d4 g c |
d4 b c |
f4 d e |
a4 g g |
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
        