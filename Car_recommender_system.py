from rich.console import Console
from rich.panel import Panel

console = Console()


def main():
    budget = get_budget()
    feul, usage = get_preferences(budget)
    recommended_car(budget, feul, usage)
    
    
    
    
cars = {
    "high_petrol": ["Toyota Corolla", "Honda Civic"],
    "high_hybrid": ["Toyota Corolla Hybrid", "Honda Vezel"],
    "high_offroad":["Toyota Fortuner", "Kia Sportage"],    
    "mid_family": ["Toyota Yaris", "Honda City"],
    "mid_city": ["Suzuki Swift", "Kia Picanto"],
    "low": ["Suzuki Mehran", "United Bravo"]
}

def get_budget():
    budget = int(input("Enter your Budget in PKR: "))
    return budget

def get_preferences(budget):
    if budget < 1500000:
        return None, None
    feul = input("Fuel type? (hybrid/petrol): ")
    usage = input("Usage type? (city/family/offroad): ")
    return feul, usage

def recommended_car(budget, feul, usage):
    if budget < 1500000:
        key = "low"
    elif budget < 3000000:
        if usage == "family":
            key = "mid_family"
        else:
            key = "mid_city"
    else:
        if feul == "hybrid":
            key = "high_hybrid"
        elif usage == "offroad":
            key = "high_offroad"
        else:
            key = "high_petrol"

    print("Recommended cars:")
    for car in cars[key]:
        console.print(f"[green]-> {car}[/green]")
        

console.print(Panel("🚗 Car Recommender System", style="bold blue"))
        
main()
