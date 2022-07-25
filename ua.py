# -*- coding: utf-8 -*-
#
# https://github.com/ewwink/Real-Fake-Random-User-Agent/
#

import random

def GetRandomUserAgent():
    browserType = ["firefox", "chrome", "opera", "edge"]
    OS = ["Windows NT 10.0; Win64; x64", "X11; Linux x86_64", "Macintosh; Intel Mac OS X 12_4"]

    OSsystem = OS[random.randint(0, len(OS)-1)]
    version = random.randint(93, 104)
    randomBrowser = browserType[random.randint(0, len(browserType)-1)]
    browserTemplate = "Mozilla/5.0 ({0}; rv:{1}.0) Gecko/20100101 Firefox/{1}.0"
    finalVersion = version

    if randomBrowser in ["chrome", "opera", "edge"]:
        patch = random.randint(4950, 5162)
        build = random.randint(80, 212)
        browserTemplate = "Mozilla/5.0 ({0}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{1} Safari/537.36"
        finalVersion = f"{version}.0.{patch}.{build}"

        if randomBrowser == "opera":
            version = random.randint(80, 90)
            patch = random.randint(3500, 4260)
            build = random.randint(80, 212)
            browserTemplate += f" OPR/{version}.0.{patch}.{build}"
        elif randomBrowser == "edge":
            patch = random.randint(800, 1250)
            build = random.randint(40, 99)
            browserTemplate += f" EDG/{version}.0.{patch}.{build}"

    userAgent = browserTemplate.format(OSsystem, finalVersion)

    return userAgent
