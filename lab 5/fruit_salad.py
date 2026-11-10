"""Fruit salad model: fruits, toppings, topping selection and mixing."""

from __future__ import annotations

import random
from collections import Counter
from dataclasses import dataclass, field
from enum import Enum


class Taste(Enum):
    SWEET = "sweet"
    SOUR = "sour"
    NEUTRAL = "neutral"


class Size(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"


class Topping(Enum):
    HONEY = ("Honey", Taste.SWEET)
    CONDENSED_MILK = ("Condensed milk", Taste.SWEET)
    LEMON_JUICE = ("Lemon juice", Taste.SOUR)
    GREEK_YOGURT = ("Greek yogurt", Taste.SOUR)
    WHIPPED_CREAM = ("Whipped cream", Taste.NEUTRAL)
    NONE = ("No topping", Taste.NEUTRAL)

    def __init__(self, label: str, taste: Taste):
        self.label = label
        self.taste = taste

    def __str__(self) -> str:
        return f"{self.label} ({self.taste.value})"


@dataclass(frozen=True)  # frozen -> hashable, so fruits can live in a set
class Fruit:
    name: str
    size: Size
    colour: str
    taste: Taste
    calories_per_100g: int = 0
    has_seeds: bool = False

    def __str__(self) -> str:
        return f"{self.name} ({self.size.value}, {self.colour}, {self.taste.value})"


@dataclass
class FruitSalad:
    fruits: set[Fruit] = field(default_factory=set)
    topping: Topping | None = None

    def add_fruit(self, fruit: Fruit) -> None:
        self.fruits.add(fruit)

    def dominant_taste(self) -> Taste:
        """Most common taste among the fruits, weighted by fruit size.

        Ties (or an empty salad) count as NEUTRAL.
        """
        weights = {Size.SMALL: 1, Size.MEDIUM: 2, Size.LARGE: 3}
        score: Counter[Taste] = Counter()
        for fruit in self.fruits:
            score[fruit.taste] += weights[fruit.size]

        ranked = score.most_common()
        if not ranked or (len(ranked) > 1 and ranked[0][1] == ranked[1][1]):
            return Taste.NEUTRAL
        return ranked[0][0]

    def choose_topping(self) -> Topping:
        """Pick a topping that balances the salad's flavour.

        - Mostly sweet  -> a sour topping cuts the sweetness.
        - Mostly sour   -> a sweet topping softens the sourness.
        - Neutral/mixed -> a neutral topping keeps the balance.
        Among the matching toppings one is chosen at random.
        """
        if not self.fruits:
            self.topping = Topping.NONE
            return self.topping

        balancing = {
            Taste.SWEET: Taste.SOUR,
            Taste.SOUR: Taste.SWEET,
            Taste.NEUTRAL: Taste.NEUTRAL,
        }
        wanted = balancing[self.dominant_taste()]
        candidates = [t for t in Topping if t.taste is wanted and t is not Topping.NONE]
        self.topping = random.choice(candidates)
        return self.topping

    def mix(self) -> list[str]:
        """Chop the fruits, toss them in random order and add the topping.

        Returns the list of steps performed.
        """
        if not self.fruits:
            raise ValueError("Cannot mix an empty salad - add some fruits first.")
        if self.topping is None:
            self.choose_topping()

        steps = []
        for fruit in sorted(self.fruits, key=lambda f: f.name):
            prep = "remove seeds and dice" if fruit.has_seeds else "dice"
            steps.append(f"{prep.capitalize()} the {fruit.name.lower()}")

        order = list(self.fruits)
        random.shuffle(order)
        steps.append("Toss together: " + ", ".join(f.name.lower() for f in order))

        if self.topping is not Topping.NONE:
            steps.append(f"Add {self.topping.label.lower()} on top")
        steps.append("Salad is ready!")
        return steps

    def total_calories(self) -> int:
        return sum(f.calories_per_100g for f in self.fruits)

    def __str__(self) -> str:
        fruits = "\n".join(f"  - {f}" for f in sorted(self.fruits, key=lambda f: f.name))
        return f"Fruit salad:\n{fruits}\n  Topping: {self.topping or 'not chosen'}"


if __name__ == "__main__":
    apple = Fruit("Apple", Size.MEDIUM, "red", Taste.SWEET, 52, has_seeds=True)
    banana = Fruit("Banana", Size.MEDIUM, "yellow", Taste.SWEET, 89)
    mango = Fruit("Mango", Size.LARGE, "orange", Taste.SWEET, 60, has_seeds=True)
    kiwi = Fruit("Kiwi", Size.SMALL, "green", Taste.SOUR, 61)
    lemon = Fruit("Lemon", Size.SMALL, "yellow", Taste.SOUR, 29, has_seeds=True)
    grapefruit = Fruit("Grapefruit", Size.LARGE, "pink", Taste.SOUR, 42, has_seeds=True)
    pear = Fruit("Pear", Size.MEDIUM, "green", Taste.NEUTRAL, 57)

    salads = {
        "Sweet salad": FruitSalad({apple, banana, mango, kiwi}),
        "Sour salad": FruitSalad({kiwi, lemon, grapefruit, pear}),
        "Balanced salad": FruitSalad({mango, grapefruit, pear}),
    }

    for title, salad in salads.items():
        print(f"=== {title} ===")
        print(f"Dominant taste: {salad.dominant_taste().value}")
        print(f"Chosen topping: {salad.choose_topping()}")
        print(salad)
        for i, step in enumerate(salad.mix(), 1):
            print(f"  {i}. {step}")
        print(f"Calories (per 100 g of each fruit): {salad.total_calories()}\n")
