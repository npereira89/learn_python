# It does download for all saved, feed and profile photos user's instagram
# through a menu used to input all the informations
import instaloader
import os, time
from datetime import datetime

#Get if a profile is private or public. 
def GetIsPrivate(profile_name):
    L = instaloader.Instaloader(max_connection_attempts=3,
                download_pictures=True,
                download_videos=False,
                download_video_thumbnails=False,
                download_geotags=False,
                download_comments=False,
                post_metadata_txt_pattern="",
                save_metadata=False,
                request_timeout=300
            )
    
    profile = instaloader.Profile.from_username( L.context, profile_name)
    result = profile.is_private

    # if it's private should login required.

    if result == True: 
                print("You need to login for the profile name " +profile_name)
                L.interactive_login(profile_name)

    return result  # return of result to menu.

def Menu():
    while True:
        print("************ACTION**************")
        print(" 1 - Download Profile picture")
        print(" 2 - Download Profile Feed")
        print(" 3 - Download Saved Photos")
        print(" 4 - Exit")
        print("********************************")

        operation = input("Select action: ")

        if operation >= "5":

            print("Invalid operation")
            continue

        else:
            L = instaloader.Instaloader(max_connection_attempts=3,
                download_pictures=True,
                download_videos=False,
                download_video_thumbnails=False,
                download_geotags=False,
                download_comments=False,
                post_metadata_txt_pattern="",
                save_metadata=False,
                request_timeout=300
            )

            profile_name = input("Insert instagram profile: ")

        if operation == "1":            

            print("Downloading profile picture....")
            L.download_profile(profile_name, profile_pic_only=True) # download profile pic from profile
            print("Download completed!!")
            time.sleep(5)
            os.system('cls')
            Menu()

        elif operation == "2":

            GetIsPrivate(profile_name)

            print("Downloading media feed....")
            L.download_profile(profile_name, profile_pic_only=False) # download photos from feed
            print("Download completed!!")
            time.sleep(5)
            os.system('cls')
            Menu() 

        elif operation == "3":
    
            L.interactive_login(profile_name)

            print("Checking media saved....")
            profile = instaloader.Profile.from_username(L.context, profile_name)
            posts_saved = profile.get_saved_posts()

            SINCE = datetime(2023, 7, 28)  # further from today, inclusive. This date is of the date that user posted in Instagram.
            UNTIL = datetime(2023, 7, 30)  # closer to today, not inclusive. This date is of the date that user posted in Instagram.

            for post in posts_saved:
                postdate = post.date

                if SINCE <= postdate <= UNTIL:
                    L.download_post(post, ":saved") # download photos saved from collection has posted for user in determinated date (postdate)
                else:
                    continue

            time.sleep(5)
            os.system('cls')
            Menu()

        elif operation == "4":

            print("Exiting the program...")
            exit(0)
        
        if operation.isnumeric()==False:
            break

Menu()