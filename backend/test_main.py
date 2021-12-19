from fastapi.testclient import TestClient
from starlette.testclient import TestClient
from main import app

client = TestClient(app)

# Test for Root
def test_read_main():
  response = client.get("/")
  assert response.status_code == 200
  assert response.json() == {
    "message": "Welcome to the root of API.",
    "links": {
      "api_root": "/",
      "get": "/quadruplex",
      "post": "/quadruplex"
    }
  }

# Test for data sent & return data
def test_create_item():
  response = client.post(
    "/quadruplex",
    json = {
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
  )
  assert response.status_code == 200
  assert response.json() == {
    "sequences": [
      {
        "name": "seq2",
        "count": 2,
        "quadruplexes": [
          {
            "start": 0,
            "end": 3
          },
          {
            "start": 7,
            "end": 10
          }
        ]
      },
      {
        "name": "seq4",
        "count": 1,
        "quadruplexes": [
          {
            "start": 3,
            "end": 6
          }
        ]
      },
      {
        "name": "seq5",
        "count": 1,
        "quadruplexes": [
          {
            "start": 4,
            "end": 7
          }
        ]
      },
      {
        "name": "seq7",
        "count": 2,
        "quadruplexes": [
          {
            "start": 4,
            "end": 7
          },
          {
            "start": 8,
            "end": 11
          }
        ]
      },
      {
        "name": "seq8",
        "count": 2,
        "quadruplexes": [
          {
            "start": 4,
            "end": 7
          },
          {
            "start": 8,
            "end": 11
          }
        ]
      },
      {
        "name": "seq9",
        "count": 2,
        "quadruplexes": [
          {
            "start": 0,
            "end": 3
          },
          {
            "start": 5,
            "end": 8
          }
        ]
      },
      {
        "name": "seq10",
        "count": 2,
        "quadruplexes": [
          {
            "start": 2,
            "end": 5
          },
          {
            "start": 11,
            "end": 14
          }
        ]
      },
      {
        "name": "seq11",
        "count": 1,
        "quadruplexes": [
          {
            "start": 11,
            "end": 14
          }
        ]
      },
      {
        "name": "seq12",
        "count": 2,
        "quadruplexes": [
          {
            "start": 6,
            "end": 9
          },
          {
            "start": 12,
            "end": 15
          }
        ]
      },
      {
        "name": "seq14",
        "count": 1,
        "quadruplexes": [
          {
            "start": 6,
            "end": 9
          }
        ]
      },
      {
        "name": "seq15",
        "count": 5,
        "quadruplexes": [
          {
            "start": 6,
            "end": 9
          },
          {
            "start": 17,
            "end": 20
          },
          {
            "start": 21,
            "end": 24
          },
          {
            "start": 25,
            "end": 28
          },
          {
            "start": 33,
            "end": 36
          }
        ]
      },
      {
        "name": "seq17",
        "count": 1,
        "quadruplexes": [
          {
            "start": 0,
            "end": 3
          }
        ]
      },
      {
        "name": "seq18",
        "count": 2,
        "quadruplexes": [
          {
            "start": 0,
            "end": 3
          },
          {
            "start": 19,
            "end": 22
          }
        ]
      },
      {
        "name": "seq19",
        "count": 2,
        "quadruplexes": [
          {
            "start": 15,
            "end": 18
          },
          {
            "start": 19,
            "end": 22
          }
        ]
      },
      {
        "name": "seq21",
        "count": 2,
        "quadruplexes": [
          {
            "start": 0,
            "end": 3
          },
          {
            "start": 20,
            "end": 23
          }
        ]
      },
      {
        "name": "seq22",
        "count": 2,
        "quadruplexes": [
          {
            "start": 0,
            "end": 3
          },
          {
            "start": 16,
            "end": 19
          }
        ]
      },
      {
        "name": "seq23",
        "count": 8,
        "quadruplexes": [
          {
            "start": 0,
            "end": 3
          },
          {
            "start": 4,
            "end": 7
          },
          {
            "start": 8,
            "end": 11
          },
          {
            "start": 12,
            "end": 15
          },
          {
            "start": 16,
            "end": 19
          },
          {
            "start": 20,
            "end": 23
          },
          {
            "start": 24,
            "end": 27
          },
          {
            "start": 28,
            "end": 31
          }
        ]
      },
      {
        "name": "seq24",
        "count": 2,
        "quadruplexes": [
          {
            "start": 6,
            "end": 9
          },
          {
            "start": 13,
            "end": 16
          }
        ]
      },
      {
        "name": "seq25",
        "count": 3,
        "quadruplexes": [
          {
            "start": 1,
            "end": 4
          },
          {
            "start": 5,
            "end": 8
          },
          {
            "start": 9,
            "end": 12
          }
        ]
      },
      {
        "name": "seq26",
        "count": 1,
        "quadruplexes": [
          {
            "start": 1,
            "end": 4
          }
        ]
      },
      {
        "name": "seq27",
        "count": 1,
        "quadruplexes": [
          {
            "start": 19,
            "end": 22
          }
        ]
      }
    ]
  }
