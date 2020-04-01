gamers = []


def add_gamer(gamer, gamers_list):
    if 'name' and 'availability' in gamer:
        gamers.append(gamer)


def build_daily_frequency_table():
    return {'Sunday': 0, 'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, "Saturday": 0}


def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer['availability']:
            count_availability[day] += 1


def find_best_night(availability_table):
    largest = float('-inf')
    best_night = ""
    for day in availability_table:
        if availability_table[day] > largest:
            largest = availability_table[day]
            best_night = day
    return best_night


kimberly = {'name': 'Kimberly Warner', 'availability': ['Monday', 'Tuesday', 'Friday']}
add_gamer(kimberly, gamers)
add_gamer({'name': 'Thomas Nelson', 'availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joyce Sellers', 'availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'Michelle Reyes', 'availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Stephen Adams', 'availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name': 'Latasha Bryan', 'availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name': 'Crystal Brewer', 'availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'James Barnes Jr.', 'availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Michel Trujillo', 'availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

count_availability = build_daily_frequency_table()
calculate_availability(gamers, count_availability)
game_night = find_best_night(count_availability)
print(game_night)


