# Discord RPG Dice Bot aka **MinionBot**

This Discord bot is designed to facilitate dice rolling for various tabletop role-playing games (RPGs). It supports a wide range of dice types and special rolling mechanics for games like Dungeons & Dragons, Call of Cthulhu, and Mork Borg.
Currently it returns messages only in Polish language.

## Features

- Standard dice rolling (d2, d3, d4, d5, d6, d8, d10, d12, d16, d20, d24, d30, d66, d100, d1000)
- Rolls with modifiers (e.g., 1d20+5)
- Advantage/Disadvantage rolls for D&D 5e
- Bonus/Penalty dice for Call of Cthulhu
- Special d66 roll for Mork Borg
- D&D stat block generation
- Auto-test functionality

## How to Deploy

1. Clone this repository to your local machine.
2. Install the required dependencies:
pip install discord.py
3. Create a `params.py` file in the root directory and add your Discord bot token:
```python
token = "YOUR_DISCORD_BOT_TOKEN"
```
4. Run the bot: 
python main.py

## Structure Overview

- `bot_config.py`: Sets up the Discord bot and handles message events.
- `responses.py`: Processes user messages and determines appropriate responses by passing to `rolls.py`.
- `rolls.py`: Contains the logic for various dice rolling functions and formatting response messages.
- `roles.py`: Handles role assignments for new members (customizable).

The bot also includes an auto-test feature that can be triggered with the command `@BotName autotest`. This runs through a series of predefined rolls to ensure all functionalities are working correctly.

## How to Use

Once the bot is running and added to your Discord server, you can use the following commands:

- Roll dice: XdY (e.g., 1d20, 3d6)
- Roll with modifier: XdY+Z (e.g., 1d20+5)
- Advantage roll (D&D 5e (d20) & Mothership (d100)): XdYa (e.g., 1d20a, 1d20a+5)
- Disadvantage roll (D&D 5e (d20) & Mothership (d100)): XdYd (e.g., 1d20d, 1d20d+5)
- Bonus die & double bonus die(Call of Cthulhu): XdYp (e.g., 1d100p, 1d100pp)
- Penalty die & double penalty die (Call of Cthulhu): XdYk (e.g., 1d100k, 1d100kk)
- Mork Borg special roll: Xd66 (e.g., 1d66)
- Generate D&D stat block: statystyki_dnd
- Get help: help

Replace X with the number of dice, Y with the type of die, and Z with the modifier value.
How It Works
The bot listens for messages in specified channels. When it receives a valid command, it processes the request and returns the result of the dice roll(s). The bot uses regular expressions to parse commands and determine which type of roll to perform.
Key components:

## Customization

You can customize the bot by modifying the following:

Allowed channels in bot_config.py
Role assignments in roles.py
Supported dice types in rolls.py

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
