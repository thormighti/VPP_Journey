#When to buy power in the right hour

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
    

class ArbitrageTrader:
    """
    Represents the "trade layer" that makes financial decisions using a Battery asset.
    This class separates the business logic of trading from the physical simulation of the battery.
    """
    def __init__(self, battery: Battery):
        self.battery = battery

    def execute_arbitrage_cycle(self, buy_price_mwh: float, sell_price_mwh: float, amount_kwh: float) -> float:
        """
        Simulates a full arbitrage cycle: buy, charge, discharge, sell.
        Returns the net profit in euros.
        """
        # --- Financial Layer: Convert prices for consistency ---
        buy_price_kwh = buy_price_mwh / 1000.0
        sell_price_kwh = sell_price_mwh / 1000.0

        # --- Physical Layer Interaction ---
        # 1. Charge the battery with the purchased energy
        amount_charged_kwh = self.battery.charge(amount_kwh)

        # 2. Discharge the battery to sell the energy, accounting for efficiency loss
        amount_delivered_kwh = self.battery.discharge(amount_charged_kwh)

        # --- Financial Layer: Calculate Profit ---
        cost_to_buy = amount_charged_kwh * buy_price_kwh
        revenue_from_sale = amount_delivered_kwh * sell_price_kwh
        net_profit = revenue_from_sale - cost_to_buy
        return net_profit
# Hourly prices for March 8, 2026 (EPEX SPOT BE)
# Prices in Euro per Megawatt-hour (€/MWh)
prices_mwh = [
    127.38, 122.48, 120.06, 117.43, 116.00, 116.70, 121.13, 113.20, 
    113.72, 105.09, 75.00, 21.67, 10.21, 0.02, 6.58, 51.78, 
    92.92, 158.70, 185.23, 154.05, 141.50, 128.55, 123.86, 119.55
]

# --- Simulation Setup ---
# 1. Create the physical asset
battery_asset = Battery(capacity_kwh=10.0, current_soc=0.2)

# 2. Create the trading agent and link it to the asset
trader = ArbitrageTrader(battery=battery_asset)

# 3. Identify buy/sell opportunities from market data
sell_price = max(prices_mwh)
buy_price = min(prices_mwh) 

# 4. Execute the trade and calculate profit
profit = trader.execute_arbitrage_cycle(buy_price, sell_price, amount_kwh=5.0)
print(f"The profit made was {profit:.2f} Euros")
