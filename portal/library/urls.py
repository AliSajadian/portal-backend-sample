from rest_framework import routers
from .views import Library_Book_TypeViewSet, Library_Book_PublisherViewSet, Library_Book_AuthorViewSet, Library_BookViewSet, Library_Loaned_BookViewSet

router = routers.DefaultRouter()
router.register('api/librarybooktype', Library_Book_TypeViewSet, 'librarybooktype')
router.register('api/librarybookpublisher', Library_Book_PublisherViewSet, 'librarybookpublisher')
router.register('api/librarybookauthor', Library_Book_AuthorViewSet, 'librarybookauthor')
router.register('api/librarybook', Library_BookViewSet, 'librarybook')
router.register('api/libraryloanedbook', Library_Loaned_BookViewSet, 'libraryloanedbook')

urlpatterns = router.urls
