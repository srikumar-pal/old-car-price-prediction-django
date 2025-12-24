from django.shortcuts import render, redirect
import pickle
import os
from django.conf import settings

# 🔐 Auth imports
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# ===============================
# Load ML model safely
# ===============================
MODEL_PATH = os.path.join(settings.BASE_DIR, "model.pkl")

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# ===============================
# Views
# ===============================

def home(request):
    return render(request, "index.html")


@login_required
def predict(request):
    if request.method == "POST":
        try:
            year = int(request.POST.get("year"))
            price = float(request.POST.get("price"))
            kms = int(request.POST.get("kms"))
            fuel = int(request.POST.get("fuel"))
            seller = int(request.POST.get("seller"))
            transmission = int(request.POST.get("transmission"))
            owner = int(request.POST.get("owner"))

            prediction = model.predict([[
                year, price, kms, fuel, seller, transmission, owner
            ]])

            predicted_price = round(float(prediction[0]), 2)

            # 🔵 Session-based history
            history = request.session.get("history", [])
            history.insert(0, {
                "price": predicted_price,
                "year": year,
                "kms": kms
            })
            request.session["history"] = history[:5]

            return render(request, "result.html", {
                "result": predicted_price,
                "history": history
            })

        except Exception:
            return render(request, "result.html", {
                "result": "Error in prediction",
                "history": request.session.get("history", [])
            })

    return redirect("home")


# ===============================
# 🔐 Signup with AUTO LOGIN
# ===============================

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # 🔥 AUTO LOGIN
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect("home")  # direct home
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {
        "form": form
    })
