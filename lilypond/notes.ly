global = {
  \key c \major
  \time 4/4
}

\parallelMusic voiceA,voiceB,voiceC,voiceD {
d4 g c |
f4 f g |
a4 b b |
c4 d e |
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
        