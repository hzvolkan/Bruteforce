# Date: 15/11/2022
# Author: Volkan
# Twitter:VolkanErk
# İnstagram:Volkanhaznedaroglu01
# Github:hzvolkan


from os import system
from time import sleep
from .const import debug
from colorama import Fore
from builtins import input
from platform import system as platform


class Display(object):

    __is_color = None
    total_lines = None
    account_exists = None

    def __init__(self, username=None, passlist=None, is_color=None):
        self.delay = 1.3
        self.username = username
        self.passlist = passlist
        self.colors_disabled = True
        self.cls = "cls" if platform() == "Windows" else "clear"

        if Display.__is_color == None:
            Display.__is_color = is_color

    def clear(self):
        if not debug or self.colors_disabled:
            system(self.cls)

            if self.colors_disabled and self.__is_color:
                self.colors_disabled = False
        else:
            print("\n\n")

    def stats(self, password, attempts, browsers, load=True):
        self.clear()
        complete = round((attempts / Display.total_lines) * 100, 2)
        account_exists = (
            self.account_exists if self.account_exists != None else ""
        )

        if self.__is_color:
            print(
                "{0}[{1}-{0}] {1}Passwordlistesi Yolu: {2}{3}{4}".format(
                    Fore.YELLOW,
                    Fore.WHITE,
                    Fore.CYAN,
                    self.passlist,
                    Fore.RESET,
                )
            )

            print(
                "{0}[{1}-{0}] {1}Kullanıcı Adı: {2}{3}{4}".format(
                    Fore.YELLOW,
                    Fore.WHITE,
                    Fore.CYAN,
                    self.username.title(),
                    Fore.RESET,
                )
            )

            print(
                "{0}[{1}-{0}] {1}Şifre: {2}{3}{4}".format(
                    Fore.YELLOW, Fore.WHITE, Fore.CYAN, password, Fore.RESET
                )
            )

            print(
                "{0}[{1}-{0}] {1}Tamamlanan: {2}{3}%{4}".format(
                    Fore.YELLOW, Fore.WHITE, Fore.CYAN, complete, Fore.RESET
                )
            )

            print(
                "{0}[{1}-{0}] {1}Denenen Şifreler: {2}{3}{4}".format(
                    Fore.YELLOW, Fore.WHITE, Fore.CYAN, attempts, Fore.RESET
                )
            )

            print(
                "{0}[{1}-{0}] {1}Proxyler: {2}{3}{4}".format(
                    Fore.YELLOW, Fore.WHITE, Fore.CYAN, browsers, Fore.RESET
                )
            )

            print(
                "{0}[{1}-{0}] {1}Bağlantı: {2}{3}{4}".format(
                    Fore.YELLOW,
                    Fore.WHITE,
                    Fore.CYAN,
                    account_exists,
                    Fore.RESET,
                )
            )

        else:
            print(
                f"[-] Şifre Listesi: {self.passlist}\n[-] Kullanıcı Adı: {self.username}\n[-] Şifre: {password}"
            )

            print(
                f"Tamamlanan: {complete}\n[-] Şifre Denemeleri: {attempts}\n[-] Proxyler: {browsers}\n[-] Çıkartılan: {account_exists}"
            )

        if load:
            sleep(self.delay)

    def stats_found(self, password, attempts, browsers):
        self.stats(password, attempts, browsers, load=False)

        if self.__is_color:
            print(
                "\n{0}[{1}!{0}] {2}HEYY Kurbanın Şifresini Buldum {3}".format(
                    Fore.YELLOW, Fore.RED, Fore.WHITE, Fore.RESET
                )
            )

            print(
                "{0}[{1}+{0}] {2}Kullanıcı Adı: {1}{3}{4}".format(
                    Fore.YELLOW,
                    Fore.GREEN,
                    Fore.WHITE,
                    self.username.title(),
                    Fore.RESET,
                )
            )

            print(
                "{0}[{1}+{0}] {2}Şifresi: {1}{3}{4}".format(
                    Fore.YELLOW, Fore.GREEN, Fore.WHITE, password, Fore.RESET
                )
            )
        else:
            print(
                "\n[!] HEYY Kurbanın Şifresini Buldum\n[+] Kullanıcı Adı: {}\n[+] Şifresi: {}".format(
                    self.username.title(), password
                )
            )

        sleep(self.delay)

    def stats_not_found(self, password, attempts, browsers):
        self.stats(password, attempts, browsers, load=False)

        if self.__is_color:
            print(
                "\n{0}[{1}!{0}] {2}Özür dilerim şifreyi bulamadım daha geniş bir passlist denermisin?{3}".format(
                    Fore.YELLOW, Fore.RED, Fore.WHITE, Fore.RESET
                )
            )
        else:
            print("\n[!] Özür dilerim şifreyi bulamadım daha geniş bir passlist denermisin?")

        sleep(self.delay)

    def shutdown(self, password, attempts, browsers):
        self.stats(password, attempts, browsers, load=False)

        if self.__is_color:
            print(
                "\n{0}[{1}!{0}] {2}Kendine dikkat et ben hep yanında olacağım -Haznedaroglu ...{3}".format(
                    Fore.YELLOW, Fore.RED, Fore.WHITE, Fore.RESET
                )
            )
        else:
            print("\n[!] Kal Sağlıcakla ...")

        sleep(self.delay)

    def info(self, msg):
        self.clear()

        if self.__is_color:
            print(
                "{0}[{1}i{0}] {2}{3}{4}".format(
                    Fore.YELLOW, Fore.CYAN, Fore.WHITE, msg, Fore.RESET
                )
            )
        else:
            print("[i] {}".format(msg))

        sleep(2.5)

    def warning(self, msg):
        self.clear()

        if self.__is_color:
            print(
                "{0}[{1}!{0}] {1}{2}{3}".format(
                    Fore.YELLOW, Fore.RED, msg, Fore.RESET
                )
            )
        else:
            print("[!] {}".format(msg))

        sleep(self.delay)

    def prompt(self, data):
        self.clear()

        if self.__is_color:
            return input(
                "{0}[{1}?{0}] {2}{3}{4}".format(
                    Fore.YELLOW, Fore.CYAN, Fore.WHITE, data, Fore.RESET
                )
            )
        else:
            return input("[?] {}".format(data))
