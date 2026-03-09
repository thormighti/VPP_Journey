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
    
    def charge(self, amount_kwh):
        #cant charge more than the capacity of the battery
        available_space = self.capacity_kwh * (1 - self.current_soc)
        actual_charge = min(amount_kwh, available_space)
        # if self.current_soc + (amount_kwh / self.capacity_kwh) > 1.0:
        #     raise ValueError("Cannot charge beyond 100% SOC")
        self.current_soc += actual_charge / self.capacity_kwh
        return actual_charge
    
    def discharge(self, amount_kwh):
        #cant discharge more than the current SOC of the battery
        available_energy = self.capacity_kwh * (self.current_soc - 0.2) # we want to keep at least 20% SOC to preserve battery health
        actual_discharge = min(amount_kwh, available_energy)
        energy__delivered = actual_discharge * self.efficiency
        self.current_soc -= actual_discharge / self.capacity_kwh
        return energy__delivered
    
    def calculate_profit(self, buy_price, sell_price, amount_kwh):
        buy_price_kwh = buy_price/1000.0
        sell_price_kwh = sell_price/1000.0
        charged = self.charge(amount_kwh)
        discharged = self.discharge(charged) 
        cost = charged * buy_price_kwh
        sell = discharged * sell_price_kwh
        return sell - cost

      

# Hourly prices for March 8, 2026 (EPEX SPOT BE)
# Prices in Euro per Megawatt-hour (€/MWh)
prices_mwh = [
    127.38, 122.48, 120.06, 117.43, 116.00, 116.70, 121.13, 113.20, 
    113.72, 105.09, 75.00, 21.67, 10.21, 0.02, 6.58, 51.78, 
    92.92, 158.70, 185.23, 154.05, 141.50, 128.55, 123.86, 119.55
]
battery1 = Battery(10.0, 0.2)
# battery1.charge(5.0)  # Charge the battery with 5 kWh
# battery1.discharge(3.0)  # Discharge 3 kWh from the battery
sell_price = max(prices_mwh)
buy_price = min(prices_mwh) 
# if (battery1.current_soc >0.6 and battery1.current_soc <= 0.9):
profit1 = battery1.calculate_profit(buy_price,sell_price, 5.0)
print(f"The profit made was {profit1:.2f} Euros")




