from sklearn.tree import DecisionTreeClassifier

X = [

    [95, 90, 92],
    [90, 88, 85],

    [75, 70, 78],
    [80, 72, 76],

    [55, 60, 58],
    [50, 52, 48],

    [35, 40, 30],
    [25, 28, 20]

]

y = [

    "Excellent Student",
    "Excellent Student",

    "Good Student",
    "Good Student",

    "Average Student",
    "Average Student",

    "Needs Improvement",
    "Needs Improvement"

]

model = DecisionTreeClassifier()

model.fit(X, y)


def predict_student(math, science, english):

    prediction = model.predict([
        [math, science, english]
    ])

    return prediction[0]