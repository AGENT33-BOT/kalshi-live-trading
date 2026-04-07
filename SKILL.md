---
name: kalshi-trading-strategy
description: Automated prediction market trading on Kalshi with research-based strategy. Only bet when markets have liquidity.
metadata:
  version: 2.0.0
  author: Pablo
  updated: 2026-04-07
---

# KALSHI TRADING SKILL - VERSION 2.0

**IMPORTANT: Only bet when market has actual liquidity!**

## Operating Procedure

### DAILY WORKFLOW

1. **CHECK LIQUIDITY FIRST**
   ```bash
   kalshi-cli --prod markets get "MARKET_TICKER"
   ```
   - Must show bid/ask > $0.00 to place bets
   - If $0.00 = no liquidity = don't bet

2. **CHECK BALANCE**
   ```bash
   kalshi-cli --prod portfolio balance
   ```

3. **RESEARCH LIVE MARKETS (with liquidity)**
   - Use WebSocket script: `kalshi-websocket-live.py`
   - Filter for markets with actual prices (not $0.00)

4. **PLACE BETS ONLY WHEN:**
   - Market has bid/ask > $0.00 (liquidity exists)
   - Game is live or starting soon
   - Price is 20-70c range (best value)

### NEW STRATEGY: Wait for Liquidity

**OLD (Lost money):**
- Placed 90+ orders on markets with $0.00
- Orders went through but 0 quantity filled
- Waste of capital

**NEW (Focus on liquidity):**
1. Only bet on markets showing actual trading
2. Test with small orders first to confirm fill
3. Wait for games to START before betting
4. Max 3 bets per day (quality over quantity)

### WINNING CATEGORIES
| Category | Win Rate | Notes |
|----------|---------|-------|
| NBAGAME (NBA winner) | 60%+ | Simple game outcome |
| ATPMATCH (ATP tennis) | 55%+ | Match winner only |

### LOSING CATEGORIES (AVOID)
| Category | Loss Rate | Notes |
|----------|----------|-------|
| NHLGOAL (NHL goals) | 85% | Player props |
| Crypto markets | 100% | All lost |
| Markets with $0.00 liquidity | N/A | Can't fill orders |

### COMMANDS

```bash
# Check balance
kalshi-cli --prod portfolio balance

# Check market liquidity
kalshi-cli --prod markets get "TICKER"

# Check settlements
kalshi-cli --prod portfolio settlements --limit 20

# View orders
kalshi-cli --prod orders list
```

### PLACE ORDER (Only if liquidity exists!)
```bash
kalshi-cli --prod orders create --market "TICKER" --side yes --qty 10 --price XX --yes
```

### FILES
- kalshi-websocket-live.py - Market scanner (checks liquidity)
- kalshi-research-bot.py - Research bot
- SKILL.md - This file

### KEY LESSON
**Liquidity > Odds!** 
- A 30c odds with $0 liquidity = worthless
- A 50c odds with $10k volume = actual tradeable

Wait for live games with real trading volume before betting!