from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Image,Followers

# Create your tests here.
class   UserTestClass(TestCase):
    def setUp(self):
        self.new_user=User(
            username='jaffar',email='jaff@gmail.com',password='pass1'
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user,User))

    def test_save_method(self):
        self.new_user.save()
        user=User.objects.all()
        self.assertEquals(len(user),1)
    
    def test_delete_method(self):
        self.new_user.save()
        self.new_user.delete()
        user = User.objects.all()
        self.assertEquals(len(user),1)


class ProfileTestClass(TestCase):
    def setUp(self):
        self.user=User(
            username='jaffar',email='jaff@gmail.com',password='pass1'
    )
        self.user.save()

        self.profile=Profile(bio='I am cool',user=self.user,profilephoto='media/album/water.png')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.new_profile.save_profile()
        profiles = Profile.objects.all()

        self.assertEquals(len(profiles),1)

    def test_delete_profile(self):
        def setUp(self):
            self.user=User(
                username='jaffar',email='jaff@gmail.com',password='pass1'
        )
        self.user.save()
        self.profile=Profile(bio='I am cool',user=self.user,profilephoto='media/album/water.png')
        self.profile.delete()
        profile = Profile.objects.all()

        self.assertEquals(len(profile),1)

class ImagePostTestClass(TestCase):
    def setUp(self):
        self.user=User(
            username='jaffar',email='jaff@gmail.com',password='pass1'
    )
        self.user.save()

        self.image=Image(name='water',user=self.user,image='media/album/water.png',caption='Hey this is great')

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_save_profile(self):
        self.image.save_profile()
        images = Image.objects.all()

        self.assertEquals(len(images),1)

    def test_delete_image(self):
        def setUp(self):
            self.user=User(
                username='jaffar',email='jaff@gmail.com',password='pass1')
        self.user.save()
        self.image=Image(name='water',user=self.user,image='media/album/water.png',caption='Hey this is great')
        self.image.delete()
        images = Image.objects.all()

        self.assertEquals(len(images),1)

class FollowersTestClass(TestCase):
    def setUp(self):
        self.currentUser=User(
            username='jaffar',email='jaff@gmail.com',password='pass1'
    )
        self.otherUser=User(
            username='hanan',email='hanan@gmail.com',password='pass1'
    )

        self.current_user.save()
        self.otherUse.save()
    def test_instance(self):
        self.follow = Followers(followers = self.currentUser,follower = self.otherUser)
        self.assertTrue(isinstance(self.follow,Followers))
    
    def test_follow(self):
        self.follow = Followers(followers = self.currentUser,follower = self.otherUser)
        self.follow.follow()

        follow = Followers.objects.all()

        self.assertEquals(follow,1)