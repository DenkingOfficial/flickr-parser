import flickrapi
import os
import urllib.request
from tqdm import tqdm
import argparse

def create_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-k", "--key", help="Flickr API Key in format 1st_part:2nd_part", required=True)
    parser.add_argument("-w", "--word", help="Search images using this keyword", required=True)
    parser.add_argument("-n", "--num", help="Number of images to parse", required=True)
    parser.add_argument("-o", "--output", help="Output folder", required=True)
    args = parser.parse_args()
    return args

def parse_images(key, word, num, output):
    key = key.split(':')
    try:
        flickr = flickrapi.FlickrAPI(key[0], key[1], cache=True)
    except:
        print('Your API key is invalid')
        exit()
    photos = flickr.walk(text=word, tag_mode='all', tags=word, extras='url_c', per_page=100, sort='relevance')
    counter = 0
    pbar = tqdm(total=num)
    for photo in photos:
        url = photo.get('url_c')
        try:
            urllib.request.urlretrieve(url, f'{output}/{counter}.jpg')
            counter += 1
            pbar.update(1)
        except:
            pass
        if counter > num - 1:
            pbar.close()
            break
    print(f'{counter} Images downloaded to {output}')

def confirm_overwriting(question: str) -> bool:
    reply = None
    while reply not in ("y", "n"):
        reply = input(f"{question} (y/n): ").lower()
    return (reply == "y")

if __name__ == "__main__":
    args = create_arguments()
    if not os.path.isdir(args.output):
        os.mkdir(args.output)
    elif os.path.isdir(args.output) and len(os.listdir(args.output)) > 0:
        user_input = confirm_overwriting('Folder is not empty, files with the same names will be overwritted, are you sure to continue?')
        if user_input == False:
            exit('Restart an application and set other output folder')
    print(f'Parsing images to {args.output}')
    parse_images(args.key, args.word, int(args.num), args.output)