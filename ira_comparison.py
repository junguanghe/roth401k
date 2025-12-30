import tkinter as tk
from tkinter import ttk


class IRAComparisonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Roth 401k vs Pre-Tax 401k Comparison")
        self.root.geometry("900x750")

        # Variables
        self.current_income = tk.DoubleVar(value=300000.0)
        self.limit_401k = tk.DoubleVar(value=24500.0)
        self.t_cur = tk.DoubleVar(value=45.0)
        self.t_fut = tk.DoubleVar(value=30.0)
        self.t_cg = tk.DoubleVar(value=15.0)
        self.num_years = tk.IntVar(value=30)
        self.annual_return = tk.DoubleVar(value=7.0)

        self.setup_ui()
        self.calculate()

    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Input section
        input_frame = ttk.LabelFrame(main_frame, text="Input Parameters", padding="10")
        input_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        # Current year income
        ttk.Label(input_frame, text="Current Year Income I ($):").grid(
            row=0, column=0, sticky=tk.W, pady=2
        )
        ttk.Entry(input_frame, textvariable=self.current_income, width=20).grid(
            row=0, column=1, sticky=tk.W, padx=5
        )

        # 401k limit
        ttk.Label(input_frame, text="401k Limit L ($):").grid(
            row=1, column=0, sticky=tk.W, pady=2
        )
        ttk.Entry(input_frame, textvariable=self.limit_401k, width=20).grid(
            row=1, column=1, sticky=tk.W, padx=5
        )

        # Current tax rate
        ttk.Label(input_frame, text="Current Tax Rate t_cur (%):").grid(
            row=2, column=0, sticky=tk.W, pady=2
        )
        ttk.Entry(input_frame, textvariable=self.t_cur, width=20).grid(
            row=2, column=1, sticky=tk.W, padx=5
        )

        # Future tax rate
        ttk.Label(input_frame, text="Future Tax Rate t_fut (%):").grid(
            row=3, column=0, sticky=tk.W, pady=2
        )
        ttk.Entry(input_frame, textvariable=self.t_fut, width=20).grid(
            row=3, column=1, sticky=tk.W, padx=5
        )

        # Capital gain tax rate
        ttk.Label(input_frame, text="Capital Gain Tax Rate t_cg (%):").grid(
            row=4, column=0, sticky=tk.W, pady=2
        )
        ttk.Entry(input_frame, textvariable=self.t_cg, width=20).grid(
            row=4, column=1, sticky=tk.W, padx=5
        )

        # Number of years
        ttk.Label(input_frame, text="Number of Years n:").grid(
            row=5, column=0, sticky=tk.W, pady=2
        )
        ttk.Entry(input_frame, textvariable=self.num_years, width=20).grid(
            row=5, column=1, sticky=tk.W, padx=5
        )

        # Annual return
        ttk.Label(input_frame, text="Annual Return r (%):").grid(
            row=6, column=0, sticky=tk.W, pady=2
        )
        ttk.Entry(input_frame, textvariable=self.annual_return, width=20).grid(
            row=6, column=1, sticky=tk.W, padx=5
        )

        # Calculate button
        ttk.Button(input_frame, text="Calculate", command=self.calculate).grid(
            row=7, column=0, columnspan=2, pady=10
        )

        # Results section
        results_frame = ttk.LabelFrame(main_frame, text="Results", padding="10")
        results_frame.grid(
            row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5
        )

        # Growth rate display
        self.growth_rate_label = ttk.Label(
            results_frame, text="Total Growth Rate G: 0.00", font=("Arial", 11, "bold")
        )
        self.growth_rate_label.grid(row=0, column=0, columnspan=2, sticky=tk.W, pady=5)

        # Intermediate results section
        intermediate_frame = ttk.LabelFrame(
            results_frame, text="Intermediate Results (Current Year)", padding="10"
        )
        intermediate_frame.grid(
            row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5
        )

        # Column headers
        ttk.Label(
            intermediate_frame, text="Roth 401k", font=("Arial", 11, "bold")
        ).grid(row=0, column=0, sticky=tk.W, pady=5, padx=5)
        ttk.Label(
            intermediate_frame, text="Pre-Tax 401k", font=("Arial", 11, "bold")
        ).grid(row=0, column=1, sticky=tk.W, pady=5, padx=5)

        # Roth breakdown
        self.roth_taxable_income_label = ttk.Label(
            intermediate_frame,
            text="Taxable Income: $0.00",
            font=("Arial", 10),
        )
        self.roth_taxable_income_label.grid(
            row=1, column=0, sticky=tk.W, pady=2, padx=5
        )

        self.roth_after_tax_income_label = ttk.Label(
            intermediate_frame,
            text="After-Tax Income: $0.00",
            font=("Arial", 10),
        )
        self.roth_after_tax_income_label.grid(
            row=2, column=0, sticky=tk.W, pady=2, padx=5
        )

        self.roth_take_home_label = ttk.Label(
            intermediate_frame,
            text="Take Home Pay: $0.00",
            font=("Arial", 10),
        )
        self.roth_take_home_label.grid(row=3, column=0, sticky=tk.W, pady=2, padx=5)

        self.roth_401k_contribution_label = ttk.Label(
            intermediate_frame,
            text="Roth 401k Contribution: $0.00",
            font=("Arial", 10, "bold"),
        )
        self.roth_401k_contribution_label.grid(
            row=4, column=0, sticky=tk.W, pady=2, padx=5
        )

        # Pre-tax breakdown
        self.pretax_401k_amount_label = ttk.Label(
            intermediate_frame,
            text="Pre-Tax 401k Contribution: $0.00",
            font=("Arial", 10, "bold"),
        )
        self.pretax_401k_amount_label.grid(row=1, column=1, sticky=tk.W, pady=2, padx=5)

        self.pretax_taxable_income_label = ttk.Label(
            intermediate_frame,
            text="Taxable Income: $0.00",
            font=("Arial", 10),
        )
        self.pretax_taxable_income_label.grid(
            row=2, column=1, sticky=tk.W, pady=2, padx=5
        )

        self.pretax_take_home_label = ttk.Label(
            intermediate_frame,
            text="Take Home Pay: $0.00",
            font=("Arial", 10),
        )
        self.pretax_take_home_label.grid(row=3, column=1, sticky=tk.W, pady=2, padx=5)

        self.pretax_tax_savings_label = ttk.Label(
            intermediate_frame,
            text="Tax Savings (to brokerage): $0.00",
            font=("Arial", 9, "bold"),
        )
        self.pretax_tax_savings_label.grid(row=4, column=1, sticky=tk.W, pady=2, padx=5)

        # Roth result frame
        roth_frame = ttk.LabelFrame(results_frame, text="Roth 401k", padding="10")
        roth_frame.grid(
            row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5
        )

        self.roth_label = ttk.Label(
            roth_frame, text="Final Value: $0.00", font=("Arial", 12, "bold")
        )
        self.roth_label.grid(row=0, column=0, sticky=tk.W)

        # Pre-tax result frame
        pretax_frame = ttk.LabelFrame(results_frame, text="Pre-Tax 401k", padding="10")
        pretax_frame.grid(
            row=2, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5
        )

        self.pretax_401k_label = ttk.Label(
            pretax_frame, text="401k Final Value: $0.00", font=("Arial", 10)
        )
        self.pretax_401k_label.grid(row=0, column=0, sticky=tk.W, pady=2)

        self.pretax_brokerage_label = ttk.Label(
            pretax_frame, text="Brokerage Final Value: $0.00", font=("Arial", 10)
        )
        self.pretax_brokerage_label.grid(row=1, column=0, sticky=tk.W, pady=2)

        self.pretax_total_label = ttk.Label(
            pretax_frame, text="Total Final Value: $0.00", font=("Arial", 12, "bold")
        )
        self.pretax_total_label.grid(row=2, column=0, sticky=tk.W, pady=5)

        # Comparison summary
        comparison_frame = ttk.LabelFrame(main_frame, text="Comparison", padding="10")
        comparison_frame.grid(
            row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5
        )

        self.comparison_label = ttk.Label(comparison_frame, text="", font=("Arial", 11))
        self.comparison_label.grid(row=0, column=0, sticky=tk.W, pady=2)

        # Break-even formula label
        self.break_even_formula_label = ttk.Label(
            comparison_frame,
            text="Break-even formula: t_fut = t_cur × [1 - t_cg × (1 - 1/G)]",
            font=("Arial", 9),
        )
        self.break_even_formula_label.grid(row=1, column=0, sticky=tk.W, pady=2)

        self.break_even_label = ttk.Label(comparison_frame, text="", font=("Arial", 10))
        self.break_even_label.grid(row=2, column=0, sticky=tk.W, pady=2)

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        results_frame.columnconfigure(0, weight=1)
        results_frame.columnconfigure(1, weight=1)
        intermediate_frame.columnconfigure(0, weight=1)
        intermediate_frame.columnconfigure(1, weight=1)
        roth_frame.columnconfigure(0, weight=1)
        pretax_frame.columnconfigure(0, weight=1)

    def calculate(self):
        try:
            # Get input values
            current_income = self.current_income.get()
            L = self.limit_401k.get()
            t_cur = self.t_cur.get() / 100.0
            t_fut = self.t_fut.get() / 100.0
            t_cg = self.t_cg.get() / 100.0
            n = self.num_years.get()
            r = self.annual_return.get() / 100.0

            # Calculate growth rate G = (1 + r)^n
            G = (1 + r) ** n

            # Intermediate calculations
            # Roth strategy
            # Taxable income (Roth doesn't reduce taxable income)
            roth_taxable_income = current_income
            # After-tax income (total)
            roth_after_tax_income = current_income * (1 - t_cur)
            # Take home pay (after contributing to Roth)
            roth_take_home = roth_after_tax_income - L
            # Roth 401k contribution (after-tax)
            roth_401k_contribution = L

            # Pre-tax strategy
            # Pre-tax 401k contribution
            pretax_401k_amount = L
            # Taxable income (after 401k contribution reduces taxable income)
            pretax_taxable_income = current_income - L
            # Take home pay (after taxes on taxable income)
            pretax_take_home = pretax_taxable_income * (1 - t_cur)
            # Tax savings (amount invested in brokerage)
            pretax_tax_savings = L * t_cur

            # Calculate Roth 401k final value
            # V_Roth = L × (1 + r)^n
            roth_final = L * G

            # Calculate Pre-tax 401k final value
            # Pre-tax 401k contribution grows and is taxed on withdrawal
            pretax_401k = L * G * (1 - t_fut)

            # Tax savings invested in brokerage
            # Tax savings = L × t_cur
            # Brokerage grows to: L × t_cur × (1 + r)^n
            # Capital gains = L × t_cur × [(1 + r)^n - 1]
            # After capital gains tax: L × t_cur × {1 + [(1 + r)^n - 1] × (1 - t_cg)}
            # Simplified: L × t_cur × [(1 + r)^n × (1 - t_cg) + t_cg]
            brokerage_value = L * t_cur * (G * (1 - t_cg) + t_cg)

            # Total pre-tax final value
            pretax_total = pretax_401k + brokerage_value

            # Update display
            self.growth_rate_label.config(
                text=f"Total Growth Rate G = (1 + r)ⁿ = {G:,.4f}"
            )

            # Update intermediate results
            # Roth breakdown
            self.roth_taxable_income_label.config(
                text=f"Taxable Income: ${roth_taxable_income:,.2f}"
            )
            self.roth_after_tax_income_label.config(
                text=f"After-Tax Income: ${roth_after_tax_income:,.2f}"
            )
            self.roth_take_home_label.config(
                text=f"Take Home Pay: ${roth_take_home:,.2f}"
            )
            self.roth_401k_contribution_label.config(
                text=f"Roth 401k Contribution: ${roth_401k_contribution:,.2f}"
            )

            # Pre-tax breakdown
            self.pretax_401k_amount_label.config(
                text=f"Pre-Tax 401k Contribution: ${pretax_401k_amount:,.2f}"
            )
            self.pretax_taxable_income_label.config(
                text=f"Taxable Income: ${pretax_taxable_income:,.2f}"
            )
            self.pretax_take_home_label.config(
                text=f"Take Home Pay: ${pretax_take_home:,.2f}"
            )
            self.pretax_tax_savings_label.config(
                text=f"Tax Savings (to brokerage): ${pretax_tax_savings:,.2f}"
            )

            self.roth_label.config(text=f"Final Value: ${roth_final:,.2f}")

            self.pretax_401k_label.config(
                text=f"401k Final Value (after tax): ${pretax_401k:,.2f}"
            )
            self.pretax_brokerage_label.config(
                text=f"Brokerage Final Value (after CG tax): ${brokerage_value:,.2f}"
            )
            self.pretax_total_label.config(
                text=f"Total Final Value: ${pretax_total:,.2f}"
            )

            # Comparison
            difference = roth_final - pretax_total
            if abs(difference) < 0.01:
                self.comparison_label.config(
                    text="Both strategies yield approximately the same final value.",
                    foreground="blue",
                )
            elif difference > 0:
                self.comparison_label.config(
                    text=f"Roth 401k is better by ${difference:,.2f}",
                    foreground="green",
                )
            else:
                self.comparison_label.config(
                    text=f"Pre-tax 401k is better by ${-difference:,.2f}",
                    foreground="orange",
                )

            # Break-even analysis
            # Break-even condition: t_fut = t_cur × [1 - t_cg × (1 - 1/(1 + r)ⁿ)]
            break_even_t_fut = t_cur * (1 - t_cg * (1 - 1 / G))
            break_even_t_fut_pct = break_even_t_fut * 100

            if abs(t_fut - break_even_t_fut) < 0.001:
                be_status = "At break-even point"
            elif t_fut < break_even_t_fut:
                be_status = "Roth is better (t_fut < break-even)"
            else:
                be_status = "Pre-tax is better (t_fut > break-even)"

            self.break_even_label.config(
                text=f"Break-even t_fut: {break_even_t_fut_pct:.2f}% | "
                f"Your t_fut: {t_fut*100:.2f}% | {be_status}",
                foreground="gray",
            )

        except Exception as e:
            self.comparison_label.config(text=f"Error: {str(e)}", foreground="red")


def main():
    root = tk.Tk()
    IRAComparisonApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
