#Win condition
import turtle
import random
#screen size 30x30 board 15x15
boardBox={ 'RR6' :(150,270), 
          'RR5' :(150,250),
          'RR4' :(150,230),
          'RR3' :(150,210),
          'RR2' :(150,190),
          'RR1' :(random.randint(130,170),random.randint(145,175)),#red finish home # done so piece wont be at the same place and you can see the differnt pieces
          'YR6' :(150,30), 
          'YR5' :(150,50),
          'YR4' :(150,70),
          'YR3' :(150,90),
          'YR2' :(150,110),
          'YR1' :(random.randint(130,170),random.randint(125,145)),#yellow finish home # done so piece wont be at the same place and you can see the differnt pieces
          'R1':(170,190),
          'R2':(170,210),
          'R3':(170,230),
          'R4':(170,250),
          'R5':(170,270),
          'R6':(170,290),
          'R7':(150,290),
          'R8':(130,290),
          'R9':(130,270),
          'R10':(130,250),
          'R11':(130,230),
          'R12':(130,210),
          'R13':(130,190),
          'Y1':(130,110),
          'Y2':(130,90),
          'Y3':(130,70),
          'Y4':(130,50),
          'Y5':(130,30),
          'Y6':(130,10),
          'Y7':(150,10),
          'Y8':(170,10),
          'Y9':(170,30),
          'Y10':(170,50),
          'Y11':(170,70),
          'Y12':(170,90),
          'Y13':(170,110),
          'G1':(110,170),
          'G2':(90,170),
          'G3':(70,170),
          'G4':(50,170),
          'G5':(30,170),
          'G6':(10,170),
          'G7':(10,150),
          'G8':(10,130),
          'G9':(30,130),
          'G10':(50,130),
          'G11':(70,130),
          'G12':(90,130),
          'G13':(110,130),
          'B1':(190,130),
          'B2':(210,130),
          'B3':(230,130),
          'B4':(250,130),
          'B5':(270,130),
          'B6':(290,130),
          'B7':(290,150),
          'B8':(290,170),
          'B9':(270,170),
          'B10':(250,170),
          'B11':(230,170),
          'B12':(210,170),
          'B13':(190,170),
          'RH':(random.randint(190,300),random.randint(190,300)),#start home # done so piece wont be at the same place and you can see the differnt pieces
          'YH':(random.randint(10,110),random.randint(10,110)),#start home # done so piece wont be at the same place and you can see the differnt pieces
          }

boardBoxLR=[
           'R5','R4','R3','R2','R1',
           'B13','B12','B11','B10','B9','B8','B7','B6','B5','B4','B3','B2','B1',
           'Y13','Y12','Y11','Y10','Y9','Y8','Y7','Y6','Y5','Y4','Y3','Y2','Y1',
           'G13','G12','G11','G10','G9','G8','G7','G6','G5','G4','G3','G2','G1',
           'R13','R12','R11','R10','R9','R8','R7',
           'RR6','RR5','RR4','RR3','RR2','RR1']

boardBoxLY=[
           'Y5','Y4','Y3','Y2','Y1',
           'G13','G12','G11','G10','G9','G8','G7','G6','G5','G4','G3','G2','G1',
           'R13','R12','R11','R10','R9','R8','R7','R6','R5','R4','R3','R2','R1',
           'B13','B12','B11','B10','B9','B8','B7','B6','B5','B4','B3','B2','B1',
           'Y13','Y12','Y11','Y10','Y9','Y8','Y7',
           'YR6','YR5','YR4','YR3','YR2','YR1']





