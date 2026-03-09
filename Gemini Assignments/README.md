# VPP Battery Arbitrage Simulator

A Python simulation of electricity price arbitrage using a Virtual Power Plant (VPP) battery storage model. Built as part of a structured 12-month energy systems engineering learning journey.

## What It Does

Models a battery storage unit that exploits electricity price differences across a 24-hour period. The system charges (buys) when prices are low and discharges (sells) when prices are high — a strategy known as energy arbitrage.

Uses real EPEX SPOT BE hourly price data from March 8, 2026 as the market dataset.

## How It Works

The `Battery` class models a physical battery asset with three core properties:
- `capacity_kwh` — total storage capacity
- `current_soc` — current state of charge as a decimal (0.0 to 1.0)
- `efficiency` — round-trip efficiency (default 0.85, meaning 15% energy is lost in the charge/discharge cycle)

Three core methods:
- `charge(amount_kwh)` — charges the battery, respects available capacity, updates SOC
- `discharge(amount_kwh)` — discharges the battery, applies efficiency loss, protects battery health by enforcing a 20% minimum SOC floor
- `calculate_profit(buy_price, sell_price, amount_kwh)` — runs a full arbitrage trade and returns net profit in euros

## Key Concepts Demonstrated

- Round-trip efficiency loss and its impact on arbitrage profitability
- State of charge tracking across charge and discharge events
- Battery health protection via minimum SOC floor (20%)
- Real electricity market price data (EPEX SPOT BE, €/MWh)

## What I Learned

> **Discovered business model associated with Energy trades(3 types) when you dont own the battery and the trading and Physical layer involved** 

## Tech Stack

- Python 3.x
- No external dependencies — standard library only

## Usage
```python
battery = Battery(capacity_kwh=10.0, current_soc=0.2)
profit = battery.calculate_profit(buy_price=0.02, sell_price=185.23, amount_kwh=5.0)
print(f"Profit: {profit:.2f} €")
```

## Part of a Larger Journey

This project is the first in a series of nine portfolio projects being built across a 12-month VPP and energy systems engineering roadmap. Future projects will add real-time data pipelines, Kafka message brokers, ML price forecasting, and an autonomous agentic trading system.