#!/usr/bin/env python

from pyknon import genmidi
from pyknon.music import NoteSeq


def gen_patterns(pattern, number_rotations=12, repeat=4):
    result = NoteSeq()
    for n in range(0, number_rotations):
        rotation = pattern.rotate(n)
        result.extend(rotation * repeat)
    return result


def piano_phase(number_rotations=12, repeat=4):
    pattern = NoteSeq("E16 F# B C#'' D'' F#' E C#'' B' F# D'' C#")
    piano1 = pattern * (number_rotations + 1) * repeat
    piano2 = gen_patterns(pattern, number_rotations, repeat)

    midi = genmidi.Midi(2, tempo=108)
    midi.seq_notes(piano1)
    midi.seq_notes(piano2, track=1, time=3*repeat)
    midi.write("midi/piano-phase.mid")


if __name__ == "__main__":
    piano_phase()
