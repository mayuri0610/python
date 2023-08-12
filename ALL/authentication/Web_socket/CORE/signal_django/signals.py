from django.contrib.auth.signals import *
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,pre_delete,pre_save,post_init,post_save,post_delete


@receiver(user_logged_in, sender=User) 
def login_success(sender, request, user, **kwargs):
    print("----------------------------------------------------------------")
    print("Logged-in Signal...... Run Intro....")
    print("Sender :", sender)
    print("Request :", request)
    print("User :", user)
    print("User Passward :", user.password)
    print(f'Kwargs : {kwargs}')
 

# user_logged_in.connect(login_success, sender=User)



@receiver(user_logged_out, sender=User) 
def log_out(sender, request, user, **kwargs):
    print("----------------------------------------------------------------")
    print("Logged-out Signal...... Run Outro....")
    print("Sender :", sender)
    print("Request :", request)
    print("User :", user)
    print(f'Kwargs : {kwargs}')

# user_logged_out.connect(log_out, sender=User)




@receiver(user_login_failed) 
def login_faield(sender, credentials, request, **kwargs):
    print("----------------------------------------------------------------")
    print("Login Failed Signal............")
    print("Sender :", sender)
    print("Credentials :", credentials)
    print("Request :", request)
    print(f'Kwargs : {kwargs}')

# user_login_failed.connect(login_faield)

@receiver(pre_save, sender=User)    #sender at that time is User but it change through models(jis model pe apply karna hai usaka nam likhana)
def at_beginning_save(sender, instance, **kwargs):
    print("----------------------------------------------------------------")
    print("Pre Save Signal............")
    print("Sender :", sender)
    print("Instance :", instance)
    print(f'Kwargs : {kwargs}')

# pre_save.connect(at_beginning_save, sender=User)


@receiver(post_save, sender=User)    #sender at that time is User but it change through models(jis model pe apply karna hai usaka nam likhana)
def at_ending_save(sender, instance,created, **kwargs):
    if created:
        print("----------------------------------------------------------------")
        print("Post Save Signal............")
        print("New Record")
        print("Sender :", sender)
        print("Instance :", instance)
        print("Created :", created)
        print(f'Kwargs : {kwargs}')
    else:
        print("----------------------------------------------------------------")
        print("Post Save Signal............")
        print("Update")
        print("Sender :", sender)
        print("Instance :", instance)
        print("Created :", created)
        print(f'Kwargs : {kwargs}')


# post_save.connect(at_ending_save, sender=User)


@receiver(pre_delete, sender=User)    #sender at that time is User but it change through models(jis model pe apply karna hai usaka nam likhana)
def at_beginning_delete(sender, instance, **kwargs):
    print("----------------------------------------------------------------")
    print("Pre Delete Signal............")
    print("Sender :", sender)
    print("Instance :", instance)
    print(f'Kwargs : {kwargs}')

# pre_delete.connect(at_beginning_delete, sender=User)



@receiver(post_delete, sender=User)    #sender at that time is User but it change through models(jis model pe apply karna hai usaka nam likhana)
def at_ending_delete(sender, instance, **kwargs):
    print("----------------------------------------------------------------")
    print("Post Delete Signal............")
    print("Sender :", sender)
    print("Instance :", instance)
    print(f'Kwargs : {kwargs}')

# post_delete.connect(at_ending_delete, sender=User)



