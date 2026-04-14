import sys
import time

COLORS = ["\033[1;31m", "\033[1;32m", "\033[1;33m", "\033[1;34m", "\033[1;35m", "\033[1;36m"]
RESET = "\033[0m"

def print_lyrics():
    lyrics = [
        "🎵 Aapka hi kehna banta~a 💖",
        "💬 Keh~do~na",
        "😊 Main sharma ke keh dungi~i",
        "❤️ Maine bhi dil diya~a",
        "👀 Aankhon ankhon ka masla",
        "✨ Achha~tha",
        "🎶 Ab le jao apna bana ke",
        "🌹 Mujhe meri ja~~an",
    ]

    delays = [1.8, 1.2, 2.0, 2.0, 2.2, 1.5, 2.2, 2.1]

    for index, line in enumerate(lyrics):
        color = COLORS[index % len(COLORS)]
        sys.stdout.write(color)
        sys.stdout.flush()

        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)

        sys.stdout.write(RESET + "\n")
        sys.stdout.flush()
        time.sleep(delays[index])

if __name__ == "__main__":
    print_lyrics()