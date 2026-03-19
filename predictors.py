from typing import Optional

class TeamBPIMap(dict[str, float]):
    def _normalize_key(self, key: object) -> object:
        if isinstance(key, str):
            return key.casefold()
        return key

    def __getitem__(self, key: str) -> float:
        return super().__getitem__(self._normalize_key(key))

    def __setitem__(self, key: str, value: float) -> None:
        super().__setitem__(self._normalize_key(key), value)

    def __contains__(self, key: object) -> bool:
        return super().__contains__(self._normalize_key(key))

    def get(self, key: str, default: Optional[float] = None) -> Optional[float]:
        return super().get(self._normalize_key(key), default)


def fetch_bpi(num_teams: int = 50, page: int = 1) -> TeamBPIMap:
    try:
        import requests
    except ImportError as exc:
        raise RuntimeError('Fetching BPI data requires the "requests" package to be installed.') from exc

    url = f"https://site.web.api.espn.com/apis/fitt/v3/sports/basketball/mens-college-basketball/powerindex?region=us&lang=en&groups=50&limit={num_teams}&page={page}&sort=bpi.bpi%3Adesc"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching data:", response.status_code)
        return TeamBPIMap()
    
    data = response.json()
    bpis = TeamBPIMap()
    
    for team in data.get("teams", []):
        bpi = float(team["categories"][0]["totals"][0])
        team_data = team["team"]

        for alias_key in ("nickname", "abbreviation", "shortDisplayName"):
            alias = team_data.get(alias_key)
            if alias:
                bpis[alias] = bpi

    return bpis

def win_probability(bpi_a: float, bpi_b: float) -> float:
    return 1 / (1 + 10 ** ((bpi_b - bpi_a) / 10))
