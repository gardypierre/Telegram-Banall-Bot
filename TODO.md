# TODO Steps for Banall Bot Correction and Token Insertion

## Approved Plan Steps:
1. [ ] Update .gitignore to ignore .env
2. [ ] Create .env with provided TELEGRAM_TOKEN
3. [ ] Create .env.example with placeholders (including APP_ID/HASH)
4. [x] Update requirements.txt: pyrogram to latest, ensure python-dotenv
5. [x] Update bot/config.py to load .env via dotenv
6. [ ] Refactor bot/__init__.py: Fix typos, remove duplicates, add admin checks, update for pyrogram 2.0+ API (get_chat_members, ban_member), improve error handling
7. [x] Update README.md with local dev/run instructions
8. [ ] Test: pip install -r requirements.txt, python -m Banall.bot (user needs to add APP_ID/HASH to .env)

Proceed step-by-step. Missing: User APP_ID/HASH (remind after edits).

