from typing import List
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import subprocess
import datetime
import json
import platform
import errors.custome_errors
from Spotify import Track, Playlist, Album, Artist

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

        with open("code_projects_location.json", "r") as f:
            self.code_projects_location = json.load(f)

        self.os = self.get_running_os()

    def listen_for_wake_word(self) -> bool:
        """Will listen for wake word

        Returns:
            bool: Wake word registered
        """
        text = self.get_audio()
        if text.count(self.wake_word) > 0:
            return True
        else:
            return False

    def get_audio(self) -> str:
        """Will get audio

        Returns:
            str: str of audio
        """
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                return said
            except Exception:
                return errors.custome_errors.DidNotUnderstand.__str__(self)

    def speak(self, msg: str) -> None:
        """Will say given message

        Args:
            msg (str): Message to say
        """
        tts = gTTS(text=msg, lang="en", tld="ie")
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
            subprocess.Popen(
                "code .", stdout=subprocess.PIPE, shell=True, cwd=path
            ).communicate()[0]
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
        subprocess.Popen(
            "google-chrome", stdout=subprocess.PIPE, shell=True
        ).communicate()[0]

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

    def take_note(self):
        pass

    def read_note(self):
        pass

    def read_from_calendar(self):
        pass

    def open_spotify(self):
        """Will open Spotify"""
        if self.os == "linux":
            subprocess.Popen(
                "spotify", stdout=subprocess.PIPE, shell=True
            ).communicate()[0]

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
