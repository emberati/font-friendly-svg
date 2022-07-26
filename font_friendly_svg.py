from picosvg.svg import SVG
from os import mkdir, path, pardir, sep, walk
import pathlib


input_path = 'C:\\Users\\emb\\Desktop\\social_media_icons'
output_path = input_path.removesuffix('\\') + '_cleaned'

if not path.exists(output_path):
    mkdir(output_path, 0o777)

print(input_path)
print(output_path)

def from_dir(svgs_dir_path):
    cleaned_svgs_with_paths = []
    for (dirpath, dirnames, filenames) in walk(svgs_dir_path):
        for filename in filenames:
            filepath = path.join(dirpath, filename)

            svg = SVG.parse(filepath)
            svg.evenodd_to_nonzero_winding(inplace=True)
            svg.round_floats(3, inplace=True)

            # print('[ICON PATH]: %s\n' % (filepath))
            # print(svg.tostring(), end='\n\n')

            cleaned_svgs_with_paths.append((filename, svg.tostring()))
    return cleaned_svgs_with_paths


def save_all(cleaned_svgs_with_paths, dirname=None):

    if dirname is None:
        dirname = output_path

    for svg_with_path in cleaned_svgs_with_paths:

        filepath = path.join(dirname, svg_with_path[0])
        print(f'{filepath=}')

        file = open(filepath, 'w')
        file.write(svg_with_dpath[1])
        file.close()

save_all(from_dir(input_path))