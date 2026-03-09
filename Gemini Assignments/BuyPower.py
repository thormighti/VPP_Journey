#When to buy power in the right hour


# The function calculate_profit needs to answer one question: "Is this trade worth it?"

# Cost to Buy: amount_kwh * buy_price

# Usable Energy: amount_kwh * efficiency (This is what you actually have available to sell later).

# Revenue from Sale: usable_energy * sell_price

# Net Profit: Revenue - Cost
class Battery:
    
    def __init__(self,  capacity_kwh:float, current_soc:float, efficiency = 0.85):
        self.capacity_kwh = capacity_kwh
        self.current_soc = current_soc
        self.efficiency = efficiency
    
    def calculate_profit(self, buy_price, sell_price):
        buy_wh = buy_price/1000.0
        sell_kwh = sell_price/1000.0
        energy_to_buy = self.capacity_kwh * (1 - self.current_soc) 
        cost = energy_to_buy * buy_wh

        #sell the energy and loss some efficiency.
        energy_to_sell = self.capacity_kwh * self.efficiency
        sell = energy_to_sell * sell_kwh
        profit = sell- cost
        return profit

# Hourly prices for March 8, 2026 (EPEX SPOT BE)
# Prices in Euro per Megawatt-hour (€/MWh)
prices_mwh = [
    127.38, 122.48, 120.06, 117.43, 116.00, 116.70, 121.13, 113.20, 
    113.72, 105.09, 75.00, 21.67, 10.21, 0.02, 6.58, 51.78, 
    92.92, 158.70, 185.23, 154.05, 141.50, 128.55, 123.86, 119.55
]
battery1 = Battery(10.0, 0.2)
highest_price = max(prices_mwh)
lowest_price = min(prices_mwh) 
# if (battery1.current_soc >0.6 and battery1.current_soc <= 0.9):
profit1 = battery1.calculate_profit(lowest_price,highest_price)
print(f"The profit made was {profit1}")




