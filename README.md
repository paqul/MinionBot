# Discord RPG Dice Bot aka **MinionBot**

This Discord bot is designed to facilitate dice rolling for various tabletop role-playing games (RPGs). It supports a wide range of dice types and special rolling mechanics for games like Dungeons & Dragons, Call of Cthulhu, and Mork Borg.
Currently it returns messages only in Polish language.

## Features

- Standard dice rolling (d2, d3, d4, d5, d6, d8, d10, d12, d16, d20, d24, d30, d66, d100, d1000)
- Rolls with modifiers (e.g., 1d20+5)
- Advantage/Disadvantage rolls for D&D 5e
- Bonus/Penalty dice for Call of Cthulhu
- Special d66 roll for Mork Borg
- COP RPG rolls (gl command with optional modifiers)
- D&D stat block generation
- Auto-test functionality
- Dynamic channel whitelist updates via mention command (authorized users [by user id] only Friik, Paqul)

## How to Deploy

1. Clone this repository to your local machine.
2. Install the required dependencies:
pip install discord.py
3. Create a `params.py` file in the root directory and add your Discord bot token:
```python
token = "YOUR_DISCORD_BOT_TOKEN"
```
4. Run the bot manually: 
python main.py
5. (Optional) Setup a service so your bot will automatically start with the machine and restart on crash. For Instructions refer to next section

## Setting Up Auto-Restart with systemd (Linux)

To ensure MinionBot automatically restarts after a reboot, crash, disconnection, or downtime, follow these steps:

1. Copy the `MinionBot.service` file from the `linux_server` folder to `/etc/systemd/system` on your Linux server.
2. Edit the `MinionBot.service` file and update the `User` and `WorkingDirectory` fields to match your setup (e.g., `User=user1`, `WorkingDirectory=/home/user1/MinionBot`).
3. Enable the service by running:
   ```
   sudo systemctl enable MinionBot.service
   ```
4. Start the service with:
   ```
   sudo systemctl start MinionBot.service
   ```
5. **Note:** After setting up systemd, do not manually run `python main.py` as described in the "How to Deploy" section. The systemd service will handle starting the bot.

## Structure Overview

- `bot_config.py`: Sets up the Discord bot and handles message events.
- `responses.py`: Processes user messages and determines appropriate responses by passing to `rolls.py`.
- `rolls.py`: Contains the logic for various dice rolling functions and formatting response messages.
- `roles.py`: Handles role assignments for new members (customizable).

The bot also includes an auto-test feature for admins from the hardcoded user ID list.
Use `@BotName autotest` (or `@BotName autotest summary`) to run dynamic tests and get one summary message.
Use `@BotName autotest legacy` to iterate through test commands on Discord chat like before.

## How to Use

Once the bot is running and added to your Discord server, you can use the following commands:

- Roll dice: XdY (e.g., 1d20, 3d6)
- Roll with modifier: XdY+Z (e.g., 1d20+5)
- Advantage roll (D&D 5e (d20) & Mothership (d100): XdYa (e.g., 1d20a, 1d20a+5)
- Disadvantage roll (D&D 5e (d20) & Mothership (d100): XdYd (e.g., 1d20d, 1d20d+5)
- Bonus die & double bonus die(Call of Cthulhu): XdYp (e.g., 1d100p, 1d100pp)
- Penalty die & double penalty die (Call of Cthulhu): XdYk (e.g., 1d100k, 1d100kk)
- Mork Borg special roll: Xd66 (e.g., 1d66)
- Generate D&D stat block: statystyki_dnd
- Get help: help
- Add channel to whitelist (admin only): @BotName Add_Channel <channel_name> or @BotName Add_Channel #channel
- Run admin autotest summary: @BotName autotest or @BotName autotest summary
- Run admin autotest legacy mode: @BotName autotest legacy
- Stop legacy autotest (admin only): @BotName stop

Replace X with the number of dice, Y with the type of die, and Z with the modifier value.
How It Works
The bot listens for messages in specified channels. When it receives a valid command, it processes the request and returns the result of the dice roll(s). The bot uses regular expressions to parse commands and determine which type of roll to perform.
Key components:

## Customization

You can customize the bot by modifying the following:

Allowed channels in bot_config.py
Role assignments in roles.py
Supported dice types in rolls.py

### Whitelist Admin Users (hardcoded)

Users allowed to add channels from Discord messages are configured in bot_config.py:

ALLOWED_ADMIN_USER_IDS = {
   111111111111111111,
}

Replace the placeholder with real Discord user IDs.

### Dynamic Whitelist Storage

The bot stores whitelist state in:

config/channel_whitelist.json

On first run, the file is created and seeded with values from channels_whitelist.py.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
