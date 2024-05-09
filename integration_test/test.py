import requests

url = 'https://www.overleaf.com/project/65c0a1c65b0ab668a0fab6ef/linked_file'
headers = {
    'Host': 'www.overleaf.com',
    'Content-Length': '241',
    'Sec-Ch-Ua': '"Chromium";v="121", "Not A(Brand";v="99"',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'X-Csrf-Token': 'ibYuiGga-d2ndYztinrB3-clGuP83GvrmX2U',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36',
    'Sec-Ch-Ua-Platform': '"Linux"',
    'Origin': 'https://www.overleaf.com',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.overleaf.com/project/65c0a1c65b0ab668a0fab6ef',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Priority': 'u=1, i',
}

cookies = {
    'overleaf_session2': 's%3AjhpKcgYvi-ojEjixUKajWH4SL9kdBZ_Q.mnx389j4xWFkoGuZd67bFetnBwP5Jfiw4hxRfOAgd10',
    'GCLB': 'CM359oSXu4HpnQEQAw',
}

paths = [
"eq_volctrl/pot_mid/freqresp_eq_volctrl_pot_mid.png",
"eq_volctrl/pot_mid/thd_eq_volctrl_pot_mid.png",
"eq_volctrl/pot_min/thd_eq_volctrl_pot_min.png",
"eq_volctrl/pot_min/freqresp_eq_volctrl_pot_min.png",
"eq_volctrl/pot_max/thd_eq_volctrl_pot_max.png",
"eq_volctrl/pot_max/freqresp_eq_volctrl_pot_max.png",
"preamp_opamp/freqresp_preamp_opamp.png",
"preamp_opamp/thd_preamp_opamp.png",
"preamp_class_a/thd_preamp_class_a.png",
"preamp_class_a/freqresp_preamp_class_a.png",
"preamp_riaa/freqresp_preamp_riaa.png",
"preamp_riaa/thd_preamp_riaa.png",
"preamp_riaa_opamp/freqresp_preamp_riaa_opamp.png",
"preamp_riaa_opamp/thd_preamp_riaa_opamp.png"
]
for path in paths:
    fname = path.split("/")[-1]
    data = {
        "parent_folder_id": "661f9926e12183726301ddd4",
        "name": fname,
        "provider": "url",
        "data": {
            "url": f"https://raw.githubusercontent.com/Niclasapdk/ESD4_project/main/integration_test/{path}"
        }
    }
    response = requests.post(url, headers=headers, cookies=cookies, json=data)
    print(fname, response)
