class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        people = [0] * 101  
        for birth, death in logs:
            people[birth - 1950] += 1 
            people[death - 1950] -= 1  
        for i in range(1, 101):
            people[i] += people[i - 1]
        max_population = max(people)
        return people.index(max_population) + 1950