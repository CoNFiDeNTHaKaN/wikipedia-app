import random
import requests

API_URL = "https://en.wikipedia.org/w/api.php"
HEADERS = {"User-Agent": "MSIT Hackathon - Wikipedia Console app."}

def show_capital_fact(capital):
    params = {
        "action": "query", "titles": capital, "redirects": 1,
        "prop": "extracts", "exintro": 1, "explaintext": 1,
        "exchars": 240, "format": "json", "formatversion": 2,
    }
    try:
        response = requests.get(API_URL, params=params, headers=HEADERS, timeout=5)
        response.raise_for_status()
        pages = response.json().get("query", {}).get("pages", [])
        if pages and pages[0].get("extract"):
            print(pages[0]["extract"])
        else:
            print("No Wikipedia summary available.")
    except (requests.RequestException, ValueError):
        print("Could not load the Wikipedia summary.")

def main():
    questions = [
        ("France", "Paris"), ("Germany", "Berlin"), ("Italy", "Rome"),
        ("Japan", "Tokyo"), ("Spain", "Madrid"), ("Canada", "Ottawa"),
    ]
    random.shuffle(questions)
    scores = [0, 0]
    print("Capital Quiz! Two players, three questions each.")
    for index, (country, capital) in enumerate(questions):
        player = index % 2
        answer = input(f"\nPlayer {player + 1}, what is the capital of {country}? ")
        if answer.strip().lower() == capital.lower():
            scores[player] += 1
            print("Correct!")
        else:
            print(f"The correct answer is {capital}.")
        show_capital_fact(capital)
    print(f"\nFinal score: Player 1: {scores[0]} | Player 2: {scores[1]}")
    if scores[0] == scores[1]:
        print("It's a tie!")
    elif scores[0] > scores[1]:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

if __name__ == "__main__":
    main()