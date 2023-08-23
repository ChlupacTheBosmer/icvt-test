import subprocess
import json

def get_video_metadata(video_path):
    try:
        # Run ffprobe command to get video metadata in JSON format
        command = ["mediainfo", "--Output=JSON", video_path]
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Parse the JSON output
        metadata = json.loads(result.stdout)
        return metadata["format"]

    except Exception as e:
        print(f"Error getting video metadata: {e}")
        return None


if __name__ == "__main__":
    video_path = r"D:\Dílna\Kutění\Python\Videos\Problematic Videos\milesight\CZ2_M2_ErySpp03_20210616_14_45.avi"
    video_metadata = get_video_metadata(video_path)

    if video_metadata:
        print("Video Metadata:")
        for key, value in video_metadata.items():
            print(f"{key}: {value}")
    else:
        print("Unable to retrieve video metadata.")