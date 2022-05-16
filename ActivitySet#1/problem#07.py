# Strings


text = "X-DSPAM-Confidence:    0.8475"

search= text.find('0.8475')
search=int(search)
print(float(text[search:]))