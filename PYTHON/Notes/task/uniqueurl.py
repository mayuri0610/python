# l1 = ['https://weconnect.chat']
# l2 =[
#     {
#         "url": "https://www.linkedin.com/company/weconnect-chat",
#         "status": 400,
#         "text_count": 0
#     },
#     {
#         "url": "https://weconnect.chat/pricing",
#         "status": 200,
#         "text_count": 7503
#     },
#     {
#         "url": "https://weconnect.chat/template/",
#         "status": 200,
#         "text_count": 4747
#     },
#     {
#         "url": "https://play.google.com/store/apps/details?id=com.weconnect.android",
#         "status": 200,
#         "text_count": 1802
#     },
#     {
#         "url": "https://weconnect.chat",
#         "status": 200,
#         "text_count": 2285
#     },
#     {
#         "url": "https://app.weconnect.chat/signup",
#         "status": 200,
#         "text_count": 9
#     },
#     {
#         "url": "https://www.novi.nl/",
#         "status": 200,
#         "text_count": 7686
#     },
#     {
#         "url": "https://weconnect.chat/features/",
#         "status": 200,
#         "text_count": 2178
#     },
#     {
#         "url": "https://www.youtube.com/watch?v=NWu9y9F06nE&list=PLeF2XYNxHZrpd7olmCrDsh6GlNhoaEog_&index=1",
#         "status": 200,
#         "text_count": 371
#     },
#     {
#         "url": "https://weconnect.chat/master-class/",
#         "status": 400,
#         "text_count": 0
#     },
#     {
#         "url": "https://www.instagram.com/weconnectchatplatform/",
#         "status": 200,
#         "text_count": 19
#     },
#     {
#         "url": "https://app.weconnect.chat/login",
#         "status": 200,
#         "text_count": 9
#     },
#     {
#         "url": "https://wecapps.s3.eu-central-1.amazonaws.com/WeConnect-chat-1.0.3_mac.dmg",
#         "status": 200,
#         "text_count": 77906518
#     },
#     {
#         "url": "https://weconnect.chat/pricing/",
#         "status": 200,
#         "text_count": 7503
#     },
#     {
#         "url": "https://weconnect.chat/about-us/",
#         "status": 200,
#         "text_count": 7986
#     },
#     {
#         "url": "https://weconnect.chat/terms-and-conditions/",
#         "status": 200,
#         "text_count": 19173
#     },
#     {
#         "url": "https://weconnect.chat/cookies-policy/",
#         "status": 200,
#         "text_count": 4276
#     },
#     {
#         "url": "https://wecapps.s3.eu-central-1.amazonaws.com/WeConnect-chat+Setup+1.0.3.exe",
#         "status": 200,
#         "text_count": 61341802
#     },
#     {
#         "url": "https://weconnect.chat/help-center/",
#         "status": 200,
#         "text_count": 1300
#     },
#     {
#         "url": "https://apps.apple.com/in/app/weconnect-chat/id6443603402",
#         "status": 200,
#         "text_count": 1607
#     },
#     {
#         "url": "https://www.medwayzorg.nl/",
#         "status": 200,
#         "text_count": 1103
#     },
#     {
#         "url": "https://weconnect.chat/privacy-policy/",
#         "status": 200,
#         "text_count": 5404
#     },
#     {
#         "url": "https://twitter.com/ChatWeconnect",
#         "status": 200,
#         "text_count": 406
#     },
#     {
#         "url": "https://weconnect.chat/weconnect-apps/",
#         "status": 200,
#         "text_count": 536
#     },
#     {
#         "url": "https://www.facebook.com/weconnect.chat",
#         "status": 200,
#         "text_count": 752
#     },
#     {
#         "url": "https://www.facebook.com/weconnect.chat",
#         "status": 200,
#         "text_count": 752
#     }
# ]


# # l3=[]

# # for item in l2:
# #     url = item["url"]
# #     if url.startswith(l1[0]):
# #         if url not in l2:
# #             l3.append(url)
        
# # unique_url_list = list(set(l3))
# # print(unique_url_list)         


# # url1=[url.rstrip('/') for url in l3]
# # uniq = list(set(url1))
# # print(uniq)
# # print(len(uniq))


# domain_name = l1[0].split('/')[2]
# l1 = [f"https://{domain_name}"]

# unique_urls = set()
# unique_l2 = []
# l3 = []

# for item in l2:
#     url = item["url"]

#     if url not in unique_urls:
#         unique_urls.add(url)
#         unique_l2.append(item)

# # print(len(l2))
# # print(len(unique_l2))

# for item in unique_l2:
#     url = item["url"]
#     if url.startswith(l1[0]):
#         if url not in unique_l2:
#             l3.append(url)

# # print(len(l3))

# url1=[url.rstrip('/') for url in l3]
# print(url1)
# uniq = list(set(url1))
# # print(uniq)
# # print(len(uniq))

# l1 = ['https://weconnect.chat/pricing']
l1 = ['https://weconnect.chat']

domain_name = l1[0].split('/')[2]

l1 = [f"https://{domain_name}"]
print(l1)


