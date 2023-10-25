import requests
import requests
import tkinter as tk


def get_exchange_rates():
    url = 'https://api.bnm.gov.my/public/exchange-rate'
    headers = {
        'Sec-Ch-Ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
        'Accept': 'application/vnd.BNM.API.v1+json',
        'Sec-Ch-Ua-Mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.5615.50 Safari/537.36',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Origin': 'https://apikijangportal.bnm.gov.my',
        'Sec-Fetch-Site': 'same-site',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://apikijangportal.bnm.gov.my/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'close'
    }

    params = {
        'session': '0900',
        'quote': 'rm'
    }


    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        sgd_rate = None
        for currency_data in data['data']:
            if currency_data['currency_code'] == 'SGD':
                sgd_rate = currency_data['rate']
                break

        if sgd_rate is not None:
            result_text = f"SGD & MYR \nDate: {sgd_rate['date']}\n" \
                          f"Buying Rate: {sgd_rate['buying_rate']}\n" \
                          f"Selling Rate: {sgd_rate['selling_rate']}\n" \
                          f"Middle Rate: {sgd_rate['middle_rate']}"
            result_label.config(text=result_text)
        else:
            result_label.config(text="SGD not found in the response.")
    else:
        result_label.config(text=f"Error: {response.status_code}")

# Tkinter setup
root = tk.Tk()
root.title("SGD Exchange Rate")
root.geometry("200x120")  # Set a larger initial window size

# Label to display result
result_label = tk.Label(root, font=('Arial', 12))
result_label.pack(pady=10)

# Call the function to get exchange rates when the Tkinter window is created
get_exchange_rates()

# Run the Tkinter event loop
root.mainloop()






