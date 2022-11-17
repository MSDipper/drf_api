from django.contrib import admin
from hotel.models import (
                        Category,
                        ImageRoom, 
                        Hotel, 
                        Comment, 
                        RatingStar, 
                        Rating,
                        Reviews
                        )


admin.site.register(Category)
admin.site.register(ImageRoom)
admin.site.register(Hotel)
admin.site.register(Comment)
admin.site.register(RatingStar)
admin.site.register(Rating)
admin.site.register(Reviews)
