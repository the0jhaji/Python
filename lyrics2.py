import time
import sys
def print_lyrics():
    lyrics = [
        "Chhane-Chhane Marela Tana Ho",
        "Ghare Kaise Rahi Janana Ho",
        "",
        "",
        "Tu Hi Batawa?",
        "Tohra Le Neeman To Sakhiye Ke Baate",
        "Sunar Milal Mardana Ho",
        "Jada Mein Dard Wala Sard Hawa Raja Ji",
        "Sard Hawa Raja Ji",
        "Uth Jaye Lahar Aisan Harad Hawa Raja Ji",
        "Tu Marad Nahi Matha Ke Dard Hawa Raja Ji",
        "Tu Marad Nahi Matha Ke Dard Hawa Raja Ji",
        "Tu Marad Nahi Matha Ke",
        "Tu Marad Nahi Matha Ke",
        "Bujhala?",
        "Marad Nahi Matha Ke",
        "Dard Hawa Raja Ji.."
    ]
    delays = [1.5, 1.5, 1.5, 2.0, 2.0, 2.0, 1.5, 2.0, 2.0, 2.0, 1.5, 1.5, 1.5, 2.0, 2.5,2.0, 2.0, 2.0]
    for i, line in enumerate(lyrics):
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)  # Simulate typing effect
        print()
        time.sleep(delays[i])

if __name__ == "__main__":
    print_lyrics()