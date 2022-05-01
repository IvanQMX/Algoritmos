class Activity:
    def __init__(self, start, finish):
        self.start = start
        self.finish = finish

    def __str__(self):
        return f'({self.start}, {self.finish})'


def printMaxActivities(arr, n):
    # Sort jobs according to finish time
    arr.sort(key=lambda x: x.finish)

    # The first activity always gets selected
    i = 0
    print(arr[i])

    for j in range(1, n):
        if arr[j].start >= arr[i].finish:
            print(arr[j])
            i = j

activities = []
activities.append(Activity(5, 9))
activities.append(Activity(1, 2))
activities.append(Activity(3, 4))
activities.append(Activity(0, 6))
activities.append(Activity(5, 7))
activities.append(Activity(8, 9))
activities.append(Activity(5, 6))
activities.append(Activity(7, 8))
n = len(activities)
print("Actividades seleccionadas :")
printMaxActivities(activities, n)
