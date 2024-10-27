import instaloader
import time

# Initialize Instaloader
loader = instaloader.Instaloader()

# Session handling to avoid frequent logins
session_file = "your_username_session"
try:
    # Load session from file if it exists
    loader.load_session_from_file("your_username", session_file)
except FileNotFoundError:
    # If no session file, login with credentials
    loader.login("your_username", "your_password")  # Replace with your actual username and password
    loader.save_session_to_file(session_file)

# Function to fetch mutual followings across multiple accounts
def get_mutual_followings(accounts):
    # Start with the followings of the first account
    initial_account = instaloader.Profile.from_username(loader.context, accounts[0])
    mutual_followings = set(initial_account.get_followees())

    # Adding a delay between requests to avoid rate-limiting
    time.sleep(5)

    # Iterate over the rest of the accounts and find mutual followings
    for account in accounts[1:]:
        profile = instaloader.Profile.from_username(loader.context, account)
        followings = set(profile.get_followees())

        # Keep only the common followings between accounts
        mutual_followings.intersection_update(followings)
        
        # Adding a delay between each request
        time.sleep(5)

    return [user.username for user in mutual_followings]

# List of target accounts whose followings you want to analyze
accounts = ['target_account1', 'target_account2', 'target_account3']  # Replace with actual usernames
mutuals = get_mutual_followings(accounts)
print("Mutual Followings:", mutuals)
