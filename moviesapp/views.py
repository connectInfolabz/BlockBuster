from django.shortcuts import render, redirect
import requests
from .models import *
from django.contrib import messages

# # Create your views here

def index(request):
    return render(request, "landing.html")

def search(request):
    if request.session.get('login_id') is None:
        messages.error(request, "Login required.")
        return redirect('index')  # Redirect to the login page or index page

    if request.method == "POST":
        query = request.POST.get("query")
        page = request.POST.get("page", 1)
        url = "https://movie-database-alternative.p.rapidapi.com/"
        querystring = {"s": f"{query}", "r": "json", "page": page}
        headers = {
            "X-RapidAPI-Key": "8a3a6b96afmsh69456c40355fe43p1575dcjsn28d506dd507c",
            "X-RapidAPI-Host": "movie-database-alternative.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        total_results = int(data.get("totalResults", 0))
        movies = data.get("Search", [])
        count = len(movies)
        total_pages = (total_results // 10) + (1 if total_results % 10 != 0 else 0)

        context = {
            "movies": movies,
            "count": count,
            "total_pages": total_pages,
            "current_page": int(page),
            "query": query
        }
        return render(request, "moviegridfw.html", context)

def movies(request):
    # Check if user is logged in
    if request.session.get('login_id') is not None:
        try:
            # Fetch movies from the API
            url = "https://imdb-top-100-movies.p.rapidapi.com/"
            headers = {
                "X-RapidAPI-Key": "2ea054400fmsh0f704edbee5f191p1346d8jsn124804ca4c24",
                "X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers)
            movies = response.json()
            count = len(movies)
            # Render the movies to the template
            return render(request, "moviegrid.html", context={"movies": movies, "count": count})
        except Exception as e:
            print(f"Error fetching movies: {e}")
            messages.error(request, "Error fetching movies. Please try again later.")
            return redirect('index')
    else:
        # User is not logged in, show login required message
        messages.error(request, "Login required.")
        return redirect('index')

def registeruser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        print(username)
        print(email)
        print(phone)
        print(password2)
        print(password1)

        if Login.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please choose a different email.")
            return redirect(index)

        else:
            try:
                if password1 == password2:
                    insertuser = Login(name=username,email=email, phone=phone, password=password1,added_on="")
                    insertuser.save()
                    userid = insertuser.id
                    messages.success(request, "Account created now you can login !!!")
                    return redirect(index)

            except:
                pass

        return redirect(index)

def verifyuser(request):
    if request.method == "POST":
        email = request.POST.get("username")
        pwd = request.POST.get("password")

        try:
            userdata = Login.objects.get(email=email, password=pwd)
            request.session["login_id"] = userdata.id
            request.session.save()
            messages.success(request, "Login Successfull!!")
            return redirect(movies)

        except Login.DoesNotExist:
            messages.error(request, "Invalid Details")
            return redirect(index)
    else:
        messages.info(request, "Some Error Occurs")

    return render(request, "landing.html")


def logout(request):
    try:
        del request.session["login_id"]
        messages.success(request, "Logout Successful!")
        return redirect(index)
    except:
        pass
    return redirect(index)