def main():
    grosspay = float(input("Enter Gross Pay:"))
    paye = grosspay*0.25
    prsi = grosspay * 0.12
    usc = grosspay * 0.10
    unionsub = 34.56
    netpay = grosspay-paye-prsi-usc-unionsub
    print("Employee Payslip")
    print("---------------------------------")
    print("Gross Pay =€{0:,.2f}\nPaye =€{1:,.2f}\nPrsi =€{2:,.2f}\nUsc =€{3:,.2f}\nUnion Sub =€{4:,.2f}".format(grosspay, paye, prsi, usc, unionsub))
    print("-----------------------------------------------------------")
    print("Net Pay =€{0:,.2f}".format(netpay))


main()
