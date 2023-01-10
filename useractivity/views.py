from sqlite3 import IntegrityError
from django.shortcuts import render,redirect
from useractivity.models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
# from django.contrib.auth.models import User
import json
from useractivity.models import User as user_tbl
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from math import ceil
from django.db.models import Q

# Create your views here.


# def signin(request):
#     print("===inside ==== signin+++",request)
#     try:
#         print("inside first try")
#         if request.method == "POST":
#             print("inside-----if-----")
#             email = request.POST['email']
#             password = request.POST['password']
#             try:

#                 user = user_tbl.objects.get(email=email,password=password)
#             except:
#                 user = user_tbl.objects.get(phone_number=email,password=password)

#         if user is not None:
#             return render(request, "user/home.html", {'email':email})

#         else:
#             messages.error(request,"Bad Crentials")
#             return redirect('Signup')

    
#     except Exception as e:
#         print("-------exception---",e)

#     return render(request, "user/login.html")



def signup(request):
    print ("-------inside signup----------")
    if request.method == "POST":
        print ("-------data------------------",request)
        print("---------fname-------",request.POST['fname'])
        print ("-------data------------------",request.POST['lname'])
        print("---------fname-------",request.POST['dob'])
        print("---------fname-------",request.POST['gender'])
        print("---------fname-------",request.POST['email'])
        print("---------fname-------",request.POST['type'])
        print("---------fname-------",request.POST['phnumber'])
        print("---------fname-------",request.POST['password'])
        print("---------fname-------",request.POST['confmpassword'])


        first_name = request.POST['fname']
        last_name =request.POST['lname']
        date_of_birth = request.POST['dob']
        genders = request.POST['gender']
        email = request.POST['email']
        types = request.POST['type']
        phone_numbers = request.POST['phnumber']
        password = request.POST['password']
        confirm_password = request.POST['confmpassword']
        print("workingggggggggg")

        try:
            if password != confirm_password:
                error_message = "Password and Confirm Password is not matching"
                return render(request, 'signup.html', {'error_message': error_message})

            if user_tbl.objects.filter(email=email).exists():
                error_message = "Email already exists"
                return render(request, 'signup.html', {'error_message': error_message})

            if user_tbl.objects.filter(phone_number=phone_numbers).exists():
                error_message = "Phone number already exists"
                return render(request, 'signup.html', {'error_message': error_message})

            print("checkkkkkkkkkkkkkk")
            myuser = user_tbl.objects.create(first_name = first_name,
                                            email=email,
                                            password=password,
                                            phone_number=phone_numbers,
                                            gender=genders,
                                            last_name = last_name,
                                            date_of_birth = date_of_birth,
                                            confirm_password = confirm_password,
                                            type=types)




            myuser.save()
            messages.success(request, "User Created Successfully!")

        # myuser = authenticate(
        #     request,
        #     username=email,
        #     password=password
        # )
        # login(request, myuser)

            return redirect("Login") 


        except Exception as e:
            print("------",e)
            # error_message = "Phone Number Or Email Address already exists"
            return render(request, 'user/signup.html', {'error_message': error_message})

    # return render(request, 'signup.html', {'error_message': error_message})



    return render(request, "user/signup.html")




def signin(request):
    print("===inside ==== signin+++",request)
    try:
        print("inside first try")
        if request.method == "POST":
            print("inside-----if-----",request)
            # email = request.POST['email']
            login_identifier = request.POST['lid']
            password = request.POST['password']
            print("------email----",request.POST['lid'])

            try:

                if '@' in login_identifier:
                    myuser = user_tbl.objects.get(email=login_identifier, password=password)

                else:
                    myuser = user_tbl.objects.get(phone_number=login_identifier, password=password)

                # print("inside 222 try")
                # myuser = user_tbl.objects.get(email=login_identifier,password=password)
                    # user_tbl = authenticate(email=email,password=password)

                # if myuser is not None:
                #     print("====inside myuser if =======")
                #     login(request,myuser)
                #     email = myuser.email
                #     return render(request, "user/home.html", {'email':email})

                # else:
                #     messages.error(request,"Bad Crentials")
                #     return redirect('Signup')


            except user_tbl.DoesNotExist:
                # If user not found, set myuser to None
                myuser = None

            # except:
            #     print("inside 111 except")
            #     myuser = user_tbl.objects.get(phone_number=email,password=password)

            if myuser is not None:
                print("====inside myuser if =======",myuser.id)
                # login(request,User)
                # email = myuser.email
                request.session['id'] = myuser.id
                return render(request, "user/home.html", {'email':login_identifier})

            else:
                error_message = "Bad Credentials"
                return render(request, 'user/login.html', {'error_message': error_message})

                # print("----inside else -----")
                # messages.error(request,"Bad Crentials")
                # return redirect('Signup')

    # else:
    #     messages.error(request,"Bad request")
    #     return redirect('Signup')
    
    except user_tbl.DoesNotExist:
        # print("---------exception----")
        # messages.error(request,"Bad Crentials")
        # return redirect('Signup')
        error_message = "Bad Credentials"
        return render(request, 'user/login.html', {'error_message': error_message})
        return render(request, "user/login.html")

    return render(request, "user/login.html")




def home(request):
    myuser = user_tbl.objects.get()
    print("*********User******",myuser)
    
    return render(request, "user/home.html")


def edit_page(request):

    return render(request, "user/edit.html")


def edit_user(request):
    try:
        myusers = user_tbl.objects.get(id = request.session['id'])
        # myusers = user_tbl.objects.get()
        print("inside try",request)
        # print("========",myusers)
        # if myusers.exists():
        if request.method == "POST":
            print("-----name----",request.POST['fname'])

            # try:
            if myusers:
            # if request.method == "POST":
                print("========",myusers)
                print("====inside if=====",request)
                print("-----name----",request.POST['fname'])


                first_names = request.POST['fname']
                last_names = request.POST['lname']
                date_of_birth = request.POST['dob']
                genderss = request.POST['gender']
                emails = request.POST['email']
                phone_numberss = request.POST['phnumber']


                # user_tbl.objects.filter(id=id).update(
                #     email = emails,
                #     first_name = first_names,
                #     last_name = last_names,
                #     date_of_birth = date_of_birth,
                #     gender = genderss,
                #     phone_number = phone_numberss
                # )

                # myusers = user_tbl.objects.get(email=emails)
                myusers.first_name = first_names
                myusers.last_name = last_names
                myusers.date_of_birth = date_of_birth
                myusers.gender = genderss
                myusers.phone_number = phone_numberss
                myusers.save()

            else:
                print("3333333333333333333")
                messages.error(request,"User can not find")

            # except Exception as e:
            #     print("[[[[[[-------",e)
            # myuser.save()

            # return {
            #     'success': True,
            #     'message': 'User Updated Successfully!'
            # }
            
            # return {
            #     'success': False,
            #     'message': 'Error updating user. Password and confirm password do not match.'
            # }

            # return HttpResponse(json.dumps({
            #     'success': True,
            #     'message': 'User Updated Successfully!'
            # }), content_type='application/json')


            # return redirect ('Home')

    except Exception as e:
        print("----exception======",e)

    return render(request, "user/home.html")


def change_password(request):

    return render(request, "user/password.html")


def user_change_password(request):
    try:
        myuser = user_tbl.objects.get(id=request.session['id'])

        if request.method == "POST":
            if myuser:
                print("password",request.POST['password'])
                print("password",request.POST['confmpassword'])

                password = request.POST['password']
                confirm_password = request.POST['confmpassword']

                myuser.password = str(password)
                myuser.confirm_password = str(confirm_password)
                

                if password != confirm_password:
                    error_message = "Password is not matching"
                    return render(request,"user/password.html",{'error_message': error_message})
                    # messages.error(request,"Password is not matching")

                # else:
                #     pass

                myuser.save()

            else:
                messages.error(request, "Bad Request")

    except Exception as e:
        print("=======",e)

    return redirect('Login')


def view_user(request):

    return render(request, "user/viewuser.html")





# def view_all_users(request, page_number=1):
#     # Calculate the index range for the users to display
#     # start_index = (page_number - 1) * 5
#     # end_index = start_index + 5

#     # # Get the search query, if any
#     # search_query = request.GET.get('search_query')

#     # if "prev" in request.GET:
#     #     page_number -= 1
#     # elif "next" in request.GET:
#     #     page_number += 1
#     # # Filter the list of users based on the search query
#     # users = user_tbl.objects.all()
#     # if search_query:
#     #     users = users.filter(
#     #         Q(first_name__icontains=search_query) |
#     #         Q(last_name__icontains=search_query) |
#     #         Q(email__icontains=search_query) |
#     #         Q(phone_number__icontains=search_query) |
#     #         Q(type__icontains=search_query)
#     #     )

#     # # Paginate the users
#     # users = users[start_index:end_index]

#     # # Calculate the total number of pages
#     # total_pages = ceil(User.objects.count() / 5)

#     # start_index = (page_number - 1) * 5
#     # end_index = start_index + 5

#     # Get the search query, if any
#     search_query = request.GET.get('search_query')

#     if "prev" in request.GET:
#         page_number -= 1
#     elif "next" in request.GET:
#         page_number += 1
#     # Filter the list of users based on the search query
#     users = user_tbl.objects.all()
#     if search_query:
#         users = users.filter(
#             Q(first_name__icontains=search_query) |
#             Q(last_name__icontains=search_query) |
#             Q(email__icontains=search_query) |
#             Q(phone_number__icontains=search_query) |
#             Q(type__icontains=search_query)
#         )

#     # Paginate the users
#     total_users = users.count()
#     start_index = (page_number - 1) * 5
#     end_index = start_index + 5
#     users = users[start_index:end_index]
#     users = users[start_index:end_index]

#     # Calculate the total number of pages
#     total_pages = ceil(total_users / 5)
#     prev_page_number = max(page_number-1, 1)
#     next_page_number = min(page_number+1, total_pages)


#     context = {
#         'users': users,
#         'page_number': page_number,
#         'total_pages': total_pages,
#         'prev_page_number': prev_page_number,
#         'next_page_number': next_page_number
#     }
#     return render(request, "user/viewuser.html",context)



def view_all_users(request, page_number=1):
    # Get the search query, if any
    search_query = request.GET.get('search_query')

    if "prev" in request.GET:
        page_number -= 1
    elif "next" in request.GET:
        page_number += 1
    # Filter the list of users based on the search query
    users = user_tbl.objects.all()
    if search_query:
        users = users.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(email__icontains=search_query) |
            Q(phone_number__icontains=search_query) |
            Q(type__icontains=search_query)
        )

    # Paginate the users
    total_users = users.count()
    page_number = max(int(page_number),1)
    start_index = (page_number - 1) * 5
    end_index = min(start_index + 5, total_users)
    users = users[start_index:end_index]

    # Calculate the total number of pages
    total_pages = ceil(total_users / 5)
    prev_page_number = max(page_number-1, 1)
    next_page_number = min(page_number+1, total_pages)

    context = {
        'users': users,
        'page_number': page_number,
        'total_pages': total_pages,
        'prev_page_number': prev_page_number,
        'next_page_number': next_page_number
    }
    return render(request, "user/viewuser.html",context)



def user_logout(request):

    return redirect('Login')




# def edit_user(request):
#     try:
#         print ("-------inside update user----------")
#         myusers = user_tbl.objects.filter()
#         myusers = get_object_or_404(id=myusers.id)
#         if request.method == "POST":
#             # myusers = get_object_or_404(user_tbl, id=myusers.id)
#             print("----inside if------")
#             first_name = request.POST['fname']
#             last_name =request.POST['lname']
#             date_of_birth = request.POST['dob']
#             genders = request.POST['gender']
#             email = request.POST['email']
#             phone_numbers = request.POST['phnumber']

#             myusers.first_name = first_name
#             myusers.last_name = last_name
#             myusers.date_of_birth = date_of_birth
#             myusers.gender = genders
#             myusers.email = email
#             myusers.phone_number = phone_numbers
#             myusers.save()
#             messages.success(request, "User Updated Successfully!")

#             return redirect("Home") 

#     except Exception as e:
#         print("======",e)

#     return render(request, "user/edit.html")


# def edit_user(request):
#     try:
#         user_list = []
#         myuser = user_tbl.objects.filter(id=id)
#         data = json.loads(request.body)

#         if data:
#             myuser.first_name = data['fname']
#             myuser.last_name = data['lname']
#             myuser.email = data['email']
#             myuser.date_of_birth = data['dob']
#             myuser.gender = data['gender']
#             myuser.phone_number = data['phnumber']
#             myuser.save()
#             user_list.append({
#                 "id" : myuser.id,
#                 "fname" : myuser.first_name,
#                 "lname" : myuser.last_name,
#                 "email" : myuser.email,
#                 "dob" : myuser.date_of_birth,
#                 "gender" : myuser.gender,
#                 "phnumber" : myuser.phone_number
#             })
#             return JsonResponse({'myuser' : user_list})
        
#         return HttpResponse(status=400)


#     except Exception as e:
#         print("99999999990",e)

#     return render(request, "user/edit.html")

