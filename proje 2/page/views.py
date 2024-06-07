from django.shortcuts import render
from django.http import HttpResponse


# proje.html sayfasındaki projelerin for döngüsüyle kullanılması (fake bir database oluşturdum)
FAKE_DB_PROJECTS = [
    f"https://picsum.photos/id/{id}/100/80" for id in range(21, 29)
]

FAKE_DB_CAROUSEL = [
    f"https://picsum.photos/id/{id}/1200/400" for id in range(24, 28)
]


def home_view(request):
    context = dict(
        FAKE_DB_CAROUSEL=FAKE_DB_CAROUSEL,
        FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
    )
    return render(request, "page/home_page.html", context)


def about_us_view(request):
    page_title = 'About'
    hero_content = 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney '
    context = dict(
        page_title=page_title,
        hero_content=hero_content,
        FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
    )
    return render(request, "page/about_us.html", context)


def contact_us_view(request):
    page_title = 'Contact'
    hero_content = 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney '
    context = dict(
        page_title=page_title,
        hero_content=hero_content,
        FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
    )
    return render(request, "page/contact_us.html", context)


def vizion_view(request):
    page_title = 'Vision'
    hero_content = 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney '
    context = dict(
        page_title=page_title,
        hero_content=hero_content,
        FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
    )
    return render(request, "page/vizion.html", context)
