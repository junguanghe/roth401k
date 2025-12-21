# IRA Comparison Tool: Active vs Passive × Pre-Tax vs Roth

A Python GUI application to compare 4 different IRA investment scenarios combining investment strategies (Active vs Passive) with IRA types (Pre-Tax vs Roth).

## Requirements

- Python 3.x
- tkinter (usually included with Python)

## How to Run

```bash
python ira_comparison.py
```

## Input Parameters

- **Deposit Year Tax Rate**: Your tax rate when making deposits (default: 30%)
- **Deposit Yearly Limit**: Maximum amount you can deposit per year (default: $24,500)
- **Number of Years**: Investment period (default: 30 years)
- **Yearly Beta - Passive**: Base annual growth rate for passive investment (default: 5%)
- **Yearly Alpha - Active Bonus**: Additional growth rate for active investment (default: 5%)
  - Passive growth rate = Beta (e.g., 5%)
  - Active growth rate = Beta + Alpha (e.g., 5% + 5% = 10%)
- **Withdrawal Tax Rate**: Your tax rate when withdrawing (default: 20%)

## How It Works

The tool compares **4 scenarios** in a 2×2 grid:

### Investment Strategies
- **Active Investment**: Uses Beta + Alpha (higher growth rate)
- **Passive Investment**: Uses only Beta (lower growth rate)

### IRA Types
- **Pre-Tax IRA**: 
  - Deposit the full yearly limit (pre-tax)
  - Money grows tax-free
  - Pay taxes when you withdraw
  - Final amount = (Initial deposit × (1 + growth_rate)^years) × (1 - withdrawal_tax_rate)

- **Roth IRA**:
  - Need pre-tax income of: yearly_limit / (1 - deposit_tax_rate) to deposit yearly_limit after taxes
  - Money grows tax-free
  - No taxes on withdrawal
  - Final amount = Initial deposit × (1 + growth_rate)^years

## Output

The program displays a 2×2 grid showing all 4 combinations:

1. **Active + Pre-Tax IRA**
2. **Active + Roth IRA**
3. **Passive + Pre-Tax IRA**
4. **Passive + Roth IRA**

Each scenario shows:
- Initial Pre-Tax Deposit
- Initial After-Tax Deposit
- Withdrawal (Pre-Tax)
- Withdrawal (After-Tax)

The program also identifies the **Best Option** based on the highest after-tax withdrawal amount.
