# -*- coding: utf-8 -*-


class Downloader(object):

    def __init__(self):
        pass

    def download(self, url, save_path):
        import ffmpeg as ff

        input_source = ff.input(url)
        save_video = ff.output(input_source, save_path)
        ff.run(save_video)

        return True
