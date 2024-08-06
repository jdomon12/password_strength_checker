import re

def check_password_strength(password):
    # Initialize the strength score
    strength_score = 0
    suggestions = []

    # Check length
    if len(password) >= 8:
        strength_score += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")

    # Check for digits
    if re.search(r"\d", password):
        strength_score += 1
    else:
        suggestions.append("Password should include at least one digit.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength_score += 1
    else:
        suggestions.append("Password should include at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength_score += 1
    else:
        suggestions.append("Password should include at least one lowercase letter.")

    # Check for special characters
    if re.search(r"[@$!%*?&]", password):
        strength_score += 1
    else:
        suggestions.append("Password should include at least one special character (@, $, !, %, *, ?, &).")

    return strength_score, suggestions

if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength, advice = check_password_strength(password)
    print(f"Password Strength Score: {strength}/5")
    if strength < 5:
        print("Suggestions to improve your password:")
        for suggestion in advice:
            print(f"- {suggestion}")
    else:
        print("Your password is strong!")
