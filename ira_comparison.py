import tkinter as tk
from tkinter import ttk


class IRAComparisonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("IRA Comparison: Active vs Passive × Pre-Tax vs Roth")
        self.root.geometry("1000x700")

        # Variables
        self.deposit_tax_rate = tk.DoubleVar(value=30.0)
        self.yearly_limit = tk.DoubleVar(value=24500.0)
        self.num_years = tk.IntVar(value=30)
        self.yearly_beta = tk.DoubleVar(value=5.0)
        self.yearly_alpha = tk.DoubleVar(value=5.0)
        self.withdrawal_tax_rate = tk.DoubleVar(value=20.0)

        self.setup_ui()
        self.calculate()

    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Input section
        input_frame = ttk.LabelFrame(main_frame, text="Input Parameters", padding="10")
        input_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)

        # Deposit tax rate
        ttk.Label(input_frame, text="Deposit Year Tax Rate (%):").grid(
            row=0, column=0, sticky=tk.W, pady=2
        )
        ttk.Entry(input_frame, textvariable=self.deposit_tax_rate, width=15).grid(
            row=0, column=1, sticky=tk.W, padx=5
        )

        # Yearly limit
        ttk.Label(input_frame, text="Deposit Yearly Limit ($):").grid(
            row=1, column=0, sticky=tk.W, pady=2
        )
        ttk.Entry(input_frame, textvariable=self.yearly_limit, width=15).grid(
            row=1, column=1, sticky=tk.W, padx=5
        )

        # Number of years
        ttk.Label(input_frame, text="Number of Years:").grid(
            row=2, column=0, sticky=tk.W, pady=2
        )
        ttk.Entry(input_frame, textvariable=self.num_years, width=15).grid(
            row=2, column=1, sticky=tk.W, padx=5
        )

        # Yearly beta (passive)
        ttk.Label(input_frame, text="Yearly Beta - Passive (%):").grid(
            row=3, column=0, sticky=tk.W, pady=2
        )
        ttk.Entry(input_frame, textvariable=self.yearly_beta, width=15).grid(
            row=3, column=1, sticky=tk.W, padx=5
        )

        # Yearly alpha (active bonus)
        ttk.Label(input_frame, text="Yearly Alpha - Active Bonus (%):").grid(
            row=4, column=0, sticky=tk.W, pady=2
        )
        ttk.Entry(input_frame, textvariable=self.yearly_alpha, width=15).grid(
            row=4, column=1, sticky=tk.W, padx=5
        )

        # Withdrawal tax rate
        ttk.Label(input_frame, text="Withdrawal Tax Rate (%):").grid(
            row=5, column=0, sticky=tk.W, pady=2
        )
        ttk.Entry(input_frame, textvariable=self.withdrawal_tax_rate, width=15).grid(
            row=5, column=1, sticky=tk.W, padx=5
        )

        # Calculate button
        ttk.Button(input_frame, text="Calculate", command=self.calculate).grid(
            row=6, column=0, columnspan=2, pady=10
        )

        # Results section - 2x2 grid
        results_frame = ttk.LabelFrame(main_frame, text="Results", padding="10")
        results_frame.grid(
            row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5
        )

        # Column headers
        ttk.Label(results_frame, text="Pre-Tax IRA", font=("Arial", 11, "bold")).grid(
            row=0, column=0, columnspan=2, pady=5
        )
        ttk.Label(results_frame, text="Roth IRA", font=("Arial", 11, "bold")).grid(
            row=0, column=2, columnspan=2, pady=5
        )

        # Row headers
        ttk.Label(
            results_frame, text="Active Investment", font=("Arial", 11, "bold")
        ).grid(row=1, column=0, sticky=tk.E, padx=5)
        ttk.Label(
            results_frame, text="Passive Investment", font=("Arial", 11, "bold")
        ).grid(row=2, column=0, sticky=tk.E, padx=5)

        # Create 4 result frames
        self.create_result_frame(results_frame, "active_pre_tax", 1, 1)
        self.create_result_frame(results_frame, "active_roth", 1, 3)
        self.create_result_frame(results_frame, "passive_pre_tax", 2, 1)
        self.create_result_frame(results_frame, "passive_roth", 2, 3)

        # Comparison summary
        comparison_frame = ttk.LabelFrame(main_frame, text="Best Option", padding="10")
        comparison_frame.grid(
            row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5
        )

        self.comparison_label = ttk.Label(
            comparison_frame, text="", font=("Arial", 12, "bold")
        )
        self.comparison_label.grid(row=0, column=0, sticky=tk.W, pady=2)

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        results_frame.columnconfigure(0, weight=1)
        results_frame.columnconfigure(1, weight=1)
        results_frame.columnconfigure(2, weight=1)
        results_frame.columnconfigure(3, weight=1)

    def create_result_frame(self, parent, name, row, col):
        """Create a result frame for one of the 4 scenarios"""
        frame = ttk.LabelFrame(parent, text=name.replace("_", " ").title(), padding="8")
        frame.grid(row=row, column=col, sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5)

        labels = {}
        labels["initial_pre_tax"] = ttk.Label(
            frame, text="Initial Pre-Tax: $0.00", font=("Arial", 9)
        )
        labels["initial_pre_tax"].grid(row=0, column=0, sticky=tk.W, pady=1)

        labels["initial_after_tax"] = ttk.Label(
            frame, text="Initial After-Tax: $0.00", font=("Arial", 9)
        )
        labels["initial_after_tax"].grid(row=1, column=0, sticky=tk.W, pady=1)

        labels["withdrawal_pre_tax"] = ttk.Label(
            frame, text="Withdrawal (Pre-Tax): $0.00", font=("Arial", 9)
        )
        labels["withdrawal_pre_tax"].grid(row=2, column=0, sticky=tk.W, pady=1)

        labels["withdrawal_after_tax"] = ttk.Label(
            frame, text="Withdrawal (After-Tax): $0.00", font=("Arial", 9, "bold")
        )
        labels["withdrawal_after_tax"].grid(row=3, column=0, sticky=tk.W, pady=1)

        # Store labels in instance variable
        setattr(self, f"{name}_labels", labels)

    def calculate(self):
        try:
            # Get input values
            deposit_tax = self.deposit_tax_rate.get() / 100.0
            yearly_limit = self.yearly_limit.get()
            years = self.num_years.get()
            beta = self.yearly_beta.get() / 100.0
            alpha = self.yearly_alpha.get() / 100.0
            withdrawal_tax = self.withdrawal_tax_rate.get() / 100.0

            # Growth rates
            passive_growth = beta
            active_growth = beta + alpha

            # Calculate all 4 scenarios
            results = {}

            # 1. Active + Pre-Tax
            results["active_pre_tax"] = self.calculate_ira(
                yearly_limit,
                years,
                active_growth,
                deposit_tax,
                withdrawal_tax,
                is_roth=False,
            )

            # 2. Active + Roth
            results["active_roth"] = self.calculate_ira(
                yearly_limit,
                years,
                active_growth,
                deposit_tax,
                withdrawal_tax,
                is_roth=True,
            )

            # 3. Passive + Pre-Tax
            results["passive_pre_tax"] = self.calculate_ira(
                yearly_limit,
                years,
                passive_growth,
                deposit_tax,
                withdrawal_tax,
                is_roth=False,
            )

            # 4. Passive + Roth
            results["passive_roth"] = self.calculate_ira(
                yearly_limit,
                years,
                passive_growth,
                deposit_tax,
                withdrawal_tax,
                is_roth=True,
            )

            # Update all labels
            for scenario, data in results.items():
                labels = getattr(self, f"{scenario}_labels")
                labels["initial_pre_tax"].config(
                    text=f"Initial Pre-Tax: ${data['initial_pre_tax']:,.2f}"
                )
                labels["initial_after_tax"].config(
                    text=f"Initial After-Tax: ${data['initial_after_tax']:,.2f}"
                )
                labels["withdrawal_pre_tax"].config(
                    text=f"Withdrawal (Pre-Tax): ${data['withdrawal_pre_tax']:,.2f}"
                )
                labels["withdrawal_after_tax"].config(
                    text=f"Withdrawal (After-Tax): ${data['withdrawal_after_tax']:,.2f}"
                )

            # Find best option
            best_scenario = max(
                results.items(), key=lambda x: x[1]["withdrawal_after_tax"]
            )
            best_name = best_scenario[0].replace("_", " ").title()
            best_value = best_scenario[1]["withdrawal_after_tax"]

            self.comparison_label.config(
                text=f"Best Option: {best_name} with ${best_value:,.2f} after-tax withdrawal"
            )

        except Exception as e:
            self.comparison_label.config(text=f"Error: {str(e)}")

    def calculate_ira(
        self, yearly_limit, years, growth_rate, deposit_tax, withdrawal_tax, is_roth
    ):
        """Calculate IRA values for a given scenario"""
        if is_roth:
            # Roth IRA
            initial_pre_tax = yearly_limit / (1 - deposit_tax)
            initial_after_tax = yearly_limit
            # Final amount after compound growth (no tax on withdrawal)
            withdrawal_pre_tax = initial_after_tax * ((1 + growth_rate) ** years)
            withdrawal_after_tax = withdrawal_pre_tax  # No tax on Roth withdrawals
        else:
            # Pre-Tax IRA
            initial_pre_tax = yearly_limit
            initial_after_tax = yearly_limit
            # Final amount after compound growth
            withdrawal_pre_tax = yearly_limit * ((1 + growth_rate) ** years)
            # After-tax withdrawal
            withdrawal_after_tax = withdrawal_pre_tax * (1 - withdrawal_tax)

        return {
            "initial_pre_tax": initial_pre_tax,
            "initial_after_tax": initial_after_tax,
            "withdrawal_pre_tax": withdrawal_pre_tax,
            "withdrawal_after_tax": withdrawal_after_tax,
        }


def main():
    root = tk.Tk()
    IRAComparisonApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
