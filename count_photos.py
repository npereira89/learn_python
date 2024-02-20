# It does to test a login instaloader application.
import instaloader

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

profile_name=input("introduza o nome: ")
pwd = input("introduza o password: ")

L.login(profile_name, pwd)        # (login)