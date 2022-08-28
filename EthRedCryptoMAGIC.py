# For Running Example : python EthRedCryptoMAGIC.py -f eth5.txt -v 10000 -n 32
# ----------------------------- Programmer Mmdrza.Com ---------------------- #
import ctypes
import time
import optparse
import multiprocessing
from bip_utils import Bip32Slip10Secp256k1, Bip39MnemonicGenerator, Bip39SeedGenerator, Bip39WordsNum, EthAddrEncoder
from rich import print


def Main():
    p = optparse.OptionParser()
    p.add_option('-f', '--file', dest="filenameEth",
                 help="Ethereum Rich Address File With Type Format .TXT [Example: -f eth5.txt] ")
    p.add_option('-v', '--view', dest="ViewPrint", help="Print After Generated This Number Print And Report")
    p.add_option('-n','--thread', dest="ThreadCount", help="Total Thread Number (Total Core CPU)")
    (options, args) = p.parse_args()
    filename = options.filenameEth
    logpx = options.ViewPrint
    thco = options.ThreadCount
    # ----------------------- START ------------------------------ #
    with open(filename) as f:
        add = f.read().split()
    add = set(add)
    z = 0
    fu = 0
    logp = 0

    while True:
        z += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f"MATCH:{fu} SCAN:{z}")
        mnemonic = Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)
        seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
        bip32_mst_ctx = Bip32Slip10Secp256k1.FromSeed(seed_bytes)
        MasterKey = bip32_mst_ctx.PrivateKey().Raw().ToHex()
        bip32_der_ctx = bip32_mst_ctx.DerivePath("m/44'/60'/0'/0/0")
        PrivateKeyBytes = bip32_der_ctx.PrivateKey().Raw().ToHex()
        addr = EthAddrEncoder.EncodeKey(bip32_der_ctx.PublicKey().KeyObject())
        Words24 = str(mnemonic)
        if addr in add:
            fu += 1
            print(f"[green1][+] MATCH ADDRESS FOUND IN LIST IMPORTED :[/green1] [white]{addr}[/white]")
            print(
                f"PrivateKey (Byte) : [green1]{PrivateKeyBytes}[/green1]\n[gold1]{mnemonic}[/gold1]\n[red1]MasterKey (Byte) : [/red1][green1]{MasterKey}[/green1]")
            with open('FoundMATCHAddr.txt', 'a') as f:
                f.write(
                    f"{addr}\n{PrivateKeyBytes}\n{mnemonic}\n{MasterKey}\n------------------------- MMDRZA.Com -------------------\n")
                f.close()
        elif int(z) % int(logpx) == 0:
            logp += int(logpx)
            print(
                f"[red][[green1]+[/green1]][GENERATED[white] {logp}[/white] ETH ADDR][WITH [white]128 THREAD[/white]][sK/Th:[white]{time.thread_time()}[/white]][/red]\n[red][[green1]{PrivateKeyBytes.upper()}[/green1]][/red]")
            print(
                f"[red][MasterKey : [white]{MasterKey.upper()}[/white]][/red]\n[white on red3][MNEMONIC : {Words24[0:64]}...][/white on red3]")
        else:
            print(
                f"[red][-][ GENERATED [cyan]{z}[/cyan] ETH ADDR ][FOUND:[white]{fu}[/white]][THREAD:[cyan]{thco}[/cyan]][/red]",
                end="\r")


jobs = []
if __name__ == '__main__':
    m = multiprocessing.Process(target=Main)
    jobs.append(m)
    m.start()
