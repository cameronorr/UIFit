import json

data = {}
data['GAP'] = []

data['GAP'].append({

	'Womens' : { 

	 	'XS' : {'ShirtLength': 22.8, 'ShoulderWidth': 14.375, 'LongSleeve': 31, 'HipWidth': 33.858, 'JeanLength': 26},
	 	'S' : {'ShirtLength': 23.622, 'ShoulderWidth': 14.75, 'LongSleeve': 31.5, 'HipWidth': 37.7953, 'JeanLength': 26},
	 	'M' : {'ShirtLength': 24.409, 'ShoulderWidth': 15.3333, 'LongSleeve': 31.875, 'HipWidth': 39.3701, 'JeanLength': 29},
	 	'L' : {'ShirtLength': 25.169, 'ShoulderWidth': 16, 'LongSleeve': 32.5, 'HipWidth': 42.12601, 'JeanLength': 29 },
	 	'XL' : {'ShirtLength': 25.9843, 'ShoulderWidth': 16.3333, 'LongSleeve': 33, 'HipWidth': 44.48821, 'JeanLength': 32},
	 	'2XL' : {'ShirtLength': 26.378, 'ShoulderWidth': 16.75, 'LongSleeve': 33.5, 'HipWidth': 46.85042, 'JeanLength': 32},
	 },

	 'Mens' : {

	 	'XS' : {'ShirtLength': 23.75, 'ShoulderWidth': 16.875, 'LongSleeve': 31.5, 'HipWidth': 28, 'JeanLength': 30},
	 	'S' : {'ShirtLength': 24.875, 'ShoulderWidth': 18.875, 'LongSleeve': 32.5, 'HipWidth': 31, 'JeanLength': 32},
	 	'M' : {'ShirtLength': 26.125, 'ShoulderWidth': 19.25, 'LongSleeve': 33.5, 'HipWidth': 34, 'JeanLength': 32},
	 	'L' : {'ShirtLength': 26.5, 'ShoulderWidth': 20.125, 'LongSleeve': 34.5, 'HipWidth': 36, 'JeanLength': 33},
	 	'XL' : {'ShirtLength': 26.875, 'ShoulderWidth': 20.875, 'LongSleeve': 35.25, 'HipWidth': 40, 'JeanLength': 34},
	 	'2XL' : {'ShirtLength': 27.25, 'ShoulderWidth': 22, 'LongSleeve': 35.75, 'HipWidth': 44, 'JeanLength': 34},


	 }

})

data['Abercrombie'] = []

data['Abercrombie'].append({

	'Womens' : { 

	 	'XS' : {'ShirtLength': 21.8, 'ShoulderWidth': 13.375, 'LongSleeve': 30, 'HipWidth': 32.858, 'JeanLength': 25},
	 	'S' : {'ShirtLength': 22.622, 'ShoulderWidth': 13.75, 'LongSleeve': 30.5, 'HipWidth': 36.7953, 'JeanLength': 25},
	 	'M' : {'ShirtLength': 23.409, 'ShoulderWidth': 14.3333, 'LongSleeve': 30.875, 'HipWidth': 38.3701, 'JeanLength': 28},
	 	'L' : {'ShirtLength': 24.169, 'ShoulderWidth': 15, 'LongSleeve': 31.5, 'HipWidth': 41.12601, 'JeanLength': 27},
	 	'XL' : {'ShirtLength': 24.9843, 'ShoulderWidth': 15.3333, 'LongSleeve': 32, 'HipWidth': 43.48821, 'JeanLength': 31},
	 	'2XL' : {'ShirtLength': 25.378, 'ShoulderWidth': 15.75, 'LongSleeve': 32.5, 'HipWidth': 45.85042, 'JeanLength': 31},
	 },

	 'Mens' : {

	 	'XS' : {'ShirtLength': 23.75, 'ShoulderWidth': 16.875, 'LongSleeve': 31.5, 'HipWidth': 28, 'JeanLength': 30},
	 	'S' : {'ShirtLength': 2.875, 'ShoulderWidth': 18.875, 'LongSleeve': 32.5, 'HipWidth': 31, 'JeanLength': 32},
	 	'M' : {'ShirtLength': 26.125, 'ShoulderWidth': 19.25, 'LongSleeve': 33.5, 'HipWidth': 34, 'JeanLength': 32},
	 	'L' : {'ShirtLength': 26.5, 'ShoulderWidth': 20.125, 'LongSleeve': 34.5, 'HipWidth': 36, 'JeanLength': 33},
	 	'XL' : {'ShirtLength': 26.875, 'ShoulderWidth': 20.875, 'LongSleeve': 35.25, 'HipWidth': 40, 'JeanLength': 34},
	 	'2XL' : {'ShirtLength': 27.25, 'ShoulderWidth': 22, 'LongSleeve': 35.75, 'HipWidth': 44, 'JeanLength': 34},


	 }

})


with open('data.txt', 'w') as outfile:
	json.dump(data, outfile)