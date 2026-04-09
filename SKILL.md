# SKILL: kalshi-live-trading v2.1

Automated prediction market trading on Kalshi - **IN-PLAY ONLY** (NBA + ATP)

## Strategy Config: KALSHI_LIVE_NBA_ATP_V2

### Universe
- **Sports:** NBA, ATP only
- **Mode:** LIVE only (in-play) ✅
- **No pre-game** - orders can't fill due to zero liquidity

---

## Risk Management

| Parameter | Value |
|-----------|-------|
| Hard stop balance | $20 |
| Daily max loss | $35 |
| Max trades/day | 5 |
| Max position % | 10-12% |
| Reserve cash | 20% |
| Max concurrent markets | 2 |

---

## Entry Rules

| Parameter | Value |
|-----------|-------|
| Price range | 20c - 70c |
| Min top of book | 25 contracts |
| Min total depth | 75 contracts |
| Max spread | 4c |
| Max queue ahead | 100 contracts |
| Stale book timeout | 1500ms |

**Required Filters:**
- ✅ Live market only
- ✅ NBA or ATP only
- ✅ Balance above floor
- ✅ Book not stale
- ✅ Spread not too wide
- ✅ Depth sufficient
- ✅ Price in range
- ✅ No existing position in market

---

## Position Sizing

| Sport | Base % |
|-------|--------|
| NBA | 6% |
| ATP | 5% |

**Edge Multiplier:**
- <10c: 0.75x
- 10-14c: 1.0x
- >14c: 1.2x

**Liquidity Multiplier:**
- Thin: 0.6x
- Normal: 1.0x
- Strong: 1.15x

---

## Exit Rules

### Take Profit (Scale Out)
| Gain (cents) | Exit % |
|--------------|--------|
| +6c | 40% |
| +10c | 35% |
| +14c | 25% |

### Time Stop
| Sport | Seconds |
|-------|---------|
| NBA | 120 |
| ATP | 90 |

### Stop Loss
| Type | NBA | ATP |
|------|-----|-----|
| Soft | -6c | -7c |
| Hard | -10c | -12c |

---

## Safety Rules

- **Order group:** KALSHI_LIVE_NBA_ATP_V2_MAIN
- **Contracts limit:** 150 per 15 seconds
- **If exceeded:** Cancel all + block new orders

### Cooldowns
| After | Cooldown |
|-------|----------|
| Loss | 10 min (per market) |
| Win | 3 min (per market) |
| 2-loss streak | 20 min (global) |

---

## Operating Procedure

### Daily Workflow

1. **Check Balance**
   ```bash
   kalshi-cli --prod portfolio balance
   ```

2. **Wait for LIVE games**
   - Use WebSocket to monitor live NBA/ATP markets
   - Only place orders when bid/ask > 0 and game is live

3. **In-Play Trading**
   - Wait 5-10 min into game for odds to stabilize
   - Look for 20-70c range (underdog value)
   - Quick exits - don't hold overnight

4. **Scale out at TP levels**
   - Exit 40% at +6c
   - Exit 35% at +10c  
   - Exit 25% at +14c
   - Hard stop at -10c (NBA) / -12c (ATP)

### Commands

```bash
# Check balance
kalshi-cli --prod portfolio balance

# Check live markets (WebSocket)
python kalshi-websocket-live.py

# Check settlements
kalshi-cli --prod portfolio settlements --limit 20
```

---

## CRON JOBS (Recommended)

- **Every 30 min:** Check for in-play opportunities
- **Every 1 hour:** P&L report

---

**REMEMBER:** No liquidity pre-game = no fills. Wait for live games!