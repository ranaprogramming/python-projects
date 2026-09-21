"""
Student Grade Calculator
--------------------------
Demonstrates:
- a basic class bundling data (name, scores) with behavior (methods)
- input validation via raising ValueError instead of silently accepting bad data
- guarding against empty-list edge cases (division by zero)
- built-in max()/min() instead of hand-written loops
- an if/elif chain for letter grading
- max(..., key=lambda ...) to compare objects by a computed value
"""


class Student:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_score(self, value):
        """Add a score, rejecting anything outside a valid 0-100 range."""
        if not (0 <= value <= 100):
            raise ValueError(f"Score must be between 0 and 100, got {value}")
        self.scores.append(value)

    def average(self):
        if not self.scores:
            return 0
        return sum(self.scores) / len(self.scores)

    def highest(self):
        return max(self.scores) if self.scores else None

    def lowest(self):
        return min(self.scores) if self.scores else None

    def letter_grade(self):
        avg = self.average()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    def __repr__(self):
        return f"Student({self.name!r}, avg={self.average():.1f}, grade={self.letter_grade()})"


def top_student(students):
    """Return the Student object with the highest average, compared via key=."""
    return max(students, key=lambda s: s.average())


def add_scores_safely(student, scores):
    """Add a batch of scores, catching and reporting any invalid ones
    instead of letting one bad value stop the whole batch."""
    for value in scores:
        try:
            student.add_score(value)
        except ValueError as e:
            print(f"  Skipped invalid score for {student.name}: {e}")


def main():
    students = [
        Student("Ali"),
        Student("Sara"),
        Student("Bilal"),
    ]

    add_scores_safely(students[0], [85, 90, 78, 92])
    add_scores_safely(students[1], [95, 88, 91, 105])   # 105 will be rejected
    add_scores_safely(students[2], [60, 72, 65, -5])    # -5 will be rejected

    print("\n--- Report Card ---")
    for s in students:
        print(f"{s.name:10} avg={s.average():5.1f}  "
              f"high={s.highest():>3}  low={s.lowest():>3}  grade={s.letter_grade()}")

    best = top_student(students)
    print(f"\nTop student: {best.name} with an average of {best.average():.1f}")


if __name__ == "__main__":
    main()