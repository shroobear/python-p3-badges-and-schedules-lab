def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_list = [badge_maker(name) for name in names]
    return badge_list

def assign_rooms(names):
    assignments = []
    for index, name in enumerate(names):
        assignments.append(f"Hello, {name}! You'll be assigned to room {index + 1}!")
    return assignments


def printer(names):
    nametags = batch_badge_creator(names)
    rooms = assign_rooms(names)
    for badge in nametags:
        print(badge)
    for assignment in rooms:
        print(assignment)

printer(["Guido", "Edsger", "Ada", "Charles", "Alan", "Grace", "Linus", "Matz"])