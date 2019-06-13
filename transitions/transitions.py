#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
'''
from random import choice
from pyknon.genmidi import Midi
from pyknon.music import Note, NoteSeq


cmajor= NoteSeq("C D E F G A B C")
dorian= NoteSeq("D E F G A B C")
dorian.stretch_dur(0.5)

def init_matrix():
  mat = [[0 for x in range(7)] for y in range(7)]
  mat[0] = [0, 3, 4, 5, 6, 1, 2]
  mat[1] = [1, 0, 3, 3, 2, 1, 1]
  mat[2] = [1, 2, 0, 4, 2, 1, 1]
  mat[3] = [4, 1, 2, 0, 5, 1, 1]
  mat[4] = [6, 1, 2, 5, 0, 1, 1]
  mat[5] = [3, 2, 3, 3, 2, 0, 1]
  mat[6] = [5, 0, 3, 3, 2, 1, 0]
  return mat

def print_matrix(mat):
  for i in range(7):
    print(mat[i])

def pick_next(current, mat):
  successors = []
  for i in range(7):
  	successors.extend([i] * mat[current][i])
  next = choice(successors)
  return next

def gen_midi(filename, note_list):
  midi = Midi(tempo=120)
  midi.seq_notes(note_list)
  midi.write("midi/" + filename)

def run():
  m = init_matrix()
  #print_matrix(m)
  numseq = []
  numnote = 0
  for i in range (64):
    numseq.extend([numnote])
    numnote = pick_next(numnote, m)
  numseq.extend([0]) #end with the root note

  notes = []
  for n in numseq:
    notes.append(dorian[n])
  '''
  bassnotes = []
  for n in range(0, len(numseq), 4):
   note = dorian[n]
  '''
  gen_midi("dorian.mid",notes)
  print notes

if __name__ == '__main__':
  run()
