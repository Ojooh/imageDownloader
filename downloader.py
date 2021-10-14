import os
import pandas as pd
import requests
import shutil
import csv


class imageDownloader():
    def __init__(self, csv_path, folder_name):
        self.csv_path = csv_path
        self.right_path = False
        self.main_dir = os.getcwd() 
        self.folder_name = folder_name

    def path_exists(self):
        if os.path.exists(self.csv_path):
            self.right_path = True
            self.img_dir = os.path.join(self.main_dir, "images", self.folder_name)
            print(self.img_dir)

            if not os.path.exists(self.img_dir) :
                os.makedirs(self.img_dir)

        else :
            self.right_path = False

    def get_CSV_data (self):
        if self.right_path:
            with open(self.csv_path, "r", encoding="utf8") as f:
                reader = csv.reader(f)
                for i, line in enumerate(reader):
                    if i >= 103:
                        image_name = line[3]
                        image_url = ""
                        if line[29] != "" and line[29] is not None:
                            image_url = line[29].split(",")
                            img_dir_cur = os.path.join(self.img_dir, image_name)
                            if not os.path.exists(img_dir_cur) :
                                os.makedirs(img_dir_cur)

                            for img in image_url:
                                self.get_img(img, img_dir_cur)
                        print(i)
                        print(image_name)
                        print(image_url)
           
        else:
            print("CSV path is not valid, please try again")
            return 0

    def get_img(self, url, diry):
        name = url.split("/")[-1]
        filename = os.path.join(diry, name)
        image_url = url
        r = requests.get(image_url, stream = True)
        r.raw.decode_content = True
        self.store_img(r, filename)

    def store_img(self, byte, name):
        with open(name,'wb') as f:
            shutil.copyfileobj(byte.raw, f)

    def download_image(self):
        print("started")
        self.path_exists()
        state = self.get_CSV_data()



if __name__ == '__main__':
    img_d = imageDownloader(r"C:\Users\david\Downloads\drinks2uproducts.csv", "drinks2u")
    img_d.download_image()

        