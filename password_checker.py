# password strength checker

import re 

# password strength check conditions:
# min 8 chars, digit, uppercase, lowercase, special char

def check_password_strength(password,conform_password):
    """
    Function to check the strength of a password.
    """
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    
    if not any(char.isdigit() for char in password):
        return "Weak: Password must include at least one number."
    
    if not any(char.isupper() for char in password):
        return "Weak: Password must include at least one uppercase letter."
    
    if not any(char.islower() for char in password):
        return "Weak: Password must include at least one lowercase letter."
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Medium: Add special characters to make your password stronger."
    
    if (password != conform_password):
    	return "Entered different password in both cases."
    	
    return "Strong: Your password is secure!"


    
    
def password_checker():
    """
    Main function to take user input and check password strength.
    """
    print("\n***Welcome to the Password Strength Checker!***")
    print("\nYour password must contains Letters, Numbers and Special characters...")

    while True:
        password = input("Enter your password (or type 'exit' to quit): ")
        if (password.lower() != "exit" ):
            conform_password = input("Re-enter your password: ")
        
        if password.lower() == "exit":
            print("Thank you for using the Password Strength Checker!")
            break
        
        result = check_password_strength(password,conform_password) 
        print(result)


# Run the password checker
if __name__ == "__main__":
    password_checker()
