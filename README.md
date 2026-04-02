# kalshi-live-trading
Autonomous prediction market trading on Kalshi using WebSocket for live data.

## Overview
This skill provides real-time prediction market trading on Kalshi. Uses WebSocket for live market prices and automatically scans for value plays (10-90 cent contracts).

## Features
- WebSocket live market data streaming
- Autonomous value play scanning
- Automatic trade execution
- Telegram notifications
- P&L reporting

## Setup

### 1. Install Dependencies
```powershell
pip install websockets cryptography requests
```

### 2. Install kalshi-cli
```powershell
go install github.com/6missedcalls/kalshi-cli/cmd/kalshi-cli@latest
```

### 3. Login to Kalshi
Get your API key from: https://kalshi.com/settings/api
```powershell
kalshi-cli auth login --api-key-id "YOUR_KEY" --private-key-file "key.pem" --prod
```

### 4. GitHub Setup (for pushing to repo)
```powershell
gh auth login
```

## Files

| File | Purpose |
|------|---------|
| `kalshi-websocket-live.py` | Test WebSocket connection, shows live prices |
| `kalshi-live-bot-v2.py` | Main trading bot - scans and places trades |
| `kalshi-pnl-report.py` | P&L report script for cron jobs |

## Usage

### Test WebSocket Connection
```bash
python kalshi-websocket-live.py
```
Shows real-time prices for all markets.

### Run Trading Bot
```bash
python kalshi-live-bot-v2.py
```
The bot continuously:
- Connects to WebSocket
- Subscribes to ticker channel
- Scans for markets priced 10-90 cents
- Places limit orders automatically
- Sends Telegram alerts

### Check Balance
```bash
kalshi-cli --prod portfolio balance
kalshi-cli --prod portfolio positions
kalshi-cli --prod portfolio fills
```

### P&L Report
```bash
python kalshi-pnl-report.py
```

## Configuration
Edit these constants in the scripts:
```python
KEY_ID = "your_api_key_id"
PRIVATE_KEY_PATH = "path\\to\\kalshi-key.pem"
TG_TOKEN = "your_telegram_bot_token"
TG_CHAT = "your_chat_id"
CONTRACTS = 5  # contracts per trade
```

## Cron Jobs
Add to OpenClaw cron:
```json
{
  "name": "kalshi-pnl-report",
  "schedule": "every 24 hours",
  "command": "python kalshi-pnl-report.py"
}
```

## Troubleshooting

### WebSocket 401 Error
- Check your API key is valid
- Ensure private key matches the key_id

### Orders Not Filling
- The market may have no liquidity
- Try different price points
- Check orderbook: `kalshi-cli --prod markets orderbook TICKER`

### CLI Not Found
Ensure Go/bin is in your PATH:
```powershell
$env:PATH += ";$env:USERPROFILE\go\bin"
```

## License
MIT