score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("Excellent")
elif score >= 50:
    print("Passable")
else:
    print("Bad")






import random

def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

    # 新增：随机成绩
    random_score = random.uniform(0, 100)
    random_result = determine_result(random_score)
    print(f"Random score: {random_score:.2f} => {random_result}")

def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
