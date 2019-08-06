import imageio
import argparse
from pathlib import Path

parser = argparse.ArgumentParser(description='Create gif from images.')
parser.add_argument('path_images', type=str)
parser.add_argument('output_name', type=str)
parser.add_argument('fps', type=int, default=30)
args = parser.parse_args()

images = []
path_images = Path(args.path_images)
path_output = path_images / '{}{}'.format(args.output_name, '.mp4')

writer = imageio.get_writer(path_output, fps=args.fps)

for file in Path(args.path_images).glob('*.png'):
    writer.append_data(imageio.imread(file))

print("{} saved".format(path_output))
