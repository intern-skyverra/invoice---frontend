def number_to_words(num):

    num = int(float(num))


    ones = [
        "",
        "ONE",
        "TWO",
        "THREE",
        "FOUR",
        "FIVE",
        "SIX",
        "SEVEN",
        "EIGHT",
        "NINE",
        "TEN",
        "ELEVEN",
        "TWELVE",
        "THIRTEEN",
        "FOURTEEN",
        "FIFTEEN",
        "SIXTEEN",
        "SEVENTEEN",
        "EIGHTEEN",
        "NINETEEN"
    ]


    tens = [
        "",
        "",
        "TWENTY",
        "THIRTY",
        "FORTY",
        "FIFTY",
        "SIXTY",
        "SEVENTY",
        "EIGHTY",
        "NINETY"
    ]


    def convert(n):

        if n < 20:
            return ones[n]

        if n < 100:
            return tens[n//10] + " " + ones[n%10]

        if n < 1000:
            return (
                ones[n//100]
                + " HUNDRED "
                + convert(n%100)
            )

        if n < 100000:
            return (
                convert(n//1000)
                + " THOUSAND "
                + convert(n%1000)
            )

        if n < 10000000:
            return (
                convert(n//100000)
                + " LAKH "
                + convert(n%100000)
            )

        return str(n)


    return convert(num) + " RUPEES ONLY"