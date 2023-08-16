from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def find_stream_by_resolution(streams, resolution):
    for stream in streams:
        if resolution in stream.resolution:
            return stream
    return None

def download_video(video_url, save_path='.', quality='720p'):
    try:
        yt = YouTube(video_url)
        
        # Filter streams to include only progressive video streams
        video_streams = yt.streams.filter(progressive=True).order_by("resolution").desc()
        
        # Find the appropriate stream based on the desired quality
        video_stream = find_stream_by_resolution(video_streams, quality)
        
        if video_stream:
            video_title = video_stream.title
            print(f"Downloading: {video_title} in {quality}")
            
            downloaded_file_path = video_stream.download(output_path=save_path, filename_prefix="download_in_progress")
            
            # Rename the downloaded file to remove the "download_in_progress" prefix
            new_filename = f"{save_path}/{video_title}.{downloaded_file_path.split('.')[-1]}"
            os.rename(downloaded_file_path, new_filename)
            
            # Convert to MP4 using moviepy
            if new_filename.endswith(".3gpp"):
                mp4_filename = new_filename.replace(".3gpp", ".mp4")
                clip = VideoFileClip(new_filename)
                clip.write_videofile(mp4_filename)
                clip.close()
                os.remove(new_filename)  # Remove the original 3gpp file
                
                print("Video converted to MP4.")
            
            print("Video downloaded and converted successfully.")
        else:
            print(f"No {quality} stream found for the video.")
    except Exception as e:
        print("Error:", str(e))

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    quality = input("Enter the desired quality (i.e, 144p, 240p, 360p, 480p, 720p, 1080p): ")
    
    download_video(video_url, quality=quality)
