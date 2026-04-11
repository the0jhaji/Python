import time
import sys
def print_lyrics():
    lyrics = [
        "Ni tainu dekh ke jee lagda",
        "Dekh deeva jagda",
        "Ni tainu dekh ke taan lagda",
        "Tu moran kolon sikhdi taura",
        
        "Dass ki chauni ae Jaan sukhauni ae",
        "Ni tu jadd vaal sukhauni ae",
        "Phir sulfe wangu chadh diyan loran",
        
        "Jo kahengi jatt kar ju goriye",
        "Dowan da changa sar ju goriye",
        "Tussi aivein na daro",
    
        "Kade milke baitho",
        "Gall kariye pyaar di",
        
        "Ni tainu dekh ke jee lagda",
        "Dekh deeva jagda",
        "Ni tainu dekh ke taan lagda",
        "Tu moran kolon sikhdi taura"
    ]
    delays = [1.5, 1.5, 1.5, 2.0, 0.5, 2.0, 2.0, 2.5, 0.5, 2.0, 2.0, 2.0, 0.5, 2.0, 2.0, 0.5, 1.5, 1.5, 1.5, 2.0]
    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)  # Simulate typing effect
        print()
        time.sleep(delays[i])

if __name__ == "__main__":
    print_lyrics()