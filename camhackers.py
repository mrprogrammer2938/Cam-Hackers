#!/usr/bin/python3
# The code write by (Mr.nope)
# Cam Hackers v2.0
import os
import time
import platform
import re
import sys
try:
  import requests
except ImportError:
  os.system("pip install requests")
# color
class color:
    green = '\033[92m'
    red = '\033[91m'
    white = '\033[0m'
    blue = '\033[96m'
help = """
Cam Hackers Argument:
    --scan <Countrie>
    --help or help | Show Argument Help
    --menu or menu | Start Cam Hackers Menu
    --banner or banner | Show Cam Hackers Tool Banner
    --version or version | Show Cam Hackers Version
"""
version = "Cam Hackers v2.0"
banner = f'''{color.green}
`:'######:::::'###::::'##::::'##::::'##::::'##::::'###:::::'######::'##:::'##:'########:'########:::'######::
'##... ##:::'## ##::: ###::'###:::: ##:::: ##:::'## ##:::'##... ##: ##::'##:: ##.....:: ##.... ##:'##... ##:
 ##:::..:::'##:. ##:: ####'####:::: ##:::: ##::'##:. ##:: ##:::..:: ##:'##::: ##::::::: ##:::: ##: ##:::..::
 ##:::::::'##:::. ##: ## ### ##:::: #########:'##:::. ##: ##::::::: #####:::: ######::: ########::. ######::
 ##::::::: #########: ##. #: ##:::: ##.... ##: #########: ##::::::: ##. ##::: ##...:::: ##.. ##::::..... ##:
 ##::: ##: ##.... ##: ##:.:: ##:::: ##:::: ##: ##.... ##: ##::: ##: ##:. ##:: ##::::::: ##::. ##::'##::: ##:
. ######:: ##:::: ##: ##:::: ##:::: ##:::: ##: ##:::: ##:. ######:: ##::. ##: ########: ##:::. ##:. ######::
:......:::..:::::..::..:::::..:::::..:::::..::..:::::..:::......:::..::::..::........::..:::::..:::......:::{color.white}\n'''
def title():
      if platform.system() == 'Linux':
            os.system("printf '\033]2;Cam Hackers\a'")
      else:
          os.system("title Cam Hackers")
def cls():
    if platform.system() == 'Linux':
          os.system("clear")
    else:
          os.system("cls")
def main():
    title()
    cls()
    print(banner)
    print(f'''   
\033[1;32m1) \033[1;37mUnited States                \033[1;32m32) \033[1;37mMexico                \033[1;32m61) \033[1;37mMoldova
\033[1;32m2) \033[1;37mJapan                        \033[1;32m32) \033[1;37mFinland               \033[1;32m62) \033[1;37mNicaragua
\033[1;32m3) \033[1;37mItaly                        \033[1;32m33) \033[1;37mChina                 \033[1;32m63) \033[1;37mMalta
\033[1;32m4) \033[1;37mKorea                        \033[1;32m34) \033[1;37mChile                 \033[1;32m64) \033[1;37mTrinidad And Tobago
\033[1;32m5) \033[1;37mFrance                       \033[1;32m35) \033[1;37mSouth Africa          \033[1;32m65) \033[1;37mSoudi Arabia
\033[1;32m6) \033[1;37mGermany                      \033[1;32m36) \033[1;37mSlovakia              \033[1;32m66) \033[1;37mCroatia
\033[1;32m7) \033[1;37mTaiwan                       \033[1;32m37) \033[1;37mHungary               \033[1;32m67) \033[1;37mCyprus
\033[1;32m8) \033[1;37mRussian Federation           \033[1;32m38) \033[1;37mIreland               \033[1;32m68) \033[1;37mPakistan
\033[1;32m9) \033[1;37mUnited Kingdom               \033[1;32m39) \033[1;37mEgypt                 \033[1;32m69) \033[1;37mUnited Arab Emirates
\033[1;32m10) \033[1;37mNetherlands                 \033[1;32m40) \033[1;37mThailand              \033[1;32m70) \033[1;37mKazakhstan
\033[1;32m11) \033[1;37mCzech Republic              \033[1;32m41) \033[1;37mUkraine               \033[1;32m71) \033[1;37mKuwait
\033[1;32m12) \033[1;37mTurkey                      \033[1;32m42) \033[1;37mSerbia                \033[1;32m72) \033[1;37mVenezuela
\033[1;32m13) \033[1;37mAustria                     \033[1;32m43) \033[1;37mHong Kong             \033[1;32m73) \033[1;37mGeorgia
\033[1;32m14) \033[1;37mSwitzerland                 \033[1;32m44) \033[1;37mGreece                \033[1;32m74) \033[1;37mMontenegro
\033[1;32m15) \033[1;37mSpain                       \033[1;32m45) \033[1;37mPortugal              \033[1;32m75) \033[1;37mEl Salvador
\033[1;32m16) \033[1;37mCanada                      \033[1;32m46) \033[1;37mLatvia                \033[1;32m76) \033[1;37mLuxembourg
\033[1;32m17) \033[1;37mSweden                      \033[1;32m47) \033[1;37mSingapore             \033[1;32m77) \033[1;37mCuracao
\033[1;32m18) \033[1;37mIsrael                      \033[1;32m48) \033[1;37mIceland               \033[1;32m78) \033[1;37mPuerto Rico
\033[1;32m19) \033[1;37mIran                        \033[1;32m49) \033[1;37mMalaysia              \033[1;32m79) \033[1;37mCosta Rica
\033[1;32m20) \033[1;37mPoland                      \033[1;32m50) \033[1;37mColombia              \033[1;32m80) \033[1;37mBelarus
\033[1;32m21) \033[1;37mIndia                       \033[1;32m51) \033[1;37mTunisia               \033[1;32m81) \033[1;37mAlbania
\033[1;32m22) \033[1;37mNorway                      \033[1;32m52) \033[1;37mEstonia               \033[1;32m82) \033[1;37mLiechtenstein
\033[1;32m23) \033[1;37mRomania                     \033[1;32m53) \033[1;37mDominican Republic    \033[1;32m83) \033[1;37mBosnia And Herzegovia
\033[1;32m24) \033[1;37mViet Nam                    \033[1;32m54) \033[1;37mSloveania             \033[1;32m84) \033[1;37mParaguay
\033[1;32m25) \033[1;37mBelgium                     \033[1;32m55) \033[1;37mEcuador               \033[1;32m85) \033[1;37mPhilippines
\033[1;32m26) \033[1;37mBrazil                      \033[1;32m56) \033[1;37mLithuania             \033[1;32m86) \033[1;37mFaroe Islands
\033[1;32m27) \033[1;37mBulgaria                    \033[1;32m57) \033[1;37mPalestinian           \033[1;32m87) \033[1;37mGuatemala
\033[1;32m28) \033[1;37mIndonesia                   \033[1;32m58) \033[1;37mNew Zealand           \033[1;32m88) \033[1;37mNepal
\033[1;32m29) \033[1;37mDenmark                     \033[1;32m59) \033[1;37mBangladeh             \033[1;32m89) \033[1;37mPeru
\033[1;32m30) \033[1;37mArgentina                   \033[1;32m60) \033[1;37mPanama                \033[1;32m90) \033[1;37mUruguay
                                                          \033[1;32m91) \033[1;37mExtra
                                  {color.red}99){color.white}Exit
    ''')
    try:  
      print()
      countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
                   "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
                   "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
                   "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
                   "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
                   "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
                   "MD", "NI", "MT", "IT", "SA", "HR", "CY", "PK", "AE", "KZ",
                   "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
                   "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
                   "-"]
      headers = {"User-Agent": "Mozilla/5.0 (X1; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

      num = int(input(f"{color.green}choose{color.red}/> {color.white}"))
      print("\n")
      if num == 99:
            print("\nExiting...")
            sys.exit()      
      elif num not in range(1, 91+1):
          raise IndexError

      country = countries[num-1]
      res = requests.get(
          f"https://www.insecam.org/en/bycountry/{country}", headers=headers
      )
      last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

      for page in range(int(last_page)):
          res = requests.get(
              f"https://www.insecam.org/en/bycountry/{country}/?page={page}",
              headers=headers
          )
          find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
          for ip in find_ip:
              print("\033[1;32m", ip)
    except requests.ConnectionError:
        print("Nope !!!")
        sys.exit()

if __name__ == '__main__':
  try:
    try:
      main()
    except EOFError:
      print("\nCtrl + D")
      print("\nExiting...")
      sys.exit()
  except KeyboardInterrupt:
    print("\nCtrl + C")
    print("\nExiting...")
    sys.exit()