class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        # Create an array to track population changes
        people = [0] * 101  # 1950 to 2050 = 101 years

        # Mark population changes for each log
        for birth, death in logs:
            people[birth - 1950] += 1  # A person is born
            people[death - 1950] -= 1  # A person dies

        # Calculate the total population for each year
        for i in range(1, 101):
            people[i] += people[i - 1]

        # Find the year with the maximum population
        max_population = max(people)
        return people.index(max_population) + 1950