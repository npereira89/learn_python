# It does download profile photos user's instagram, all saved photos instagram with 
# a determinated date break and feed photos through a menu
import instaloader
import os, time
from datetime import datetime



def get_is_private(profile_name): #Get if a profile is private or public. 
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

    if result == True:   # if it's private should login required.
                
                print("You need to login for the profile name " +profile_name)
                L.interactive_login(profile_name)

    return result 

def menu():

    print("************ACTION**************")
    print(" 1 - Download Profile picture")
    print(" 2 - Download Profile Feed")
    print(" 3 - Download Saved Photos")
    print(" 4 - Exit")
    print("********************************")

    operation = int(input("Select action: "))

    if operation >= 5:
        print("Invalid operation")
        menu()
    elif operation <= 4:
        return int(operation)
    
L=instaloader.Instaloader(max_connection_attempts=3,
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

    operation = menu()
    
    if operation <=3:
        profile_name = input("Insert instagram profile: ")

    if operation == 1:            
        
        print("Downloading profile picture....")

        L.download_profile(profile_name, profile_pic_only=True) # download profile pic from profile
        print("Download completed!!")

        time.sleep(5)
        os.system('cls')

    elif operation == 2:
        
        get_is_private(profile_name)

        print("Downloading media feed....")

        L.download_profile(profile_name, profile_pic_only=False) # download photos from feed
        print("Download completed!!")

        time.sleep(5)
        os.system('cls')

    elif operation == 3:

        L.interactive_login(profile_name)

        print("Checking media saved....")

        profile = instaloader.Profile.from_username(L.context, profile_name)
        posts_saved = profile.get_saved_posts()

        date_string = input("Since date you want: ")


        SINCE = datetime.strptime(date_string, "%Y-%m-%d")  # further from today, inclusive. This date is of the date that user posted in Instagram.
        UNTIL = datetime.now() # closer to today, not inclusive.

        path = os.path.join('.\\', f"{profile_name}")

        try:
            os.makedirs(path)
            print(f"Folder created successfully at {path}")
            os.chmod(path, 0o777)
        except FileExistsError:
            print(f"Folder already exists at {path}")

        for post in posts_saved:
            postdate = post.date

            if SINCE <= postdate <= UNTIL:        
                if os.path.isdir(path)==True:
                    os.chdir(path)
                    L.download_post(post, "saved_collection" ) # download photos saved from collection has posted for user in determinated date (postdate)
            else:
                continue

        time.sleep(5)
        os.system('cls')

    elif operation == 4:

        print("Exiting the program...")
        os.sys.exit(0) 