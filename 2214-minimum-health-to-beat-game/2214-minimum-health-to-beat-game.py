class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_dmg = max (damage)
        return sum(damage) - armor + 1 if max_dmg >= armor else sum(damage) - max_dmg + 1