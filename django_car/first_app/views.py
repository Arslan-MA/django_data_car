from django.shortcuts import render
from first_app.models import Car


def cars(request):
    if request.method == "POST":
        stamp = request.POST.get('car_stamp')
        release = request.POST.get('car_release')
        color = request.POST.get('car_color')
        mileage = request.POST.get('car_mileage')
        price = request.POST.get('car_price')

        print(stamp, release, color, mileage, price)

        if stamp:
            Car.objects.create(stamp=stamp,
                               release=release,
                               color=color,
                               mileage=mileage,
                               price=price)

    return render(request, 'index.html')


def data_car(request):
    car = Car.objects.all()

    return render(request, 'index_data.html', context={"data_cars": car})
