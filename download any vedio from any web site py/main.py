import requests


def download_video(url):
    response = requests.get(url, stream=True)

    if response.status_code == 200:
        with open('video.mp4', "wb") as file:
            for chunk in response.iter_content(chunk_size=4096):
                file.write(chunk)

        print("Download complete!")
    else:
        print("Failed to download the video.")


video_url = input('Enter Video Url : ')


download_video(video_url)
