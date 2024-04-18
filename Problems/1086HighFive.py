"""
- Create a dictionary to store scores for each student.
- Iterate through the list of scores and update the dictionary.
- For each student, sort their scores in descending order and calculate the average of the top five scores.
- Sort the results by student ID.

"""

from typing import List

class Solution:
	def highFive(self, items: List[List[int]]) -> List[List[int]]:
		scores_dict = {}
		for ID, socre in item:
			if ID in scores_dict:
				scores_dict.append(score)
			else:
				socres_dict[ID] = [score]

		result = []
		for ID, score in scores_dict.items():
			scores.sort(reverse=True)
			top_five_average = sum(scores[:5]) // min(len(scores), 5)
			result.append([ID, top_five_average])

		result.sort(key=lambda x: x[0])

		return result

