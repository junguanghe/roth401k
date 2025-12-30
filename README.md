# Roth 401k vs Pre-Tax 401k Comparison Tool

A Python GUI application to compare Roth 401k vs Pre-Tax 401k strategies, accounting for tax savings invested in a brokerage account.

## Requirements

- Python 3.x
- tkinter (usually included with Python)

## How to Run

```bash
python ira_comparison.py
```

## Input Parameters

- **Current Year Income (I)**: Your current annual income (default: $300,000)
- **401k Limit (L)**: Annual 401k contribution limit (default: $24,500)
- **Current Tax Rate (t_cur)**: Your marginal tax rate now (default: 45%)
- **Future Tax Rate (t_fut)**: Expected marginal tax rate at withdrawal (default: 30%)
- **Capital Gain Tax Rate (t_cg)**: Tax rate on long-term capital gains (default: 15%)
- **Number of Years (n)**: Investment period (default: 30 years)
- **Annual Return (r)**: Expected annual return rate (default: 7%)

## How It Works

### Roth 401k Strategy

When contributing **L** dollars to a Roth 401k:

- You need pre-tax income of **L / (1 - t_cur)** to contribute L after taxes
- The contribution **L** grows tax-free: **L × (1 + r)ⁿ**
- Withdrawal is tax-free
- **Final Value (Roth)**: V_Roth = L × (1 + r)ⁿ

### Pre-Tax 401k Strategy

When contributing **L** dollars to a pre-tax 401k:

- You contribute **L** pre-tax (costs **L × (1 - t_cur)** after taxes)
- The 401k grows: **L × (1 + r)ⁿ**
- Withdrawal is taxed: **L × (1 + r)ⁿ × (1 - t_fut)**
- **Tax savings**: The difference **L × t_cur** is saved immediately
- **Brokerage investment**: The tax savings **L × t_cur** are invested in a taxable brokerage account
  - This grows to: **L × t_cur × (1 + r)ⁿ**
  - Capital gains = **L × t_cur × [(1 + r)ⁿ - 1]**
  - After capital gains tax: **L × t_cur × {1 + [(1 + r)ⁿ - 1] × (1 - t_cg)}**
  - Simplified: **L × t_cur × [1 + (1 + r)ⁿ - 1 - t_cg × ((1 + r)ⁿ - 1)]**
  - Or: **L × t_cur × [(1 + r)ⁿ × (1 - t_cg) + t_cg]**
- **Final Value (Pre-tax)**:
  - V_PreTax = L × (1 + r)ⁿ × (1 - t_fut) + L × t_cur × [(1 + r)ⁿ × (1 - t_cg) + t_cg]

## Break-Even Condition

We want to find when **V_Roth = V_PreTax**:

```
L × (1 + r)ⁿ = L × (1 + r)ⁿ × (1 - t_fut) + L × t_cur × [(1 + r)ⁿ × (1 - t_cg) + t_cg]
```

Dividing both sides by **L**:

```
(1 + r)ⁿ = (1 + r)ⁿ × (1 - t_fut) + t_cur × [(1 + r)ⁿ × (1 - t_cg) + t_cg]
```

Expanding and simplifying:

```
(1 + r)ⁿ = (1 + r)ⁿ - t_fut × (1 + r)ⁿ + t_cur × (1 + r)ⁿ × (1 - t_cg) + t_cur × t_cg
```

```
0 = -t_fut × (1 + r)ⁿ + t_cur × (1 + r)ⁿ × (1 - t_cg) + t_cur × t_cg
```

```
t_fut × (1 + r)ⁿ = t_cur × (1 + r)ⁿ × (1 - t_cg) + t_cur × t_cg
```

Dividing both sides by **(1 + r)ⁿ**:

```
t_fut = t_cur × (1 - t_cg) + t_cur × t_cg / (1 + r)ⁿ
```

```
t_fut = t_cur × [(1 - t_cg) + t_cg / (1 + r)ⁿ]
```

**Break-even condition:**

```
t_fut = t_cur × [1 - t_cg × (1 - 1/(1 + r)ⁿ)]
```

Or equivalently:

```
t_fut = t_cur × [1 - t_cg × ((1 + r)ⁿ - 1) / (1 + r)ⁿ]
```

**Interpretation:**

- If **t_fut < t_cur × [1 - t_cg × (1 - 1/(1 + r)ⁿ)]**, then **Roth is better**
- If **t_fut > t_cur × [1 - t_cg × (1 - 1/(1 + r)ⁿ)]**, then **Pre-tax is better**
- If they're equal, both strategies yield the same final value

**Key Insight:** The break-even future tax rate is **lower** than the current tax rate because the pre-tax strategy allows you to invest the tax savings, offsetting some of the tax differential.

## Output

The program displays:

- **Total Growth Rate (G)**: (1 + r)ⁿ
- **Roth Final Value**: Total after-tax value from Roth 401k
- **Pre-tax Final Value**: Total after-tax value from pre-tax 401k + brokerage account
- **Break-Even Analysis**: Shows which strategy is better based on your inputs
