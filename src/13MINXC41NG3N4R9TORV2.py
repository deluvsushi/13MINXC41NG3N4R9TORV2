import menu_configs
from json import load
from requests import post
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

auids = [ ]
with open("auids.json") as data:
    auids_list = load(data)
    for auid in auids_list:
        auids.append(auid)

        # -- coin generator functions --


def get_tapjoy_reward(auid: str):
    data = {"userId": auid, "repeat": "200"}
    request = post(f"https://samino.sirlez.repl.co/api/tapjoy", json=data)
    print(f"Generating Coins In {auid} - {request.text}")


def generating_process(auid: str):
    Thread(target=get_tapjoy_reward, args=([auid])).start()


def main_process():
    for auid in auids:
        auid = auid["auid"]
        try:
            with ThreadPoolExecutor(max_workers=5) as executor:
                _ = [executor.submit(generating_process, auid)]
        except Exception as e:
            print(f">> Error in main process - {e}")


def main():
    print(
        """Script by deluvsushi
Github : https://github.com/deluvsushi"""
    )
    print(menu_configs.banner)
    select = int(
        input(
            """
1) Generate Coins
Select >> """
        )
    )

    if select == 1:
        main_process()

main()
