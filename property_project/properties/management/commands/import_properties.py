import csv
from django.core.management.base import BaseCommand
from properties.models import Property


def clean_number(value):
    """Convert values like 2.6K, 1.2M, or 500 into numbers."""
    if not value:
        return None

    value = str(value).strip().upper()

    try:
        if value.endswith("K"):
            return int(float(value[:-1]) * 1000)

        if value.endswith("M"):
            return int(float(value[:-1]) * 1000000)

        return int(float(value))

    except ValueError:
        return None


class Command(BaseCommand):
    help = "Import real estate properties from CSV"

    def handle(self, *args, **kwargs):

        file_path = "properties/clean_real_estate_data.csv"

        with open(file_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            Property.objects.all().delete()

            count = 0

            for row in reader:

                Property.objects.create(
                    title=row.get("Title", ""),
                    address=row.get("Address", ""),
                    city=row.get("City", ""),

                    price=int(float(row["Price"])),

                    bedroom=clean_number(row.get("Bedroom")),
                    bathroom=clean_number(row.get("Bathroom")),
                    floors=clean_number(row.get("Floors")),
                    parking=clean_number(row.get("Parking")),

                    face=row.get("Face", ""),

                    year=clean_number(row.get("Year_AD")),

                    views=clean_number(row.get("Views")),

                    area=float(row["Area_SqFt"])
                    if row.get("Area_SqFt") else None,

                    road=row.get("Road", ""),

                    road_width=float(row["Road_Width_Feet"])
                    if row.get("Road_Width_Feet") else None,

                    road_type=row.get("Road Type", ""),

                    build_area=float(row["Build_Area_SqFt"])
                    if row.get("Build_Area_SqFt") else None,

                    posted=row.get("Posted", ""),

                    amenities=row.get("Amenities", ""),
                )

                count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully imported {count} properties."
            )
        )