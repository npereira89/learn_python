# It does download profile photos user's instagram, all saved photos instagram with 
# a determinated date break and feed photos through a menu
import os
import time
from datetime import datetime
import instaloader


def get_is_private(profile_name, link_insta):  # Get if a profile is private or public.

    profile = instaloader.Profile.from_username(link_insta.context, profile_name)

    result = profile.is_private

    if result:  # if it's private should login required.

        print("You need to login for the profile name " + profile_name)
        link_insta.interactive_login(profile_name)

    return result


def main_menu():
    print("************ACTION**************")
    print(" 1 - Download Profile picture")
    print(" 2 - Download Profile Feed")
    print(" 3 - Download Saved Photos")
    print(" 4 - Download Videos Stories")
    print(" 5 - Exit")
    print("********************************")

    operation = int(input("Select action: "))
    return operation


user = instaloader.Instaloader(max_connection_attempts=3,
                               download_pictures=True,
                               download_videos=False,
                               download_video_thumbnails=False,
                               download_geotags=False,
                               download_comments=False,
                               post_metadata_txt_pattern="",
                               save_metadata=False,
                               request_timeout=300
                               )

while True:
    operation = main_menu()

    if operation >= 6:
        print("Invalid operation")
        os.system('cls')

    if operation <= 4:
        profile_name = input("Insert instagram profile: ")

    if operation == 1:
        print("Downloading profile picture....")
        user.download_profile(profile_name, profile_pic_only=True)  # download profile pic from profile
        print("Download completed!!")
        time.sleep(5)
        os.system('cls')

    elif operation == 2:

        get_is_private(profile_name, user)

        print("Downloading media feed....")

        user.download_profile(profile_name, profile_pic_only=False)  # download photos from feed
        print("Download completed!!")

        time.sleep(5)
        os.system('cls')

    elif operation == 3:

        user.interactive_login(profile_name)

        print("Checking media saved....")

        profile = instaloader.Profile.from_username(user.context, profile_name)
        posts_saved = profile.get_saved_posts()

        date_string = input("Since date you want: ")

        SINCE = datetime.strptime(date_string,
                                  "%Y-%m-%d")  # further from today, inclusive.
        # This date is of the date that user posted in Instagram.
        UNTIL = datetime.now()  # closer to today, not inclusive.

        path = os.path.join('.\\', f"{profile_name}")

        try:
            os.makedirs(path)
            print(f"Folder created successfully at {path}")
        except FileExistsError:
            print(f"Folder already exists at {path}")

        for post in posts_saved:
            postdate = post.date

            if SINCE <= postdate <= UNTIL:
                if os.path.isdir(path):
                    os.chdir(path)
                    user.download_post(post,
                                       "saved_collection")  # download photos saved from collection
                    # has posted for user in determinate date (postdate)
            else:
                continue

        time.sleep(5)
        os.system('cls')

    elif operation == 4:

        user.interactive_login(profile_name)

        print("Downloading story instagram....")
        profile = instaloader.Profile.from_username(user.context, profile_name)

        path = os.path.join('.\\', f"{profile_name}")

        try:
            os.makedirs(path)
            print(f"Folder created successfully at {path}")
        except FileExistsError:
            print(f"Folder already exists at {path}")

        os.chdir(path)
        user.download_stories(userids=[profile.userid], filename_target='stories')
        os.system('cls')

    elif operation == 5:

        print("Exiting the program...")
        os.sys.exit(0)
