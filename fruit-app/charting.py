import matplotlib.pyplot as plt
import json
import sys
from datetime import datetime


def create_fruit_bar_chart(names, values, nutrition_type, top_n):
    """Create a horizontal bar chart for fruit nutrition data."""
    plt.figure(figsize=(12, 6))
    bars = plt.barh(names[::-1], values[::-1], color='mediumseagreen')

    for bar, value in zip(bars, values[::-1]):
        plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                 f'{value}', va='center', fontsize=10)

    unit = 'kcal' if nutrition_type == 'calories' else 'g'
    plt.xlabel(f'{nutrition_type.capitalize()} ({unit})')
    plt.ylabel('Fruit')
    plt.title(f'Top {top_n} Fruits by {nutrition_type.capitalize()}')
    plt.tight_layout()
    plt.show()