# waffles-bot

Waffles is a Telegram bot that facilitates group discussions by asking questions at a configured frequency. Users can add this bot to their Telegram groups, and it will initiate discussions by posting questions for group members to respond to.

## Usage

1. Copy the `.env.sample` file to `.env` and fill in the configuration values. This file will hold sensitive information such as the Telegram bot token and other settings.

2. Build the service using Docker Compose:
   ```bash
   docker-compose build
   ```

3. Run the service in either development or production environment:
   - For development:
     ```bash
     docker-compose up -d waffles-bot-dev
     ```
   - For production:
     ```bash
     docker-compose up -d waffles-bot-prod
     ```
