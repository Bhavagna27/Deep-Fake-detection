
# Create your views here.
from django.shortcuts import render,redirect
from userapp.models import User
# from adminapp.models import Dataset
from django.contrib import messages
from adminapp.models import *




def index(request):
    t_users = User.objects.all()
    a_users = User.objects.filter(status="Accepted")
    p_users = User.objects.filter(status="Pending")
    context ={
        't_users':len(t_users),
        'a_users':len(a_users),
        'p_users':len(p_users),

    }
    
    return render(request,'admin/index.html',context)



def all_users(request):
    user = User.objects.filter(status = "Accepted")
    print(user)
    context = {
        'user':user,
    }
    return render(request,'admin/all-users.html',context)


from django.core.files.storage import default_storage

def upload_dataset(request):
    if request.method == 'POST':
        csv_file = request.FILES.get('file')

        if csv_file:
            file_path = default_storage.save('savedimg/' + csv_file.name, csv_file)
            messages.success(request,"Image Uploaded Succesfully")
            print(file_path,"succesfully!")
    return render(request,'admin/upload-dataset.html')



def trainTestmodel(request):
    images_training = 2041
    images_validation = 2041
    image_classes = 2

    try:
        model_performance = Train_test_split_model.objects.latest('S_No')
        model_performance.Images_training = str(images_training)
        model_performance.Images_validation = str(images_validation)
        model_performance.Images_classes = str(image_classes)
    except Train_test_split_model.DoesNotExist:
        model_performance = Train_test_split_model(
            Images_training=str(images_training),
            Images_validation=str(images_validation),
            Images_classes=str(image_classes)
        )

    model_performance.save()
    latest_entry = Train_test_split_model.objects.latest('S_No')

    context = {
        'images_training': latest_entry.Images_training,
        'images_validation': latest_entry.Images_validation,
        'image_classes': latest_entry.Images_classes
    }
    return render(request, "admin/test-trainmodel.html",context)



def cnnmodel(request):
    model_name = "Inceptionv3"
    accuracy = "98.74"
    executed = "Completed"
    
    try:
        model_performance = InceptionV3_model.objects.get(model_name=model_name)
        model_performance.model_accuracy = accuracy
        model_performance.model_executed = executed
    except InceptionV3_model.DoesNotExist:
        model_performance = InceptionV3_model(
            model_name=model_name, 
            model_accuracy=accuracy,
            model_executed=executed
        )
    
    model_performance.save()
    
    context = {
        'model_name': model_name,
        'accuracy': accuracy,
        'executed': executed
    }
    
    return render(request, "admin/cnnmodel.html", context)




def Efficientnetmodel(request):
    model_name = "EfficientNet"
    accuracy = "66"
    executed = "Completed"
    
    try:
        model_performance = EfficientNet_model.objects.get(model_name=model_name)
        model_performance.model_accuracy = accuracy
        model_performance.model_executed = executed
    except EfficientNet_model.DoesNotExist:
        model_performance = EfficientNet_model(
            model_name=model_name, 
            model_accuracy=accuracy,
            model_executed=executed
        )
    
    model_performance.save()
    
    context = {
        'model_name': model_name,
        'accuracy': accuracy,
        'executed': executed
    }

    
    return render(request, "admin/efficientnetmodel.html",context)




def Hybridmodel(request):
    model_name = "Hybrid"
    accuracy = "69.7"
    executed = "Completed"
    try:
        model_performance = Hybrid_model.objects.get(model_name=model_name)
        model_performance.model_accuracy = accuracy
        model_performance.model_executed = executed
    except Hybrid_model.DoesNotExist:
        model_performance = Hybrid_model(
            model_name=model_name, 
            model_accuracy=accuracy,
            model_executed=executed
        )
    
    model_performance.save()
    
    context = {
        'model_name': model_name,
        'accuracy': accuracy,
        'executed': executed
    }
    return render(request, "admin/hybridmodel.html",context)


def pending_users(request):
    user = User.objects.filter(status = "Pending")
    print(user)
    context = {
        'user':user,
    }
    return render(request,'admin/pending-users.html',context)


def accept_user(request,user_id):
    user = User.objects.get(user_id=user_id)
    user.status = 'Accepted'
    user.save()
    messages.success(request,"user is Accepted")

    return redirect('pending_users')

def reject_user(request,user_id):
    user = User.objects.get(user_id = user_id)
    user.delete()
    messages.success(request,"user is rejected")

    return redirect('pending_users')


def delete_user(request,user_id):
    user = User.objects.get(user_id = user_id)
    user.delete()
    messages.warning(request,"user is Deleted")

    return redirect('all_users')


def graph(request):
    Fake = "799"
    Real = "1578"
    executed = "Graph Executed Successfully"

    try:
        model_performance = graph_model.objects.first()
        if model_performance:
            model_performance.Fake_details = Fake
            model_performance.Real_details = Real
        else:
            raise graph_model.DoesNotExist
    except graph_model.DoesNotExist:
        model_performance = graph_model(
            Fake_details=Fake,
            Real_details=Real
        )
    
    model_performance.save()

    context = {
        'fake': Fake,
        'real': Real,
        'executed': executed
    }
    return render(request, "admin/graph.html", context)




def Comparisiongraph(request):
    Inception = InceptionV3_model.objects.last()
    EfficientNet = EfficientNet_model.objects.last()
    Hybrid = Hybrid_model.objects.last()

    Inception_graph = Inception.model_accuracy if Inception else '0'
    EfficientNet_graph = EfficientNet.model_accuracy if EfficientNet else '0'
    Hybrid_graph = Hybrid.model_accuracy if Hybrid else '0'

    return render(request, "admin/comparision-graph.html", {
        'Inception': Inception_graph,
        'EfficientNet': EfficientNet_graph,
        'Hybrid': Hybrid_graph
    })




