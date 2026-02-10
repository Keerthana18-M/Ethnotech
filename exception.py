# --- STEP 1: Create your Custom Exception ---
class AgeRestrictionError(Exception):
    """Exception raised when a user is too young for a movie."""
    def __init__(self, age, movie_name):
        self.age = age
        self.movie_name = movie_name
        super().__init__(f"Access Denied: {age} is too young for {movie_name}.")

# --- STEP 2: The Main Project Logic ---
def buy_ticket():
    # A simple database of movies and their age requirements
    movies = {
        "Baby's Day Out": 0,
        "The Batman": 13,
        "Deadpool": 18,
        "Toxic": 18
    }

    print("--- Welcome to the Cinema Booking System ---")
    print(f"Available Movies: {', '.join(movies.keys())}")

    try:
        # 1. Get User Input
        choice = input("\nEnter the movie name: ").strip()
        
        if choice not in movies:
            raise KeyError("That movie is not in our current schedule.")

        user_age = int(input("Enter your age: "))

        # 2. Check for Negative Age (Logic Error)
        if user_age < 0:
            raise ValueError("Age cannot be a negative number.")

        # 3. Check Age Requirement (Custom Exception)
        if user_age < movies[choice]:
            raise AgeRestrictionError(user_age, choice)

    # --- STEP 3: Handle the Errors ---
    except ValueError as ve:
        print(f"Input Error: {ve}")
        
    except KeyError as ke:
        print(f"Selection Error: {ke}")
        
    except AgeRestrictionError as are:
        print(are)  # This prints the message we defined in the __init__
        print("Please choose a different movie suitable for your age.")
        
    except Exception as e:
        print(f"Something went wrong: {e}")

    else:
        # Runs only if no exceptions were raised
        print(f"Payment Successful! Enjoy watching '{choice}'.")

    finally:
        # Runs no matter what
        print("Thank you for using the Cinema Booking System.")

# Run the project
if __name__ == "__main__":
    buy_ticket()