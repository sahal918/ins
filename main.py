# Import necessary libraries
import time

# Function to follow a user
def follow_user(username):
    print(f"Following {username}...")
    # Code to follow the user

# Function to unfollow a user
def unfollow_user(username):
    print(f"Unfollowing {username}...")
    # Code to unfollow the user

# Function to calculate remaining time
def calculate_remaining_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    print(f"Remaining time: {minutes} minutes {seconds} seconds")

# Main program
def main():
    # Get user credentials
    username = input("Enter your Instagram username: ")
    password = input("Enter your Instagram password: ")

    # Login to Instagram
    print("Logging in...")
    # Code to login

    # List of usernames to follow
    usernames = input("Enter the usernames to follow (separated by commas): ").split(",")

    # Follow users
    for username in usernames:
        follow_user(username)
        time.sleep(30)
        calculate_remaining_time(180)

    # Wait for 3 minutes
    print("Waiting for 3 minutes...")
    time.sleep(180)
    calculate_remaining_time(180)

    # Unfollow users
    for username in usernames:
        unfollow_user(username)
        time.sleep(15)
        calculate_remaining_time(90)

    # Sleep for 5-10 minutes
    sleep_time = random.randint(300, 600)
    print(f"Sleeping for {sleep_time} seconds...")
    time.sleep(sleep_time)
    calculate_remaining_time(sleep_time)

    # Repeat the process
    main()

# Run the program
if __name__ == "__main__":
    main()
