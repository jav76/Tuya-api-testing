import tinytuya as tt
import json


def importDevices():
    with open("devices.json") as file:
        data = json.load(file)
        return data


if __name__ == '__main__':

    print("Running")
    devices = importDevices()
    for key, val in devices[0].items():
        print("Key: " + key + " Val: " + val)

