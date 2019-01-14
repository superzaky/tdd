package com.my.company.model;

public class Franc extends Money {
    
    public Franc(int amount, String currency) {
        super(amount, currency);
    }

    public String currency() {
        return currency;
    }
}
