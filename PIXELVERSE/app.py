from flask import Flask, render_template
import sqlite3
from datetime import date

app = Flask(__name__)

DATABASE = "database.db"
# =========================
# PLAYER REWARD SYSTEM
# =========================

def give_reward(xp_earned=50, coins_earned=25, won=False):

    conn = get_db()

    player = conn.execute(
        "SELECT * FROM player WHERE id = 1"
    ).fetchone()

    if player is None:
        conn.close()
        return

    games_played = player["games_played"] + 1
    games_won = player["games_won"]

    if won:
        games_won += 1

    new_xp = player["xp"] + xp_earned
    new_coins = player["coins"] + coins_earned

    # Every 1000 XP = 1 level
    new_level = (new_xp // 1000) + 1

    conn.execute("""
        UPDATE player
        SET
            coins = ?,
            xp = ?,
            games_played = ?,
            games_won = ?,
            level = ?
        WHERE id = 1
    """, (
        new_coins,
        new_xp,
        games_played,
        games_won,
        new_level
    ))

    conn.commit()
    conn.close()


# =========================
# DATABASE CONNECTION
# =========================

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# =========================
# CREATE PLAYER TABLE
# =========================

def create_database():

    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS player (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            coins INTEGER DEFAULT 0,
            xp INTEGER DEFAULT 0,
            games_played INTEGER DEFAULT 0,
            games_won INTEGER DEFAULT 0,
            streak INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1,
            last_login TEXT
        )
    """)

    player = conn.execute(
        "SELECT * FROM player WHERE id = 1"
    ).fetchone()

    if player is None:

        conn.execute("""
            INSERT INTO player
            (
                id,
                name,
                coins,
                xp,
                games_played,
                games_won,
                streak,
                level,
                last_login
            )
            VALUES
            (1, 'Pixel Warrior', 100, 0, 0, 0, 1, 1, ?)
        """, (str(date.today()),))

    conn.commit()
    conn.close()


# =========================
# HOME / DASHBOARD
# =========================

@app.route("/")
def home():

    conn = get_db()

    player = conn.execute(
        "SELECT * FROM player WHERE id = 1"
    ).fetchone()

    conn.close()

    return render_template(
        "index.html",
        player=player
    )


# =========================
# TIC TAC TOE
# =========================

@app.route("/tic-tac-toe")
def tic_tac_toe():

    return render_template(
        "tic_tac_toe.html"
    )


# =========================
# MEMORY MASTER
# =========================

@app.route("/memory-master")
def memory_master():

    return render_template(
        "memory_master.html"
    )


# =========================
# SNAKE RUSH
# =========================

@app.route("/snake-rush")
def snake_rush():

    return render_template(
        "snake_rush.html"
    )


# =========================
# SPACE BLAST
# =========================

@app.route("/space-blast")
def space_blast():

    return render_template(
        "space_blast.html"
    )


# =========================
# RUN APP
# =========================

if __name__ == "__main__":

    create_database()

    app.run(debug=True)