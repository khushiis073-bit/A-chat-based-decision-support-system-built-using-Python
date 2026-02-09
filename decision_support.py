print("🤖 Welcome to the Interactive Decision Support System\n")

decision_type = input(
    "Select decision type (career / personal / financial): "
).lower()

score = 0

print("\nAnalyzing your decision...\n")

if decision_type == "career":
    print("Career Decision Selected\n")

    q1 = input("Does this decision align with your long-term career goals? (yes/no): ")
    if q1 == "yes":
        score += 3
    else:
        score -= 3

    q2 = input("Does this option offer growth and learning opportunities? (yes/no): ")
    if q2 == "yes":
        score += 2
    else:
        score -= 2

    q3 = input("Are you genuinely interested in developing the required skills? (yes/no): ")
    if q3 == "yes":
        score += 2
    else:
        score -= 2



elif decision_type == "personal":
    print("Personal Decision Selected\n")

    q1 = input("Will this decision improve your emotional well-being? (yes/no): ")
    if q1 == "yes":
        score += 3
    else:
        score -= 3

    q2 = input("Will this decision help maintain your mental peace? (yes/no): ")
    if q2 == "yes":
        score += 2
    else:
        score -= 2

    q3 = input("Are the chances of future regret low? (yes/no): ")
    if q3 == "yes":
        score += 1
    else:
        score -= 1



elif decision_type == "financial":
    print("Financial Decision Selected\n")

    q1 = input("Is this a financially safe option? (yes/no): ")
    if q1 == "yes":
        score += 3
    else:
        score -= 3

    q2 = input("Is the financial risk manageable? (yes/no): ")
    if q2 == "yes":
        score += 2
    else:
        score -= 2

    q3 = input("Does this decision have long-term financial benefits? (yes/no): ")
    if q3 == "yes":
        score += 2
    else:
        score -= 2


else:
    print("Invalid decision type selected.")
    print("Please restart and choose: career / personal / financial")
    exit()


print("\n Final Decision Score:", score)

print("\n Decision Recommendation:")
if score >= 5:
    print("✅ This decision appears to be a strong and positive choice. Proceed with confidence.")
elif score >= 2:
    print("⚠️ This decision involves some risk. Consider proper planning before proceeding.")
else:
    print("❌ This decision may not be advisable at the moment. Reconsider your options.")

print("\n  Thank you for using the Decision Support System.")
