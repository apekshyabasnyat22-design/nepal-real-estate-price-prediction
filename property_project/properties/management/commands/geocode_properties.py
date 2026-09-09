import time
import re
import requests

from django.core.management.base import BaseCommand
from properties.models import Property


class Command(BaseCommand):
    help = "Add latitude and longitude to properties using OpenStreetMap"

    def clean_text(self, text):
        if not text:
            return ""

        junk_phrases = [
            r"house for sale in.*",
            r"residential house sale\s*:?",
            r"nearby\s+",
        ]

        cleaned = text
        for phrase in junk_phrases:
            cleaned = re.sub(phrase, "", cleaned, flags=re.IGNORECASE)

        return cleaned.strip(" ,:-")

    def build_query(self, main_text, city):
        if not main_text:
            return None
        if city and city.lower() in main_text.lower():
            return f"{main_text}, Nepal"
        return f"{main_text}, {city}, Nepal"

    def get_queries(self, property):
        clean_address = self.clean_text(property.address)
        clean_title = self.clean_text(property.title)
        clean_city = self.clean_text(property.city)

        queries = []

        address_query = self.build_query(clean_address, clean_city)
        if address_query:
            queries.append(address_query)

        title_query = self.build_query(clean_title, clean_city)
        if title_query:
            queries.append(title_query)

        address_parts = [part.strip() for part in clean_address.split(",") if part.strip()]
        if len(address_parts) >= 2:
            if address_parts[-1].lower() != clean_city.lower():
                neighborhood = address_parts[-1]
            else:
                neighborhood = address_parts[-2]

            neighborhood_query = self.build_query(neighborhood, clean_city)
            if neighborhood_query and neighborhood_query not in queries:
                queries.append(neighborhood_query)

        # Final fallback: city name only (approximate, city-center location)
        if clean_city:
            city_query = f"{clean_city}, Nepal"
            if city_query not in queries:
                queries.append(city_query)

        return queries

    def handle(self, *args, **kwargs):

        properties = Property.objects.filter(
            latitude__isnull=True,
            longitude__isnull=True
        )

        total = properties.count()

        self.stdout.write(
            self.style.SUCCESS(
                f"Found {total} properties without coordinates."
            )
        )

        headers = {
            "User-Agent": "NepalRealEstatePricePrediction/1.0"
        }

        for number, property in enumerate(properties, start=1):

            queries = self.get_queries(property)

            found = False

            for query in queries:

                self.stdout.write(
                    f"[{number}/{total}] Searching: {query}"
                )

                try:

                    response = requests.get(
                        "https://nominatim.openstreetmap.org/search",
                        params={
                            "q": query,
                            "format": "json",
                            "limit": 1
                        },
                        headers=headers,
                        timeout=10
                    )

                    data = response.json()

                    if data:

                        property.latitude = float(data[0]["lat"])
                        property.longitude = float(data[0]["lon"])

                        property.save(
                            update_fields=[
                                "latitude",
                                "longitude"
                            ]
                        )

                        self.stdout.write(
                            self.style.SUCCESS(
                                f"   Found: {property.latitude}, "
                                f"{property.longitude}"
                            )
                        )

                        found = True
                        break

                    else:

                        self.stdout.write(
                            self.style.WARNING(
                                "   Not found"
                            )
                        )

                except Exception as error:

                    self.stdout.write(
                        self.style.ERROR(
                            f"   Error: {error}"
                        )
                    )

                time.sleep(1)

            if not found:

                self.stdout.write(
                    self.style.WARNING(
                        "   Could not find location after both attempts"
                    )
                )

                time.sleep(1)