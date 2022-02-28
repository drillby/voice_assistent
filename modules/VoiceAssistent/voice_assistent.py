import datetime
import json
import os
import platform
import subprocess
from typing import List

import playsound
import speech_recognition as sr
from gtts import gTTS

from ..Spotify import Album, Artist, Playlist, Track

track = Track.Track()
playlist = Playlist.Playlist()
album = Album.Album()
artist = Artist.Artist()


class VoiceAssistent:
    def __init__(self, wake_word: str):
        self.wake_word = wake_word

        with open("speach_responses.json", "r") as f:
            self.speach_responses = json.load(f)

        with open("speach_key_words.json", "r") as f:
            self.key_words = json.load(f)

        with open("paths.json", "r") as f:
            self.paths = json.load(f)

        self.os = self.get_running_os()

    def get_audio(self) -> str:
        """Will get audio file

        Returns:
            str: returns said text, if no text is recognized empty str is returned
        """
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                return str(said).lower()
            except Exception:
                return ""

    def speak(self, msg: str) -> None:
        """Will say given message

        Args:
            msg (str): Message to say
        """
        tts = gTTS(text=msg, lang="en")
        voice_file = "voice.mp3"
        tts.save(voice_file)
        playsound.playsound(voice_file)

        return

    def get_running_os(self) -> str:
        """Will recognize running OS

        Returns:
            int: 1=linux, 2=windows
        """
        _os = platform.system().lower()
        return _os

    def get_pid_of_app(self, app: str) -> List[int]:
        """Will return the pid of the application

        Args:
            app (str): Name of the application

        Returns:
            List: List of PIDs(ints) related to the application
        """
        if self.os == "linux":
            return (
                subprocess.Popen(f"pidof {app}", shell=True, stdout=subprocess.PIPE)
                .communicate()[0]
                .decode("utf-8")
                .split(" ")
            )

    def get_opened_apps(self) -> str:
        """Will return a ByteString of the opened apps

        Returns:
            str: Opened apps
        """
        if self.os == "linux":
            return (
                subprocess.Popen("xlsclients", stdout=subprocess.PIPE)
                .communicate()[0]
                .decode("utf-8")
            )
        if self.os == "windows":
            return (
                subprocess.Popen("tasklist", stdout=subprocess.PIPE)
                .communicate()[0]
                .decode("utf-8")
            )

    def open_code(self, path: str) -> None:
        """Will open VSCode in the given path

        Args:
            path (str): Path to folder where you want to open VSCode
        """
        if self.os == "linux":
            os.popen(f"code {path}")
        elif self.os == "windows":
            pass

        return

    def close_code(self) -> None:
        """Will close VSCode"""
        if self.os == "linux":
            subprocess.Popen(
                f"kill {int(self.get_pid_of_app('code')[-1])}",
                stdout=subprocess.PIPE,
                shell=True,
            ).communicate()[0]
        elif self.os == "windows":
            pass

        return

    def open_chrome(self):
        """Will open Google Chrome"""
        os.popen("google-chrome")

        return

    def close_chrome(self):
        """Will close Google Chrome"""
        if self.os == "linux":
            subprocess.Popen(
                f"kill {int(self.get_pid_of_app('chrome')[-1])}",
                stdout=subprocess.PIPE,
                shell=True,
            ).communicate()[0]

        elif self.os == "windows":
            pass

        return

    def search_on_internet(self, search: str) -> None:
        """Will open Google Chrome and search for given search string

        Args:
            search (str): What you want to search for
        """
        url = "https://www.google.com/search?q="
        search = search.replace(" ", "+")
        url = url + search

        if self.os == "linux":
            subprocess.Popen(
                f"google-chrome {url}", stdout=subprocess.PIPE, shell=True
            ).communicate()[0]

        elif self.os == "windows":
            pass

        return

    def take_note(self, text: str) -> None:
        note_path = self.paths["linux"]["notes"]
        date = datetime.datetime.now()
        file_name = str(date).replace(":", "-").replace(" ", "_")[:19] + "-note.txt"
        with open(f"{note_path}/{file_name}", "w") as f:
            f.write(text)

    def read_note(self):
        pass

    def read_from_calendar(self):
        pass

    def open_spotify(self):
        """Will open Spotify"""
        if self.os == "linux":
            subprocess.Popen("spotify")

        elif self.os == "windows":
            pass

    def close_spotify(self):
        """Will close Spotify"""
        subprocess.Popen(
            f"kill {int(self.get_pid_of_app('spotify')[-1])}",
            stdout=subprocess.PIPE,
            shell=True,
        ).communicate()[0]

    def play_song(self, track_name: str) -> None:
        track.play(track_name, "drillby-Z97-D3H")

        return

    def play_artist(self, artist_name):
        artist.play(artist_name, "drillby-Z97-D3H")

        return

    def play_album(self, album_name: str):
        album.play(album_name, "drillby-Z97-D3H")

        return

    def play_playlist(self, playlist_name: str):
        playlist.play(playlist_name, "drillby-Z97-D3H")

        return
