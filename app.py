from flask import Flask, render_template, request

app = Flask(__name__)

mood_data = {
    "happy": {
        "msg": "You're glowing today, and the world is brighter because of your smile. Keep radiating that sunshine — you're a beautiful reminder that joy is contagious. 🌞✨",
        "tip": "Keep spreading your joy. Try this upbeat playlist:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"
    },
    "sad": {
        "msg": "It’s okay to feel sad. Your tears are not a sign of weakness, but a sign that you care deeply. Let the storm pass — your sky will clear again. 🌧️💙",
        "tip": "Take a deep breath and listen to this gentle hug in musical form:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro"
    },
    "stressed": {
        "msg": "You’ve been strong for so long. It’s okay to pause. Breathe. Re-center. You’re doing your best, and that’s more than enough. One step at a time. 🌿💪",
        "tip": "Let this playlist soothe your thoughts and lighten your load:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0"
    },
    "tired": {
        "msg": "Rest isn't a reward, it’s a necessity. Close your eyes, release the weight you’ve been carrying. You deserve deep rest and gentle care. 😴🛌",
        "tip": "Unwind with this calming soundscape:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DX3Ogo9pFvBkY"
    },
    "lonely": {
        "msg": "You may feel alone, but the universe is quietly wrapping you in invisible love. You are worthy, loved, and never truly alone. 💜🌌",
        "tip": "Let this playlist remind you that you're surrounded by love:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DX3PIPIT6lEg5"
    },
    "grateful": {
        "msg": "Gratitude turns what we have into enough. Savor the beauty in each breath, each moment. Life is a collection of small wonders. 🌻✨",
        "tip": "Celebrate the now with this peaceful playlist:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DX6GwdWRQMQpq"
    },
    "anxious": {
        "msg": "Anxiety is loud, but your breath is louder. Inhale peace, exhale doubt. You are safe, and this moment will pass. 🌬️🕊️",
        "tip": "Ease your mind with this calming playlist:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DX4sWSpwq3LiO"
    },
    "excited": {
        "msg": "Your energy is electric! Let it flow freely, chase those dreams, and light up every room you walk into. You're unstoppable. ⚡🎉",
        "tip": "Dance it out with this happy burst of rhythm:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DX1tW4VlEfDSS"
    },
    "hopeless": {
        "msg": "Even the darkest nights give way to sunrise. There is hope woven into tomorrow, waiting just beyond the fog. Hold on. ☀️🫶",
        "tip": "Let these melodies carry your heart toward light:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DWVIiR5qh2MFm"
    },
    "peaceful": {
        "msg": "Stillness is a gift. Let the world slow down and simply be. In this moment, all is well, and so are you. 🕊️🌸",
        "tip": "Drift into peace with every gentle note:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DX3PFzdbtx1Us"
    },
    "motivated": {
        "msg": "You're fired up, and the universe can feel it. Let your passion blaze trails. You’ve got this. Keep going. 🚀💥",
        "tip": "Fuel your fire with this fierce playlist:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DX76Wlfdnj7AP"
    },
    "hopeful": {
        "msg": "The best chapters of your story are still being written. Keep your chin up, your heart open — magic is near. 🌈📖",
        "tip": "Nourish your heart with positivity:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
    },
    "angry": {
        "msg": "Anger is valid. Let it pass like a storm — loud, powerful, but always temporary. Choose to release, not suppress. You’re in control. 🔥🌧️",
        "tip": "Here's a playlist to help you release it all:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DWZ6KLSZ9uD1x"
    },
    "insecure": {
        "msg": "You are enough. Not when you achieve more. Not when you fix yourself. But right now, as you are. Beautiful and whole. 💕🪞",
        "tip": "Let these sounds build you back up:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DWU0ScTcjJBdj"
    },
    "bored": {
        "msg": "Boredom is your imagination knocking. Explore, create, or wander freely — the world is full of possibilities. 🎈✨",
        "tip": "Run wild through new sounds and rhythms:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DWZIQpJDq3p8w"
    },
    "creative": {
        "msg": "The spark is alive in you. Paint, write, build — let your ideas break free and dance into the world. 🎨💡",
        "tip": "Grab your tools and vibe with this inspiring mix:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DXdxtfF6gmoYI"
    },
    "heartbroken": {
        "msg": "Heartbreak means you dared to love deeply. The ache is real, but so is your capacity to heal. You will love again, and harder. ❤️‍🩹",
        "tip": "Let these melodies gently mend the pieces:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DXdwmD5Q7Gxah"
    },
        "calm": {
        "msg": "Breathe in peace, breathe out tension. In this stillness, you find your strength. Serenity suits you. 🌊🧘",
        "tip": "Float through these mellow tunes:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7"
    },
    "inspired": {
        "msg": "The world better watch out — you’re brimming with brilliance. Let your vision unfold into reality. 🚀📝",
        "tip": "Fuel your inspiration with these creative sounds:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DWXRqgorJj26U"
    },
    "relaxed": {
        "msg": "You’ve earned this exhale. Let everything soften — your shoulders, your breath, your mind. All is well. 🌙💆",
        "tip": "Drift deeper with these chill vibes:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DWU0ScTcjJBdj"
    },
    "romantic": {
        "msg": "Ah, the heart flutters and the world seems to glow. Love is in the air, and you're dancing with its rhythm. 💖🌹",
        "tip": "Sway to the melodies of love:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DX50QitC6Oqtn"
    },
    "energetic": {
        "msg": "You’re buzzing like a live wire! Let that momentum lead the way — you’re a force of nature. ⚡💃",
        "tip": "Match your pace with these power beats:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DX1g0iEXLFycr"
    },
    "melancholy": {
        "msg": "There's beauty in the blues. You feel deeply, and that's a strength, not a burden. Let it wash over you gently. 🌧️🎭",
        "tip": "Find gentle resonance in these sounds:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DX3YSRoSdA634"
    },

    "proud": {
        "msg": "Look at how far you’ve come. Every little win, every lesson learned — you earned this pride. Own it. 👏🏽🎓",
        "tip": "Celebrate yourself with this empowering playlist:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DX5wDmLW735Yd"
    },
    "confused": {
        "msg": "Confusion means you're growing. Answers will come. Be patient with your process — you're finding your way. ⏳🧭",
        "tip": "Clear the fog with clarity in melodies:",
        "playlist": "https://open.spotify.com/playlist/37i9dQZF1DWYmmr74INQlb"
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    context = None
    if request.method == "POST":
        mood = request.form["mood"]
        context = mood_data.get(mood)
    return render_template("index.html", context=context)

if __name__ == "__main__":
    app.run(debug=True)
