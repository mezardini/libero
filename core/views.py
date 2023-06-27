from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
import random

# Create your views here.
import csv






class GeneratePlayer(APIView):
    def get(self, request):
        random_number = random.randint(2, 2690)
        with open('core/data.csv', 'r') as file:
            # Create a CSV reader
            reader = csv.reader(file)

            # Specify the row number and column indexes
            row_number = random_number  # Example: 2nd row (index starts at 0)
            column_indexes = [1,2, 4, 5, 6]  # Example: Columns 2, 4, and 6 (index starts at 0)

            # Iterate over the rows to find the desired row
            for i, row in enumerate(reader):
                if i == row_number:
                    # Create a dictionary to store the values
                    data = {
                        'name': row[column_indexes[0]] if len(row) > column_indexes[0] else None,
                        'Nationality': row[column_indexes[1]] if len(row) > column_indexes[1] else None,
                        'Team': row[column_indexes[2]] if len(row) > column_indexes[2] else None,
                        'League': row[column_indexes[3]] if len(row) > column_indexes[3] else None,
                        'Age': row[column_indexes[4]] if len(row) > column_indexes[4] else None
                    }

                    # Print the dictionary
                    return JsonResponse(data)