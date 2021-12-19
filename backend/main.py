from fastapi import FastAPI, Path, Query, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import Optional, final
from pydantic import BaseModel
from typing import List
from itertools import groupby
from fastapi.middleware.cors import CORSMiddleware
import re

app = FastAPI()
data = {}

# Allow CORS - Cross-Origin Resource Sharing (CORS)
# https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Class Object sequence
class ObjectSequence(BaseModel):
  name: str
  sequence: str

# Class Array of sequence
class ArrayOfSequences(BaseModel):
  sequences: List[ObjectSequence] = []

# Class Quadruplex
class ObjectQuadruplex(BaseModel):
  start: int
  end: int

# Class Quadruplexes - [Start, End] + Count
class ArrayOfQuadruplexes(BaseModel):
  name: str
  quadruplexes: List[ObjectQuadruplex] = []
  count: int

# Class Array Of Sequences & Quadruplexes
class ArrayOfSequencesAndQuadruplexes(BaseModel):
  sequences: List[ArrayOfQuadruplexes] = []

# --------------
# GET [Root] - /
# --------------
@app.get("/")
def read_root():
  root = {
    "message": "Welcome to the root of API.",
    "links": {
      "api_root": "/",
      "get": "/quadruplex",
      "post": "/quadruplex"
    }
  }
  return root

# -----------------
# GET - /quadruplex
# -----------------
@app.get("/quadruplex")
def display_all_sequences():
  data = {
    "sequences": [
      {
         "name": "seq1",
         "sequence": "ATTC"
      },
      {
         "name": "seq2",
         "sequence": "GGGGTATGGGG"
      },
      {
         "name": "seq3",
         "sequence": "GATTACA"
      },
      {
         "name": "seq4",
         "sequence": "CATGGGGTA"
      },
      {
        "name": "seq5",
        "sequence": "ATTCGGGG"
      },
      {
        "name": "seq6",
        "sequence": "GATTGGGC"
      },
      {
        "name": "seq7",
        "sequence": "GGATGGGGGGGGGTC"
      },
      {
        "name": "seq8",
        "sequence": "GGGAGGGGGGGGTTC"
      },
      {
        "name": "seq9",
        "sequence": "GGGGAGGGGGTTC"
      },
      {
        "name": "seq10",
        "sequence": "GAGGGGAGATTGGGGTTCGG"
      },
      {
        "name": "seq11",
        "sequence": "GGATTTTCGTTGGGGGG"
      },
      {
        "name": "seq12",
        "sequence": "GGATTTGGGGTCGGGGTTTT"
      },
      {
        "name": "seq13",
        "sequence": "GTTTTGGATTTTCTTTTGG"
      },
      {
        "name": "seq14",
        "sequence": "GGGCCCGGGGCGATTCCCCCGG"
      },
      {
        "name": "seq15",
        "sequence": "GAAATTGGGGGCCCCTTGGGGGGGGGGGGGGGCGGGGGGG"
      },
      {
        "name": "seq16",
        "sequence": "GATGGAAGTTAACCTTGGAAGTTGGAAGTTAACCTAACCTCGG"
      },
      {
        "name": "seq17",
        "sequence": "GGGGGAAGTTAACCTATTCGGAAGTTAACCTGGG"
      },
      {
        "name": "seq18",
        "sequence": "GGGGATGGAAGTTAACCTCGGGG"
      },
      {
        "name": "seq19",
        "sequence": "GGGAAATTACCCGGCGGGGGGGGG"
      },
      {
        "name": "seq20",
        "sequence": "GGGATGGAGAGAGGTCGGG"
      },
      {
        "name": "seq21",
        "sequence": "GGGGATGTTAATTAATTATCGGGG"
      },
      {
        "name": "seq22",
        "sequence": "GGGGAGCTTAAGGTAAGGGG"
      },
      {
        "name": "seq23",
        "sequence": "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"
      },
      {
        "name": "seq24",
        "sequence": "GGGCATGGGGCATGGGG"
      },
      {
        "name": "seq25",
        "sequence": "TGGGGGGGGGGGGGGACATTAGG"
      },
      {
        "name": "seq26",
        "sequence": "CGGGGATGGTAGGCAGGTGG"
      },
      {
        "name": "seq27",
        "sequence": "GGCAGGGTGGGTACAGGGTGGGG"
      }
    ]
  }
  return data

# ----------------------------------------------------
# POST - /quadruplex - Create Sequence by Class Object
# ----------------------------------------------------
@app.post("/quadruplex")
def send_sequence(seqArr: ArrayOfSequences):
  sort_data = seqArr.dict(exclude_unset=True)
  find = find_g_quadruplex(sort_data)
  # raise HTTPException(status_code=400, detail="Sequence already exists!")
  return find

# --------------------------
# Find Quadruplexes - Gs
#	It should only return sequences which have at least 4 consecutive G
#	For those sequences it returns the start an end positions of all the G’s
#	Finally it returns the number of subsequences that have at least four consecutive G’s
# --------------------------
def find_g_quadruplex(data: ArrayOfSequencesAndQuadruplexes):
  sequences = data['sequences']
  count = 0
  response = {
    "sequences": []
  }

  for i in sequences:
    name = i['name']
    seq = i['sequence']
    count = 0
    quadruplexes = []

    for seq in re.finditer('GGGG', seq):
      start = seq.start()
      end = seq.end() - 1 if seq else None

      quadruplex = {
        "start": start,
        "end": end
      }
      quadruplexes.append(quadruplex)
      count += 1

    if count >= 1:
      arrayOfSequences = {
        "name": name,
        "count": count,
        "quadruplexes": quadruplexes
      }
      response['sequences'].append(arrayOfSequences)

  #print('response:', response)
  return response
