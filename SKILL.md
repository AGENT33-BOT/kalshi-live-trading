# SKILL: kalshi-live-trading v2.0

Automated prediction market trading on Kalshi - **IN-PLAY ONLY**

## ⚠️ KEY CHANGE v2.0

**ONLY TRADE AFTER GAMES START!**

Pre-game orders can't fill due to no liquidity. Only bet when:
- Game has started (live trading active)
- You can see real bids/asks

## Operating Procedure

### DAILY WORKFLOW

1. **CHECK BALANCE FIRST**
   ```bash
   kalshi-cli --prod portfolio balance
   ```

2. **WAIT FOR GAMES TO START**
   - Use WebSocket to monitor live markets
   - Only place orders when bid/ask > 0

3. **IN-PLAY TRADING RULES**
   - Wait 5-10 minutes into game for odds to stabilize
   - Bet on clear game momentum
   - Quick exit - don't hold overnight

### WINNING CATEGORIES
| Category | Win Rate | Notes |
|----------|---------|-------|
| NBAGAME (NBA winner) | 60%+ | Simple game outcome |
| ATPMATCH (ATP tennis) | 55%+ | Match winner only |

### LOSING CATEGORIES (AVOID)
| Category | Notes |
|----------|-------|
| NHL props | No liquidity |
| Pre-game orders | Can't fill |
| Crypto markets | All lost |

## Position Sizing (v2.0)

- **MAX 20%** of available balance per bet
- **MAX 5 bets** per day
- **STOP** when balance hits $20

## Commands

```bash
# Check balance
kalshi-cli --prod portfolio balance

# Check live markets (WebSocket)
python kalshi-websocket-live.py

# Check settlements
kalshi-cli --prod portfolio settlements --limit 20
```

## CRON JOBS
- **Every 30 min:** Check for in-play opportunities
- **Every 1 hour:** P&L report

---

**Remember:** No liquidity pre-game = no fills. Wait for live!
