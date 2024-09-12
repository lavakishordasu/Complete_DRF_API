from django.urls import path,include
# from watchlist_app.api.views import movie_list,movie_details
# from watchlist_app.api.views import MovieListAV,MovieDetailAV
from watchlist_app.api.views import WatchListAV,WatchListDetailAV,StreamPlatformAV,StreamDetailAV,ReviewList,ReviewDetails,ReviewList,ReviewCreate

urlpatterns = [
   
    # path('list/',movie_list,name='movie_list'),    #Function based urls
    # path('<int:pk>',movie_details,name="movie-details")

    # path('list/',MovieListAV.as_view(),name = 'movie_list'), #classed based urls
    # path('<int:pk>',MovieDetailAV.as_view(),name = 'movie-detail'),

    path('list/',WatchListAV.as_view(),name = 'watch-list'),
    path('<int:pk>/',WatchListDetailAV.as_view(),name='watchlist-detail'),
    path('stream/',StreamPlatformAV.as_view(),name='stream-platform'),
    path('stream/<int:pk>/',StreamDetailAV.as_view(),name='stream-detail'),

    path('review/',ReviewList.as_view(),name='review-list'),
    path('review/<int:pk>/',ReviewDetails.as_view(),name='review_details'),

    path('<int:pk>/review-create/',ReviewCreate.as_view(),name = 'review-create'),    #create a new review    (3.30)
    path('<int:pk>/reviews/',ReviewList.as_view(),name='review-list'),     #for this link we get all the reviews
    path('review/<int:pk>/',ReviewDetails.as_view(),name='review_details'),  #we get single review details





















]

