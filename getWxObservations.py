#!/usr/bin/python3

def getObs(station):
    output = {
      "station":"KOSH",
      "when": "2021-10-04T12:00",
      "temperature":20
    }
    return output
    
if __name__ == "__main__":
    print(getObs("KOSH"))

    
