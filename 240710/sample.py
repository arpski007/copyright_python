import sympy as sp

# Define symbols
Re, rho, v, D, mu, V, A, m = sp.symbols('Re rho v D mu V A m')

# Define equations
equations = [
    sp.Eq(Re, rho * v * D / mu),
    sp.Eq(V, v * A),
    sp.Eq(A, 0.25 * sp.pi * D ** 2),
    sp.Eq(m, V * rho)
]

# Function to solve equations
def solve_equations(given_vars, given_values):
    known_vars = dict(zip(given_vars, given_values))
    unknown_vars = [var for var in [Re, rho, v, D, mu, V, A, m] if var not in known_vars]

    solutions = sp.solve(equations, unknown_vars, dict=True)
    
    if solutions:
        solution = solutions[0]  # Take the first solution set
        return {str(var): solution[var].subs(known_vars) for var in unknown_vars if var in solution}
    
    return "No solutions found with the given variables."

# Get input from the user
given_vars = []
given_values = []

for _ in range(4):
    while True:
        var_name = input("Enter the variable name (Re, rho, v, D, mu, V, A, m): ").strip()
        try:
            var_value = float(input(f"Enter the value for {var_name}: ").replace(',', ''))
            given_vars.append(sp.symbols(var_name))
            given_values.append(var_value)
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Solve and display the results
solutions = solve_equations(given_vars, given_values)

print("Solutions:")
if isinstance(solutions, dict):
    for var, value in solutions.items():
        print(f"{var} = {value}")
    
    # Check the type of fluid flow if Reynolds number is calculated
    if 'Re' in solutions:
        reynolds_number = solutions['Re']
        if reynolds_number < 2000:
            flow_type = "Laminar flow"
        elif 2000 <= reynolds_number <= 4000:
            flow_type = "Transition flow"
        else:
            flow_type = "Turbulent flow"
        print(f"Flow type: {flow_type}")
else:
    print(solutions)