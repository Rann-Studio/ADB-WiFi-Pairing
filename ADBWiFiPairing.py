import qrcode_terminal
import subprocess
from nanoid import generate
import asyncio
from zeroconf import ServiceBrowser, Zeroconf
import sys

class ADBPairingHandler:
    def __init__(self):
        self.address = None
        self.port = None

    def update_service(self, zeroconf, type_, name):
        pass

    def remove_service(self, zeroconf, type, name):
        pass

    def add_service(self, zeroconf, type_, name):
        info = zeroconf.get_service_info(type_, name)
        if info:
            self.address = info.parsed_addresses()[0]
            self.port = info.port
            zeroconf.close()

class ADBHandler:
    @staticmethod
    def pair_device(address, port, password):
        adb_command = f'adb pair {address}:{port} {password}'
        try:
            result = subprocess.check_output(adb_command, shell=True, text=True)
            print(result)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

    @staticmethod
    def connect_device(address):
        print('Enter port to connect')
        print('Developer options -> Wireless debugging -> IP address & Port')
        port = input('Port: ')
        adb_command = f'adb connect {address}:{port}'
        try:
            result = subprocess.check_output(adb_command, shell=True, text=True)
            print(result)
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")

class ADBWiFiPairing:
    def __init__(self):
        self.check_adb()
        
        self.name = 'ADB_WIFI_' + generate()
        self.password = generate(size=8)

        self.show_qr()
        print("Scan QR code to pair new devices")
        print("Developer options -> Wireless debugging -> Pair device with QR code")
        asyncio.run(self.discover_service())

    def check_adb(self):
        try:
            subprocess.check_output("adb version", stderr=subprocess.PIPE, shell=True)
        except subprocess.CalledProcessError:
            print("adb is not available. Make sure you have adb installed and added to the system's PATH.")
            sys.exit(1)

    def show_qr(self):
        wifi_config = f'WIFI:T:ADB;S:{self.name};P:{self.password};;'
        qrcode_terminal.draw(wifi_config)

    async def discover_service(self):
        zeroconf = Zeroconf()
        listener = ADBPairingHandler()
        browser = ServiceBrowser(zeroconf, "_adb-tls-pairing._tcp.local.", listener)

        while not listener.address or not listener.port:
            await asyncio.sleep(0.1)

        ADBHandler.pair_device(listener.address, listener.port, self.password)
        ADBHandler.connect_device(listener.address)

if __name__ == "__main__":
    ADBWiFiPairing()
