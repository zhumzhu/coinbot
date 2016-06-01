#!/usr/bin/python
# -*- coding: utf-8 -*-
from settings import DB
from peewee import *
from playhouse.sqlite_ext import SqliteExtDatabase
import datetime

db = SqliteExtDatabase(DB)

class BaseModel(Model):
    coinType = CharField()       # Type of the Virtual Coin
    price =  DoubleField()       # Unit Price of the trade
    volume = DoubleField()       # Volume of the Trade
    timestamp = DateTimeField(   # Now
        default = datetime.datetime.now) 
    class Meta:
        database = db

class CoinCapTransaction(BaseModel):
    percent = DoubleField()      # Price Change in Percentage
    supply = DoubleField()       # Supply
    cap24hrChange = FloatField() # Cap Change in 24 Hours
    vWAP = DoubleField()         # Volume weighted price based on 24hours of trading data on all exchanges
    vWAPBTC = DoubleField()      # vWap by BTC
    marketCap = DoubleField()    # Market Capitalization, total value of the coin

class CoinCapBTCTrans(CoinCapTransaction):
    pass

class CoinCapAltTrans(CoinCapTransaction):
    delta = DoubleField()        # DeltaPrice
    cap24hrChangePercent = FloatField()
    capPercent = FloatField()

class YunbiTrans(BaseModel):
    sell = DoubleField()
    buy = DoubleField()
    high = DoubleField()
    low = DoubleField()
