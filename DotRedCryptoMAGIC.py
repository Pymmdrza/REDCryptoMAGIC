# For Running Example : python DotRedCryptoMAGIC.py -f dot1000.txt -v 1000 -n 32
# ------------------ Programmer Mmdrza.Com ~ Telegram Channel : @CryptoAtttacker ------------------------ #

import ctypes
import time
import optparse
import multiprocessing
from bip_utils import Bip39MnemonicGenerator, Bip39WordsNum, Substrate, SubstrateBip39SeedGenerator, SubstrateCoins
from rich import print


def Main():
    p = optparse.OptionParser()
    p.add_option('-f', '--file', dest="filenameDot",
                 help="Polkadot Rich Address File With Type Format .TXT [Example: -f dot1000.txt] ")
    p.add_option('-v', '--view', dest="ViewPrint", default='10000',
                 help="Print After Generated This Number Print And Report(Default: 10000)")
    p.add_option('-n', '--thread', dest="ThreadCount", default='8',
                 help="Total Thread Number (Total Core CPU)(Default: 8)")
    (options, args) = p.parse_args()
    filename = options.filenameDot
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
        # --------------- Generate Seed from Mnemonic --------------- #
        seed_bytes = SubstrateBip39SeedGenerator(mnemonic).Generate()
        # --------------- Construct from Seed --------------- #
        substrate_ctx = Substrate.FromSeed(seed_bytes, SubstrateCoins.POLKADOT)
        MasterPrivateKey = substrate_ctx.PrivateKey().Raw().ToHex()
        MasterPublicKey = substrate_ctx.PublicKey().RawCompressed().ToHex()
        substrate_ctx = substrate_ctx.ChildKey("//hard")
        PrivateKeyExt = substrate_ctx.PrivateKey().Raw().ToHex()
        substrate_ctx = substrate_ctx.DerivePath("//0/1")
        PrivateKeyBytes = substrate_ctx.PrivateKey().Raw().ToHex()
        Pub2Addr = substrate_ctx.PublicKey().ToAddress()
        addr = substrate_ctx.PublicKey().ToAddress()
        addrEx = substrate_ctx.PublicKey().ToAddress()
        Words24 = str(mnemonic)
        if addr in add or addrEx in add or Pub2Addr in add:
            fu += 1
            print(f"[green1][+] MATCH ADDRESS FOUND IN LIST IMPORTED :[/green1] [white]{addr}[/white]")
            print(f"[red][[green1]{addrEx}[/green1]][/red]")
            print(f"[red][PUB: [white]{Pub2Addr}[/white]][/red]")
            print(
                f"PrivateKey (Byte) : [green1]{PrivateKeyBytes}[/green1]\n[gold1]{mnemonic}[/gold1]\n[red1]MasterKey (Byte) : [/red1][green1]{MasterPrivateKey}[/green1]\n[gold1]{MasterPublicKey}[/gold1]")
            with open('FoundMATCHAddr.txt', 'a') as f:
                f.write(
                    f"{addr}\n{addrEx}\n{Pub2Addr}\n{PrivateKeyBytes}\n{mnemonic}\n{MasterPrivateKey}\n{PrivateKeyExt}\n{MasterPublicKey}------------------------- MMDRZA.Com -------------------\n")
                f.close()
        elif int(z) % int(logpx) == 0:
            logp += int(logpx)
            print(
                f"[red][[green1]+[/green1]][GENERATED[white] {logp}[/white] DOT ADDR][WITH [white]{thco} THREAD[/white]][sK/Th:[white]{time.thread_time()}[/white]][/red]\n[red][[green1]{PrivateKeyBytes.upper()}[/green1]][/red]")
            print(
                f"[red][MasterKey : [white]{MasterPrivateKey.upper()}[/white]][/red]\n[white on red3][MNEMONIC : {Words24[0:64]}...][/white on red3]")
        else:
            print(
                f"[red][-][ GENERATED [cyan]{z}[/cyan] POLKADOT ADDRESS ][FOUND:[white]{fu}[/white]][THREAD:[cyan]{thco}[/cyan]][DATAIMPORTED:[white]{filename}[/white]][/red]",
                end="\r")


jobs = []
if __name__ == '__main__':
    m = multiprocessing.Process(target=Main)
    jobs.append(m)
    m.start()
