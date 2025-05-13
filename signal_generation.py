# strategy_engine.py  
class StrategyEngine:  
    def detect_market_regime(self, data):  
        adx = data["adx"]  # From TA-lib  
        ema = data["ema20"]  
        price = data["last_price"]  
        return "BULLISH" if (adx > 25 and price > ema) else "RANGE"  

    def generate_signal(self, symbol):  
        oi_data = DataFetcher().get_oi_data(symbol)  
        regime = self.detect_market_regime(oi_data)  
        if regime == "BULLISH":  
            return {  
                "strategy": "BUY CE",  
                "strike": oi_data["max_ce_oi_strike"],  
                "reason": f"OI buildup: +{oi_data['ce_oi_change']}%"  
            }  