import os
import webbrowser
from pathlib import Path

HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Noob Alert!</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            overflow: hidden;
        }
        .container {
            text-align: center;
            animation: fadeIn 0.5s ease-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: scale(0.8); }
            to { opacity: 1; transform: scale(1); }
        }
        .noob-text {
            font-size: 5rem;
            font-weight: 900;
            background: linear-gradient(45deg, #ff6b6b, #feca57, #48dbfb, #ff9ff3);
            background-size: 300% 300%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: gradient 3s ease infinite;
            text-shadow: 0 0 30px rgba(255, 107, 107, 0.5);
            filter: drop-shadow(0 0 20px rgba(254, 202, 87, 0.5));
        }
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .subtitle {
            font-size: 1.5rem;
            color: #feca57;
            margin-top: 20px;
            opacity: 0.9;
        }
        .emoji {
            font-size: 8rem;
            animation: bounce 1s ease infinite;
        }
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-20px); }
        }
        .stars {
            position: fixed;
            width: 100%;
            height: 100%;
            top: 0;
            left: 0;
            pointer-events: none;
            overflow: hidden;
        }
        .star {
            position: absolute;
            width: 4px;
            height: 4px;
            background: white;
            border-radius: 50%;
            animation: twinkle 2s ease-in-out infinite;
        }
        @keyframes twinkle {
            0%, 100% { opacity: 0.3; }
            50% { opacity: 1; }
        }
        .btn {
            margin-top: 40px;
            padding: 15px 40px;
            font-size: 1.2rem;
            background: linear-gradient(45deg, #ff6b6b, #ee5a24);
            border: none;
            border-radius: 50px;
            color: white;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 10px 30px rgba(255, 107, 107, 0.4);
        }
        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 15px 40px rgba(255, 107, 107, 0.6);
        }
    </style>
</head>
<body>
    <div class="stars" id="stars"></div>
    <div class="container">
        <div class="emoji">&#128540;</div>
        <div class="noob-text">YOU ARE A NOOB!</div>
        <div class="subtitle">There is no escape from this truth</div>
        <button class="btn" onclick="alert('Still a noob!')">Try Again</button>
    </div>
    <script>
        const starsContainer = document.getElementById('stars');
        for (let i = 0; i < 100; i++) {
            const star = document.createElement('div');
            star.className = 'star';
            star.style.left = Math.random() * 100 + '%';
            star.style.top = Math.random() * 100 + '%';
            star.style.animationDelay = Math.random() * 2 + 's';
            starsContainer.appendChild(star);
        }
    </script>
</body>
</html>
"""


def main():
    html_path = Path(__file__).parent / "noob_alert.html"
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(HTML_CONTENT)
    
    webbrowser.open(f'file://{html_path.absolute()}')


if __name__ == '__main__':
    main()
