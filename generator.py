import imageio
import os


clip = os.path.abspath('My face reveal hope you like it.mp4')

def gifMaker(inputPath,tarFormat):
    outputPath = os.path.splitext(inputPath)[0] + tarFormat
    
    print(f'converting {inputPath} \n to {outputPath}')
    
    reader = imageio.get_reader(inputPath)
    
    fps = reader.get_meta_dat()['fps']
    
    writer = imageio.get_writer(outputPath,fps=fps)
    
    for frame in reader:
        writer.append_data(frame)
        print(f'Frame {frame}')
        
    print("Done!")
    writer.close()
    
    
gifMaker(clip,'.gif')