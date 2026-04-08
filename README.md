# kalshi-live-trading
Autonomous prediction market trading on Kalshi with WebSocket live data

## What This Does
- Real-time market data via WebSocket
- Auto-scan for value plays (10-90c)
- Places trades automatically
- Telegram alerts

## Setup

```powershell
# 1. Install dependencies
pip install websockets cryptography

# 2. Install kalshi-cli
go install github.com/6missedcalls/kalshi-cli/cmd/kalshi-cli@latest

# 3. Login to Kalshi
kalshi-cli auth login --api-key-id "YOUR_KEY" --private-key-file "key.pem" --prod

# 4. Authenticate gh (for repo creation)
gh auth login
```

## Files
- `kalshi-websocket-live.py` - WebSocket test script
- `kalshi-live-bot-v2.py` - Trading bot
- `kalshi-pnl-report.py` - P&L report cron

## Usage

### Test WebSocket
```bash
python kalshi-websocket-live.py
```

### Run Bot
```bash
python kalshi-live-bot-v2.py
```

### Check Positions
```bash
kalshi-cli --prod portfolio balance
kalshi-cli --prod portfolio positions
```

## API Keys
Get your API key from https://kalshi.com/settings/api

## Telegram Alerts
Edit the TG_TOKEN and TG_CHAT in the scripts to enable alerts.

## License
MIT