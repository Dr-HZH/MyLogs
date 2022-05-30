from random import Random
from django.db.models.functions import datetime
from django.shortcuts import render
from plogs.models import Avatar, plog


# Create your views here.

def getIndex(request):
    # with open('plogs/static/流水账.txt', "r", encoding="utf-8") as f:
    #     content = f.read().split("\n")
    #
    # plog_article = ""
    # plog_title = ""
    # plog_abstract = ""
    # for line in content:
    #     # print(line)
    #     if "#" in line:
    #         if plog_article == "" and plog_title == "":
    #             pass
    #         else:
    #             plog.objects.create(plog_title=plog_title, plog_content=plog_article, plog_abstract=plog_abstract)
    #         plog_abstract = ""
    #         plog_article = ""
    #         plog_title = line
    #     else:
    #         if line == "":
    #             continue
    #         else:
    #             plog_article = plog_article + "\n" + line
    #             if len(plog_abstract) <= 15:
    #                 plog_abstract = plog_abstract + "\n" + line
    #
    # f.close()
    Avatars = Avatar.objects.all()
    print(len(Avatars))
    avatar = Avatars[0]
    return render(request, 'Index.html', {
        "id": avatar.AvatarId,
        'Name': avatar.AvatarName,
        'major': avatar.AvatarMajor,
        'school': avatar.AvatarSchool,
        'mail': avatar.AvatarMail,
    })


def getLogs(request):
    all_logs = plog.objects.all()
    return render(request, 'Logs.html', {
        'logs': all_logs,
    })


def getPlog(request, plog_id):
    is_Photo_Exists = False
    photos = []
    if plog_id is None:
        plog_id = 1
    all_plogs = plog.objects.all()
    if len(all_plogs) < 1:
        Flag = True
    else:
        thisLog = all_plogs[0]
    for log in all_plogs:
        if log.plog_id == plog_id:
            thisLog = log
            break
    section = thisLog.plog_content.split('\n')
    thisLog.plog_title = thisLog.plog_title + "\t"
    if thisLog.plog_img1:
        photos = [thisLog.plog_img2, thisLog.plog_img3, thisLog.plog_img4,
                  thisLog.plog_img5, thisLog.plog_img6, thisLog.plog_img7, thisLog.plog_img8,
                  thisLog.plog_img9]
        is_Photo_Exists = True
    return render(request, 'Detail.html', {
        'plog': thisLog,
        'section': section,
        "is_Photo_Exists": is_Photo_Exists,
        "photos": photos,
        'type': "Plog",
        "title": thisLog.plog_title,
    })


def getAvatar(request, Avatar_id):
    all_avatars = Avatar.objects.all()
    thisAvatar = all_avatars[0]
    for avatar in all_avatars:
        if Avatar.AvatarId == Avatar_id:
            thisAvatar = avatar
            break
    return render(request, "Detail.html", {
        'type': "Avatar",
        "title": avatar.AvatarName,
        "avatar": thisAvatar,

    })
