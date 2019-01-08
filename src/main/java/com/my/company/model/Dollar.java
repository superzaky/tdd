package com.my.company.model;

public class Dollar extends Money {
    private String currency;

    public Dollar(int amount, String currency) {
        super(amount, currency);
    }

    public String currency() {
        return currency;
    }

    public Money times(int multiplier) {
        return Money.dollar(amount * multiplier);
    }
}
