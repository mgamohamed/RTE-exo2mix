# -*- coding: utf-8 -*-
# adelshb, github.com/adelshb
# 2018/02/14

import pandas as pd
import time

def check():

    date = time.strftime("%d/%m/%Y")
    url = "http://www.rte-france.com/getEco2MixXml.php?type=mix&&dateDeb=" + date +"&dateFin=" + date +"&mode=NORM"

    data = eco2mix_parser(url)

    Sum = data['Charbon-Global'].astype(int) + data['Fioul-Global'].astype(int)

    if Sum.tolist()[-1] > 3000:
        api.update_status("Energy Alert")

    return Sum.tolist()[-1]

