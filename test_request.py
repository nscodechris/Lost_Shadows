
import requests
import os
from bs4 import BeautifulSoup
import re

CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))


class MusicDownload:
    def __init__(self, url):
        self.url = url
        self.folder_url = "https://drive.google.com/drive/folders/15TyBVDzYyffK0SOBLBCFKgtjeaDiFq1Y"
        self.name_list = []
        self.id_list = []
        self.url_name_class = "Q5txwe"
        self.url_name_attribute = "aria-label"
        self.url_id_class = "WYuW0e"
        self.url_id_attribute = "data-id"
        self.music_name_dict = {}
        self.music_id_dict = {}
        self.folder_name_list = []
        self.x = 0

    def get_folder_name(self):
        URL = self.folder_url
        page = requests.get(URL)
        # print(page.text)
        soup = BeautifulSoup(page.content, "html.parser")
        # print(soup)
        results = soup.find(id="drive_main_page")
        # print(results.prettify())
        job_elements_name = results.find_all("div", class_=self.url_name_class)
        for job_elements_name in job_elements_name:
            # title_music = results["div aria-label"]
            # print(job_elements, end="\n"*2)
            music_name = job_elements_name[self.url_name_attribute]
            self.folder_name_list.append(music_name)

    def get_music_name_id(self):
        URL = self.url
        page = requests.get(URL)
        # print(page.text)
        soup = BeautifulSoup(page.content, "html.parser")
        # print(soup)
        results = soup.find(id="drive_main_page")
        # print(results.prettify())
        job_elements_name = results.find_all("div", class_=self.url_name_class)
        for job_elements_name in job_elements_name:
            # title_music = results["div aria-label"]
            # print(job_elements, end="\n"*2)
            music_name = job_elements_name[self.url_name_attribute]
            self.name_list.append(music_name)
        job_elements_id = results.find_all("div", class_=self.url_id_class)
        for job_elements_id in job_elements_id:
            music_id = job_elements_id[self.url_id_attribute]
            self.id_list.append(music_id)
        MusicDownload.create_folders(self)
    def download_file_from_google_drive(self, id, destination):
        URL = "https://docs.google.com/uc?export=download"

        session = requests.Session()

        response = session.get(URL, params={'id': id}, stream=True)
        token = MusicDownload.get_confirm_token(self, response)

        if token:
            params = {'id': id, 'confirm': token}
            response = session.get(URL, params=params, stream=True)

        MusicDownload.save_response_content(self, response, destination)

    def get_confirm_token(self, response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value

        return None

    def save_response_content(self, response, destination):
        CHUNK_SIZE = 32768

        with open(destination, "wb") as f:
            for chunk in response.iter_content(CHUNK_SIZE):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)


    def create_folders(self):

        regex = "([^\\s]+(\\.(?i)(jpe?g|png|gif|bmp|mp3))$)"
        p = re.compile(regex)

        # print(f"self x {main_folder.x}")
        for i in self.name_list:
            if re.search(p, i):
                folder_name = self.folder_name_list[main_folder.x]
                # print(folder_name)
                self.music_name_dict = {folder_name: self.name_list}
                self.music_id_dict = {folder_name: self.id_list}
                main_folder.x += 1
                MusicDownload.download_music(self)
            else:
                for i in self.name_list:
                    rootdir = CURR_DIR_PATH + "\\music"
                    if i not in os.listdir(rootdir):
                        os.mkdir(rootdir + "\\" + i)

            try:
                get_music = MusicDownload(f"https://drive.google.com/drive/folders/{main_folder.id_list[main_folder.x]}")
                # main_folder.x += 1
                get_music.get_folder_name()
                get_music.get_music_name_id()
            except:
                print()


    def download_music(self):
        for key, value in self.music_id_dict.items():
            for x in range(0, len(value)):
                # print(x)
                folder = key
                file_id = value[x]
                # print(file_id)
                song_name = self.music_name_dict[key][x]
                # print(folder, file_id, song_name)
                print(f"Downloading music: {song_name}")
                destination = CURR_DIR_PATH + "\\music" + "\\" + folder + "\\" + song_name
                MusicDownload.download_file_from_google_drive(self, file_id, destination)
                print(f"The music {song_name} has been downloaded")

main_folder = MusicDownload("https://drive.google.com/drive/folders/15TyBVDzYyffK0SOBLBCFKgtjeaDiFq1Y")
main_folder.get_folder_name()
main_folder.get_music_name_id()
