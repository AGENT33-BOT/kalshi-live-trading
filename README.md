# kalshi-live-trading
Autonomous prediction market trading on Kalshi using WebSocket for live data.

## Strategy Update (April 2026)

### WINNING Categories (Use These)
- NBA Game Winner (NBAGAME) - Simple, 60%+ win rate
- ATP Tennis Match Winner (ATPMATCH) - Simple, 55%+ win rate
- Colombia Soccer (DIMAYOR) - Good results

### LOSING Categories (AVOID)
- NHL player props (goals, points, shots) - 85% loss rate
- Multi-game parlays - Too complex
- Crypto price markets (BTC/ETH) - All lost
- WTA Tennis - Bad results
- Player mentions/props

## Updated Files

| File | Purpose |
|------|---------|
| `kalshi-websocket-live.py` | Test WebSocket |
| `kalshi-live-bot-strategy.py` | Strategy bot |
| `analyze_kalshi.py` | P&L analyzer |

## Commands

```bash
# Test WebSocket
python kalshi-websocket-live.py

# Run strategy bot
python kalshi-live-bot-strategy.py

# Check positions
kalshi-cli --prod portfolio balance
```

## Strategy Rules
1. Only bet NBAGAME or ATPMATCH (simple winners)
2. NO player props (NHLGOAL, NHLPTS, etc.)
3. NO multi-game parlays
4. NO crypto markets
5. Research first, then bet

## License
MIT