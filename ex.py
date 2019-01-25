#coding: utf-8

from horoscope import generate_prophecies, used_lists
from datetime import datetime as dt

def generate_page(head, body):
	page = f"<html>{head}{body}</html>"
	return page

def generate_head(title):
	head = f"""<head>
	<meta charset='utf-8'>
	<title>{title}</title>
	</head>
	"""
	return head

def generate_body(header, paragraphs, footer_link, footer):
	body = f"<h1>{header}</h1>"
	for p in paragraphs:
		body = body + f"<p>{p}</p>"
	body = body + f"""<br/><hr/>
	<a href = "{footer_link}"">{footer}</a>"""
	return f"<body>{body}</body>"\

def save_page(title, header, paragraphs, footer_link = "about.html", footer = "О проекте", output="index.html"):
	fp = open(output, "w", encoding="utf-8")
	today = dt.now().date()
	page = generate_page(
		head=generate_head(title),
		body=generate_body(header=header, paragraphs=paragraphs, footer_link = footer_link, footer = footer)
	)
	print(page, file=fp)
	fp.close()

def generate_list(context = [], list_type = "ul"):
    html_text = ""
    for list_elem in context:
        html_text = html_text + f"""\t<li>{list_elem}</li>\n"""
    return f"""<{list_type}>\n{html_text}</{list_type}>"""


def about():
    about = []
    context = []
    # used_li =[]
    about.append("""<img src = "https://st2.depositphotos.com/1000400/6403/v/950/depositphotos_64033463-stock-illustration-zodiac-signs-with-latin-names.jpg" width="100px" height="100px">""")
    used_li = used_lists()
    parameters = ["Времена дня", "Глаголы", "Ожидания"]
    for i in range(3):
        context.append(parameters[i]+":\n"+generate_list(used_li[i]))
    about.append(generate_list(context, "ol"))
    return about

#####################

today = dt.now().date()

save_page(
	 title="Гороскоп на сегодня",
	 header="Что день " + str(today) + " готовит",
	 paragraphs=generate_prophecies()
 )
save_page(
	title = "Гороскоп на сегодня",
	header = "О чем все это",
	paragraphs = about(),
	footer_link = "index.html",
	footer = "Гороскоп",
	output = "about.html")
print(about())

