import time

def login(username, password):
    # Code to login to Instagram
    pass

def follow_user(username):
    # Code to follow a user on Instagram
    pass

def unfollow_user(username):
    # Code to unfollow a user on Instagram
    pass

def main():
    # Login to Instagram
    login("your_username", "your_password")
    
    # List of usernames to follow
    usernames = ["user1", "user2", "user3"]
    
    # Follow users one by one with a gap of 30 seconds
    for username in usernames:
        follow_user(username)
        print("Followed", username)
        time.sleep(30)
    
    # Wait for 3 minutes
    time.sleep(180)
    
    # Unfollow users one by one with a gap of 15 seconds
    for username in usernames:
        unfollow_user(username)
        print("Unfollowed", username)
        time.sleep(15)
    
    # Sleep for 5 to 10 minutes
    sleep_time = random.randint(300, 600)
    print("Sleeping for", sleep_time, "seconds")
    time.sleep(sleep_time)
    
    # Repeat the process
    main()

if __name__ == "__main__":
    main()
