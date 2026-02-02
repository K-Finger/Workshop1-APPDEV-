import requests
from charting import create_fruit_bar_chart

BASE_URL = "https://www.fruityvice.com/api/fruit"


def get_all_fruits():
    """Fetch all fruits from the API"""
    response = requests.get(f"{BASE_URL}/all")

    if response.status_code != 200:
      raise Exception("Request failed")

    return response.json()


def get_fruit_by_name(name):
    """Fetch a specific fruit by name"""
    response = requests.get(f"{BASE_URL}/{name}")

    if response.status_code != 200:
      raise Exception("Request failed")

    return response.json()


def display_fruit_info(fruit):
    """Display fruit information in the console"""
    print("\n" + "=" * 50)
    print(f"  {fruit['name'].upper()}")
    print("=" * 50)

    print("\n  CLASSIFICATION")
    print("  " + "-" * 20)
    print(f"  Family: {fruit['family']}")
    print(f"  Order:  {fruit['order']}")
    print(f"  Genus:  {fruit['genus']}")

    print("\n  NUTRITION (per 100g)")
    print("  " + "-" * 20)
    nutritions = fruit['nutritions']
    print(f"  Calories:      {nutritions['calories']} kcal")
    print(f"  Carbohydrates: {nutritions['carbohydrates']} g")
    print(f"  Sugar:         {nutritions['sugar']} g")
    print(f"  Fat:           {nutritions['fat']} g")
    print(f"  Protein:       {nutritions['protein']} g")
    print("=" * 50 + "\n")


def display_all_fruits():
    """Fetch and display all fruits"""
    fruits = get_all_fruits()

    print("\n" + "=" * 80)
    print("  ALL FRUITS FROM FRUITYVICE API")
    print("=" * 80)
    print(f"\n  {'Name':<15} {'Family':<15} {'Calories':<10} {'Sugar':<10} {'Protein':<10}")
    print("  " + "-" * 60)

    for fruit in fruits:
        name = fruit['name'][:14]
        family = fruit['family'][:14]
        calories = fruit['nutritions']['calories']
        sugar = fruit['nutritions']['sugar']
        protein = fruit['nutritions']['protein']
        print(f"  {name:<15} {family:<15} {calories:<10} {sugar:<10} {protein:<10}")

    print("\n" + "=" * 80)
    print(f"  Total fruits: {len(fruits)}")
    print("=" * 80 + "\n")


def graph_fruits_by_nutrition(nutrition_type, top_n=10):
    """Create a bar graph of fruits ordered by a nutrition value"""
    valid_types = ['calories', 'fat', 'sugar', 'carbohydrates', 'protein']
    if nutrition_type not in valid_types:
        print(f"Invalid nutrition type! Choose from: {valid_types}")
        return

    fruits = get_all_fruits()

    sorted_fruits = sorted(
        fruits,
        key=lambda x: x['nutritions'][nutrition_type],
        reverse=True
    )[:top_n]

    names = [fruit['name'] for fruit in sorted_fruits]
    values = [fruit['nutritions'][nutrition_type] for fruit in sorted_fruits]

    create_fruit_bar_chart(names, values, nutrition_type, top_n)


if __name__ == "__main__":
    print("\n" + "*" * 60)
    print("  WELCOME TO APP DEV CLUB'S FRUIT APP!")
    print("  Use Fruityvice REST API")
    print("*" * 60)

    while True:
        print("\nWhat would you like to do?")
        print("  1. Look up a specific fruit")
        print("  2. See all fruits")
        print("  3. Graph fruits by nutrition")
        print("  4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            fruit_name = input("Enter fruit name (e.g., apple, banana): ").strip().lower()
            try:
                fruit = get_fruit_by_name(fruit_name)
                display_fruit_info(fruit)

            # HANDLE REQUEST ERROR
            except Exception:
                print(f"\nType '{fruit_name}' correctly bozo")

        elif choice == "2":
            display_all_fruits()

        elif choice == "3":
            print("\nAvailable nutrition types:")
            print("  - calories")
            print("  - fat")
            print("  - sugar")
            print("  - carbohydrates")
            print("  - protein")
            nutrition = input("\nEnter nutrition type: ").strip().lower()
            graph_fruits_by_nutrition(nutrition)

        elif choice == "4":
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, 3, or 4.")
