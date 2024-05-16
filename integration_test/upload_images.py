import os
import fnmatch

base_dir = "figures/test_data"

def find_png_images(directory):
    png_files = []
    for root, _, files in os.walk(directory):
        for filename in fnmatch.filter(files, '*.png'):
            png_files.append(os.path.join(root, filename))
    return png_files

directory = '.'
png_images = find_png_images(directory)
png_filenames = list(map(lambda s: s.split("/")[-1], png_images))
if len(png_filenames) != len(set(png_filenames)): # duplicates
    print("Duplicate files!")
    from collections import defaultdict
    indices = defaultdict(list)
    for index, item in enumerate(png_filenames):
        indices[item].append(index)
    for item, index_list in indices.items():
        if len(index_list) > 1:
            for idx in index_list:
                print(png_images[idx])
    print("Aborting...")
    exit(-1)

import pyoverleaf
api = pyoverleaf.Api()
api.login_from_browser()
projects = api.get_projects()
project = list(filter(lambda p: p.name == "ESD4", projects))[0]
project_id = project.id
io = pyoverleaf.ProjectIO(api, project_id)

for img in png_images:
    print(img)
    imgname = img.split("/")[-1]
    with io.open(os.path.join(base_dir, imgname), "wb+") as f:
        with open(img, "rb") as i:
            f.write(i.read())
