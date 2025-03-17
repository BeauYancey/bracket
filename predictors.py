import requests

def fetch_bpi(num_teams: int = 50, page: int = 1) -> dict[str, str]:
    url = f"https://site.web.api.espn.com/apis/fitt/v3/sports/basketball/mens-college-basketball/powerindex?region=us&lang=en&groups=50&limit={num_teams}&page={page}&sort=bpi.bpi%3Adesc"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching data:", response.status_code)
        return {}
    
    data = response.json()
    bpis = {}
    
    for team in data.get("teams", []):
        team_name = team["team"]["abbreviation"]
        bpi = float(team["categories"][0]["totals"][0])
        bpis[team_name] = bpi
    
    return bpis

def win_probability(bpi_a: float, bpi_b: float) -> float:
    return 1 / (1 + 10 ** ((bpi_b - bpi_a) / 10))