import urllib.request
import moviepy.video.io.VideoFileClip
import praw
from moviepy.editor import CompositeVideoClip
import textwrap
import shutil
from termcolor import colored

videos = int(input('How many videos do you want:  '))
count = 1
video = moviepy.editor.VideoFileClip('bg_Image/WhatsApp Video 2022-07-13 at 3.34.42 PM.mp4')
reddit = praw.Reddit(client_id='UvjXADxJw01gjlm3KU9vlQ', client_secret='f2rc7lN8lbMTwBEaRd0bT46L31CrEg', user_agent='Python1.0', username='ODOshmockenberg',)
subreddit = reddit.subreddit("MapPorn")
Text3 = False
Text4 = False
destination = 'D:\Reddit Videos'
Error = 0
LogoError = 0
IndexError = 0
ErrnoError = 0

for submission in subreddit.hot(limit=None):


    url = str(submission.url)
    title = submission.title
    parts = textwrap.wrap(title, 25)


    try:
        # Check if the link is an image
        if url.endswith("jpg") or url.endswith("jpeg") or url.endswith("png"):

            # Retrieve the image and save it in current folder
            Imagename = f"Images/image{count}.png"
            save = urllib.request.urlretrieve(url, Imagename)
            try:
                logo = (moviepy.editor.ImageClip(Imagename).set_duration(10).resize(height=250).set_pos('center'))
            except:
                Error += 1
                LogoError += 1
            txt1 = (moviepy.editor.TextClip(parts[0], fontsize=30, color='white'))
            txt1 = txt1.set_position((10, 15)).set_duration(10)


            if len(title) > 25:
                try:
                    Text2 = True
                    txt2 = (moviepy.editor.TextClip(parts[1], fontsize=30, color='white'))
                    txt2 = txt2.set_position((10, 40)).set_duration(10)
                except:
                    Error += 1
                    IndexError += 1
                    print(colored('IndexError', 'green'))

                if len(title) > 50:
                    try:
                        Text3 = True
                        txt3 = (moviepy.editor.TextClip(parts[2], fontsize=30, color='white'))
                        txt3 = txt3.set_position((10, 70)).set_duration(10)
                    except:
                        Error += 1
                        IndexError += 1
                        print(colored('IndexError', 'green'))
                    if len(title) > 75:
                        try:
                            Text4 = True
                            txt4 = (moviepy.editor.TextClip(parts[3], fontsize=30, color='white'))
                            txt4 = txt4.set_position((10, 100)).set_duration(10)
                        except:
                            Error += 1
                            IndexError += 1
                            print(colored('IndexError', 'green'))

                if Text3 == True:
                    if Text4 == True:
                        final_video = moviepy.editor.CompositeVideoClip([video, logo, txt1, txt2, txt3, txt4])
                    else: final_video = moviepy.editor.CompositeVideoClip([video, logo, txt1, txt2, txt3])
                else:

                    final_video = moviepy.editor.CompositeVideoClip([video, logo, txt1, txt2,])
            else:
                final_video = moviepy.editor.CompositeVideoClip([video, logo, txt1])
            try:
                video_name = f'{count, title}test.mp4'
                final_video.write_videofile(video_name, fps=60)
            except IOError:
                print('Errno32')
                ErrnoError += 1
                Error += 1


            print('This is number :', count)
            count += 1

            try:
                shutil.move(video_name, destination)
                print(video_name + " was moved")
            except :
                print(video_name + " was not found")
            if count == videos:
                succesful = videos - Error
                print(colored(f'{succesful}videos', 'red'))
                break
    except:
        Error +=1
