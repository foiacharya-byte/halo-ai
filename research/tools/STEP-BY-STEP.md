# Step-by-step (for non-technical users) — get r/vadodara research data for free

You do **not** need to pay anything. You do **not** need to know coding.
Just follow these steps in order. Takes about 15 minutes the first time.

---

## What you'll end up with
Three spreadsheet files (in the `instruments` folder) full of *patterns* from
real Vadodara Reddit conversations — what people ask for, where trust breaks,
how they write — with **no names, no phone numbers, no personal info** in them.

---

## PART 1 — Get your free Reddit "key" (one time)

You need two secret codes from Reddit. They're free.

1. Open a browser and **log in to Reddit** (make a free account if needed).
2. Go to this page: **https://www.reddit.com/prefs/apps**
3. Scroll to the bottom. Click the button **"create another app…"** (or
   "are you a developer? create an app").
4. Fill the small form:
   - **name:** `halo-vadodara-research`
   - Choose the **"script"** option (round button on the left).
   - **redirect uri:** type `http://localhost:8080`
   - Leave the rest blank.
5. Click **"create app"**.
6. You'll now see your app box. Two things you need from it:
   - The **client id** = the short code shown *right under the words*
     "personal use script" (looks like `Ab3xYz...`).
   - The **secret** = the longer code next to the word **"secret"**.
   👉 Keep this browser tab open; you'll copy these in Part 3.

> These are like a username/password for reading public Reddit data politely.
> Never share them or post them anywhere.

---

## PART 2 — Make sure Python is on your computer (one time)

The script needs "Python" (free software). Check if you already have it:

**On Windows:**
1. Click Start, type **`cmd`**, press Enter (a black window opens).
2. Type this and press Enter: `python --version`
3. If you see something like `Python 3.11`, you're good — skip to Part 3.
4. If not, go to **https://www.python.org/downloads/**, click the big yellow
   download button, run the installer, and **tick the box that says "Add
   Python to PATH"** before clicking Install. Then redo steps 1–3.

**On Mac:**
1. Open **Terminal** (press Cmd+Space, type `Terminal`, Enter).
2. Type: `python3 --version`
3. If you see `Python 3.x`, you're good. If not, install from
   **https://www.python.org/downloads/** and try again.

---

## PART 3 — Put in your Reddit key (one time)

1. Open the folder `research/tools` on your computer (where this file is).
2. Find the file **`credentials.example.txt`**.
3. **Make a copy** of it and **rename the copy** to exactly: `credentials.txt`
4. Open `credentials.txt` in any text editor (Notepad on Windows, TextEdit on
   Mac). Replace the placeholder text with your two codes from Part 1:
   ```
   client_id=Ab3xYz...           <- your short code
   client_secret=longer-secret    <- your longer secret
   user_agent=halo-research by u/your_reddit_username
   ```
5. **Save** the file. Done — you never touch this again.

> The `credentials.txt` file stays only on your computer and is set to never be
> uploaded anywhere.

---

## PART 4 — Run it (each time you want fresh data)

1. Open the black command window again (`cmd` on Windows / `Terminal` on Mac).
2. Go into the tools folder. Type `cd ` (with a space), then drag the
   `research/tools` folder from your file explorer into the window and press
   Enter. (This points the window at the right folder.)
3. Copy-paste **one** of these lines and press Enter:

   **Best high-quality threads from the last month:**
   ```
   python halo_reddit_coder.py --listing top --time month --limit 100 --with-comments
   ```
   (On Mac, type `python3` instead of `python`.)

   **Newest posts right now:**
   ```
   python halo_reddit_coder.py --listing new --limit 100 --with-comments
   ```

4. Wait a minute. When it finishes it prints something like:
   `Coded 100 threads ... Rows appended to ../instruments/`
   That means it worked. 🎉

5. **Do this once or twice a day**, not more. The script will politely refuse
   if you try again within 6 hours — that's on purpose (we don't hammer Reddit).

---

## PART 5 — Look at your results

1. Open the `research/instruments` folder.
2. Open these files in Excel / Google Sheets / Numbers:
   - `pain-coding-sheet.csv` — what people need & what frustrates them
   - `trust-coding-sheet.csv` — where trust breaks
   - `language-tone-log.csv` — how Barodians write
3. Each row is one Reddit thread, labelled R001, R002… with **codes only**
   (no names, no numbers). The legend for the codes is at the bottom of each
   file and in `../reddit-research-plan.md`.

---

## PART 6 — Turn it into Halo questionnaire answers

Open `../reddit-workflow.md` and read section **§6**. In short:
- Count which "pain code" shows up most → that's Vadodara's biggest problem.
- See whether people give real recommendations ("I used them") or just drop
  phone numbers → tells you how much the Halo Score is needed.
- Match the top problems to the draft questions in `../deep-dive.md` §3.

---

## If something goes wrong

- **"missing credentials"** → your `credentials.txt` isn't named exactly right,
  or the two codes aren't pasted in. Redo Part 3.
- **"python is not recognized"** → Python isn't installed / not on PATH. Redo
  Part 2 (tick "Add Python to PATH").
- **"Rate limited (429)"** → Reddit asked you to slow down. Just wait a few
  hours and run again. Never try to get around this.
- **"Last run was X h ago"** → you're running too soon. Wait until 6h have
  passed.

## Honest note
The data is the **real** Reddit conversations. The auto-labelling is a smart
first guess, not perfect. If you have time, open a few threads yourself and
check that the codes look right — and that's it. No money, no rule-breaking,
just the answers you wanted.
