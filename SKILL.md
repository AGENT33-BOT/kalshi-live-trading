# SKILL: kalshi-trading-strategy

Automated prediction market trading on Kalshi with research-based strategy.

## Operating Procedure

### DAILY WORKFLOW

1. **CHECK BALANCE FIRST**
   ```bash
   kalshi-cli --prod portfolio balance
   ```

2. **RESEARCH LIVE MARKETS**
   - Check ESPN for live NBA scores/records
   - Check tennis schedules
   - Only bet on categories with POSITIVE history

3. **FILTER MARKETS (Use WebSocket)**
   - ONLY: NBAGAME, ATPMATCH (simple game winners)
   - AVOID: NHL props, multi-game parlays, crypto, WTA

4. **PLACE BETS (Limit Orders)**
   - Use available balance wisely
   - Target 50-80c odds (value plays)

### WINNING CATEGORIES
| Category | Win Rate | Notes |
|----------|---------|-------|
| NBAGAME (NBA winner) | 60%+ | Simple game outcome |
| ATPMATCH (ATP tennis) | 55%+ | Match winner only |
| DIMAYOR (Colombia soccer) | Good | Won on Boyaca Chico |

### LOSING CATEGORIES (AVOID)
| Category | Loss Rate | Notes |
|----------|----------|-------|
| NHLGOAL (NHL goals) | 85% | Player props |
| NHLPTS, NHLAST | 80%+ | Points/shots |
| Multi-game parlays | 70%+ | Too complex |
| Crypto markets | 100% | All lost |
| WTA Tennis | 60%+ | Bad results |

### COMMANDS

```bash
# Check balance
kalshi-cli --prod portfolio balance

# Check settlements (wins/losses)
kalshi-cli --prod portfolio settlements --limit 50

# View positions
kalshi-cli --prod portfolio positions
```

### PLACE ORDER FORMAT
```bash
kalshi-cli --prod orders create --market "TICKER" --side yes --qty 10 --price XX --yes
```

### EXAMPLE BETTING WORKFLOW
1. Research games on ESPN
2. Find NBAGAME or ATPMATCH markets
3. Check if odds make sense vs real records
4. Place limit order at target price
5. Wait for fill or cancel

## CRON JOBS
- Check balance every 6 hours
- P&L report every 24 hours

## FILES
- analyze_kalshi.py - P&L analyzer
- kalshi-websocket-live.py - Market scanner