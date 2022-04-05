import subprocess
import os

def cutVideo():
    # file_time = ffmpeg.probe(file_name)['format']['duration']    # 视频总时长 秒
    print(file_name)

if __name__ == '__main__':
    iPath = 'C://Users//liliu//Videos//Captures//'
    start_time = '00:02:20'     # 开始时间
    lasts_time = '00:02:00'     # 截取多长时间

    file_Suffix = ['.mp4', '.MP4']
    file_names = [name for name in os.listdir(iPath) for item in file_Suffix if
                  os.path.splitext(name)[1] == item]
    for i in file_names:
        file_name = iPath + i
        save_name = iPath + '截取' + i
        print(save_name)
        subprocess.call('ffmpeg//bin//ffmpeg.exe -y -i ' +  file_name + ' -ss ' + start_time + ' -t '+ lasts_time + ' -acodec copy -vcodec copy -async 1 ' + save_name)


print('完成')