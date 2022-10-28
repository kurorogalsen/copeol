from collections import UserList
from datetime import date
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from copeol_app import forms
from copeol_app.models import Commande, Facture, Fiche_analyse, Fiche_reception
from .forms import AnalyseForm, CommandeForm, FactureForm, ReceptionForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


def index(request):
    return render(request,
                  "admin/base_site.html",
                  context={'prenom': 'Moustapha'})


# Login
def login_view(request):
    form = forms.LoginForm(request.POST or None)
    msg = None
    if not request.user.is_authenticated:
        if request.method == "POST":

            if form.is_valid():
                #l = request.user.groups.values_list('name',flat = True) # QuerySet Object
                #l_as_list = list(l)
                #usergroup = request.user.groups.all()
                #print(l)
                user = authenticate(username=request.POST.get("username"),
                                    password=request.POST.get("password"))
                if user is not None:
                    login(request, user)
                    username = request.user.username
                    if request.user.groups.all():
                        usergroup = request.user.groups.all()
                    useraccess = 0
                    superadmin = False
                    vente = False
                    labo = False
                    reception = False

                    print(user.is_superuser)
                    if request.user.is_superuser:
                        superadmin = True
                        useraccess = -1
                    try:
                        print(usergroup[0].id)
                        useraccess = usergroup[0].id
                        print("myuser")
                        print(user.is_superuser())
                        if request.user.is_superuser:
                            superadmin = True
                            useraccess = -1
                        elif useraccess == 1:
                            vente = True
                        elif useraccess == 2:
                            labo = True
                        elif useraccess == 3:
                            reception = True
                        else:
                            superadmin = True

                    except:
                        print("error somewhere in group user")

                    request.session['role'] = useraccess
                    request.session['username'] = username

                    context = {
                        "superadmin": superadmin,
                        "vente": vente,
                        "labo": labo,
                        "reception": reception,
                        "username": username,
                        "user": request.user
                    }
                    return render(request, 'home/home.html', context)

                else:
                    messages.error(request, 'Invalid credentials.')
            else:
                messages.error(request, 'Error validating the form.')
        return render(request, "auth/login.html", {"form": form, "msg": msg})
    return redirect("home")


#Edit profile
def editprofile(request, id):
    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    user = User.objects.get(id=id)

    user.username = username
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    if password2 == password1 :
        user.set_password(password1)
    else:
        messages.add_message(request, messages.ERROR, 'Les mots de passe sont différents.')
    user.save()
    return redirect('/')

# Dashboard
def home(request):
    if request.user.is_authenticated:
        return render(request, "home/home.html")
    return redirect('login')


# users/views
def users_get(request):
    users_form = SignUpForm()
    print("user form")
    users = get_user_model().objects.all().order_by('-id')
    allgroup = Group.objects.all()
    if request.method == 'POST':
        print("Entrée post")
        users_form = SignUpForm(request.POST)
        if users_form.is_valid():
            print("Entrée valid")
            users_form.save()
            aded_username = users_form.cleaned_data['username']
            print(aded_username)
            aded_user = User.objects.get(username=aded_username)
            aded_group = users_form.cleaned_data['group']
            the_group = Group.objects.get(name=aded_group)
            the_group.user_set.add(aded_user)
            messages.success(request, 'Account created successfully')
        else:
            messages.error(request, 'Champs invalides')
    return render(request,
                  'home/home.html',
                  context={
                      'users_form': users_form,
                      'users': users,
                      'groups': allgroup
                  })


def user_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('users')


def user_update(request, id):

    username = request.POST['username']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    role = request.POST['group']

    user = User.objects.get(id=id)

    user.username = username
    user.first_name = first_name
    user.last_name = last_name
    user.email = email

    user.save()

    for group in user.groups.all():
        ancien_group = group
        ancien_group.user_set.remove(user)

    new_group = Group.objects.get(id=role)
    new_group.user_set.add(user)

    return redirect('users')


# commandes/views
def commande_get(request):
    commande_form = CommandeForm()
    commande = Commande.objects.all().order_by('-id')
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,
                  'home/home.html',
                  context={
                      'commande_form': commande_form,
                      'commande': commande
                  })


def commande_delete(request, id):
    commande = Commande.objects.get(id=id)
    commande.delete()
    return redirect('commandes')


def commande_update(request, id):
    lv_commande = request.POST['lv_commande']
    provenance_commande = request.POST['provenance_commande']
    date_commande = request.POST['date_commande']

    commande = Commande.objects.get(id=id)

    commande.lv_commande = lv_commande
    commande.provenance_commande = provenance_commande
    commande.date_commande = date_commande

    commande.save()
    return redirect('commandes')


# reception/views
def reception_get(request):
    reception_form = ReceptionForm()
    reception = Fiche_reception.objects.all().order_by('-id')
    if request.method == 'POST':
        form = ReceptionForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,
                  'home/home.html',
                  context={
                      'reception_form': reception_form,
                      'reception': reception
                  })


def reception_delete(request, id):
    reception = Fiche_reception.objects.get(id=id)
    reception.delete()
    return redirect('receptions')


def reception_update(request, id):
    lv_livraison = request.POST['lv_livraison']
    poids_brut = request.POST['poids_brut']
    provenance_livraison = request.POST['provenance_livraison']
    date_livraison = request.POST['date_livraison']

    reception = Fiche_reception.objects.get(id=id)

    reception.lv_livraison = lv_livraison
    reception.poids_brut = poids_brut
    reception.provenance_livraison = provenance_livraison
    reception.date_livraison = date_livraison

    reception.save()
    return redirect('receptions')


# analyse/views
def analyse_get(request):
    analyse_form = AnalyseForm()
    analyse = Fiche_analyse.objects.all().order_by('-id')
    if request.method == 'POST':
        form = AnalyseForm(request.POST)
        if form.is_valid():
            form.save()
            analyse_latest_id = Fiche_analyse.objects.latest('id').id
            print(analyse_latest_id)
            fiche_analyse = 'Fiche analyse ' + str(analyse_latest_id)
            facture_percentenge = form.cleaned_data[
                'humidite'] + form.cleaned_data[
                    'impuretes'] + form.cleaned_data[
                        'taux_graines_defectueuses']
            facture_poids = form.cleaned_data['fiche_reception'].poids_brut
            facture_provenance = form.cleaned_data[
                'fiche_reception'].provenance_livraison
            facture_date = form.cleaned_data['fiche_reception'].date_livraison

            facture = Facture(fiche_analyse=fiche_analyse,
                              provenance=facture_provenance,
                              pnc=int(facture_poids *
                                      (1 - facture_percentenge / 100)),
                              date_facture=date.today().strftime('%Y-%m-%d'))
            facture.save()
    return render(request,
                  'home/home.html',
                  context={
                      'analyse_form': analyse_form,
                      'analyse': analyse
                  })


def analyse_delete(request, id):
    analyse = Fiche_analyse.objects.get(id=id)
    analyse.delete()
    return redirect('analyses')


def analyse_update(request, id):
    fiche_reception = request.POST['fiche_reception']
    variete = request.POST['variete']
    humidite = request.POST['humidite']
    impuretes = request.POST['impuretes']
    taux_graines_defectueuses = request.POST['taux_graines_defectueuses']

    analyse = Fiche_analyse.objects.get(id=id)

    analyse.fiche_reception = fiche_reception
    analyse.variete = variete
    analyse.humidite = humidite
    analyse.impuretes = impuretes
    analyse.taux_graines_defectueuses = taux_graines_defectueuses

    analyse.save()
    return redirect('analyses')


# facture/views
def facture_get(request):
    facture_form = FactureForm()
    facture = Facture.objects.all().order_by('-id')
    if request.method == 'POST':
        form = FactureForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request,
                  'home/home.html',
                  context={
                      'facture_form': facture_form,
                      'facture': facture
                  })


def facture_delete(request, id):
    facture = Facture.objects.get(id=id)
    facture.delete()
    return redirect('factures')


def facture_update(request, id):
    prix_unitaire = request.POST['prix_unitaire']
    frais_livraison = request.POST['frais_livraison']
    frais_dechargement = request.POST['frais_dechargement']
    date_facture = date.today().strftime('%Y-%m-%d')

    facture = Facture.objects.get(id=id)

    facture.prix_unitaire = float(
        prix_unitaire.replace(',', '').replace(' ', ''))
    facture.frais_livraison = float(
        frais_livraison.replace(',', '').replace(' ', ''))
    facture.frais_dechargement = float(
        frais_dechargement.replace(',', '').replace(' ', ''))
    facture.date_facture = date_facture
    pnc = float(facture.pnc)

    print(prix_unitaire)
    print(frais_livraison)
    print(frais_dechargement)
    print(pnc)
    facture.montant_total = (float(pnc) * float(prix_unitaire)) + float(
        frais_livraison) + float(frais_dechargement)

    facture.save()
    return redirect('factures')
