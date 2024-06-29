from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Collection, Medicine, Profile
from .forms import ProfileForm, CollectionForm, MedicineForm
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.


def index(req):
    return render(req, "base/index.html")


@login_required
def profile(request):
    profile_instance = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile_instance)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile_instance)

    context = {
        'form': form,
        'profile': profile_instance,
    }

    return render(request, 'base/profile.html', context)


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            # Save the form to the model
            user = form.save()

            login(request, user)
            messages.success(request, "account created successfully")
            return redirect("index")
    else:
        form = UserCreationForm()

    context = {"form": form}
    return render(request, "registration/register.html", context)


@login_required
def openstaande_afhaalacties(request):
    collections = Collection.objects.filter(user=request.user, Collected=False)
    context = {'collections': collections}
    return render(request, 'base/openstaande_afhaalacties.html', context)


@login_required
def mark_collected(request, collection_id):
    collection = Collection.objects.get(id=collection_id, user=request.user)
    if collection and not collection.Collected:
        collection.Collected = True
        collection.save()
        messages.success(request, "Gemarkeerd als Opgehaald")
    return redirect('openstaande_afhaalacties')


@staff_member_required
def add_collection(request):
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            new_collection = form.save(commit=False)
            new_collection.save()

            messages.success(request, "Afhaling Succesvol toegevoegd")
            return redirect('add_collection')
    else:
        form = CollectionForm()

    return render(request, 'base/add_collection.html', {'form': form})


@staff_member_required
def all_collections(request):
    collections = Collection.objects.all()
    context = {'collections': collections}
    return render(request, 'base/all_collections.html', context)


@staff_member_required
def approve_collection(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    if request.method == 'POST':
        collection.CollectedApproved = True
        collection.CollectedApprovedBy = request.user
        collection.save()
        messages.success(request, "Afhaling Succesvol goedgekeurd")
        return redirect('all_collections')
    return redirect('all_collections')


@staff_member_required
def delete_collection(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    if request.method == 'POST':
        collection.delete()
        messages.success(request, "Afhaling Succesvol deleted")
        return redirect('all_collections')
    return redirect('all_collections')


@staff_member_required
def list_medicines(request):
    medicine = Medicine.objects.all()
    context = {'medicines': medicine}
    return render(request, 'base/list_medicines.html', context)


@staff_member_required
def edit_medicine(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)

    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            return redirect('list_medicines')
    else:
        form = MedicineForm(instance=medicine)

    return render(request, 'base/edit_medicine.html', {'form': form, 'medicine': medicine})


@staff_member_required
def delete_medicine(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)

    medicine.delete()
    return redirect('list_medicines')


@staff_member_required
def add_medicine(request):
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_medicines')
    else:
        form = MedicineForm()
    return render(request, 'base/add_medicine.html', {'form': form})
