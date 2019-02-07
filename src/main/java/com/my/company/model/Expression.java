package com.my.company.model;

public interface Expression {
    Money reduce(Bank bank, String to);
}
