# SKILL: kalshi-live-trading

Autonomous prediction market trading on Kalshi. Trade sports, politics, and events with real money.

## Trigger Phrases
- "trade on kalshi"
- "kalshi trading"
- "prediction markets"
- "start kalshi bot"

## What This Skill Does

1. **Start Autonomous Bot** - Scans for value plays (30-70¢) every 5 minutes
2. **Production Trading** - Uses real money on Kalshi
3. **Telegram Alerts** - Notifies you when trades are placed
4. **Dashboard** - Monitor positions and trades

## Setup Required

### Install kalshi-cli
```powershell
go install github.com/6missedcalls/kalshi-cli/cmd/kalshi-cli@latest
```

### Login
```powershell
# Demo mode
kalshi-cli auth login --api-key-id "YOUR_KEY" --private-key-file "path\to\key.pem"

# Production (real money)
kalshi-cli auth login --api-key-id "YOUR_KEY" --private-key-file "path\to\key.pem" --prod
```

## Commands

### Check Balance
```powershell
kalshi-cli --prod portfolio balance
```

### List Markets
```powershell
kalshi-cli --prod markets list --status open --limit 20
```

### Place Order
```powershell
kalshi-cli --prod orders create --market TICKER --side yes --qty 5 --price 50
```

## Running the Bot

Save as `kalshi-prod-bot.ps1` and run:
```powershell
.\kalshi-prod-bot.ps1
```

The bot:
- Scans every 5 minutes
- buys 30-70¢ contracts (value plays)
- sends Telegram alerts
- runs continuously

## Cron Jobs

- Check bot status every 30 minutes
- Monitor for new live sports markets

## Files
- `kalshi-prod-bot.ps1` - Main trading bot
- `kalshi-dashboard.ps1` - Monitoring dashboard
