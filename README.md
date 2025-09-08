# Ai_Bot

Welcome to **Ai_Bot**!  
This repository contains a Telegram bot that generates images from text prompts using the FusionBrain Text2Image API.

---

## Features

- **Text-to-Image Generation:** Send a `/gen` command with a prompt, and the bot will reply with an AI-generated image.
- **FusionBrain API Integration:** Uses FusionBrain's API to generate and retrieve images.
- **Telegram Bot:** Easily deployable for Telegram, responds to user commands.

---

## How It Works

- The bot listens for the `/gen` command in Telegram chats.
- When invoked, it extracts the prompt, calls the FusionBrain API (via `Text2ImageAPI` in `logic.py`), and sends the generated image back.
- Images are processed and saved locally before sending.

### Main Files

- `main.py`: Bot entry point. Handles Telegram commands and message routing.
- `logic.py`: Contains the `Text2ImageAPI` class which manages API requests, image generation, polling, and decoding from base64.
- `config.py`: Stores configuration variables (bot token, API key, secret).

---

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Muhro5142/Ai_Bot.git
   cd Ai_Bot
   ```

2. **Install requirements:**
   - Python 3.x required.
   - Install dependencies (e.g., `telebot`, `requests`, `Pillow`):
     ```bash
     pip install pyTelegramBotAPI requests pillow
     ```

3. **Configure your credentials:**
   - Edit `config.py` and insert your Telegram bot token, FusionBrain API key, and secret.

4. **Run the bot:**
   ```bash
   python main.py
   ```

---

## Usage

- In Telegram, start a chat with your bot.
- Send `/gen <description>` (e.g., `/gen a sunset over mountains`).
- The bot will reply with the generated image.

---

## Contributing

Contributions are welcome.  
Feel free to fork, open issues, or submit pull requests for new features or bug fixes.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Author

Developed by [Muhro5142](https://github.com/Muhro5142)

---

**Enjoy generating AI art!**
