from django.db import models
import numpy as np
from sklearn.neighbors import NearestNeighbors
import pandas as pd
# Create your models here.

class ResortInfo(models.Model):
    def __str__(self):
        return self.ResortName

    ResortName = models.CharField(max_length=200)
    Continent = models.CharField(max_length=200)
    Country = models.CharField(max_length=200)
    State = models.CharField(max_length=200, blank=True, null=True)
    URL = models.CharField(max_length=200, blank=True, null=True)
    Currency = models.CharField(max_length=200)
    Altitude = models.FloatField(blank=True, null=True)
    Easy = models.FloatField(blank=True, null=True)
    Intermediate  = models.FloatField(blank=True, null=True)
    Difficult = models.FloatField(blank=True, null=True)
    Funicular = models.FloatField(blank=True, null=True)
    Gondola = models.FloatField(blank=True, null=True)
    Chairlift = models.FloatField(blank=True, null=True)
    Buttons = models.FloatField(blank=True, null=True)
    MovingCarpet = models.FloatField(blank=True, null=True)
    Adult = models.FloatField(blank=True, null=True)
    Youth = models.FloatField(blank=True, null=True)
    Child = models.FloatField(blank=True, null=True)
    ResortSize = models.FloatField(blank=True, null=True)
    Variety = models.FloatField(blank=True, null=True)
    Lifts = models.FloatField(blank=True, null=True)
    Reliability = models.FloatField(blank=True, null=True)
    SlopePreparation = models.FloatField(blank=True, null=True)
    Access = models.FloatField(blank=True, null=True)
    Orientation = models.FloatField(blank=True, null=True)
    Cleanliness = models.FloatField(blank=True, null=True)
    EnvironmentallyFriendly = models.FloatField(blank=True, null=True)
    Friendliness = models.FloatField(blank=True, null=True)
    RestaurantsAndFood = models.FloatField(blank=True, null=True)
    ApresSki = models.FloatField(blank=True, null=True)
    SkiInSkiOutAccomodation = models.FloatField(blank=True, null=True)
    FamiliesAndChildren = models.FloatField(blank=True, null=True)
    Beginners  = models.FloatField(blank=True, null=True)
    Advanced = models.FloatField(blank=True, null=True)
    SnowParks = models.FloatField(blank=True, null=True)
    CrossCountry = models.FloatField(blank=True, null=True)
    AerialTramway = models.FloatField(blank=True, null=True)
    RopeTow = models.FloatField(blank=True, null=True)
    PeopleMover = models.FloatField(blank=True, null=True)
    GondolaAndLift = models.FloatField(blank=True, null=True)
    CogRailway = models.FloatField(blank=True, null=True)
    Heliskiing = models.FloatField(blank=True, null=True)
    CatSkiing = models.FloatField(blank=True, null=True)


def get_recommendations(dataset, preferences):
    df = pd.DataFrame(dataset)
    df = df.rename(columns=lambda x: x.strip())

    numericCols = [col for col in df.columns if isinstance(df[col], int)]
    dropCols = [col for col in numericCols if df[col].sum() == 0]
    df2 = df[[col for col in df.columns if col not in dropCols]]

    df2 = df[['ResortName','ResortSize', 'ApresSki', 'Advanced']]
    df2.dropna(axis=0, inplace=True)
    df2.reset_index(drop=True, inplace=True)

    X = np.array(df2[['ResortSize', 'ApresSki', 'Advanced']].append(pd.Series(data=preferences, index=['ResortSize', 'ApresSki', 'Advanced']), ignore_index=True))
    nbrs = NearestNeighbors(n_neighbors=374, algorithm='kd_tree').fit(X)
    distances, indices = nbrs.kneighbors(X)
    return list(df2.ix[indices[-1,1:]]['ResortName'].values)[:10]
