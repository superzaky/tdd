package com.my.company.model;

public class Dollar extends Money {

    public Dollar(int amount, String currency) {
        super(amount, currency);
    }

    public String currency() {
        return currency;
    }
}
