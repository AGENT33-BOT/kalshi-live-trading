# KALSHI WEBSOCKET - LIVE MARKET DATA + AUTO BET
import asyncio
import base64
import json
import time
import websockets
import requests
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding

KEY_ID = "84889d41-b383-4b6a-b8da-f51c0983ae90"
PRIVATE_KEY_PATH = "C:\\Users\\digim\\.kalshi\\private_key.pem"
WS_URL = "wss://api.elections.kalshi.com/trade-api/ws/v2"

# Telegram
TG_TOKEN = "8249656817:AAFAI3oulkDWJZHJ7STSYlDfK-_UJCPo-7U"
TG_CHAT = "5804173449"

def load_private_key(path):
    with open(path, 'rb') as f:
        return serialization.load_pem_private_key(f.read(), password=None)

def sign_message(private_key, text):
    message = text.encode('utf-8')
    signature = private_key.sign(
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.DIGEST_LENGTH),
        hashes.SHA256()
    )
    return base64.b64encode(signature).decode('utf-8')

def telegram(msg):
    try:
        requests.post(f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage",
                    json={"chat_id": TG_CHAT, "text": msg}, timeout=10)
    except Exception as e:
        print(f"Telegram error: {e}")

async def main():
    print("Loading key...")
    private_key = load_private_key(PRIVATE_KEY_PATH)
    
    timestamp = str(int(time.time() * 1000))
    msg_string = timestamp + "GET" + "/trade-api/ws/v2"
    signature = sign_message(private_key, msg_string)
    
    headers = {
        "KALSHI-ACCESS-KEY": KEY_ID,
        "KALSHI-ACCESS-SIGNATURE": signature,
        "KALSHI-ACCESS-TIMESTAMP": timestamp
    }
    
    print(f"Connecting to {WS_URL}...")
    
    ws = await websockets.connect(WS_URL, extra_headers=headers)
    
    print("Connected! Subscribing...")
    
    sub_msg = {"id": 1, "cmd": "subscribe", "params": {"channels": ["ticker"]}}
    await ws.send(json.dumps(sub_msg))
    
    print("\n=== RESEARCH: Finding NBA/ATP opportunities ===")
    
    plays = []
    count = 0
    async for msg in ws:
        data = json.loads(msg)
        t = data.get("type")
        
        if t == "subscribed":
            print("Subscribed to ticker channel")
        
        elif t == "ticker":
            d = data.get("msg", {})
            ticker = d.get("market_ticker", "")
            ask = float(d.get("yes_ask_dollars", 0))
            bid = float(d.get("yes_bid_dollars", 0))
            
            if ask and ask > 0 and ask < 1:
                # Filter for NBA GAME and ATP MATCH (our winning categories)
                if "NBAGAME-26APR" in ticker or "ATPMATCH-26APR" in ticker:
                    # Value play: between 15c and 80c
                    if ask >= 0.15 and ask <= 0.80:
                        plays.append((ticker, round(ask*100)))
                        print(f"[FOUND] {ticker}: {int(ask*100)}c")
                    count += 1
                    
                    if count >= 50:
                        break
        
        elif t == "error":
            print(f"Error: {data}")
    
    # Report findings
    if plays:
        msg = "RESEARCH: Found opportunities!\n\n"
        for p in plays[:8]:
            msg += f"{p[0]}: {p[1]}c\n"
        if len(plays) > 8:
            msg += f"... +{len(plays)-8} more"
        telegram(msg)
    else:
        telegram("RESEARCH: No good NBA/ATP opportunities (15-80c) right now")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStopped")