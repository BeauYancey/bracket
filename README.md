# March Madness Bracket Builder

This program predicts the winner of a college basketball matchup between two teams.

## What BPI Means

BPI stands for `Basketball Power Index`.

It is a rating that estimates how strong a team is compared with other teams. In simple terms:

- A higher BPI usually means a stronger team
- A lower BPI usually means a weaker team
- If one team's BPI is much higher than the other team's BPI, that team is more likely to win

You do not need to understand the full formula to use this program. You only need a reasonable number for each team.

If you want official BPI information for men's teams, ESPN publishes it here:

[ESPN Men's College Basketball BPI](https://www.espn.com/mens-college-basketball/bpi)

If you cannot find an exact BPI value, you can still make a rough estimate:

- Very strong team: around `12` to `18`
- Good team: around `6` to `11`
- Average team: around `0` to `5`
- Weak team: below `0`

Those numbers are only rough guidelines, but they are good enough if you just want to run the program and compare teams.

## Choose The Easiest Way To Use It

You have two options:

### Option 1: Manual mode

Use this if you want the simplest setup.

- You do not need to install any extra Python packages
- You will need to know each team's BPI value and type it in yourself

### Option 2: ESPN mode

Use this if you want the program to look up BPI values for you.

- You need an internet connection
- You need to install the package listed in `requirements.txt`
- You start the program with the `-m` option

## What You Need

Before running the program, make sure you have:

- A computer with Windows, macOS, or Linux
- Python 3 installed

If you want to use ESPN mode, you also need:

- An internet connection

## Step 1: Install Python 3

If Python is not already installed:

- Go to [python.org](https://www.python.org/downloads/)
- Download Python 3 for your computer
- Run the installer

If you are using Windows, check the box called `Add Python to PATH` during installation.

## Step 2: Open a command-line window

Use one of these:

- Windows: `PowerShell` or `Command Prompt`
- macOS: `Terminal`
- Linux: `Terminal`

## Step 3: Go to this project folder

In the command-line window, move into the folder that contains this project.

Example on macOS or Linux:

```bash
cd /path/to/bracket
```

Example on Windows:

```powershell
cd C:\Users\YourName\Downloads\bracket
```

## Step 4: Decide Which Mode You Want

### Manual mode

Run:

```bash
python3 bracket.py
```

If `python3` does not work, try:

```powershell
python bracket.py
```

or:

```powershell
py bracket.py
```

In this mode, the program asks for:

1. The first team name
2. That team's BPI value
3. The second team name
4. That team's BPI value

Example:

```text
Enter the first team: Florida
We couldn't find Florida's BPI. Please enter it now: 12.4
Enter the second team: Duke
We couldn't find Duke's BPI. Please enter it now: 10.8
```

This is the best option if:

- You do not want to install anything extra
- You already know the BPI numbers you want to use

If you do not know a team's BPI:

- Check [ESPN Men's College Basketball BPI](https://www.espn.com/mens-college-basketball/bpi)
- Or enter a rough estimate based on how strong you think the team is

### ESPN mode

First, install the required package:

```bash
python3 -m pip install -r requirements.txt
```

If `python3` does not work on your system, try:

```powershell
python -m pip install -r requirements.txt
```

or:

```powershell
py -m pip install -r requirements.txt
```

Then run:

```bash
python3 bracket.py -m
```

If needed, try:

```powershell
python bracket.py -m
```

or:

```powershell
py bracket.py -m
```

In this mode, the program tries to download BPI ratings from ESPN before interactive mode starts.

Example:

```text
Enter the first team: Florida
Enter the second team: Duke
```

If the program finds both teams, it will use the downloaded BPI values automatically.

If it cannot find a team, it will still ask you to type in that team's BPI value manually.

## What Team Names Can You Type?

The program accepts:

- Team nickname
- Team abbreviation
- Team short display name

Examples:

- `Florida`
- `florida`
- `FLA`
- `Duke`

## What Happens Next

After you enter two teams, the program prints the predicted winner.

Then it asks for another matchup so you can keep using the program without restarting it.

## How To Stop The Program

You can stop it at any time by:

- Typing `quit` when asked for a team name or BPI
- Pressing `Ctrl + C`

## Help Command

If you want to see the built-in usage message, run:

```bash
python3 bracket.py --help
```

## Common Problems

### `python3` is not recognized

Try one of these instead:

- `python bracket.py`
- `py bracket.py`

If none of those work, install Python from [python.org](https://www.python.org/downloads/).

### `No module named requests`

This only matters for ESPN mode.

Install the required package with:

```bash
python3 -m pip install -r requirements.txt
```

### The program says it cannot fetch BPI data

Possible reasons:

- You are not connected to the internet
- The required package is not installed
- ESPN's API is temporarily unavailable

If that happens, run the program without `-m` and enter BPI values manually instead:

```bash
python3 bracket.py
```

### The program asks for a BPI value even in ESPN mode

That means the team name you entered was not found in the downloaded data.

Try:

- A different spelling
- The team abbreviation
- The team's short display name

If it still is not found, type the BPI value manually.

### I do not know a team's BPI

Start here:

- Check [ESPN Men's College Basketball BPI](https://www.espn.com/mens-college-basketball/bpi)
- If you still cannot find it, enter an estimate

Quick estimation guide:

- Very strong team: `12` to `18`
- Good team: `6` to `11`
- Average team: `0` to `5`
- Weak team: below `0`

If you are unsure, approximate values are fine. This program is meant for simple matchup prediction, not precise forecasting.

## Short Version

If you want the fastest possible instructions:

### Simplest setup

1. Install Python 3
2. Open a terminal in this folder
3. Run `python3 bracket.py`
4. Type team names and BPI values when asked

### Automatic ESPN lookup

1. Install Python 3
2. Open a terminal in this folder
3. Run `python3 -m pip install -r requirements.txt`
4. Run `python3 bracket.py -m`
5. Type two team names when asked
