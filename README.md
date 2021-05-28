# FfmPeg-Transcoding
Transcoding - It is a process of converting an audio or video file from one encoding format to another in order to increase the number of compatible target device a media file can be played on . In other words it is the process of exporting digital video into a particular format.

Basically, When the video is streaming over enough bandwidth networks, the delivered video quality is good. But when the link is congested and bandwidth is not enough to transmit all the video packets, the delivered video quality is worse. So in this case, we can use transcoding to let the bandwidth requirement for video streaming become less. Then the delivered video quality may not be good, but can still be acceptable.

Implementation 

1. Download a yuv format file and convert into mpegts 
2. Open the terminal and run the python.py file(when there is enough bandwidth) and python1.py(when there is no enough bandwidth)
3. Open xterminal h1(sender) and h2(reciever) and in case of transcoding h3(for transcoding)
4. In h1 - command is - ffmpeg -re -i abc.ts(video file) -c copy -f mpegts udp://192.168.10.2:1234
5. In h2 - command is - ffmpeg -i  udp://192.168.10.2:1234 -c copy new.ts(recieving file)
6. After recieving in h2 convert recieved file to yuv format.
7. Compare original yuv and recieved yuv using PSNR value 
8. For enough bandwidth PSNR value will be high and when there is no enough bandwidth there will be less PSNR value
9. When transcoding is used using H3 xterm (run same python1.py file where there is no enough bandwidth) we will get better PSNR value than previous(no enough bandwidth)
 
