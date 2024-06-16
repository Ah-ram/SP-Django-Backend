import os

from first_project import settings
from travel.entity.models import Travel
from travel.repository.travel_repository import TravelRepository


class TravelRepositoryImpl(TravelRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def list(self):
        return Travel.objects.all()

    def create(self, travelName, travelLocation, travelProperty, travelContent, travelPrice, travelImage):
        uploadDirectory = os.path.join(settings.BASE_DIR, '../../../../ui/Jimin/first/src/assets/images/uploadImages')
        if not os.path.exists(uploadDirectory):
            os.makedirs(uploadDirectory)

        imagePath = os.path.join(uploadDirectory, travelImage.name)
        with open(imagePath, 'wb+') as destination:
            for chunk in travelImage.chunks():
                destination.write(chunk)
        travel = Travel(
            travelName=travelName,
            travelLocation=travelLocation,
            travelProperty=travelProperty,
            travelContent=travelContent,
            travelPrice=travelPrice,
            travelImage=travelImage.name
        )
        travel.save()
        return travel

