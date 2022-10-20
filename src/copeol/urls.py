from django.contrib import admin
from django.urls import path
from copeol_app.views import analyse_delete, analyse_get, analyse_update, commande_delete, commande_get, commande_update, facture_delete, facture_get, facture_update, index, login_view, home, reception_delete, reception_get, reception_update
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path('test', index, name="copeol-app-index"),
    #path('', admin.site.urls),
    #path('', admin.site.urls),

    path('login/', login_view, name="login"),
    #path('', home, name="home"),
    path('home/', home, name="home"),

    path('home/commandes/', commande_get, name="commandes"),
    path('home/commandes/update/<int:id>', commande_update, name="commande-update"),
    path('home/commandes/delete/<int:id>', commande_delete, name="commande-delete"),

    path('home/receptions/', reception_get, name="receptions"),
    path('home/receptions/update/<int:id>', reception_update, name="reception-update"),
    path('home/receptions/delete/<int:id>', reception_delete, name="reception-delete"),

    path('home/analyses/', analyse_get, name="analyses"),
    path('home/analyses/update/<int:id>', analyse_update, name="analyses-update"),
    path('home/analyses/delete/<int:id>', analyse_delete, name="analyses-delete"),

    path('home/factures/', facture_get, name="factures"),
    path('home/factures/update/<int:id>', facture_update, name="factures-update"),
    path('home/factures/delete/<int:id>', facture_delete, name="factures-delete"),

    path("logout/", LogoutView.as_view(), name="logout")
]

admin.site.site_header  =  "Copeol administration"  
admin.site.site_title  =  "Copeol administration"
admin.site.index_title  =  "Copeol administration"