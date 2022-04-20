def plant_recommendation(care):
    if care == 'low':
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'high': # I didn't notice that in first time :D
        print('orchid')

plant_recommendation('low')
plant_recommendation('medium')
plant_recommendation('high')