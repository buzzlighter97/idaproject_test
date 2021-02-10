from images_app.models import ImageModel
from images_app.forms import ImageForm
from django.shortcuts import get_object_or_404, render
from .models import ImageModel
from PIL import Image

def index(request):
    images = ImageModel.objects.all()
    context={'images': images}
    return render(request, 'index.html', context)

def image_view(request, id):
    image = get_object_or_404(ImageModel, pk=id)
    form = ImageForm(request.POST or None, instance=image)
    print(image.image.url)
    if not form.is_valid():
        context = {
            "image": image,
            "form": form,
        }
        return render(request, "image_page.html", context)
    new_width = form.cleaned_data["width"]
    new_height = form.cleaned_data["height"]
    if image.width != new_width or image.height != new_height:
        new_image = Image.open(str(image.name))
        new_image = new_image.resize((form.cleaned_data["width"], form.cleaned_data["height"]))
        new_image.save()

        new_image_object = ImageModel.objects.create(image=new_image)

        context = {
                "image": new_image_object,
                "form": form,
            }
        return render(request, 'image_page.html', context)
    return render(request, "image_page.html", {'image':image, 'form': form})