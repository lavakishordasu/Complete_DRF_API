from rest_framework import serializers
# from watchlist_app.models import Movie
from watchlist_app.models import WatchList,StreamPlatform,Review

# These are the normal Serilizers
# notes 
# -> core arguments(3.18)

# # type-2
# def validate_name(value): #this validation for objects value level and this is out side the class
#     if len(value) < 2:
#         raise serializers.ValidationError("Name should be at least 2 characters long.")
#     else:
#         return value

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators = [validate_name])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.description = validated_data.get('description',instance.description)
#         instance.active = validated_data.get('active',instance.active)
#         instance.save()
#         return instance


# # ------------------------------------------------------------
# #3.17 Field level validations

# # these are custom validations
# # type1
#     def validate(self,data):    #this validation for objects level validation
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name not be same as description.")
#         else:
#             return data

#     # def validate_name(self,value): #this validation for objects value level
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name should be at least 2 characters long.")
#     #     else:
#     #         return value
        



# --------------------------------------------------------------------------------
# Model serializers(3.19)

# from watchlist_app.models import Movie

# createind a custom serializer field which is not in database (3.20)



# class MovieSerializer(serializers.ModelSerializer):
#     len_name = serializers.SerializerMethodField()
#     rating = serializers.SerializerMethodField()
#     class Meta:
#         model = Movie
#         fields = "__all__"
        # or
        # induvial_fields 
        # fields = ['id','name','description']
        #or
        # exclude = ['active']

    # def get_len_name(self,obj):
    #     return len(obj.name)
    
    # def get_rating(self,obj):
    #     rating = 5
    #     return rating
    
    # def validate(self,data):    #this validation for objects level validation
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name not be same as description.")
    #     else:
    #         return data

    # def validate_name(self,value): #this validation for objects value level
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name should be at least 2 characters long.")
    #     else:
    #         return value
        

# ----------------------------------------------------------------------------------

# 3.26 serilization relationship
class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        # fields = "__all__"
        exclude = ('watchlist',)



# Updateing with new models(3.20)

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = WatchList
        fields = "__all__"
        


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True,read_only = True)     #this is nessted Serializer (3.24)
    # watchlist = serializers.StringRelatedField(many=True)   #this will display only movie names (serialization realtions)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True,read_only = True) #this will display
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many = True,
    #     read_only = True,
    #     view_name = "watchlist-detail"
    # )

    class Meta:
        model = StreamPlatform
        fields = "__all__"