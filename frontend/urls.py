from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
import backend.views as bViews
urlpatterns = [
    path('',home,name="homepage"),
    path('contact/',ContactUs,name="contact-us"),
    path('shop/',Shop,name="shop"),
    path('checkout/',bViews.Checkout,name="checkout"),
    path('cart/',UserCart,name="cart"),
    path('product/<int:product_id>/',ShopDetails,name="product-details"),
    path('post/',Post,name="post"),
    path('about/',About,name="about"),
    path('blogs/',Blogs,name="blogs"),

    # path('about-us/',Homepage.as_view(),name='about-us'),
    # path('contact-us/',Homepage.as_view(),name='contact-us'),
    path('dashboard/',bViews.AdminDashboard,name='dashboard'),
    path('categories',bViews.AddCategory,name='all-categories'),
    path('edit-category/<int:category_id>/',bViews.EditCategory,name='edit-category'),
    path('delete-category/<int:category_id>/',bViews.DeleteCategory,name='delete-category'),
    path('products/',bViews.AllProducts,name='all-products'),
    path('add-product/',bViews.AddProduct,name='add-product'),
    path('edit-product/<int:product_id>/',bViews.EditProduct,name='edit-product'),
    path('delete-product/<int:product_id>/',bViews.DeleteProduct,name='delete-product'),
    path('signup/',bViews.AddUser,name='signup'),
    path('login/',bViews.UserLogin,name='login'),
    path('logout/',bViews.UserLogout,name='logout'),
    path('404/',bViews.Error404,name='404'),
    path('500/',bViews.Error500,name='500'),
    path('banners/',bViews.AllBanners,name='all-banners'),
    path('add-banner/',bViews.AddBanner,name='add-banner'),
    path('edit-banner/<int:banner_id>/',bViews.EditBanner,name='edit-banner'),
    path('delete-banner/<int:banner_id>/',bViews.DeleteBanner,name='delete-banner'),
    path("add-to-cart/",bViews.AddToCart,name="add-to-cart"),
    path("remove-cart-item/",bViews.RemoveFromCart,name="remove-from-cart"),
    path("update-cart-quantity/",bViews.UpdateCartQunatity,name="update-cart-quantity"),
    path('add-company',bViews.AddCompany,name="add-company"),
    path('edit-company',bViews.EditCompany,name="edit-company"),
    path('cart',bViews.ViewCart,name="cart"),
    path('add-address/',bViews.AddAddress,name="add-address"),
    path('place-order',bViews.OrderProduct,name="place-order"),
    path('orders',bViews.AllOrders,name="orders"),
    path('all-orders/',bViews.AllOrders,name='admin-orders'),
    path('complete-order',bViews.CompleteOrder,name='complete-order'),
    path('signup-newsletter',bViews.Newsletter,name="signup-newsletter"),
    path('approve-newsletter/',bViews.ApproveNewsletter,name="approve-newsletter"),
    path('newsletters/',bViews.AllNewsletters,name="newsletters"),
    path('contact-form/',bViews.ContactForm,name="contact-form"),
    path('contactforms/',bViews.AllContactForms,name="contact-forms"),
    path('approve-contact-form/',bViews.AproveContactForm,name="approve-contact-form"),
    path('add-review/',bViews.AddReview,name="add-review"),
    path('read-review/',bViews.ReadView,name="read-review"),
    path('all-reviews/',bViews.AllReviews,name="all-reviews"),
    # path("product/<int:product_id>/",ProductDetails,name="product-details"),
    path('shop/',Shop,name='shop'),
    path("add-blog/",bViews.AddBlog,name="add-blog"),
    path("edit-blog/<int:blog_id>/",bViews.EditBlog,name="edit-blog"),
    path("delete-blog/<int:blog_id>/",bViews.DeleteBlog,name="delete-blog"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)