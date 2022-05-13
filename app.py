import jinja2

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader("template"))

jinja_var = {
    "contact": {
        "user_id": "5077035",
        "recommended_ids": ["19416626", "19407734"]
    },
    "lookups": {
        "recommended_restaurants":
        {
            "19416626":
            {
                "name": "Frenchette",
                "url": "https://resy.com/cities/ny/frenchette",
                "thumbnail": "https://image.resy.com/3/003/2/1946/6b5a2e03692b6079da3caf09d55ba393e5be2dbd/jpg/1:1/400"
            },
            "19407734":
            {
                "name": "Golden Diner",
                "url": "https://resy.com/cities/ny/golden-diner",
                "thumbnail": "https://image.resy.com/3/003/2/9520/775230f7cc2862c86eb97d45dbdc74fe18c1fe87/jpg/1:1/400"
            }
        }
    }
}

template = jinja_env.get_template("dynamic_Tonatiuh-jimenez.html")
print(template.render(jinja_var))
